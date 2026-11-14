# DESIGN.md: Building Apps With Claude

Written 2026-11-14 from the look already built in `index.html`; the values below are
copied from its `:root` variables. Change a value there and here in the same commit.

## The idea

A reading room: a cream wall, dark wooden shelves, cloth-bound books with gold
lettering, a library card for progress, crimson bookmarks for books read. Warm and
quiet, never techy.

One exception, on purpose (Jose, 2026-11-14): the start menu. It is a futuristic book
floating in space, with stars, two orbit rings, a planet's edge and specks of data
drifting up. The numbers on it are the reader's own (name, books read, and one star
per book on the cover that turns gold once the book is read). It opens onto a paper
page and then the warm library, so the space look never reaches the reading pages.

## Colors (light, then dark)

| Variable | Light | Dark | Used for |
|---|---|---|---|
| `--wall` / `--wall-2` | #F4ECDF / #E9DCC7 | #1A1219 / #0D090C | The background wall |
| `--paper` | #FFFCF6 | #231A20 | Book pages, cards |
| `--ink` / `--muted` | #1F1613 / #7B6A5D | #F3E9DC / #B3A196 | Text, quieter text |
| `--line` | #E6D8C3 | #3A2D33 | Rules and borders |
| `--crimson` / `--crimson-soft` | #B0142F / #F7E4E2 | #E35A70 / #3A1A21 | Accent, bookmarks, main buttons |
| `--caramel` / `--caramel-soft` | #9A6A33 / #F4E8D4 | #D9B26F / #33281B | Second accent |
| `--gold` | #C9A25B | #C9A25B | Spine lettering, details |
| `--wood-hi` / `--wood` / `--wood-lo` | #9A6A43 / #6B4329 / #3E2617 | #8A6440 / #3A2A22 / #140E0B | Shelves |
| `--code-bg` / `--code-ink` | #241A16 / #F3E9DC | #120D10 / #EADFD2 | Prompt and code boxes |
| `--ink-soft` | #EFE6DA | #2C2228 | Soft filled panels |
| `--stripe` | rgba(120,90,60,.035) | rgba(255,255,255,.018) | Faint wallpaper stripes |
| `--spot` | rgba(255,250,240,.9) | rgba(255,196,130,.13) | The lamp glow on the wall |

Each book's own cloth color is in the `BOOK` table in the script, not here.

The start menu has its own colors, set on `.intro` and the same in light and dark
(space is always night):

| Variable | Value | Used for |
|---|---|---|
| `--sp-0` / `--sp-1` / `--sp-2` | #05070F / #0B1230 / #18224F | Space, the cover, the planet |
| `--sp-holo` | #7FE3FF | Glowing lines, orbit, unread stars |
| `--sp-gold` | #E8C88A | Main button, read stars, the cover's inner frame |
| `--sp-text` / `--sp-dim` | #EAF2FF / rgba(190,215,255,.66) | Text, quieter text |
| `--sp-page` and its ink, red, muted | #FBF6EC, #1F1613, #B0142F, #7B6A5D | The paper page inside the book |

The star colors are repeated once in the script that draws the sky (`paint`); change
them in both places.

## Fonts

- `--display` Bodoni Moda: titles and headings.
- `--body` Instrument Sans: everything you read.
- `--script` Pinyon Script: small handwritten touches only ("a reading room for
  builders").
- `--mono` JetBrains Mono: prompts and code.

## Shape

- Rounded corners are small: 4px on most cards and boxes, 2px on fine details, fully
  round (99px) for pills and meters.
- Depth comes from soft, warm shadows and thin inset gold lines on the books
  (`inset 0 0 0 1px #C9A25B` plus a long low shadow), not from heavy borders.
- Main parts: the library card (crimson header, ruled lines like a real card), the
  shelves and spines, the open book (a cloth-colored cover band, then a paper page),
  the reading bar (wood, with "Back to the shelves"), and the prompt boxes (dark, with
  a Copy button).

## Rules

- Use the variables; don't add new hex values in rules. A new color gets a variable
  with both a light and a dark value. (Two older rules already use #B0142F directly;
  leave them unless that part is being changed anyway.)
- Check every change at 390px first, then desktop, in both light and dark.
- Phone layout lives in the `@media (max-width: 760px)` blocks: the main one near the
  end of the `<style>`, plus a one-line one for the cover icon in the reader section.
  Every animation has a `prefers-reduced-motion` fallback; keep that for new ones.
