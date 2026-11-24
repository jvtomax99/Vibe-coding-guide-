Rewritten 2026-11-14 to match the site Jose built in another chat (`index.html`).
Gaps marked TO FILL for Jose.

# SPEC: Building Apps With Claude

## What it is

Site title: **The Launch Manual** (small line: "building apps with Claude"), chosen by
Jose 2026-11-14. The repo and these docs keep the working name.

A one-page course site, drawn as a small library aboard a ship: 28 short books on glass shelves
(about nine and a half hours of reading), plus a Glossary and a Sources book. Tap a spine to take
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

1. **The library.** All 28 books on shelves, grouped in six parts (How your apps
   work, Claude Code, CLAUDE.md Anthropic's way, Talking to Claude, Making it feel
   premium, Practice) plus
   Start here and the reference books.
   - Done when: every book opens from its spine on a phone and on a desktop.
2. **Reading a book.** One book open at a time as a paper page on a dark surround,
   turned a section at a time: a title page, a Contents page listing the book's
   sections, then one section per page (a long one scrolls inside its page). Arrows,
   the keyboard's arrow keys or a sideways swipe turn the page; the foot of the screen
   says where you are ("SECTION 2 OF 4"); the Contents button pulls the book's section
   list up over the page, with the current section marked, and a tap jumps there (on a
   wide screen the same list sits beside the page). The Contents page is still the
   second page of each book. (Pull-up list added 2026-11-15 at Jose's request.) The book reopens on the page you
   left. Previous book, next book and "mark as read" are on the last page.
   (Reworked 2026-11-14, Phase 2.)
   - Done when: a reader goes from Start here to the next book and back to the shelves
     without the browser's Back button; every section of a book can be reached from
     its Contents; and no table or copy box is cut by a page turn.
3. **Library card.** Now the top of the shelves screen: the reader's name and how many books they've read, saved only in
   their browser (`localStorage`, key `bac-course-v1`). "Return all books" clears the
   read marks and the saved pages; the name stays.
   - Done when: closing and reopening the page keeps the name and the read marks.
4. **Copy buttons.** Every prompt and template can be copied with one tap.
   - Done when: tapping Copy puts the exact text on the clipboard and the button says
     "Copied".
5. **Check yourself.** A quiz with a score: 40 questions, three of them on each of
   Books 6, 7 and 8 (added 2026-11-15), three on Book 17 (added 2026-11-19) and three
   each on Books 20, 21, 22 and 24 (added 2026-11-23) and three each on Books 25 and 26 (added
   2026-11-24). Each of those thirty right answers is what the book itself says.
   - Done when: answering every question shows a score that matches the right answers.
6. **Glossary and Sources.** Plain definitions, and the official pages every claim
   comes from, with the month they were read.
   - Done when: every Claude Code or GitHub claim in the books matches a page listed
     in Sources.
   - Sources ends with "Going further": outside reading and watching (what vibe coding
     is, doing it well, doing it safely), marked as other people's views, not as the
     source of the books' claims. Start here carries the library's own rule for what
     always gets a check before launch. (Added 2026-11-14.)
7. **Light and dark.** The paper page follows the phone's setting. The ship around it
   (shelves, start menu, the surround of an open book) is always night.
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

9. **Stays current.** No download and no update button to hunt for: when the site
   comes back to the front of the phone (and a few seconds after it opens), it asks
   the host whether the page has changed. If it has, the start menu and the shelves
   reload by themselves; inside a book a small "New version. Tap to refresh" button
   appears instead, and the reload happens on the tap or on going back to the
   shelves. (Added 2026-11-14.)
   - Done when: with the site left open on the shelves, a change merged to main shows
     up the next time the reader comes back to it, without them refreshing; and a
     reader inside a book is never reloaded without tapping.

10. **Book 6, "Your first back end".** Added 2026-11-15 (Jose's OK on the plan the same
   day). Seven sections: do you need one (three questions and what it starts costing),
   which login to pick, Firebase from zero, rules (an open one beside a safe one, and how
   a rule goes live), Vercel from zero, scheduled jobs and their limits, a before-launch
   check. Each section names the month it was checked against the official pages.
   - Compared: Firebase's own codelab and quickstarts (written for developers, assume a
     command line), Vercel's getting-started pages (one service only), and paid no-code
     courses (mostly one tool, rarely the costs). Where this one differs: it starts with
     whether to have a back end at all, and every risky shortcut comes with its cost and
     its fix.
   - Changed from the plan: "emailed code" became "emailed link", because Firebase's own
     page offers only a link; the book says what a code would take.
   - Not in it: payments, push notifications, App Check setup (one paragraph on what it
     is), Supabase beyond the existing mention in Book 5.
   - Done when: the book opens from its spine as Book 6 at 390px and desktop, all seven
     sections are reachable from its Contents, every Firebase and Vercel step matches a
     page listed in Sources, and every "Book N" in the other books points at the right
     book.

