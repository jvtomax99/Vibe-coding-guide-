# DESIGN.md: Building Apps With Claude

Rewritten 2026-11-14 for Phase 2 (the inside now matches the start menu). The values
below are copied from the `:root` variables in `index.html`. Change a value there and
here in the same commit.

## The idea

A small library aboard a ship. Everything outside the page is night: a dark console,
a planet in the window, glass shelves lit along their front edge in cyan, navy books
with gold lettering. The one warm, bright thing is the paper page you read.

- **Start menu.** A realistic picture, rendered in Blender the same way as the Phillis
  Brown site's start screen: a dark book with gold lettering ("The Launch Manual") on
  a ship's console, three glowing light pillars, a glass orb, and a planet outside the
  window. The lights breathe while it waits. A choice plays a short clip of the cover
  opening. The reader's name and books read sit on top of the picture as text; nothing
  about a reader is baked into the picture.
- **Shelves.** The top of that same picture (the window and the planet) as a band,
  with the reader's name and count on it, then the next book as a cover with "Open
  the book", then one glass ledge per part. Tap a spine and the book turns to show
  its cover.
- **An open book.** A dark surround with stars and one paper page, like the readers
  in the Phillis Brown site: a title page, a Contents page, then one section per
  page. A foot line says where you are ("AUDIT A CLAUDE.MD · SECTION 2 OF 4").

Realistic over flat (Jose, 2026-11-14): light comes from somewhere, books have
thickness and a lit edge, glass glows. No flat color blocks.

## Colors

The ship (same in light and dark; space is always night):

| Variable | Value | Used for |
|---|---|---|
| `--void` | #05070F | The background, text on gold buttons |
| `--hull` / `--panel` | #0A0F1E / #0E1629 | Darker and lighter console surfaces |
| `--holo` (`--holo-rgb`) | #7FE3FF | Edge light on the shelves, outlines, small labels |
| `--sgold` / `--sgold-lo` | #E8C88A / #C9A25B | Main buttons, lettering, bookmarks, meters |
| `--stext` / `--sdim` | #EAF2FF / rgba(200,220,255,.74) | Text on the dark, quieter text |

The paper page (light, then dark; the phone's setting picks):

| Variable | Light | Dark | Used for |
|---|---|---|---|
| `--paper` | #F8F5EE | #121827 | The page |
| `--ink` / `--muted` | #141824 / #666C7A | #E7EDF8 / #98A3B8 | Text, quieter text |
| `--line` | #DDD6C8 | #273149 | Rules and borders |
| `--soft` / `--ink-soft` | #EFEBE1 / #ECE7DC | #182036 / #1C2540 | Soft filled panels, inline code |
| `--accent` / `--accent-soft` | #0F6C86 / #E0EEF1 | #7FE3FF / #12303B | Links, section labels, main buttons on the page |
| `--accent-2` / `--accent-2-soft` | #8A6A2B / #F3EAD6 | #E8C88A / #2E2718 | Second accent ("try this" boxes, small rules) |
| `--gold` | #C9A25B | #C9A25B | Focus rings, fine details |
| `--code-bg` / `--code-ink` | #0B1020 / #DCE8F7 | #070B16 / #DCE8F7 | Prompt and code boxes |

Inside `.library` the page variables are swapped for console values (`--paper` becomes
`--panel`, `--ink` becomes `--stext`, `--accent` becomes `--holo`), so the shelves are
dark in both settings without a second set of rules.

Each book's own cloth color is in the `BOOK` table in the script, not here: one color
family per shelf (navy, teal, plum, graphite, oxblood; old gold for Start here; pale
silver for the two reference books).

The start menu keeps its own `--sp-*` variables on `.intro`. They hold the same values
as the ship colors above. The picture's own colors (navy shell, gold foil, cyan and
amber light) are set in `start-source/scene.py` and `start-source/tex.py`.

## Fonts

- `--display` Bodoni Moda: titles and headings.
- `--body` Instrument Sans: everything you read.
- `--mono` JetBrains Mono: prompts and code, and the small spaced-out capital labels
  on the dark ("BOOKS READ", "SECTION 2 OF 4").

## Shape

- Rounded corners are small: 4px on most cards and boxes, 2px on fine details, fully
  round for pills, meters and the page-turn buttons.
- On the dark, depth comes from light: a cyan line along an edge, a soft glow, a deep
  shadow underneath. On the page, depth comes from the stacked paper edge and a faint
  shadow down the inner margin.
- Main parts: the window band, the next-book cover, the shelves and spines, the open
  book (top bar with "Back to the shelves" and Contents, the paper page, the foot
  with the two round page-turn buttons), and the prompt boxes (dark, with a Copy
  button).

## Rules

- Use the variables; don't add new hex values in rules. A new page color gets a
  variable with both a light and a dark value. A new ship color gets one value.
- Check every change at 390px first, then desktop, in both light and dark.
- Phone layout lives in the `@media (max-width: 760px)` block near the end of the
  `<style>`; wide-screen layout (the contents beside the page, the cover beside the
  shelves) in the `@media (min-width: 1000px)` blocks. Every animation has a
  `prefers-reduced-motion` fallback; keep that for new ones.
- Every `<h3>` in a lesson starts a new page. Use `<h4>` for a heading that should not.
