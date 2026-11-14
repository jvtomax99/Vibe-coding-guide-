# CLAUDE.md: Vibe Coding Guide

A phone-first installable web app that teaches how to build an app with AI
("vibe coding") from idea to live site: GitHub, Claude Code, hosting
(Vercel, GitHub Pages), Firestore, and the habits that keep a beginner's
project from breaking. Plain HTML, CSS and JS, no build step, same as Jose's
other apps. Jose builds it to learn and to teach others (who: TO FILL in
`SPEC.md`).

Read first: `HANDOFF.md` if there is one, `SPEC.md` (what, who, phases and
what's next), `docs/ARCHITECTURE.md` (map of files). Look: `DESIGN.md`
(not made yet: `docs/design-rules.md`, section 1, is Phase 0). The rules
shared by all of Jose's projects are in `.claude/rules/general.md`; where
this file differs, this file wins.

## Rules for this repo

- **Every how-to step needs a source.** Tools in this app (GitHub, Vercel,
  Firebase, Claude Code) rename buttons and move menus often. Each step that
  tells someone what to click or type links the vendor's own docs page and
  the date it was checked. Never write a step from memory. A summary site
  or Wikipedia is not a source.
- **Stale steps get rechecked.** A step whose checked date is over 90 days
  old shows a "may be out of date" mark until someone rechecks it.
- **Plain English for people who can't read code.** Jose is the first
  reader. Define every technical word the first time it appears (and in the
  glossary). Code shows up only when the reader has to copy it, in one
  block, all at once.
- **Real examples come from Jose's public repos only.** Lessons can link
  real files in `jvtomax99/Interp`, `Citizenship-study-app-`,
  `Cruelty-Free-Beauty-`, `CPA-study-app`, `Lions-Roar-`,
  `Phillis-bookshelves-` and `Cat-app`. Never quote or link `Reels` or
  `claude-skills` (private). Never name a real person other than Jose, a
  client, or anything about Interp's hospital work beyond what its public
  README says, without his OK.
- **Never teach an unsafe default as fine.** Firestore "test mode" lets
  anyone read and overwrite the data; API keys in a public repo get stolen.
  When a lesson shows a shortcut like that, it says what it costs and how to
  close it before going live.
- **A new file the app loads** goes in the precache list in `sw.js`, and the
  cache name there is bumped, or returning users keep the old app.
- **Public repo.** Paid raw files (fonts, models, music) can't be committed
  (`docs/assets.md`, section 9) unless Jose makes it private.
- **Budget:** TO FILL (`docs/assets.md`, section 1, asks for it once).

## Preview, checks and going live

- **Hosting:** not decided (TO FILL in `SPEC.md`, Phase 0). Until it is,
  merging to `main` is treated as going live.
- **Preview.** Serve the repo with `python3 -m http.server 8123` and send
  Playwright screenshots at 390 px, then 1440 px, plus a "try this" list.
- **Site check.** `node .github/site-check.cjs index.html` (needs
  Playwright). It runs on every pull request and must be green before
  merging. It passes with a note until `index.html` exists. A new page goes
  into the list in `.github/workflows/site-check.yml`.
- **Into `main`:** pull request, phone notification saying it needs Jose's
  "push", wait for his OK, then one line on how to undo it.

## Helpers: the main model thinks, cheaper models fetch

The main conversation plans, decides, writes the real code and reviews.
Repetitive work goes to the agents in `.claude/agents/`: `scout` (Haiku,
finding things and reading long files or logs), `test-runner` (Haiku,
running checks and reporting only failures), `builder` (Sonnet, exactly
specified text edits like lesson copy or glossary entries, never logic).
Don't delegate a one-line search. Check what a helper reports before relying
on it.

## Tools

- **Taste skill** (`.claude/skills/taste/`): it asks for the Playwright MCP
  server. In a cloud session use the installed Playwright instead and run
  its `references/extract.js` with `page.evaluate` (`SOURCE.md` there says
  how).
- **Refactor.** `docs/refactor.md`, run when Jose asks for "Refactor:
  CLEANUP.md items ...".
- **Keep this file lean.** It loads every session. Suggest a one-line
  addition for a lasting decision; remove lines that no longer apply.