11. **Book 7, "Updates without reinstalling".** Added 2026-11-15 (Jose's OK on the plan
   the same day). Six sections: why people keep seeing the old version, apps with no
   offline worker, three update styles for apps with one, what never updates by itself
   (name, icon, saved data), store wrappers in brief, and asking Claude for it (a
   version on screen, a two-phone test). It steers readers to no offline worker unless
   they need the app without signal.
   - Compared: web.dev's "Learn PWA: Update" and service worker lifecycle (the same
     patterns, in code, for developers), MDN's service worker guide (correct on the
     waiting rule, also code-first), Capacitor's "Deploying updates" (one line on what is
     allowed, then a paid product). Where this one differs: it starts from the symptom,
     gives a pick-one table and a prompt per style.
   - Not in it: building a store wrapper or submitting to a store, paid live-update
     services, push notifications, worker code to read.
   - Done when: the book opens from its spine as Book 7 at 390px and desktop, all six
     sections are reachable from its Contents, every claim about browsers and stores
     matches a page listed in Sources, and every "Book N" elsewhere points at the right
     book.

12. **Book 8, "From web app to the App Store and Play Store".** Added 2026-11-15 (Jose's
   OK on the plan the same day). A book for deciding, not a build guide. Six sections:
   do you need a store at all, the three routes, accounts and fees, why thin wrappers
   get rejected, what you can't do from a phone, deciding and asking Claude.
   - Compared: Capacitor's docs (assume a Mac, a terminal and Node, and never ask
     whether to do it), Apple's and Google's own pages (fees and rules, one store each,
     for developers), Chrome's Trusted Web Activity pages (Play Store only). web.dev's
     "PWAs in app stores" page is gone and PWABuilder's docs would not load, so neither
     is used. Where this one differs: "should you?" comes first and both stores sit side
     by side.
   - Not in it: step-by-step Xcode or Android Studio, store listings and screenshots,
     payments and in-app purchases, push notifications, paid build services, how to do
     a rewrite.
   - Done when: the book opens from its spine as Book 8 at 390px and desktop, all six
     sections are reachable from its Contents, every fee and rule matches a page listed
     in Sources, and every "Book N" elsewhere points at the right book.

13. **Text size.** Added 2026-11-15 at Jose's request (plan OK'd the same day). An "Aa"
   button beside Contents opens a smaller A and a bigger A: five steps, 90% to 140%,
   default 100%. The size applies to everything on the paper page, tables and copy boxes
   included, and is saved in `bac-course-v1` as `size`; "Return all books" keeps it, like
   the name. After a change the reader stays on the paragraph they were reading.
   - Compared: Apple Books (small and big A, fonts under Customize; users report the
     control sometimes missing), Kindle (Aa menu with a size slider, spacing and margins,
     pinch to resize). Where this one differs: one control in plain sight, and the place
     is kept on a resize.
   - Not in it: fonts, line spacing, margins, extra themes, pinch to resize.
   - Done when: at 390px, sideways and desktop, every step changes the page, nothing on
     a page reaches past the paper's edge at 140% (wide tables scroll inside their own
     box, as at 100%), the reader stays on the same paragraph, and the size survives a
     reload and "Return all books".

