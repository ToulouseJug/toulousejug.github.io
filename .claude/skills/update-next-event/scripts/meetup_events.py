#!/usr/bin/env python3
"""Read the Toulouse JUG Meetup group from its public web pages (no login, no API key).

Run from the repo root, with `python3 -I` (isolated mode, stdlib only):

  meetup_events.py list  [--posts content/post]   events on the group page, as JSON
  meetup_events.py show  EVENT_ID                 one event with its raw description, as JSON
  meetup_events.py photo EVENT_ID DEST_DIR        download the event photo to DEST_DIR/promo.<ext>

Meetup renders these pages with Next.js and embeds the data as JSON in
<script id="__NEXT_DATA__">. This script reads that. If Meetup changes the format it
exits with an error instead of guessing.

Every event gets:
  when   "upcoming" or "past" (computed from its end time, not from Meetup's `status`)
  post   path of the content/post/*.md whose `event:` front matter points at it, or null
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

GROUP = "toulouse-java-user-group"
EVENTS_URL = "https://www.meetup.com/%s/events/" % GROUP
USER_AGENT = "toulousejug-site-updater/1.0 (+https://www.toulousejug.org)"
PHOTO_HOSTS = {"secure.meetupstatic.com", "secure-content.meetupstatic.com"}
MAX_PHOTO_BYTES = 15 * 1024 * 1024


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def http_get(url, limit=None):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "fr"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read(limit + 1) if limit else response.read()
    except urllib.error.URLError as error:
        fail("cannot fetch %s: %s" % (url, error))
    if limit and len(data) > limit:
        fail("response too large: " + url)
    return data


def apollo_state(url):
    html = http_get(url).decode("utf-8", "replace")
    match = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not match:
        fail("no __NEXT_DATA__ in %s: Meetup's page format probably changed" % url)
    try:
        return json.loads(match.group(1))["props"]["pageProps"]["__APOLLO_STATE__"]
    except (KeyError, ValueError) as error:
        fail("unexpected __NEXT_DATA__ structure in %s (%r)" % (url, error))


def deref(apollo, value):
    if isinstance(value, dict) and "__ref" in value:
        return apollo.get(value["__ref"], {})
    return value


def parse_time(text):
    try:
        parsed = dt.datetime.fromisoformat(text)
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed


def normalize(apollo, event, full=False):
    venue = deref(apollo, event.get("venue")) or {}
    photo = deref(apollo, event.get("featuredEventPhoto")) or deref(apollo, event.get("displayPhoto")) or {}
    start = event.get("dateTime") or ""
    end = event.get("endTime") or ""
    end_time = parse_time(end)
    if end_time is None:
        start_time = parse_time(start)
        end_time = start_time + dt.timedelta(hours=3) if start_time else None
    past = end_time is not None and end_time < dt.datetime.now(dt.timezone.utc)
    result = {
        "id": str(event.get("id")),
        "title": event.get("title"),
        "status": event.get("status"),
        "when": "past" if past else "upcoming",
        "dateTime": start,
        "date": start[:10],
        "endTime": end or None,
        "url": (event.get("eventUrl") or "").rstrip("/"),
        "type": event.get("eventType"),
        "online": event.get("isOnline"),
        "venue": {key: venue.get(key) for key in ("name", "address", "city")} if venue else None,
        "going": (event.get("going") or {}).get("totalCount"),
        "photoUrl": photo.get("highResUrl"),
    }
    if full:
        result["description"] = event.get("description") or ""
    return result


def post_index(posts_dir):
    """Map Meetup event id -> content/post file, from each post's `event:` front matter."""
    index = {}
    directory = pathlib.Path(posts_dir)
    if not directory.is_dir():
        return index
    for path in sorted(directory.glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines()[:40]:
            match = re.match(r"event:\s*\S*/events/(\d+)", line)
            if match:
                index[match.group(1)] = str(path)
    return index


def fetch_event(event_id):
    if not re.fullmatch(r"\d+", event_id):
        fail("event id must be numeric")
    apollo = apollo_state(EVENTS_URL + event_id + "/")
    event = apollo.get("Event:" + event_id)
    if not event:
        fail("event %s not found in the page data" % event_id)
    return apollo, event


def dump(value):
    json.dump(value, sys.stdout, ensure_ascii=False, indent=2)
    print()


def cmd_list(args):
    apollo = apollo_state(EVENTS_URL)
    index = post_index(args.posts)
    events = []
    for key, value in apollo.items():
        if key.startswith("Event:") and isinstance(value, dict) and value.get("dateTime"):
            event = normalize(apollo, value)
            event["post"] = index.get(event["id"])
            events.append(event)
    events.sort(key=lambda e: parse_time(e["dateTime"]) or dt.datetime.min.replace(tzinfo=dt.timezone.utc))
    dump(events)


def cmd_show(args):
    apollo, event = fetch_event(args.event_id)
    result = normalize(apollo, event, full=True)
    result["post"] = post_index(args.posts).get(result["id"])
    dump(result)


def sniff_extension(data):
    if data.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    return None


def cmd_photo(args):
    apollo, event = fetch_event(args.event_id)
    url = normalize(apollo, event)["photoUrl"]
    if not url:
        fail("event %s has no photo" % args.event_id)
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in PHOTO_HOSTS:
        fail("unexpected photo host: " + url)
    data = http_get(url, MAX_PHOTO_BYTES)
    extension = sniff_extension(data)
    if not extension:
        fail("downloaded file is not a JPEG, PNG or WebP image")
    destination = pathlib.Path(args.dest_dir)
    destination.mkdir(parents=True, exist_ok=True)
    path = destination / ("promo." + extension)
    if path.exists() and not args.force:
        fail("%s already exists (use --force to overwrite)" % path)
    path.write_bytes(data)
    dump({"path": str(path), "bytes": len(data), "source": url})


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)

    list_parser = commands.add_parser("list", help="events on the group page")
    list_parser.add_argument("--posts", default="content/post", help="posts directory (default: content/post)")
    list_parser.set_defaults(run=cmd_list)

    show_parser = commands.add_parser("show", help="one event, with its raw description")
    show_parser.add_argument("event_id")
    show_parser.add_argument("--posts", default="content/post")
    show_parser.set_defaults(run=cmd_show)

    photo_parser = commands.add_parser("photo", help="download an event photo as promo.<ext>")
    photo_parser.add_argument("event_id")
    photo_parser.add_argument("dest_dir")
    photo_parser.add_argument("--force", action="store_true", help="overwrite an existing promo file")
    photo_parser.set_defaults(run=cmd_photo)

    args = parser.parse_args()
    args.run(args)


if __name__ == "__main__":
    main()
