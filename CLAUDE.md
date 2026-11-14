# CLAUDE.md: Building Apps With Claude

A one-page course site (the "library"): cream wall, wooden shelves, one 3D book per lesson. Public repo, hosted on GitHub Pages, so merging to main is going live.

## Commands
- Preview: npx serve . then open http://localhost:3000
- Check: open index.html in Playwright at 390px and 1280px wide, open the shelves (#shelves) and two books (#start, #audit), and report any console errors.

## How the page works (what the code doesn't make obvious)
- Each lesson is a `<section class="lesson" id="...">`. The script turns it into a book: the spine and cover come from the BOOK table (colors, spine title, height) and the ICON table (cover drawing), both keyed by the section id. A new lesson needs an entry in both.
- Books are numbered by their order in the page; text that says "Book N" must be updated when lessons are added or moved.
- Progress and the reader's name live in localStorage under "bac-course-v1". Keep that key so readers keep their progress.

## Writing rules
- Written for people who can't read code: plain words, no jargon without explaining it.
- Examples use the five made-up apps (FlashDeck, ExamTown, TeamDesk, Corner Gym, Pocket Pet). Never real people's projects.
- No em dashes and no ampersands in the text.
- Any claim about Claude Code or GitHub must match the current official docs; update the Sources book when you use a new page.

## Working with me
- I can't read code. End each change with screenshots at 390px and desktop, plus a short "try this" list.
- Changes go on a branch with a pull request; I approve before anything merges to main.