14. **Book 17, "Checks you can trust".** Added 2026-11-19 (Jose's OK on the plan the
   same day), after a gap review found the library tells readers to insist on checks but
   never how to tell a real check from a fake one. Six sections: why "all tests pass"
   proves little (four ways a check lies), break it on purpose, what your checks should
   cover, reading a pull request without reading code, a lock on the checks (a CLAUDE.md
   line and a GitHub warning when tests change), and a second opinion. Placed after The
   workflow, so Debugging, Prompt library and Build from zero became Books 18 to 20.
   - Compared: Google's "What to look for in a code review" (asks whether tests would
     fail when the code is broken, but assumes reading every line), GitHub's review docs
     and GitHub Skills course (the buttons, not judging), Stryker's mutation testing intro
     (for developers with a tool). Where this one differs: moves that need no code
     reading, a red-flag list read off the Files changed screen, and a lock GitHub runs.
   - Not in it: writing or reading tests, test tools, coverage numbers, CODEOWNERS (a
     solo owner can't approve their own pull request), setting up CI (Build from zero does).
   - Done when: the book opens from its spine as Book 17 at 390px and desktop, all six
     sections are reachable from its Contents, every Anthropic and GitHub claim matches a
     page in Sources, every "Book N" elsewhere points at the right book, and the quiz has
     22 questions.

15. **Part 5, "Making it feel premium", and "Life after launch".** Asked by Jose
   2026-11-23: "anything that can help make an app through vibe coding that feels
   premium and elevated ... without guessing." Plan OK'd the same day: three design
   books in a new part between Talking to Claude and Practice, then a fourth book,
   "Life after launch", in Practice after Build from zero. One pull request per book.
   - [x] **Book 20, "What makes an app look expensive"** (2026-11-23). Six sections: why
     AI-built apps look alike, one most important thing per screen, space and text sizes
     from a short list, one accent color and a contrast number, corners shadows and
     icons, a ten-line checklist with a review prompt. Build from zero became Book 21.
   - [x] **Book 21, "Decide the look before you build"** (2026-11-23). Six sections: map
     the screens (paper or Claude Whiteboards), references, DESIGN.md with its CLAUDE.md
     line, Claude Design and its handoff to Claude Code, three options and a screenshot
     beside the mockup, the frontend-design plugin. Build from zero became Book 22.
     Changed from the plan: the plugin section says plainly that a cloud session doesn't
     load plugins installed on a computer, so phone readers are steered to DESIGN.md.
   - [x] **Book 22, "The finishing pass"** (2026-11-23). Six sections: the empty,
     loading, error and too-much screens; tap feedback and movement, with the reduce
     motion setting; the words; fonts, icons and pictures with their licenses (and the
     cost of committing a paid one); the real-phone test with a speed check and an
     accessibility check; a fresh-eyes review and when to stop. Build from zero became
     Book 23. Nothing is quoted from Apple's Human Interface Guidelines, Material
     Design or the Google Fonts FAQ: those pages would not load for the fact-check.
   - [x] **Book 24, "Life after launch"** (2026-11-23), in Practice after Build from
     zero; the quiz became Book 25. Plan: for one person who can't read code looking
     after an app friends or coworkers use, on the free plans. Six sections: knowing it
     broke (what Vercel and Firebase tell you for free, and a daily check on GitHub
     Actions), a "Report a problem" button built on Book 7's version number, going back
     before fixing, backing up a shared database, keeping libraries current with
     Dependabot, handing over and switching off. Not in this version: paid monitoring
     or error-tracking services, on-call or incident process, analytics, privacy and
     deleting data on request (its own gap under Later).
     Answer to the open question: Firestore's scheduled backups, point-in-time recovery
     and export all need the Blaze plan, so the book's free route is an owner-only
     backup button and a tested restore.
     Compared: Vercel's production checklist (written for teams; its answers to this
     book's questions are Log Drains and Observability Plus, both paid), Firebase's
     launch checklist (the closest; the book quotes it on owners and budget alerts, but
     it stops at launch day and says nothing on backups) and the Open Source Guides'
     "Best Practices for Maintainers" (about people and process, for projects with
     contributors). Where this one differs: free plans only, each job ends in a prompt,
     and it covers getting data back and handing over, which none of the three do for
     a one-person app.
     Not claimed because the page could not be read word for word: that GitHub switches
     off scheduled checks in a quiet public repo, GitHub's account successor setting,
     and emails for failed Actions runs. The daily-check prompt asks Claude instead.
   - Compared: Refactoring UI (the closest in spirit; a paid book, $99 to $149, written
     for developers), Apple's Human Interface Guidelines (a large reference for
     designers; its pages would not load for the fact-check, so nothing is quoted from
     it), and Anthropic's frontend-design plugin (instructions for Claude, not for the
     person judging the result). Where this one differs: no code and no design training
     needed, rules as short lists, and each book ends in prompts and a checklist.
   - Not in it: a Figma tutorial, logo or brand design, 3D scenes, animation libraries,
     paid template walkthroughs.
   - Done when (each book): it opens from its spine at 390px and desktop, every section
     is reachable from its Contents, every claim about an Anthropic product or a
     standard matches a page in Sources, every "Book N" elsewhere points at the right
     book, and the quiz count on the page matches the number of questions.

