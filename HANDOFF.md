# Handoff: screen fixes from the November review

**Goal:** fix findings 11 to 15 in `docs/review-2026-11/REVIEW.md`, as one pull request Jose approves before it goes live.

**Done so far:**
- The whole-site review is in `docs/review-2026-11/REVIEW.md`. Its book numbers predate Book 17, so add 1 to any book after 16.
- Findings 1 to 10 (the text fixes) and the Phase 2 check-off are live (PR #22, merged 2026-11-19).

**Next step:** finding 11. At 140% text size, a long file name in a code box title pushes the Copy button past the paper's edge in the Starter kit (Book 13, sections 2, 6 and 7). Let the title wrap or shorten with "...", so the button always stays inside the box.

**Left after that:**
- **12.** Tables with three or four columns turn into tall, narrow strips at 390px (Book 9 modes table, Book 6 sign-in and cron tables, Book 7 update styles). Show each row as a small card on narrow screens. One CSS rule should cover every table.
- **13.** Light-mode grey text is 4.42:1 against the paper, and the minimum is 4.5. It's rgb(102,108,122). Darken that one variable a touch; dark mode already passes.
- **14.** Buttons smaller than 44px:
  - "Return all books": 17px tall.
  - Copy: 27px.
  - Contents: 31px.
  - Text size and Back: 33 to 35px.
  - Page arrows with the phone sideways: 38px.
- **15.** The book count disagrees: the desktop side panel says "Book 1 of 20", the library card says "of 21" and Start here says "21 short books". Now there are 22 numbered books (0 to 21), so pick one count and use it in all three places.

**Files to read first:**
1. `CLAUDE.md`, for the rules and the look check.
2. `DESIGN.md`, for the color variables. Use them, not new hex values.
3. `docs/review-2026-11/REVIEW.md`, findings 11 to 15.
4. In `index.html`, the `/* ============ READER` CSS block and `.code .label`.

**How the earlier sweep was run:** Playwright, every page of every book at 390 light and dark, 390 at 90% and 140% text, 844x390 sideways, and 1280 light and dark. It flagged anything reaching past `#sheet`, page sideways scroll, and console errors. Re-run that after the fixes. Delete this file when the work is done.
