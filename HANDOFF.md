# HANDOFF (written 2026-11-14, delete when this work is done)

## Goal

Jose asked (2026-11-14): "Let's work on the inside of the app. The aesthetic needs to
match the intro. And I want more of a kindle style outline, like Phillis bookshelves
app." So: restyle the shelves and the reading pages to match the start menu (the
rendered space scene), and make reading feel like the Phillis Brown readers.

## What "like Phillis" means (checked in jvtomax99/Phillis-bookshelves-, public)

- Shelf: dark room, one book picked at a time showing its cover, with its title, a
  short line and an "Open the book" button under it. Swipe or arrows to move.
- Reader (`read/<book>/index.html` there): a dark surround with one paper page fixed
  on screen. First a title page, then a "Contents" page (numbered chapters with page
  numbers, the current one in color), then chapters. A footer says
  "THE ASK · P. 3 OF 40". Left and right arrows turn pages.

## Next step

Nothing is built. Jose's rule: show draft pictures first, build only after he picks.
Make Playwright mocks (390px and desktop) and ask him with buttons:

1. The shelves in the space look (dark console, cyan and gold light, books standing
   in the scene). Keep the five shelf groups findable.
2. The reader, in two versions side by side:
   - A (recommended): Kindle look, moved through by section. Title page, a Contents
     page listing the book's sections with numbers, then one section per "page" with
     previous and next, and a footer like "SECTION 3 OF 7". A long section scrolls
     inside its page.
   - B: true page turns like Phillis, one screen of text at a time.

Why A: the books are lessons, not stories. They hold 26 tables and 44 copy boxes
(`starter` has 8, `library` 12). Cutting those at screen height splits tables and
prompt boxes across pages on a phone. Kindle and Apple Books both offer a scrolling
mode beside page turns for this kind of content.

## Decisions already made (do not reopen)

- Start menu: rendered Blender scene, live since PR #4. Site title "The Launch Manual".
- Site icon: the book and the planet, live since PR #5.
- Jose wants realistic over flat, previews before building, and says "push" to approve
  a merge. A push notification every time something needs him.

## Risks to raise with Jose

- DESIGN.md says the reading room is "warm and quiet, never techy". This request
  reverses that for the whole site; DESIGN.md needs rewriting, not patching.
- Dark surround is fine, but the page people read for 15 minutes should stay light
  paper (or offer a dark page that follows the phone's setting, as today).
- Keep the `bac-course-v1` storage key and every book id, so progress and shared
  links (`#audit`) keep working.
- This is a big feature under `.claude/rules/general.md`: plan, mocks, his OK, and a
  reviewer subagent before the pull request. SPEC.md needs a Phase 2 entry for it.

## Files to read first

`docs/ARCHITECTURE.md`, `DESIGN.md`, `SPEC.md`, then in `index.html` the markers
`/* ============ LIBRARY (home)`, `/* ============ READER (one book open)`, the
`BOOK` and `ICON` tables, and `function show()`.

## Rendering tools (only if new pictures are needed)

`start-source/README.md` says how to render. Blender is not installed in a fresh cloud
session: `pip install bpy pillow`, and ask Jose first (installing outside the package
list). A full re-render takes about two hours on 4 cores.