16. **Book 25, "Strangers will try things"** (2026-11-24). Asked by Jose 2026-11-24 from
   the "Security beyond keys and rules" gap under Later; plan OK'd the same day. In
   Practice after Life after launch; the quiz became Book 26. For a reader whose app
   other people use and who can't read code. Six sections: who attacks a small app,
   text one person types and another sees (with a harmless test line), apps that send
   people's words to Claude, a second sign-in step and recovery codes, GitHub's secret
   scanning and push protection, code from strangers (fixed versions, an integrity
   check, the package name checked).
   - Not in this version: Claude Code as a risk (outside MCP servers, skills and
     plugins; its own gap under Later), privacy and work rules (also under Later), paid
     scanners and firewalls. It says plainly that it closes common holes and that an app
     holding money, health or children's data needs a paid review.
   - Compared: OWASP's Top 10 (2025) and its Top 10 for LLM Applications (the standard,
     "for developers"; titles and developer fixes), MDN's page on cross-site scripting
     (accurate, long, every example in code) and the Security section of Vercel's
     production checklist (fourteen one-line items, half for paid plans, none explained).
     Where this one differs: every risk comes with a test or a prompt a non-programmer
     can run.
   - Left out because no official page was found: whether Anthropic's Console has a
     second sign-in step, and AI tools inventing package names.
   - Done when: as item 15's "Done when (each book)".

17. **Book 26, "What you let Claude touch"** (2026-11-24). Asked by Jose 2026-11-24 from
   the "Claude Code as a risk" gap under Later; plan OK'd the same day ("Write it as
   planned"). In Practice after Strangers will try things; the quiz became Book 27. For a
   reader who builds from a phone in cloud sessions and can't read code. Six sections:
   Claude works with your access (and the three things that are dangerous together),
   pages and files that give orders, connectors and MCP servers, plugins, skills and
   hooks, modes and limits (auto mode, the mode never to use, deny rules, the cloud
   network setting), and what to do when something looks off. Cloud sessions come first
   in every section; the terminal is the second case.
   - Not in this version: writing MCP servers or hooks, setting up the terminal sandbox,
     company-managed settings, browser agents.
   - Compared: Simon Willison's "The lethal trifecta" (written for people who use these
     tools; names the danger, gives no steps), the MCP specification's Security Best
     Practices (for people who build servers; needs code and OAuth) and OWASP's
     "Excessive Agency" (for developers designing an AI feature). Where this one
     differs: every risk comes with a setting a non-programmer can check from a phone
     or a prompt to send, and it says which limits are enforced and which are only
     requests.
   - Not quoted, because the page was not read in full: the hooks reference's
     "Security considerations" and the MCP page's scope definitions.
   - Done when: as item 15's "Done when (each book)".

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
- The two YouTube links in Sources ("Going further") were never opened by a person; a
  robot can't check them. Jose taps both, and any dead one is replaced or removed.

