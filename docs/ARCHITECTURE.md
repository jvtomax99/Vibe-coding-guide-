# Architecture

Short map; keep it current. Read this at session start instead of exploring.

There is no app code yet (Phase 0). The plan, the same as Jose's other apps: plain
HTML, CSS and JavaScript, no framework, no build step, nothing to install. GitHub
Pages serves the folder from `main` as it is.

## Now

- `CLAUDE.md` Claude's rules for this repo. `.claude/rules/general.md` the rules
  shared by all of Jose's projects (identical everywhere; never edit one copy alone).
- `SPEC.md` What the app does, who for, "Done when" per feature, Not in v1, Later,
  Phases.
- `docs/` How work is done: `design-rules.md` (how `DESIGN.md` gets made and used),
  `assets.md` (buying and crediting assets), `refactor.md`, `cleanup-audit.md`.
  `docs/design/` will hold the taste skill's reports on the sites Jose picks.
- `.claude/agents/` Cheap helpers: `scout`, `test-runner` (Haiku), `builder`
  (Sonnet). `.claude/skills/taste/` the taste skill (Senlin's, MIT).
- `.github/site-check.cjs` and `.github/workflows/site-check.yml` The check every
  pull request runs. It passes with a note until `index.html` exists.
- `firestore.rules`, `firebase.json` Firestore's security rules, set to refuse
  everything. Not used until Firestore is added; kept so a database never starts in
  "test mode".
- `.nojekyll` Tells GitHub Pages to serve every file as it is.
- `CREDITS.md` Every asset, where from, license, cost.

## Planned (Phase 1 to 3; update as it is built)

- `index.html` The one page. `css/app.css` the whole look (variables from
  `DESIGN.md`). `manifest.webmanifest` and `sw.js` make it install and work offline.
- `js/` One small file each: `app.js` (starts the app, picks the screen from the
  address, e.g. `#/`, `#/path/github`, `#/lesson/<id>`, `#/glossary`, `#/kit`),
  `store.js` (what the phone remembers, one `localStorage` entry).
- `content/` What the app teaches, kept out of the code so lessons change without
  touching it: `paths.json` (the order), `lessons/<id>.json` (cards, steps, each step
  with `source` and `checked`), `glossary.json`, `kit/` (the starter-kit templates).
- `tools/check-content.mjs` Fails on a step with no source or checked date, a term
  with no glossary entry, or a real-project link to a file that doesn't exist.
- `assets/` `icons/`, `images/`, `fonts/` as `docs/assets.md` section 12 says.
