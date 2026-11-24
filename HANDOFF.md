# HANDOFF (written 2026-11-24; delete this file when its work is done)

## Goal

Next gap from SPEC.md "Later": **Claude Code as a risk** (outside MCP servers, skills and
plugins run with your access; pages and files Claude reads can carry instructions).
Books 22, 24 and 25 are live (PRs #27, #28, #29). Jose approved the plan below on
2026-11-24 ("Write it as planned"), so no new plan approval is needed. He still approves
the merge. First step: write the plan into SPEC.md as item 17.

## The plan (approved 2026-11-24)

Book 26, working title "What you let Claude touch", shelf 6 after `secure`; the quiz
becomes Book 27. Putting it on shelf 2 would renumber Books 11 to 26 everywhere.
Six sections: (1) Claude works with your access; the three ingredients that make it
dangerous together. (2) Pages and files that give orders. (3) Connectors and MCP servers.
(4) Plugins, skills and hooks. (5) Modes and limits: auto mode, the mode never to use,
deny rules (Book 13), a cloud session's network setting (Book 5). (6) When something
looks off. Lead with cloud sessions: most readers work from a phone.
Not in it: writing MCP servers or hooks, the terminal sandbox setup, company-managed
settings, browser agents.

## Facts read word for word on the live pages, November 2026

code.claude.com/docs/en/security
- "Auto mode is the built-in starting permission mode for interactive terminal and VS Code sessions."
- "no system is completely immune to all attacks"
- Habits list: "Review suggested commands before approval"; "Avoid piping untrusted content directly to Claude"; "Verify proposed changes to critical files"; "Report suspicious behavior with `/feedback`".
- "We encourage either writing your own MCP servers or using MCP servers from providers that you trust." Anthropic "does not security-audit or manage any MCP server."
- "Servers in a project's `.mcp.json` have their own approval prompt"
- Cloud: "By default, a session runs its shell commands and file edits in an isolated, Anthropic-managed VM."; "network access is limited by default and can be configured to be disabled or allow only specific domains"; "GitHub credentials are stored encrypted on Anthropic's servers and never enter the session VM."

code.claude.com/docs/en/permissions
- "Rules are evaluated in order: deny, then ask, then allow."
- "Permission rules are enforced by Claude Code, not by the model."
- auto: "Runs without routine prompts; before actions such as shell commands and network requests run, a background classifier checks that they align with your request."
- The skip-all-prompts mode: "Only use this mode in isolated environments like containers or VMs where Claude Code can't cause damage."

code.claude.com/docs/en/mcp
- "Verify you trust each server before connecting it. Servers that fetch external content can expose you to prompt injection risk."

code.claude.com/docs/en/plugins/security, /plugins, /discover-plugins
- "Plugins can run code on your computer, with access to your files and shell. Make sure you trust a plugin before installing, updating, or using it."
- "Anthropic does not control what MCP servers, files, or other software are included in plugins and cannot verify that they will work as intended or that they won't change."
- "Whatever the tier, a plugin you install can run code with your user privileges."
- "A plugin can run hooks and MCP servers, so read the pane before you install."
- "command hooks and monitors are shell commands that run with your full user permissions."

platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- "Use Skills only from trusted sources: those you created yourself or obtained from Anthropic."
- "a malicious Skill can direct Claude to call tools or run code in ways that don't match the Skill's stated purpose."
- "Skills that fetch data from external URLs pose particular risk, as fetched content might contain malicious instructions."

code.claude.com/docs/en/cloud-environments, /claude-code-on-the-web
- "A new environment starts at **Limited** with **Allow package managers** checked." Levels: None, Limited, Full ("Any domain").
- "all GitHub operations go through a dedicated proxy that keeps your real GitHub credentials outside the session's VM"
- "the proxy rejects branch deletions and pushes of anything other than a branch, such as a tag. It doesn't limit which branches a push can update."

code.claude.com/docs/en/sandboxing
- "The sandbox is off by default." "The sandbox covers shell commands only."

anthropic.com/research/prompt-injection-defenses (about browser agents, Nov 2025)
- "But prompt injection is far from a solved problem, particularly as models take more real-world actions."

simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- "Access to your private data"; "Exposure to untrusted content"; "The ability to externally communicate". "If your agent combines these three features, an attacker can easily trick it into accessing your private data and sending it to that attacker."

genai.owasp.org/llmrisk/llm062025-excessive-agency/
- Root causes: "excessive functionality", "excessive permissions", "excessive autonomy".

NOT read word for word (pages too long to load in full), so don't quote: the hooks
reference's "Security considerations", the MCP page's scope definitions, anything on
code.claude.com/docs/en/skills about bundled scripts.

Compared: Willison's essay (for tool users, no steps), the MCP spec's Security Best
Practices (for server builders, needs code and OAuth), OWASP "Excessive Agency" (for
developers).

## How each book was done (follow the same routine)

Insert the section before `<section class="lesson" id="quiz"`; add BOOK, ICON, widen
SHELF_NOTES; three quiz questions and the counts ("Thirty-seven", "0 of 37"); glossary
by hand beside neighbours; a Sources group; Start here stat, og:description, README,
SPEC (top paragraph, features 1 and 5, a new numbered item), docs/ARCHITECTURE id list.
Site check, look check, a reviewer that hasn't seen the work, fix, pull request,
screenshots, try-this list, phone notification, clickable question. After a merge,
`git merge --ff-only origin/main` (a hard reset with a forced push is blocked here).

## Still open, Jose's call

- The site uses small capital labels and gradients, which Book 20 calls signs of the
  generic AI look.
- No reader has been watched using Books 20 to 25.
- `docs/CLEANUP.md` is missing; the rules say to offer `docs/cleanup-audit.md`.
