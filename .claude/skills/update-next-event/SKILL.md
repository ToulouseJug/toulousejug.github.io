---
name: update-next-event
description: Sync the Toulouse JUG site with its Meetup group. Use when the user says "update next event", "update events", "new event", "add the latest event", "sync meetup" or "catch up on events". Creates a post and a promo image dir for every Meetup event that has no post yet, fixes stale drafts, and updates the `next*` params in config.toml used by the home page. Never commits or pushes.
---

# update-next-event

Bring the site in line with the Toulouse JUG Meetup group (`toulouse-java-user-group`).
Event data comes from Meetup's public pages through a bundled helper; no login or API key.

## How the site uses events

- **Home "Prochain événement"**: driven only by `config.toml` `[Params]`: `next` (title), `nextDate`, `nextFlyer`, `nextEvent`. If `next` is absent, or `nextDate` is not in the future at build time, the home page says "en cours de préparation" (template safety net; still clean the config up).
- **Home "Dernier événement"**: the newest *published* post in `content/post/`, displaying that post's `date`. So `date` must be the **event day**.
- **Hugo hides future-dated posts** (no `buildFuture`). An announced event therefore gets a post dated on the event day with **no `draft`**: it appears by itself on the first build on/after that day. `hugo serve` also hides it unless run with `-F`.
- A post is linked to its Meetup event by its `event:` front matter. That is how "has no post yet" is decided.

