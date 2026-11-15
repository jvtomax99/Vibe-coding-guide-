# HANDOFF (written 2026-11-15)

Delete this file when Jobs 2 and 3 are done.

## Goal

Make The Launch Manual a guide that lets Jose's friends, who can't read code, repeat what
he did with his own apps without guessing. Three jobs, one at a time, stopping for Jose's
OK after each:

1. **Audit** the 20 books against the current official docs. DONE, nothing edited. Results below.
2. **Fix and fill** the existing books from the approved audit.
3. **New books**, one at a time, each with a plan, a comparison with 2 or 3 similar guides,
   and Jose's OK before building:
   (a) "From web app to the App Store and Play Store": the three routes (installable web
   app, a wrapper such as Capacitor, a full rewrite), costs, developer accounts and fees,
   and the review rules that get thin wrappers rejected (Apple's minimum functionality
   rule, Google's tester requirement for new personal accounts). Check each against the
   current Apple and Google pages before writing.
   (b) "Updates without reinstalling": how a new version reaches users on each route, what
   can and can't change without a new store review, and the prompt to ask Claude for it.
   (c) "Is my app safe?": one checklist book on keys and secrets, database rules, logins,
   and what to ask Claude to check before sharing an app.
   The audit also suggests a fourth, "Your first back end" (gaps 5 to 7 below). Not decided.

## Next step

Jose answered the three questions on 2026-11-15: fix everything in the audit and fill
gaps 1, 2, 3 and 8, as two pull requests; rename the leaked names and shift TeamDesk's
numbers; go on without the two unread repos (retry before Job 3b).

On 2026-11-15 Jose widened the job: all ten gaps go in the guide, including things his
own apps don't do yet. Order he chose: (1) pull request #9, the audit's fixes, which he
merges first; (2) one pull request for gaps 1, 2, 3, 8 and 9 in Start here, Book 5 and
Book 16, written and checked, waiting on #9; (3) three new books, one pull request each,
each with a short plan he OKs first: "Your first back end" (gaps 5, 6, 7), "Updates
without reinstalling" (gap 4), "From web app to the App Store and Play Store" (gap 10).
"Is my app safe?" stays on the list after those.

State on 2026-11-15: #9 is merged. Step (2) is pull request #10, waiting for Jose's
"push". Jose OK'd the plan for "Your first back end": new Book 6, right after Hosting,
seven sections: do you need one (a three-question test and what it starts costing);
which login to pick (none, anonymous, emailed code, Google); Firebase from zero (make the
project, turn on sign-in, where the config goes); rules (an open rule beside a safe one,
and how rules get from the repo to the live database); Vercel from zero (connect the
repo, add a key, read function logs); scheduled jobs and their limits; a before-launch
check prompt. Not in it: payments, push notifications, App Check setup (one paragraph
on what App Check is), Supabase beyond the existing mention. Each section says the month
it was checked. Fetch every Firebase and Vercel step from the official page that day.
Update, later on 2026-11-15: #10 is merged. "Your first back end" is written as Book 6
(id `backend`) on the branch `first-back-end`, with its pull request waiting for Jose's
"push". Books 6 to 17 became 7 to 18, and the count is 19. Next after that merge: a short
plan for "Updates without reinstalling", then Jose's OK, before any writing.
Update 2: #11 is merged. Jose OK'd the plan for "Updates without reinstalling" (six
sections, Book 7 after the back-end book, without reading the two private repos). It is
written as Book 7 (id `updates`) on the branch `updates-book`, pull request waiting for
Jose's "push". Books 7 to 18 became 8 to 19, and the count is 20. Next: a short plan for
"From web app to the App Store and Play Store", then Jose's OK. Open question for Jose:
whether "Is my app safe?" is still needed now that Book 6 ends with a before-launch check.
Leftover merged branch `first-back-end` can also be deleted (ask Jose).
A leftover branch, `day-one-steps`, holds the same commit as #10 and can be deleted
once #10 is merged (ask Jose first). A new book needs a BOOK and an ICON
entry, and every "Book N" in the text after it renumbered.

