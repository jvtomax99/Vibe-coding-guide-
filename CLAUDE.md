# CLAUDE.md: Building Apps With Claude

A one-page course site (the "library"): the inside of a ship at night, glass shelves, one 3D book per lesson, read one section at a time on a paper page. Written for Jose's friends and coworkers who build apps with Claude and can't read code. Public repo, hosted on GitHub Pages from `main` at https://jvtomax99.github.io/Vibe-coding-guide-/, so merging to main is going live.

## Commands
- Preview: `python3 -m http.server 8000`, then open http://localhost:8000 (nothing to install).
- Site check: `node .github/site-check.cjs index.html`. It also runs on every pull request and must be green before merging.
- Look check: open index.html in Playwright at 390px and 1280px wide, open the shelves (#shelves) and two books (#start, #audit), turn a few pages in each, and report any console errors.

## How the page works (what the code doesn't make obvious)
- Each lesson is a `<section class="lesson" id="...">`. The script turns it into a book: the spine and cover come from the BOOK table (colors, spine title, height) and the ICON table (cover drawing), both keyed by the section id. A new lesson needs an entry in both.
- The script also cuts each book into pages: a title page, a Contents page, then one page per `<h3>`. So every `<h3>` in a lesson starts a new page and shows up in that book's Contents; use `<h4>` for a heading that should stay on the same page. Content before the first `<h3>` goes on the Contents page, unless the section has `data-open="A name"`, which gives it its own first page with that name.
- Books are numbered by their order in the page; text that says "Book N" must be updated when lessons are added or moved.
- Progress, the reader's name and the page they were on in each book live in localStorage under "bac-course-v1". Keep that key so readers keep their progress.
- Links never start with "/": the site lives in the `/Vibe-coding-guide-/` subfolder on GitHub Pages, so they would break there and not locally. The site check catches it.
- The start menu is a rendered picture and clip in `start/` (phone and desktop sets). To change the scene or the cover's title, change `start-source/` and render again; `start-source/README.md` says how. The site's title is "The Launch Manual".
- Colors are the variables at the top of the `<style>`. The ship colors are the same day and night; only the paper page has a light and a dark set (the phone's setting picks). Use them instead of new hex values; `DESIGN.md` lists them.

## Writing rules
- Written for people who can't read code: plain words, no jargon without explaining it.
- Examples use the five made-up apps (FlashDeck, ExamTown, TeamDesk, Corner Gym, Pocket Pet). Never real people's projects.
- No em dashes and no ampersands in the text.
- Any claim about Claude Code or GitHub must match the current official docs; update the Sources book when you use a new page.
- When a book shows a risky shortcut (a key in the code, an open database), it also says what it costs and how to close it, because readers copy what they see.

## Working with me
- I can't read code. End each change with screenshots at 390px and desktop, plus a short "try this" list.
- Changes go on a branch with a pull request; I approve before anything merges to main.
- Another chat also works on this site. Fetch `main` before writing and again before pushing, and edit files in place rather than rewriting them, so neither chat erases the other's work.
- The repo is public: paid raw files (fonts, images, music) can't be committed (`docs/assets.md`, section 9).
- Taste skill (`.claude/skills/taste/`): it asks for the Playwright MCP server; in a cloud session use the installed Playwright instead (`SOURCE.md` there says how).
- "Refactor: CLEANUP.md items ..." means run `docs/refactor.md`.
