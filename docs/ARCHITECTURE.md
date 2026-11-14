# Architecture

Short map; keep it current. The whole site is one file, `index.html` (about 2,100
lines: HTML, CSS and JavaScript together), so find a part by its marker below with a
search instead of reading the file top to bottom.

## Files

- `index.html` The site. Fonts come from Google Fonts; nothing else loads from
  outside.
- `.nojekyll` Tells GitHub Pages to serve every file as it is.
- `CLAUDE.md`, `.claude/rules/general.md` Rules for Claude. `.claude/agents/` cheap
  helpers (`scout`, `test-runner`, `builder`). `.claude/skills/taste/` design
  analysis.
- `SPEC.md` What, who, Done when, Not in v1, Later, Phases. `DESIGN.md` the look.
  `CREDITS.md` fonts and other assets with their licenses.
- `docs/` How work is done: `design-rules.md`, `assets.md`, `refactor.md`,
  `cleanup-audit.md`.
- `.github/site-check.cjs` and `.github/workflows/site-check.yml` The check every pull
  request runs: no missing files, no links starting with "/", the page opens at phone
  and desktop width with no script error.

## Inside index.html

Search for these markers:

- `:root{` The color, font and wood variables, then the dark versions
  (`prefers-color-scheme: dark` and `[data-theme="dark"]`).
- `/* ============ LIBRARY (home) ============ */` The wall, shelves and spines.
- `/* ============ READER (one book open) ============ */` An open book.
- `id="intro"` The start menu (once per visit, skipped on a link straight to a book):
  a space scene with a futuristic book and three choices, `#introGo` (start or
  continue), `#introOpen` (the shelves) and `#introGloss` (the glossary). Its styles
  start at `/* Opening (the start menu)`.
- `id="libraryView"` The heading, the library card (`#borrower`, `#readCount`,
  `#resetBtn`) and `#case`, where the script builds the shelves.
- `id="readerView"` The reading bar and `<main id="main">`, which holds every lesson.
- `<!-- ===================== START =====================` and the markers after it:
  one `<section class="lesson" id="...">` per book, with `data-part` (its shelf group),
  `data-title` and `data-min` (minutes). Ids in order: start, anatomy, stack, git,
  forks, hosting, agent, toolkit, claudemd, audit, starter, request, vocab, workflow,
  debug, library, project, quiz, then glossary and sources.
- The `<script>` at the end, in parts marked by comments: storage (`KEY =
  "bac-course-v1"`), `BOOK` (cloth colors, spine titles, heights), `ICON` (cover
  drawings), numbering the books, building the shelves, each book's foot (previous,
  mark as read, next), the library card, the start menu (it fills in the reader's numbers and draws the
  stars on `#introStars`), copy buttons, the quiz
  (`renderQuiz`), the glossary.

## What the browser stores

One `localStorage` entry, `bac-course-v1`: the reader's name and which books are
read. Nothing leaves the phone.
