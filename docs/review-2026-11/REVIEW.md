# Whole-site review, November 2026

Done 2026-11-19 on `main` at 7cc5f17. Report only: nothing on the site was changed.
Book numbers below are as of that commit. Book 17, "Checks you can trust", was added to main the same day, so the old Books 17 to 20 are now 18 to 21.
Readers assumed: friends and coworkers who use Claude only from a phone or browser (no terminal), and nobody besides Jose has read the books yet.

How it was checked:
- **Reading.** All 23 books read in full as a beginner who can't read code.
- **Facts.** Two fact-checks against the official pages: one for the Claude Code books, one for the app-building books. Each checked about 50 to 75 claims. The most serious finding (number 1 below) was checked a second time on its own.
- **Links.** All 90 outside links tested.
- **Screens.** Every page of every book opened at seven setups: phone light, phone dark, phone with text at 90%, phone with text at 140%, phone sideways, desktop light, desktop dark.
- **Phase 2.** Its "Done when" checks were run as a test on phone and desktop.
- **Not verified:** Safari. Only Chromium is installed here, so anything iPhone-specific was not tested in a real Safari.

Ranked: wrong or dangerous, then blocks a phone-only reader, then broken on a screen, then confusing, then polish. "Size" is the work to fix it: S is under an hour, M is a session, L is a phase.

## 1. Wrong or dangerous

**1. The branch rule in Book 3 does not stop Claude as written.**
- **Size:** S.
- **Where:** Book 3, "Protect main with a branch rule". The rule is called the lock in Books 10, 12, 13 and 19 too.
- **What's wrong:** The steps say to require a pull request and a passing check. That alone doesn't stop anyone who owns the repo, or anything working with the owner's access. Both the reader and Claude in a cloud session work that way.
  - GitHub: "By default, the restrictions of a branch protection rule don't apply to people with admin permissions to the repository".
  - Anthropic (security page): "A rule that access can bypass doesn't block a session's push".
  - Anthropic's best-practices page asks for a rule "the task can't bypass", and the book quotes it, but its steps don't deliver one.
- **Fix:**
  - Add a step: tick "Do not allow bypassing the above settings". Or, with a ruleset, leave the bypass list empty.
  - Say why: "Without it the rule doesn't apply to you, so it doesn't apply to Claude working as you."
  - Also fix the path: rulesets are now under Settings, then Rulesets (not "Rules, then Rulesets").
- **Sources:**
  - docs.github.com: about-protected-branches
  - code.claude.com/docs/en/security.md
  - code.claude.com/docs/en/routines.md, "Repositories and branch permissions"

**2. No book says what to do once a key has leaked.**
- **Size:** S.
- **Where:** Book 3 "Public repos" says a committed key stays in the history forever. Its Try-it has Claude search for one. Book 5 says a key pasted into the chat is "in the conversation for good".
- **What's wrong:** Neither book gives the next step. GitHub's page says the first step is to revoke or rotate the key. Cleaning the history needs a terminal. Revoking works from a phone.
- **Fix:** Add "If a key was ever committed or pasted, go to that service's website today, delete the key and make a new one, and put the new one in an environment variable. Once the old key is dead, the history no longer matters." Add "and how to revoke it" to the Book 3 prompt.
- **Source:** docs.github.com: removing-sensitive-data-from-a-repository.

**3. In a Claude project thread, more of the Starter kit stops working than Books 10 and 13 say.**
- **Size:** S.
- **Where:** Book 10 "Where hard limits don't reach", and Book 13 item C.
- **What's wrong:** The books say only hooks and permissions are ignored there. Anthropic's projects page says path rules, subfolder CLAUDE.md files, skills, agents, `.mcp.json` and plugins don't load either. So Starter kit items E (path rule), F (reviewer) and G (/handoff) silently do nothing in a project thread. Hooks and permissions are also ignored in a session with more than one repo.
- **Fix:** "In a project thread, Claude reads only the repo's main CLAUDE.md and rules without `paths:`. For the rest, start a plain session on one repo."
- **Sources:** code.claude.com/docs/en/claude-projects.md and settings.md. Confirmed by one fact-check; not checked a second time.