Corrections to the audit table below, found while re-checking: the Windows symlink note
IS still on Anthropic's memory page, so it stayed. Vercel's terms do say the free plan is
for "personal or non-commercial use". The cloud pages say each session gets "its own
branch" and never mention a claude/ prefix. The settings page says nothing about path
rules in project threads, so the guide does not claim it.

Also still open: Jose should tap the two YouTube links in Sources, section 3. They could
not be checked by a robot.

## Done

- Job 1, the audit (below).
- A side change, live on main through pull request #8: Start here gained section 4, "What
  needs a check before launch"; Book 5 gained the Lovable case and Supabase's Row Level
  Security; the Glossary gained three entries; Sources gained "Going further". To undo it,
  press "Revert" on pull request #8.

## Left

- Job 2, then Job 3 (a), (b), (c).
- Two facts to confirm before writing: Vercel's free plan being personal use only, and
  cloud sessions working on a `claude/...` branch.

## Rules for the next chat

- Jose's other repos are for learning what he did, read only. Never change them, never
  name them in the guide, never copy their details. Reels and claude-skills are private.
  Examples use only FlashDeck, ExamTown, TeamDesk, Corner Gym and Pocket Pet.
- This file is in a public repo. Keep it free of anything from the private repos.

## Files to read first

`CLAUDE.md`, `SPEC.md`, `docs/ARCHITECTURE.md`, then this file. `index.html` holds every book.

## The audit (Job 1, 2026-11-14)

About 70 claims were checked against the live official pages. Most of the guide is
accurate. Reels and Cat-app were not read; the app findings cover six apps.

### Part 1: fact check

I checked about 70 claims against the live pages. Most of the guide is accurate, and the Anthropic quotes match the current best-practices page nearly word for word. These are the ones that are not right.

