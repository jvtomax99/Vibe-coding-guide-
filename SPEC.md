Drafted 2026-11-14 from Jose's one-line brief and his other repos. Gaps marked
TO FILL for Jose. No app code until the TO FILL items in "Phase 0" are answered.

# SPEC: Vibe Coding Guide

Name: TO FILL (working name "Vibe Coding Guide", from the repo name).

## What it is

A free, phone-first web app that walks a beginner from "I have an app idea" to "my
app is live and I can change it safely", using AI to write the code. It covers the
whole chain in one path, in plain English: what vibe coding is and what the human
still has to do, GitHub, Claude Code, hosting (Vercel and GitHub Pages), Firestore,
and the habits from Jose's eight projects that keep a project from breaking. It
installs to the Home Screen and works offline, like his other apps.

## Who it's for

- Jose first: to learn the tools he already uses well enough to explain them.
- Others: TO FILL. Who are they (coworkers, friends, interpreters, strangers online),
  how many, and do they already have a GitHub account? Spanish too, like the
  Citizenship app, or English only?
- What they need (assumed until Jose confirms): short lessons on a phone, no code
  knowledge assumed, every technical word explained, and exact steps they can follow
  with a laptop open next to them.

## How similar tools do it, and where this one can be better

Checked 2026-11-14:

- **GitHub Skills** (https://skills.github.com): free hands-on courses that run
  inside a real repo you create from a template; GitHub Actions checks each step.
  Strong on doing, but it teaches GitHub alone, and assumes you will write the
  changes yourself.
- **Firebase codelabs** ("Get to know Firebase for web",
  https://firebase.google.com/codelabs/firebase-get-to-know-web): build a small
  guestbook with Firestore and security rules. Good and official, but written for
  developers, and it is Firebase only.
- **Paid "vibe coding for non-coders" courses** (many on Udemy, e.g.
  https://www.udemy.com/course/the-complete-vibe-coding-for-non-coders-guide/):
  video courses, mostly tied to one tool (v0, Lovable, Cursor), quality unverified.
  None found covers GitHub, hosting and a database together for non-programmers.

Where ours can be better:

1. **One path across all the tools.** Each vendor teaches only its own piece; the
   hard part for a beginner is how the pieces connect (a merge on GitHub is what
   makes Vercel deploy; a Firestore rule is why a screen is silently empty).
2. **Real failures from real apps.** Jose's repos already hold a list of things that
   broke and why (a forgotten cache bump, Firestore rules that refuse with no error,
   `:hover` that never fires on a phone, iOS zooming on small text boxes). No course
   teaches from that.
3. **The working method, not just the tools.** The rules files Jose uses on every
   project (`CLAUDE.md`, `SPEC.md`, `.claude/rules/general.md`) are the most useful
   thing he has learned. The app explains them and hands them out as a starter kit.

Copy from them: GitHub Skills' "do it in a real repo" approach (our steps end in
something the reader actually did, with a check they can see), and the codelabs'
habit of showing the security rule next to the code that needs it.

## Features (v1)

1. **Lessons.** Short lessons in a fixed order, grouped in paths: Start here (what
   vibe coding is, what the AI does and what you do), GitHub, Claude Code, Hosting,
   Firestore, Going live safely. Each lesson is a few cards; each how-to step links
   the vendor's docs page with the date it was checked.
   - Done when: a reader finishes the Start here path on a phone, and a check script
     fails if any how-to step has no source link or checked date.
2. **Glossary.** Every technical word (repo, commit, branch, pull request, merge,
   deploy, environment variable, collection, document, security rule, service
   worker...) with a one-sentence plain definition. A glossary word in a lesson can
   be tapped to see its definition without leaving the lesson.
   - Done when: every glossary word used in a lesson opens its definition, and the
     check script fails on a lesson word marked as a term that has no entry.
3. **From a real project.** Lessons show where the idea lives in one of Jose's public
   repos, with a link to the real file on GitHub (Interp's `firestore.rules`,
   Citizenship's `sw.js`, the site check workflow).
   - Done when: every link opens a file that exists on that repo's `main` (the check
     script tests them).
4. **Starter kit.** The rules files Jose starts every project with, each explained
   line by line in plain words, with one button to copy it.
   - Done when: a reader can copy `CLAUDE.md`, `SPEC.md` and `general.md` templates
     and the copied text matches the files in this repo.
5. **Your progress.** Lessons you finished are marked, and Home shows where you left
   off. Saved on the phone only (`localStorage`), no account.
   - Done when: closing and reopening the app keeps the marks, offline too.
6. **Installable and offline.** Same pattern as Jose's other apps
   (`manifest.webmanifest`, `sw.js`).
   - Done when: it installs to an iPhone and an Android Home Screen and opens in
     airplane mode.

## Not in v1

- Accounts, sign-in, or progress that moves between phones.
- A live database (see the Firestore decision in Phase 0).
- An AI chat tutor inside the app.
- Comments, a forum, or anything other people post.
- Video lessons (a how-to video like the Citizenship app's can come later).
- Running real git or real deploys inside the app.

## Later

- **A live Firestore demo**: a tiny guestbook in the app, with its security rule
  shown beside it, so the Firestore lesson teaches by showing the real thing.
- Progress synced between phones with Firebase sign-in.
- Quick checks at the end of a lesson, with spaced repetition like the study apps.
- Spanish.
- A how-to promo video made with Remotion, like the Citizenship and CPA apps.

## Phases

- [x] **Phase 0a. Project setup.** `CLAUDE.md`, shared rules, docs, agents, taste
  skill, site check, safe default Firestore rules (2026-11-14).
- [ ] **Phase 0b. Jose's answers.** Fill the TO FILL items:
  - Name, who "others" are, English only or Spanish too, budget.
  - **Hosting.** Recommended: Vercel, because it is one of the tools the app
    teaches, Interp already uses it, and a branch preview link is itself a lesson.
    GitHub Pages is free and simpler (five of Jose's apps use it).
  - **Firestore in v1?** Recommended: no. Progress on the phone is enough for v1;
    the live demo in "Later" teaches Firestore better than hidden sync code would.
  - **DESIGN.md**, following `docs/design-rules.md` section 1 (template or not, then
    1 to 3 sites Jose likes, run through the taste skill).
- [ ] **Phase 1. The shell.** `index.html`, `css/app.css`, `js/app.js`, `sw.js`,
  `manifest.webmanifest`, Home with the list of paths, one sample lesson. Site check
  green; deployed where Phase 0b decided.
- [ ] **Phase 2. Lessons and glossary.** All six paths written with sources, the
  glossary, the content check script.
- [ ] **Phase 3. Real projects and starter kit.** Features 3 and 4.
- [ ] **Phase 4. Progress and offline polish.** Feature 5, install and airplane-mode
  check on real phones.