**4. "Private repo: works on the free tier" (Vercel) may fail for Claude's commits.**
- **Size:** S.
- **Where:** Book 5, "GitHub Pages or Vercel".
- **What's wrong:** Vercel: "The Hobby Plan does not support collaboration for private repositories ... the commit author must be the owner of the Hobby team." In a cloud session the commit author is Claude, not the reader. So preview links in a private repo on the free plan can be refused.
- **Fix:** "Works on the free tier only for commits under your own name. Claude's commits may be refused, so keep the repo public or plan on the paid plan."
- **Source:** vercel.com/docs/deployments/troubleshoot-project-collaboration. One source.

## 2. Blocks a phone-only reader

**5. The new reader's first steps are in the last book.**
- **Size:** M.
- **What's wrong:** Every Try-it from Book 1 on says "open a Claude Code session". The steps that make that possible (a GitHub account, a Claude plan, connecting the two, a first session from the phone) are the first section of Book 19. Start here points there in one line under "How to use this library". A beginner who reads in order hits a Try-it they can't do on page 4 of Book 1.
- **Fix:** Move "Before step 1" into Start here as its own page, or make it the first page Book 1 opens on. Keep a pointer in Book 19.

**6. The "keys and commands to know by heart" are mostly terminal-only.**
- **Size:** S.
- **Where:** Book 9 table. Book 16 steps 5 and "Steering".
- **What's wrong:** Several of the table's commands don't work from the phone:
  - Esc and Esc Esc are keyboard keys.
  - `claude --resume` is typed in a terminal.
  - Anthropic's docs say /resume doesn't work from the app or the web.
  - /rewind and /btw are not on the list of commands that work from mobile and web.
- **Fix:** Add a phone column:
  - Instead of Esc: send a new message to change direction.
  - Instead of /rewind: "Rewind to here" on a message at claude.ai/code.
  - Instead of resume: reopen the session from the list.
- **Sources:** code.claude.com/docs/en/mobile.md, remote-control.md ("Limitations"), claude-code-on-the-web.md.

**7. Three exercises end on commands a phone reader probably can't run.**
- **Size:** S.
- **Where:**
  - Book 13: the Try-it ends with "type /permissions yourself and check your rules are in the list". Item D says "/hooks shows the result".
  - Book 11: /memory "opens one for editing".
- **What's wrong:** All three open terminal screens. None is on Anthropic's list of commands that work from web and mobile. That makes them very likely terminal-only; no page names them outright. (/context all is on the list and works, so the Book 9 and 12 exercises are fine.)
- **Fix:** For a phone reader, "Ask Claude to read .claude/settings.json back to you, then ask it to read .env and check it's refused."

**8. Personal rules in CLAUDE.local.md or ~/.claude never reach a cloud session.**
- **Size:** S.
- **Where:**
  - Book 10, "Where should a new rule go?": "Only your personal taste: CLAUDE.local.md".
  - Book 11, the "Where it can live" table.
- **What's wrong:** A cloud session starts from a fresh copy of the repo, so an uncommitted file isn't there. The home folder on the reader's computer doesn't come along either.
- **Fix:** "If you only use Claude from a phone, CLAUDE.local.md won't reach your sessions. Keep personal rules in the shared rules file, or ask Claude to put them in your cloud environment's setup script." Anthropic's cloud-environments page documents the second way.

**9. "/doctor prompt-audit once a month" may not be available on the phone.**
- **Size:** S.
- **Where:** Books 11 (its Try-it), 12 and 19.
- **What's wrong:** The audit runs through the built-in /claude-api skill. Anthropic's page says /claude-api "is also unavailable when you type it from mobile or web".
- **Fix:** "If it isn't offered on your phone, send the Monthly CLAUDE.md trim prompt from Book 18." That prompt does the same job.
- **Not verified:** No page says directly whether /doctor itself works in a cloud session.

