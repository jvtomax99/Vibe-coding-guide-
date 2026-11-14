Rewritten 2026-11-14 to match the site Jose built in another chat (`index.html`).
Gaps marked TO FILL for Jose.

# SPEC: Building Apps With Claude

## What it is

Site title: **The Launch Manual** (small line: "building apps with Claude"), chosen by
Jose 2026-11-14. The repo and these docs keep the working name.

A one-page course site, drawn as a small library: 18 short books on wooden shelves
(the site says about four hours; the books' own minute counts add to
about five, see Later), plus a Glossary and a Sources book. Tap a spine to take
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
   their browser (`localStorage`, key `bac-course-v1`). "Return all books" clears the
   read marks; the name stays.
   - Done when: closing and reopening the page keeps the name and the read marks.
4. **Copy buttons.** Every prompt and template can be copied with one tap.
   - Done when: tapping Copy puts the exact text on the clipboard and the button says
     "Copied".
5. **Check yourself.** A short quiz with a score.
   - Done when: answering every question shows a score that matches the right answers.
6. **Glossary and Sources.** Plain definitions, and the official pages every claim
   comes from, with the month they were read.
   - Done when: every Claude Code or GitHub claim in the books matches a page listed
     in Sources.
7. **Light and dark.** Follows the phone's setting.
   - Done when: every screen is readable with the phone in dark mode and in light mode.

8. **Start menu.** The first screen of a visit: a realistic picture of a futuristic
   book ("The Launch Manual") on a ship's console with a planet outside, showing the
   reader's name and books read, with three choices: start or continue with the next
   unread book, browse the shelves, or open the Glossary. A choice plays the cover
   opening, then goes there. It never closes by itself. Shown once per visit and
   skipped on a link straight to a book. (Added 2026-11-14.)
   - Done when: each of the three choices lands on the right screen on a phone and on
     a desktop, a reader with books read sees "Continue with Book N" naming their
     next unread book, and with "reduce motion" on the choice goes straight there.

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
- Fix the reading time: the intro and Start here say "about four hours", but the
  books' `data-min` values add up to 308 minutes (about five hours). Change one or the
  other (Jose's call, in `index.html`).

## Phases

- [x] **Phase 0. Project setup.** CLAUDE.md, shared rules, docs, helpers, site check
  (2026-11-14).
- [x] **Phase 1. The site goes live.** Jose's `index.html` on `main`, GitHub Pages on,
  the site check green, screenshots of the live site at 390px and desktop with no
  console errors. Live at https://jvtomax99.github.io/Vibe-coding-guide-/ on
  2026-11-14 (PR #1).
- [ ] **Phase 2.** TO FILL with Jose.
