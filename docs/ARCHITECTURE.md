# Architecture

Short map; keep it current. The whole site is one file, `index.html` (about 2,300
lines: HTML, CSS and JavaScript together), so find a part by its marker below with a
search instead of reading the file top to bottom.

## Files

- `index.html` The site. Fonts come from Google Fonts; nothing else loads from
  outside.
- `404.html` The "not found" page GitHub Pages shows for any wrong address under the
  site: a small page of its own in the ship's colors with one button back to the
  shelves. It can appear at any depth, so every link in it is a full address.
- `sitemap.xml` The one address search engines are asked to list (the site's front
  page). It matches the canonical line and `og:url` in `index.html`.
- `start/` The start menu's pictures and clips, one set for phones (portrait, 780 by
  1690) and one for desktops (1920 by 1200): `closed-*.webp` (the waiting picture),
  `glow-*.webp` (the same with the lights up; it fades in and out over the first),
  `open-*.mp4` and `.webm` (the cover opening), `open-*.webp` (that clip's last frame).
- `icons/` The site's icon in each size (browser tab, phone home screen, link
  preview), all shrunk from `icons/source.png`.
- `start-source/` How the start menu and the icon were made (Blender from Python).
  Not used by the site.
- `.nojekyll` Tells GitHub Pages to serve every file as it is.
- `CLAUDE.md`, `.claude/rules/general.md` Rules for Claude. `.claude/agents/` cheap
  helpers (`scout`, `test-runner`, `builder`). `.claude/skills/taste/` design
  analysis.
- `SPEC.md` What, who, Done when, Not in v1, Later, Phases. `DESIGN.md` the look.
  `CREDITS.md` fonts and other assets with their licenses.
- `docs/` How work is done: `design-rules.md`, `assets.md`, `refactor.md`,
  `cleanup-audit.md`.
- `.github/site-check.cjs` and `.github/workflows/site-check.yml` The check every pull
  request runs, on `index.html` and `404.html`: no missing files, no links starting
  with "/", only full addresses in `404.html`, and each page opens at phone and desktop
  width with no script error.

## Inside index.html

Search for these markers:

- `:root{` The color and font variables: the ship colors (same day and night), then
  the paper page's colors with their dark versions (`prefers-color-scheme: dark` and
  `[data-theme="dark"]`).
- `/* ============ LIBRARY (home) ============ */` The window, the next-book cover,
  the glass shelves and spines. `.library` swaps the page colors for console colors,
  so the shelves are dark in both settings.
- `/* ============ READER (one book open) ============ */` An open book: the dark
  surround, the paper page (`.sheet`), the title page (`.tp`), the Contents page
  (`.cp`), section pages (`.pg.sec`), and the contents beside the page on wide
  screens (`.rail`).
- `id="intro"` The start menu (once per visit, skipped on a link straight to a book):
  the rendered scene from `start/` with three choices, `#introGo` (start or
  continue), `#introOpen` (the shelves) and `#introGloss` (the glossary). A choice
  plays the cover-opening clip, then shows the library or the book. Its styles start
  at `/* Opening (the start menu)`.
- `id="libraryView"` The window picture with the reader's name and count on it
  (`#borrower`, `#readCount`), the next-book cover (`#contLink`), `#resetBtn`, and
  `#case`, where the script builds the shelves.
- `#rail` The book's section list. Beside the page on wide screens; below 1000px the
  Contents button (`openToc()`) adds `.toc-open` to the reader, which pulls the same
  list up over the page with a backdrop (`#tocBack`) and a Close button.
- `id="readerView"` The top bar (back, the text size button `#tszBtn` with its panel
  `#tszPanel`, `#tocBtn`), `#rail`, the page `#sheet` with
  `<main id="main">` holding every lesson, and the foot (`#pgPrev`, `#readProg`,
  `#pgNext`).
- `<!-- ===================== START =====================` and the markers after it:
  one `<section class="lesson" id="...">` per book, with `data-part` (its shelf group),
  `data-title` and `data-min` (minutes), and sometimes `data-open` (a name for the
  page made from whatever comes before the first `<h3>`). Ids in order: start, anatomy, stack, git,
  forks, hosting, backend, updates, stores, agent, toolkit, claudemd, audit, starter, request, vocab, workflow, checks,
  debug, library, look, design, finish, project, after, secure, trust, stranger, fivesec, quiz, then the
  Reference shelf: glossary, sources and kit ("Check my app", a form and not a text).
- The `<script>` at the end, in parts marked by comments: storage (`KEY =
  "bac-course-v1"`), `BOOK` (cloth colors, spine titles, heights), `ICON` (cover
  drawings), numbering the books and cutting each into pages (each lesson gets
  `_pages`: title page, Contents, one per `<h3>`), building the shelves, each book's
  foot (previous, mark as read, next; it sits on the book's last page), the
  next-book cover, turning pages (`go()`, arrows, keys, swipes) and `show()`, the start menu (it fills in the reader's numbers, picks the phone
  or desktop pictures and plays the clip), staying current (`askHost()` compares the page's own date with the
  host's and reloads or shows `#updBtn`), copy buttons, the quiz
  (`renderQuiz`), the glossary, and "Check my app": the six questions (`KQ`), then one
  function per part of the kit (`rules`, `audit`, `fix`, `you`, `notChecked`, `books`),
  each taking the answers and returning text, `facts()`, which turns the answers into the
  yes or no flags those functions use, and `paint()`, which fills the page. To change
  what a kit says, change those functions. Book numbers made by the script are read from
  the page, so they stay right when books move; the few written into the section's own
  text (Books 11, 13, 17, 20, 21 and 25) must be changed by hand.

## What the browser stores

One `localStorage` entry, `bac-course-v1`: the reader's name (`name`), which books
are read (`done`), the page they were on in each book (`pos`), the text size step
(`size`, left out at the default) and the six answers in "Check my app" (`kit`, left out
until one is given). "Return all books" clears `done` and `pos` only. The size is applied as `--tz` on `#main`, which
zooms each lesson. Nothing leaves the
phone.