**10. Smaller phone gaps.**
- **Size:** S each.
- **"Type @ and a path"** (Book 14) is a terminal and IDE feature. Fix: "Name the file: 'look at js/match.js'."
- **Book 3 defines Push as "sending commits from a computer".** Fix: "Sending commits up to GitHub. In a cloud session Claude does this for you."
- **The GitHub clicks in Books 3, 4 and 19** (branch rules, Fork, compare across forks, Collaborators, Pages) are website screens. Fix: say once, "Do these on github.com in your phone's browser; the GitHub app doesn't have these screens." (GitHub's mobile page doesn't list them; not proven absent.)

## 3. Broken on a screen

**11. At the biggest text size, the Copy button pokes past the paper's edge.**
- **Size:** S.
- **Where:** Book 13, sections 2, 6 and 7. A long file name in the box's title pushes the button out, by up to 59px. Screenshot: `copy-button-140.png`.
- **What's wrong:** This breaks feature 13's "Done when": nothing on a page reaches past the paper's edge at 140%.
- **Fix:** Let the title wrap or shorten with "...", so the button always stays inside the box.

**12. Tables with three or four columns turn into tall, narrow strips on a phone.**
- **Size:** M.
- **Where:** Book 9's mode table shows one or two words per line (screenshot: `narrow-table-390.png`). Book 6's sign-in and cron tables and Book 7's update-style table do the same.
- **What's wrong:** Those pages run 6 to 8 phone screens at normal size, and 13 to 15 screens at 140%.
- **Fix:** On narrow screens, show each row as a small card: the first column as its heading, the other columns as labeled lines. One CSS change covers every table.

**13. Light-mode grey text is slightly too faint.**
- **Size:** S.
- **Where:** The grey used for card descriptions, captions, "In this book", "Previous book" and the prompt labels.
- **What's wrong:** It measures 4.42:1 against the paper. The accessibility minimum for normal-size text is 4.5:1. Some of it is body-size text (the five app descriptions in Start here, the four kinds of content in Book 11). Dark mode passes.
- **Fix:** Darken that one color variable a touch.

**14. Some buttons are smaller than a thumb.**
- **Size:** S.
- **What's wrong:** Apple's guideline, and the library's own Book 15, say 44px. These fall short:
  - "Return all books": 17px tall.
  - Copy: 27px.
  - Contents: 31px.
  - Text size and Back: 33 to 35px.
  - Previous and next page with the phone sideways: 38px.
- **Fix:** Pad them to 44px. That matters most for "Return all books", which wipes progress.

**15. The book count disagrees with itself.**
- **Size:** S.
- **What's wrong:**
  - The side panel on desktop says "Book 1 of 20".
  - The library card says "2 of 21".
  - Start here says "21 short books".
  - The cause: Start here is numbered Book 0 and the panel subtracts it. The quiz also counts as a book, "Book 20".
- **Fix:** Pick one count and use it in all three places. 21 is simplest.

## 4. Confusing

**16. The time promises don't match.**
- **Size:** S.
- **What's wrong:**
  - Start here says "about six and a half hours" and "each book takes 10 to 20 minutes".
  - The minutes on the covers add up to 401. Book 6 says 30 and Book 19 says 45.
  - The whole library is about 27,700 words, roughly 2.5 hours of plain reading. The rest is doing the Try-its, which nothing says.
- **Fix:** "About two and a half hours of reading, plus the exercises." Change the per-book line to "most books take 10 to 20 minutes".

**17. The hardest books come before readers know how to use Claude.**
- **Size:** L.
- **What's wrong:**
  - Books 6, 7 and 8 (back end, updates, stores) are 37% of all the words in 3 of 21 books. Book 6 alone is 4,700 words; Book 17 is 350.
  - They sit on shelf 1, between Book 5 and "How Claude Code works" (Book 9). A beginner reading in order meets Firestore rules, service workers and Play Store tester rules before they've learned what a session is.
  - Book 7's section 5 and Book 8 also cover store wrappers twice.
- **Fix:** Move the three to their own shelf after the practice build ("When your app grows"), and let Book 7 point to Book 8 for wrappers.
- **Cost:** Every "Book N" reference changes. There are about 50, all of them correct today, so a script should do the renumbering.
- **Before deciding:** Watch the friend test below first.

