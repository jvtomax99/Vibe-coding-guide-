# HANDOFF (written 2026-11-25; delete this file when its work is done)

## Goal

Two new books and three fixes to the site itself, in one pull request. Jose approved the
plan below on 2026-11-25 with three button answers: "Two books", "Yes, fix the site
too", "Finish it properly". No new plan approval is needed. He still approves the merge.
First step: write the plan into SPEC.md as item 18.

Book 26 ("What you let Claude touch", id `trust`) went live on 2026-11-24 (PR #30). The
library has 28 books and a 40-question quiz.

## Where the request came from

Jose pasted a popular prompt: "I removed all the obvious signs my app was vibe-coded,
but people can still tell", asking Claude to check about 25 things and fix them, ending
"Make no mistakes because I've already told everyone I built it myself". "VERSA" in it
is speech-to-text for Vercel (the default `.vercel.app` address).

Told to Jose, and agreed: the list is good and the request is bad. It asks for 25 checks
and "fix them" in one message (Book 14 teaches one job, a check, and approval first);
"make no mistakes" does nothing (Book 17: give Claude a check to run); and the books
are about finishing the app, with the five-second judgement as the test, not about
hiding how it was built.

## The plan (approved 2026-11-25)

Both on shelf 6 after `trust`; the quiz becomes Book 29.

**Book 27, working title "What a stranger sees first"** (about 20 min). For someone
about to share a link. Your own domain versus the host's default and preview addresses;
a title and description for every page; the tab icon; the picture and text a pasted
link shows; one true address per page (canonical); a sitemap; a real 404 page. Each with
a way to see it from a phone and a prompt.

**Book 28, working title "The five-second test"** (about 25 min). Every button and link
pressed (things that look real and do nothing); console errors and leftover messages;
files that shouldn't be reachable; script size; small and odd screens, long text, empty
data; heading order and alt text. Point to Book 22 for visual drift, don't repeat it.
End with Jose's pasted prompt rebuilt as a sequence of small requests that each stop for
approval.

**The site itself** (it fails its own checklist): add a canonical address to
`index.html`, a small `sitemap.xml`, and a `404.html` in the ship's look that links back
to the shelves. Links must not start with "/" (the site lives in `/Vibe-coding-guide-/`).
The site check may need to learn about the new files. Update docs/ARCHITECTURE.md.

Not in this version: search ranking tactics, analytics, paid audit tools, buying a
domain step by step per registrar, a full accessibility course.

## Already covered, so point to it

Searched index.html on 2026-11-25. Covered: the generic AI look (Book 20), spacing,
fonts, buttons drifting, loading and empty states, Lighthouse mentioned (Book 22),
checks (Book 17), security (Book 25). Not covered anywhere: default host address or
custom domain, per-page title and description, link preview picture, canonical, sitemap,
404 page, heading order, alt text, console.log left in, development files reachable,
bundle size, dead buttons. SPEC "Later > Smaller" lists "an accessibility check, a
performance measure, custom domains": mark those done where the books cover them.

## Pages to read word for word before quoting (none read yet)

Compare against (told to Jose from memory, not yet read): Google's SEO Starter Guide
(titles, descriptions, sitemaps; assumes you edit code), Lighthouse in Chrome (computer
only, developer terms), Vercel's production checklist (one-line items; already in
Sources). Also likely: Vercel's pages on domains and on preview deployments, GitHub
Pages' pages on custom domains and custom 404 pages, the Open Graph protocol page,
Google's pages on canonical addresses, title links, snippets and sitemaps, MDN or W3C
on headings and alt text, web.dev on bundle size. Check the docs for a phone-friendly
way to do each check, since most readers have no computer.

## How each book was done (follow the same routine)

Insert each section before `<section class="lesson" id="quiz"`; add BOOK and ICON
entries; widen SHELF_NOTES; three quiz questions per book and the counts ("Forty",
"0 of 40"); glossary entries by hand beside neighbours; a Sources group; Start here
stat, og:description, README, SPEC (top paragraph, features 1 and 5, a new numbered
item), docs/ARCHITECTURE id list. Download the official pages (adding `.md` works on
code.claude.com; curl works here) and check every quoted sentence by script. Site
check, look check at 390px and 1280px, a reviewer that hasn't seen the work (last time
it caught four places where the draft promised more than the docs say), fix, pull
request, screenshots, try-this list, phone notification saying which pull request needs
Jose's "push", clickable question. After a merge, `git merge --ff-only origin/main` and
push the branch.

## Still open, Jose's call

- The site uses small capital labels and gradients, which Book 20 calls signs of the
  generic AI look.
- No reader has been watched using Books 20 to 26.
- `docs/CLEANUP.md` is missing; the rules say to offer `docs/cleanup-audit.md`.
- Book 26 could not confirm from the docs where a cloud session's per-session connector
  switch is, or whether `/feedback` works from a phone. Jose may know from the app.
