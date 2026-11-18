# Toulouse JUG website

Hugo static site for https://www.toulousejug.org/ (Java User Group Toulousain), hosted on GitHub Pages. Content is in French.

## Two repos, one remote

Both point at `git@github.com:ToulouseJug/toulousejug.github.io.git`:

| Directory | Branch | Contains |
|-----------|--------|----------|
| `/` (repo root) | `source` | Hugo sources: `content/`, `data/`, `static/`, `themes/`, `config.toml` |
| `public/` | `master` | Generated site. Separate nested `.git`, ignored by the root repo. GitHub Pages serves this branch. |

Never edit files in `public/` by hand: they are overwritten by the build.

## Commands

Hugo is **not** installed locally. Use the pinned Docker image (it is an old Hugo; don't swap it for a newer one):

```sh
HUGO=registry.gitlab.com/pages/hugo@sha256:017b3e0d3620cf4a7d782656237b7aa8793909339d927c15dcd5bdd26180a849

# preview at http://localhost:1313
docker run -it --rm --volume=$(pwd):/src -p 1313:1313 $HUGO hugo serve --bind 0.0.0.0

# build into public/ (drop -it when there is no TTY, e.g. when run by Claude)
docker run --rm --volume=$(pwd):/src $HUGO hugo -d public/
```

The build prints a few `WARN` lines (deprecated `Page.Dir`, missing section/taxonomy layouts). They are known and harmless. Only `ERROR` matters.

## Layout

- `content/post/YYYY-MM-DD-slug.md`: one file per event. Front matter: `title`, `date`, `host`, `draft`, `sponsors`, `partners`, `authors`, `flyer`, `event` (Meetup URL).
- `content/page/`, `content/team/`: static pages.
- `data/*.toml`: hosts, sponsors, partners, authors, members, menus, promotions.
- `static/images/`: copied as-is to the site. Event flyers live in `static/images/<date>-<slug>/`.
- `themes/LessOrMore/`: the theme, edited in place (it's committed in this repo, not a submodule). The home page is `themes/LessOrMore/layouts/_default/index.html`, the `<head>` / SEO meta tags are in `layouts/partials/head.html`.
- `config.toml` `[Params]`: site tagline, SEO `tags`, and the upcoming event shown on the home page (`next`, `nextDate`, `nextFlyer`, `nextEvent`). Update these when announcing a new event.

## Workflow words

When the user says:

- **"commit"**: commit and push the `source` branch.
- **"deploy"**: commit and push `source`, build `public/`, then commit and push `public` (`master`).

Follow the `commit-deploy` skill (`.claude/skills/commit-deploy/SKILL.md`) for both.

## Rules

- **Ask before doing anything irreversible or surprising.** Pushes are shared state, and the `master` push goes live on the public site. If something unexpected shows up (untracked files, unrelated modifications, build errors, a diverged remote), stop and ask.
- Never force-push either repo. Never rewrite published history.
- Stage files by name on `source`; don't `git add -A` there. Tools drop stray files in the repo root (`.orca/`, `.nod/`, edits to `.gitignore`) that are not part of the site.
- Never commit `.DS_Store`, `.idea/`, or secrets.
- Commit messages: short, imperative, descriptive of the change (older history just says "update", don't copy that).