| Book | Claim | Verdict | Official page | Fix |
|---|---|---|---|---|
| 8 CLAUDE.md, 9 Audit, Glossary | "Claude Code reads CLAUDE.md, not AGENTS.md" | Outdated | [memory, AGENTS.md section](https://code.claude.com/docs/en/memory#agents-md) | Claude Code now reads AGENTS.md by itself when there is no CLAUDE.md. With both, it reads only CLAUDE.md unless you import it or change a setting. The import advice stays; the Windows symlink note is no longer on the page, so drop it. |
| 6, 8, 9, 10, 16 | "/memory shows which files loaded", and prompts that tell Claude to "run /memory" or "show me /permissions output" | Wrong as written | [memory](https://code.claude.com/docs/en/memory), [best practices](https://code.claude.com/docs/en/best-practices) | /memory also lists files that don't exist yet; Anthropic's check is `/context all`. Both are commands you type, Claude can't run them for you. Reword the five prompts. |
| 6 Modes table | Manual mode, Shift+Tab, Esc, Esc Esc | Incomplete | [permission modes](https://code.claude.com/docs/en/permission-modes) | Those are terminal keys. Cloud sessions (what your friends use on a phone) offer Accept edits, Plan and Auto from a menu, with no Manual. Add a "on your phone" column. |
| 7 Toolkit, 10 Starter kit C and D | Permissions and hooks in `.claude/settings.json` are enforced | Incomplete | [settings in cloud sessions](https://code.claude.com/docs/en/settings#settings-in-cloud-sessions) | True in a cloud session on one repo. In a cloud thread inside a Claude project, the repo's permission rules and hooks don't apply, and path rules don't load. Say so. |
| 10 Starter kit C | `Bash(git push --force *)` blocks force pushes | Incomplete | [permissions, what a Bash rule doesn't match](https://code.claude.com/docs/en/permissions) | A push written another way (`git -C . push`) slips past. Say the GitHub branch rule is the real lock. |
| 4 Git | "A Firebase apiKey is public by design" | Right, but risky as written | [Firebase API keys](https://firebase.google.com/docs/projects/api-keys) | True only for the key Firebase creates, limited to Firebase services. Other Google keys (Gemini, Maps) are secrets. Readers will copy the short version. |
| 2 Anatomy | localStorage lasts "until the user clears it or switches phones" | Incomplete | WebKit's storage policy (to cite in Job 2) | On iPhone, Safari can erase a site's saved data after 7 days without a visit unless the app is on the Home Screen. One of your own apps warns users about this. |
| 3 Stack, 5 Hosting | GitHub Pages for any app with no secrets | Incomplete | [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) | Pages may not run an online business or take passwords or card numbers; 1 GB site, 100 GB a month. |
| 3, 5 | Vercel "free tier" for TeamDesk, a work tool | Not confirmed today | [Vercel fair use](https://vercel.com/docs/limits/fair-use-guidelines) | Vercel's free plan has been personal, non-commercial use only. The page would not load for me; I'll confirm before writing. |
| 6 | Cloud sessions work "on a claude/... branch" | Not confirmed | [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) | Not on the pages I read. Say "its own branch". |
| 13 Workflow | Over-building line called "Anthropic's suggested wording" | Paraphrase | [prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Quote it exactly or drop the label. |
| Sources | "Everything comes from these pages" | Outdated | n/a | Firebase, Vercel, permission modes, commands, settings and cloud session pages are used but not listed. |
| Start | "about four hours" | Wrong | n/a | The books add up to 308 minutes. Already in your SPEC under Later. |

Checked and right: the 200-line target, four import hops, HTML comments stripped, file locations, the two-question test, the four kinds of content, "be ambitious", "skip style", two failed corrections then /clear, auto mode as the default, /effort and ultrathink, /rewind, /btw, /rename, /doctor prompt-audit, hook exit code 2, deny and ask rules, skill and helper file formats, the fork pull request steps, Sync fork, collaborators, secrets not copying to forks, no license means all rights reserved, Pages needing a paid plan for private repos, and the scheduled-task branch rule.

One finding that is not a doc error but breaks your own rule: the made-up apps carry real details. Book 16 names a repo `lions-roar-classes`, the quiz names `ringside.js`, and TeamDesk's numbers (73 lines, 513 imported, 586 total, an 18,000-line page, the "practice switch", the api file names) are exact copies of one of your real apps. Those repos are public, so anyone can match them. I'd change the two literal names for certain and shift TeamDesk's numbers.

### Part 2a: what your apps actually use

All six are plain HTML, CSS and JavaScript with no framework. Five are hosted on GitHub Pages straight from `main`; one runs on Vercel with server code. Five have no login and no database: progress lives in the phone's browser storage, with a backup file in two of them. The sixth has anonymous sign-in plus an emailed 6-digit code, a Firestore database and file storage with a rules file in the repo, server functions that hold the Claude key, a daily scheduled job and push notifications. No app has a key in its front end besides the Firebase config, and none uses App Check.

Three apps install to the Home Screen with an offline worker, and each updates differently: one shows the update on the second open, one reloads itself when the app goes to the background, one fetches the page fresh every time and has a robot that bumps the version on every merge. The other three have no worker and simply load the newest files. None uses Capacitor or any store wrapper; none is in the App Store or Play Store. Other recurring pieces: a site check on pull requests, 3D with three.js, promo videos made with Remotion, sounds and art made with paid generators outside the repo, and one app that takes content requests through GitHub issues handled by a robot.

### Part 2b: what a beginner would still have to guess

1. Getting started at all: making a GitHub account, installing the Claude GitHub app, opening the first cloud session from a phone. Book 16 starts at "create the repo".
2. Turning GitHub Pages on, finding the live link, and how long a merge takes to show.
3. Installing on a phone: the manifest, icons, the iPhone "Share, then Add to Home Screen" steps, and why iPhone users should do it (the 7-day erase).
4. Updates: the guide says "bump CACHE_VERSION" but never shows the three update styles your apps use or how to ask for one. This is Job 3b.
5. Firebase from zero: creating the project, turning on sign-in, where the config goes, how rules get deployed, what a safe rule looks like.
6. Logins: which kind to pick and why (none, anonymous, emailed code, Google).
7. Vercel from zero: connecting the repo, adding a key, reading function logs, scheduled jobs.
8. Backups for apps that save on the phone.
9. Paid generators: where keys for them live when Claude runs in the cloud.
10. Stores: nothing yet. This is Job 3a.

Where I'd disagree with your plan: Job 2 names only the Git, Forks, request and hosting books, but gaps 1, 2 and 3 are the ones that stop a beginner on day one, and they belong in Start here and Book 16. I'd add those two books to Job 2. Gaps 5 to 7 are big enough to be a new book ("Your first back end") instead of padding the hosting book.
