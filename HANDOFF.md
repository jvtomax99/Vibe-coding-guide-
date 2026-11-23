# HANDOFF (written 2026-11-23; delete this file when its work is done)

## Goal

SPEC.md item 15: four new books Jose approved on 2026-11-23. Two are live, two are left.

- [x] Book 20, "What makes an app look expensive" (id `look`), live, PR #25.
- [x] Book 21, "Decide the look before you build" (id `design`), live, PR #26.
- [ ] "The finishing pass" (id `finish`): drafted in `docs/drafts/book-finish.html`, not in the site yet.
- [ ] "Life after launch": not started.

Jose's rules for this job: one pull request per book; each ends with screenshots at 390px
and desktop, a "try this" list, a phone notification saying it needs his "push", and a
clickable question. He approves each merge. He picked a new chat for the last two books.

## Next step

Put "The finishing pass" into `index.html` as Book 22 on a fresh branch from `main`.

1. Insert `docs/drafts/book-finish.html` right before the line
   `<!-- ===================== PART 6 ===================== -->`.
2. Before inserting, replace every "Book 22" in `index.html` with "Book 23" (they all mean
   "Build your next app from zero", id `project`). The draft already says "Book 23" for it.
   The quiz becomes Book 24. Check the result with a scout: every "Book N" must point at
   the book the sentence means (books are numbered by section order, Start here is 0).
3. Add a `finish` entry to both `BOOK` and `ICON` in the script, and widen the
   `SHELF_NOTES` line for "5 · Making it feel premium".
4. Forward pointers to add now that the book exists: in Book 20, the "Filler words" row
   and the sentence about icon and font licenses can say "Book 22"; in Book 21, the screen
   list's empty, waiting and failed states can point to Book 22.
5. Three quiz questions (append inside `Q.push(...)`), then update "Twenty-eight" and
   "0 of 28 answered" to 31. Glossary terms worth adding: License, Loading state or
   "Skeleton", Reduce motion. The glossary array `G` is NOT sorted by the script and is
   only roughly alphabetical; place entries by hand next to their neighbours.
6. Sources: add the pages named in the draft's last line to "Design and polish", and
   change its intro to "Books 20 to 22".
7. Counts: Start here stat ("24 ... about eight hours" becomes 25 and about eight and a
   half), the `og:description`, README.md, SPEC.md (top paragraph, feature 1, feature 5,
   and the checkbox in item 15), `docs/ARCHITECTURE.md` (the id list).
8. Delete `docs/drafts/book-finish.html` in the same pull request.
9. Site check, look check (shelves, every page of the new book, `#start`, `#audit`), then
   a reviewer subagent that hasn't seen the work, against SPEC.md item 15. Fix what it
   finds, then the pull request.

## Facts already checked for "The finishing pass" (November 2026)

Every quote in the draft was read on the live page. Pages that would NOT load, so nothing
may be quoted from them: Apple's Human Interface Guidelines, Material Design 3 (m3.material.io),
the Google Fonts FAQ. Neither PageSpeed page says it is free, so the draft doesn't claim it.
WCAG's own tap-size minimum is 24 by 24 CSS pixels; the draft quotes web.dev's 48 instead,
which matches Book 15's "44 to 48px".

## Then: "Life after launch"

Goes in "6 · Practice" after `project`, before the quiz. Source list: the "Life after
launch" bullet under "Gaps found in the 2026-11-19 review" in SPEC.md (knowing it broke,
Vercel's one-hour logs on the free plan, bug reports with the version number, backing up
and restoring the shared database, whether Firestore's managed backups need the paid plan,
keeping libraries current, handing an app over). Compare 2 or 3 similar guides first and
write the plan into SPEC.md item 15 before writing the book. Every Vercel, Firebase and
GitHub claim needs a page in Sources read this month.

## What tripped me up

- A book's forward references ("Book 22 covers the words") are wrong until that book
  exists. Write them only when the target book is in the same pull request or already live.
- After a pull request merges, restart the branch from `main` before the next book.
- The reviewer each time caught claims that went a little past the official page. Quote
  the page, or say plainly that it is this library's own advice.
- The site itself uses small capital labels and gradients, which Book 20 lists as signs of
  the generic AI look. A reviewer flagged it as a nitpick. Jose has not been asked whether
  he wants the site brought in line; it is his call, not something to change unasked.

## Files to read first

`CLAUDE.md`, `SPEC.md` item 15, `docs/ARCHITECTURE.md`, `docs/drafts/book-finish.html`,
and in `index.html` the two sections `id="look"` and `id="design"` as the model.
