Rewritten 2026-11-14 to match the site Jose built in another chat (`index.html`).
Gaps marked TO FILL for Jose.

# SPEC: Building Apps With Claude

## What it is

A one-page course site, drawn as a small library: 18 short books on wooden shelves
(about four hours of reading), plus a Glossary and a Sources book. Tap a spine to take
a book off the shelf, tap again to read it. It teaches how apps are put together
(front end, back end, Git and GitHub, forks, hosting, secrets and data), how Claude
Code works, how to write CLAUDE.md the way Anthropic recommends, how to talk to
Claude, and a full practice build. Every example uses five made-up apps.

## Who it's for

- Jose first, to learn the tools he already uses well enough to explain them.
- Friends and coworkers he hands it to directly, beginners the way he was (Jose,
  2026-11-14). Not a public course for strangers.
- TO FILL: do they already have GitHub accounts? English only, or Spanish later?

## How similar tools do it (checked 2026-11-14)

- GitHub Skills (https://skills.github.com): hands-on courses inside a real repo,
  GitHub only.
- Firebase codelabs (https://firebase.google.com/codelabs/firebase-get-to-know-web):
  official and good, written for developers, Firebase only.
- Paid "vibe coding for non-coders" courses on Udemy: video, mostly one tool each.

Where this one is better: one path across all the tools for people who can't read
code, Anthropic's own CLAUDE.md guidance in plain words, and failures drawn from real
apps (told through the made-up ones).

## Features (as built)

1. **The library.** All 18 books on shelves, grouped in five parts (How your apps
   work, Claude Code, CLAUDE.md Anthropic's way, Talking to Claude, Practice) plus
   Start here and the reference books.
   - Done when: every book opens from its spine on a phone and on a desktop.
2. **Reading a book.** One book open at a time, with previous, next and "mark as
   read" at its foot, and a way back to the shelves.
   - Done when: a reader goes from Start here to the next book and back to the shelves
     without the browser's Back button.
3. **Library card.** The reader's name and how many books they've read, saved only in
   their browser (`localStorage`, key `bac-course-v1`). "Return all books" clears it.
   - Done when: closing and reopening the page keeps the name and the read marks.
4. **Copy buttons.** Every prompt and template can be copied with one tap.
   - Done when: tapping Copy puts the exact text on the clipboard and the button says
     "Copied".
5. **Check yourself.** A short quiz with a score.
6. **Glossary and Sources.** Plain definitions, and the official pages every claim
   comes from, with the date they were read.
   - Done when: every Claude Code or GitHub claim in the books matches a page listed
     in Sources.
7. **Light and dark.** Follows the phone's setting.

## Not in v1

- Accounts, sign-in, or progress that moves between phones.
- A database (no Firestore; decided 2026-11-14).
- Installing to the Home Screen or working offline.
- An AI chat tutor, comments, or anything readers post.
- Video lessons. Spanish.

## Later

- Install and offline (`manifest.webmanifest`, `sw.js`), like Jose's study apps.
- Spanish.
- A short how-to video, like the Citizenship and CPA apps.
- A live demo book showing a real Firestore rule beside the data it protects.

## Phases

- [x] **Phase 0. Project setup.** CLAUDE.md, shared rules, docs, helpers, site check
  (2026-11-14).
- [ ] **Phase 1. The site goes live.** Jose's `index.html` on `main`, GitHub Pages on,
  the site check green, screenshots of the live site at 390px and desktop with no
  console errors.
- [ ] **Phase 2.** TO FILL with Jose.