**18. The glossary has gaps and is out of order.**
- **Size:** S.
- **Missing terms the books use:** push, clone, cloud session, security rules, Capacitor, webview, rollback, UTC.
- **Out of order on screen:**
  - "Backup file" comes before "Anonymous sign-in".
  - "Collaborator", "License" and "Sync fork" come right after "Fork".
  - "Home Screen app" comes before "GitHub Pages".
  - "WebGL" comes last.
- **Fix:** Add the missing terms, and sort the list when the page is built.

**19. Book 2 hands a beginner twelve tools at once, some they'll never touch.**
- **Size:** S.
- **What's wrong:** The table lists twelve tools at once. Remotion, Node and npm are things a phone-only reader never meets.
- **Fix:** Cut it to the six they will meet (GitHub Pages, Vercel, Firebase, Claude API, PWA, GitHub Actions). Move the rest to the glossary.

**20. Small factual slips.**
- **Size:** S each.
- **Safari's seven-day rule** (Books 1 and 19): WebKit's words are "seven days of Safari use without user interaction on the site". A visit with no tap may not count. Reword to match.
- **Fork workflows** (Book 4): GitHub's docs say only that scheduled workflows are off in a new fork. Soften to "may not run until you switch them on", and add "turn on Pages in the fork's settings".
- **Repos Claude can see** (Book 4): "cloud sessions only see repos you've given them access to". In fact sessions can read any public repo. What may fail is opening the pull request there.

## 5. Polish

These are size S each.

**21. Typo:** "an 15,000-line file" should be "a 15,000-line file". It appears in Books 2 and 12.

**22. Small accuracy fixes in the Claude Code books.**
- **Book 11, AGENTS.md:** "Once both exist it reads CLAUDE.md alone" should say "by default"; a setting loads both.
- **Book 11, Organization row:** a managed CLAUDE.md on a computer doesn't reach cloud sessions.
- **Book 9, /usage:** on a phone it shows only the current session.
- **Book 13, item D:** point the hook at `"$CLAUDE_PROJECT_DIR"/.claude/hooks/...`, as Anthropic's hooks page advises.
- **Book 10, Plugins row:** on the web a plugin is added to your Claude account.
- **Start here:** `.claude/rules/` loads only when Claude works on certain files, "when they list paths".
- **Book 19, taking access back:** disconnect GitHub in Claude's settings (Connectors), and also remove the app on GitHub if you installed it.

**23. Twelve source links now redirect.** They all still land on the right pages, but should be updated to the new addresses:
- four GitHub pages (forks, sync, account, workflow events)
- four Vercel cron pages (now under /docs/schedules/)
- Vercel import
- OWASP
- Veracode
- one Google Play page

**24. Quiz balance.** 9 of the 19 questions are on Books 6 to 8. None is on Books 1 to 3 or Book 9, and none on branch rules or leaked keys, the two biggest safety points above.

## What passed

- No console errors on any page, at any of the seven setups.
- No page scrolls sideways.
- All 90 outside links work.
- Every "Book N" reference points at the right book.
- No em dashes. The only ampersands are inside a Firestore rule, where the code needs them.
- Every risky shortcut except the two in section 1 states its cost and how to close it.
- The start menu downloads about 0.6 MB on a phone, which is fine.
- **Phase 2's "Done when" holds at 390px and desktop:**
  - all 23 books open from their spines;
  - every Contents entry lands on its section;
  - previous and next book work without the browser's Back;
  - an old save (name and read marks) still shows;
  - the book reopens on the page it was left on;
  - "Return all books" keeps the name;
  - dark mode reads cleanly.
- **Feature 13 (text size)** passes except finding 11.

## A 15-minute test with one real reader

This will reorder the list above more than anything else can. Pick a friend who has never used Claude Code. Hand them your phone with the site open, and say only "start wherever it tells you". Don't help.

1. Watch Start here and Book 1. Note the first word they ask about, and whether they try the Try-it.
2. Then ask them to open Book 6 and read its first two pages.
3. Afterwards, ask three questions:
   - What would you do first if you wanted to build an app tomorrow?
   - Where did you want to stop?
   - What was a word you didn't know?

If they stall at the Try-it in Book 1, finding 5 goes first. If they stall in Book 6, finding 17 does.