### Gaps found in the 2026-11-19 review (Book 17 came from the first one)

- **Security beyond keys and rules (done: Book 25).** What users type and the app shows to others
  (cross-site scripting; today one word, "escaped", in the Prompt library). Prompt
  injection in apps that send users' text to the Claude API, and showing model output as
  HTML (OWASP Top 10 for LLM apps lists it first). Two-factor sign-in on GitHub, Google,
  Vercel and Anthropic. (What to do when a key leaks is done: Books 3 and 5, PR #22.) GitHub
  secret scanning and push protection. Code from strangers: CDN scripts, pinned versions,
  made-up package names.
- **Claude Code as a risk (done: Book 26).** Third-party MCP servers, skills and plugins run with your
  access; pages and files Claude reads can carry instructions.
- **Life after launch (done: Book 24).** Knowing it broke (logs kept one hour on Vercel's free plan),
  users reporting bugs with the version number, backing up and restoring the shared
  database (check whether Firestore's managed backups need the paid plan), keeping
  libraries current, and handing an app over (TeamDesk has one non-developer behind it).
- **Other people's data, at work.** A plain privacy note, deleting data on request,
  collecting less. For coworkers: whether the employer allows a work tool on a personal
  Firebase project that sends colleagues' messages to an outside AI service.
- **Debugging is thin (about 340 words).** Revert first when live breaks, find which
  change broke it, tell a code bug from a settings bug Claude can't see, what to do when
  Claude goes in circles.
- **Smaller.** An accessibility check to run, a performance measure, a one-page payments
  decision (hosted checkout, never touch card numbers), custom domains.
- **Reading order.** Books 6 to 8 (about 10,000 words) come before How Claude Code works,
  and "Before step 1" was in the last book (moved to Start here in PR #22). A beginner path: Start here, a first tiny
  build, How Claude Code works, Checks you can trust, then the rest when needed.

## Phases

- [x] **Phase 0. Project setup.** CLAUDE.md, shared rules, docs, helpers, site check
  (2026-11-14).
- [x] **Phase 1. The site goes live.** Jose's `index.html` on `main`, GitHub Pages on,
  the site check green, screenshots of the live site at 390px and desktop with no
  console errors. Live at https://jvtomax99.github.io/Vibe-coding-guide-/ on
  2026-11-14 (PR #1).
- [x] **Phase 2. The inside matches the start menu.** Checked off 2026-11-19: every Done when line below tested at 390px and desktop (every book open from its spine, every Contents entry reaches its section, an old save keeps its name and read marks, `#audit` opens its book, dark and light both readable). Results in `docs/review-2026-11/REVIEW.md`. Asked by Jose 2026-11-14: "The
  aesthetic needs to match the intro. And I want more of a kindle style outline, like
  Phillis bookshelves app." The shelves become glass ledges on the ship's dark console
  with navy books and gold lettering, and the next book shown as a cover with "Open
  the book". Reading becomes feature 2 above. Jose picked from draft pictures: sections
  instead of screen-height page turns, the drafted shelves, and a page that follows
  the phone's setting.
  - Compared (2026-11-14): Jose's Phillis Brown readers (true page turns, title page,
    numbered Contents, "P. 3 OF 40"), Kindle and Apple Books (both offer a scrolling
    mode beside page turns). Where this one differs: pages are whole sections, because
    the books hold 26 tables and 44 copy boxes that screen-height pages would squeeze
    or strand.
  - Not in this phase: a font size control, bookmarks or highlights, a search across
    books, shelves rendered in Blender.
  - Done when: the Done when lines of features 1, 2 and 7 hold at 390px and desktop,
    old links such as `#audit` still open their book, and a reader's saved name and
    read marks from before the change are still there.