Decisions already made with the user (don't re-ask): future date and no draft for announced events; always handle **every** Meetup event that has no post; never commit or push from this skill.

## Steps

Run everything from the repo root. The helper is stdlib-only Python:

```sh
H=.claude/skills/update-next-event/scripts/meetup_events.py
python3 -I $H list                       # events on the group page + their post (or null)
python3 -I $H show <eventId>             # one event with its raw Meetup description
python3 -I $H photo <eventId> <dir>      # saves <dir>/promo.<jpg|png|webp>
```

If the helper fails (network, or Meetup changed its page format), report the exact error and stop. Don't scrape another way or invent event data.

### 1. List and pick what to create

Run `list`. Candidates are events with `post: null` and `status` not `CANCELLED` / `DRAFT`.

Ask the user (AskUserQuestion) before creating a post for anything that is not a regular JUG evening: other title patterns (e.g. "JUGxDevFest" talk slot, "Deviens Conférencier au DevFest"), another venue or an online event, or a time that isn't an evening. Regular evenings ("Soirée …" at Epitech or another known host) need no question.

### 2. Create each post

For each chosen event run `show <id>` and create the files below. Paths use the event date `YYYY-MM-DD` and a short slug.

**Post** `content/post/YYYY-MM-DD-<slug>.md`, slug = lowercase ASCII from the title, `-` separators, keep `.` and `+` like existing files (`soiree-spring-ai`, `soiree-java.lang`). It becomes the URL, so keep it short and clean.

```yaml
---
title: <Meetup title, verbatim; double-quote it if it contains ": " or "#">
date: YYYY-MM-DD              # the event day, never the announcement day
host: <id from data/hosts.toml>
sponsors: [monkeypatch, openairlines]
partners: [jetbrains]
authors: [abos]
flyer: images/YYYY-MM-DD-<slug>/promo.<ext>
event: https://www.meetup.com/toulouse-java-user-group/events/<id>   # the helper's `url`, no trailing slash
---
```

- **No `draft` key.**
- **host**: match the venue name to `data/hosts.toml` (case-insensitive: "EPITECH - Amphi rez-de-chaussée" → `epitech`). No match or online event: ask. A new host also needs a `data/hosts.toml` entry and a logo in `static/images/sponsors/`; don't invent one.
- **sponsors**: the names after "Merci à nos sponsors" (or in a sentence like "offerts par nos généreux sponsors : …") mapped to ids in `data/sponsors.toml`. A sponsor named only in a speaker bio (e.g. the speaker's employer) is not a sponsor. A named sponsor with no entry: ask. Regular evenings that name none: copy the newest existing post's.
- **partners / authors**: copy from the newest existing post (check it rather than trusting the values above).
- **Special events** (DevFest slot, joint meetups with other communities, anything not a regular evening): omit `host`, `sponsors` and `partners` unless the description names them, and keep `authors`. The templates handle missing keys (most old posts have none). Never put JUG sponsors on an event they didn't sponsor.

**Body**: convert the Meetup markdown to the site's style. See `content/post/2025-05-20-soiree-java.lang.md` against its Meetup original for the model.

- Opening line: "La prochaine soirée du Java User Group Toulousain aura lieu le **mardi 20 mai à 19h** chez **Epitech** **Toulouse**." becomes "Nouvelle soirée du Java User Group Toulousain le mardi 20 mai à 19h chez Epitech Toulouse." Other phrasings of the intro ("Le **mercredi 12 novembre à 19h**, veille du DevFest …"): keep the wording, fix stray spacing (`19h ,` → `19h,`).
- Bold: remove it on dates, times, venues and language notes. Keep it on people's names and on explicit warnings (e.g. "accessible qu'aux visiteurs munis d'un billet").
- Keep the other intro paragraphs and their wording. Keep Meetup's tense even for past events; don't rewrite prose.
- `**== Talk title**` followed by `Speaker : **Name**` becomes `### Talk title - par Name` (two speakers: `par A et B`). The title may be a link (`**==** [Title](url)`): keep it as a link in the heading. No `Speaker :` line: just `### Talk title`. Keep the abstract paragraphs and bullet lists as they are.
- A speaker bio ("Le speaker :", "À propos de …", "Bio:") stays as a plain paragraph under its talk.
- Consecutive lines that are really a list (several `Label : [link](url)` lines in a row) become Markdown bullets: Hugo would merge them into one paragraph otherwise. Emoji-led paragraphs stay as they are.
- Drop Meetup scaffolding and the `\*\*\*` / `***` separators: a leading `## Détails`, and unescape other backslash escapes (`\_`, `\-`, …).
- Drop the closing boilerplate: the apéro line, the CFP paragraph and bare `bit.ly` link, "Si vous ne connaissez pas le JUG, découvrez notre groupe sur toulousejug.org", "Merci à nos sponsors …", the "Nous recherchons activement des volontaires …" call and its needs list. Anything unusual after the talks (a thank-you to a partner, a special announcement) is content: keep it, in sentence case without bold.
- Do not invent speakers' X handles. Leave the plain name; the user can add `({{< x handle >}})` later. Never leave `{{<` or `{{%` from Meetup text unescaped.
- A regular evening without talks ("Venez comme vous êtes") simply has no `###` sections.

**Image** `static/images/YYYY-MM-DD-<slug>/`: run `photo <id> static/images/YYYY-MM-DD-<slug>` and use the printed `path`'s extension in `flyer:`. If the event has no photo, create the post without `flyer:` and tell the user. Never overwrite an existing `promo.*` without asking.

Existing flyers are 1920×1080. Check the downloaded size with `sips -g pixelWidth -g pixelHeight <file>`: wider than 1920 (a raw photo can be 6000px, several MB, and the home page loads it) → `sips -Z 1920 -s formatOptions 85 <file>` in place. Much smaller than 1200 wide: keep it (it's all Meetup has) and tell the user.

### 3. Fix stale posts

For every existing post whose Meetup event is now `when: "past"` and that still has `draft: true`: remove the `draft` line and set `date:` to the event day. Report each one. Leave everything else in existing posts alone.

### 4. Update `config.toml`

`next` is the earliest event with `when: "upcoming"` and not cancelled. Edit only these four lines in `[Params]`:

```toml
  next = "<title>"
  nextDate = YYYY-MM-DD        # unquoted TOML date
  nextFlyer = "images/YYYY-MM-DD-<slug>/promo.<ext>"
  nextEvent = "<event url>"
```

No upcoming event: **delete** those four lines (the home page then shows "en cours de préparation", i.e. TBD). Leave other params alone. The "previous event" needs no config; it follows from the newest published post.

**A past event is never `next`.** Once an event's date has passed (end time before now), it is the "Dernier événement" via its post, not the "Prochain événement". This applies even if the current `next*` lines already point at it, or Meetup still lists it: if nothing else is upcoming, remove the four lines and leave the next event as TBD. Don't fill `next*` with the latest past event to avoid an empty slot. Whenever you run, also check the existing `nextDate`: if it is in the past, it is stale and gets replaced by the next upcoming event, or deleted.

### 5. Verify

Build into the scratchpad with a local base URL so nothing in `public/` changes (the Hugo image and command are in `CLAUDE.md`):

```sh
docker run --rm --volume=$(pwd):/src --volume=<scratchpad>/check:/out <hugo-image> hugo -b http://127.0.0.1:1313/ -d /out
```

Check: no `ERROR`; each past post exists as `<scratchpad>/check/post/<file-name-without-.md>/index.html`; a future-dated post does **not**; the home page's "Prochain événement" / "Dernier événement" blocks show the expected titles and dates. "Prochain événement" must never show a date in the past: either an upcoming event or "en cours de préparation".

A `hugo serve` the user already has running (check `docker ps` for port 1313) picks up new posts but **keeps stale `config.toml` params in memory**: after removing `next*` it keeps showing the old next event. Trust the scratchpad build, then `docker restart <container>` and reload the browser tab so the user's preview matches.

### 6. Report, then stop

Summarize: files created (posts, image dirs), events skipped and why, stale drafts fixed, the `next*` result, and judgment calls the user may want to change (host/sponsor mapping, bios kept, missing X handles). Then tell them to say "commit" or "deploy" (the `commit-deploy` skill). Do not commit, push or build into `public/` here. New posts and images are untracked files: that's expected, and the commit step stages them by name.
