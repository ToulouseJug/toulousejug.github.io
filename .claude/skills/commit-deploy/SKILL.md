---
name: commit-deploy
description: Commit and push the Toulouse JUG Hugo site, or deploy it. Use when the user says "commit" (commit + push the `source` branch) or "deploy" (commit + push `source`, build `public/`, then commit + push `public` on `master`).
---

# commit / deploy

The user's words have fixed meanings in this repo:

- **"commit"** means: commit and **push** `source` (steps 1 to 3).
- **"deploy"** means: everything in "commit", then build `public/`, then commit and push `public` on `master` (steps 1 to 6).

Repo layout (two git repos, same remote) is described in `CLAUDE.md`. `public/` is a nested repo on `master`; the root is on `source`.

Run all commands from the repo root `/Users/arnaud/Lab/toulousejug.github.io` and use `git -C public ...` for the nested repo, so a stray `cd` can't point git at the wrong repo.

## Ask first, don't guess

Pushing is hard to undo and `master` goes live. **Stop and ask the user** (AskUserQuestion) instead of deciding alone when:

- there are untracked files, or modified files that don't look related to the change (stray `.orca/`, `.nod/`, `.gitignore` edits from tools; unreferenced images; `.DS_Store`);
- a change looks accidental or broken (for example a Go template printing a raw slice into a meta tag);
- the current branch isn't `source`, or `public/` isn't on `master`;
- a push is rejected / the remote has diverged (never force-push);
- the build prints an `ERROR`, or the `public/` diff contains deletions, renames or new files you can't explain.

When the answer is clear and reversible, just proceed and mention what you did.

## Steps

### 1. Inspect `source`

```sh
git status -sb
git diff            # read it; check it matches what the user is expecting
git log --oneline -3
```

Confirm the branch is `source` and that it is not behind `origin/source`.

### 2. Commit `source`

Stage **by name** (never `git add -A` on `source`), only files the user wants in this commit:

```sh
git add <file> <file> ...
git commit -m "<short imperative summary>" -m "<optional bullets>"
```

Write a descriptive message (e.g. "Add SEO meta tags, put next event before last event"), not "update". Add the commit attribution trailers required by the session's system instructions, if any.

### 3. Push `source`

```sh
git push origin source
```

If the user only said "commit", stop here and report the commit hash.

### 4. Build into `public/` (deploy only)

```sh
docker run --rm --volume=$(pwd):/src \
  registry.gitlab.com/pages/hugo@sha256:017b3e0d3620cf4a7d782656237b7aa8793909339d927c15dcd5bdd26180a849 \
  hugo -d public/ 2>&1 | grep -E 'ERROR|Pages|Static|Total'
```

- Docker must be running. Don't pass `-it` (no TTY).
- Ignore `WARN` lines; stop on `ERROR`.
- Optional dry run before committing source: build into the scratchpad instead (`--volume=<scratchpad>/out:/out ... hugo -d /out`) to check output without touching `public/`.

### 5. Review the `public/` diff

```sh
git -C public status -sb
git -C public status --porcelain | grep -v '^ M'     # anything that isn't a plain modification
git -C public diff --stat | tail -3
```

Typical, expected output: many `index.html` files modified (every page includes the head, header and copyright footer), plus any new files from `static/`. Sample one page diff to confirm the changes match the source change. If anything looks off, ask before committing.

### 6. Commit and push `public`

```sh
git -C public add -A          # fine here: public/ is generated output
git -C public commit -m "Rebuild site from source <short sha of source HEAD>" -m "<one line on what changed>"
git -C public push origin master
```

Add the same attribution trailers as in step 2, if any.

## Report

Finish with a short summary: both commit hashes, the branches pushed, and anything you left out of the commit (and why). Mention that GitHub Pages can take a minute or two to publish.
