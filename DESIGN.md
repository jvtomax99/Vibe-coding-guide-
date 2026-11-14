# DESIGN.md: Building Apps With Claude

Written 2026-11-14 from the look already built in `index.html`; the values below are
copied from its `:root` variables. Change a value there and here in the same commit.

## The idea

A reading room: a cream wall, dark wooden shelves, cloth-bound books with gold
lettering, a library card for progress, crimson bookmarks for books read. Warm and
quiet, never techy.

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

Each book's own cloth color is in the `BOOK` table in the script, not here.

## Fonts

- `--display` Bodoni Moda: titles and headings.
- `--body` Instrument Sans: everything you read.
- `--script` Pinyon Script: small handwritten touches only ("a reading room for
  builders").
- `--mono` JetBrains Mono: prompts and code.

## Rules

- Use the variables; never a new hex value in a rule. A new color gets a variable with
  both a light and a dark value.
- Check every change at 390px first, then desktop, in both light and dark.
- Phone layout changes live in the `@media` blocks at the end of the `<style>`.
