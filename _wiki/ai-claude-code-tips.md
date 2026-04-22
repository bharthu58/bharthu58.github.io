---
layout: page
title: "AI — Claude Code Tips"
domain: "AI / LLM"
---

## 10 Tips from the Claude Code Team

### 1. Parallel Sessions (Git Worktrees)
Use `git worktree` to run multiple Claude sessions on the same repo simultaneously:
- Main repo → Worktree 2a (Claude Session 1), 2b (Claude Session 2), 2e (Claude Session 5)
- Each session works in isolation without blocking others
- Dramatically increases throughput on large tasks

### 2. Plan Mode for Complex Tasks
- Claude 1 writes the plan → Claude 2 reviews (Staff Eng perspective)
- If sideways → re-plan
- Invest in planning before coding. Also useful for verification.

### 3. Treat CLAUDE.md Like a Memory System
- After every correction, tell Claude: "Update CLAUDE.md so you don't make that mistake again."
- Edit ruthlessly over time — mistake rate actually drops
- CLAUDE.md is the persistent memory system across sessions

### 4. Turn Repeat Work into Skills
- Any task done >1x/day → turn into a Custom Skill (Command/Agent)
- Examples: `/techdebt` to kill duplicated code, Sync Slack/GDrive/Asana/GitHub in one context, Analytics agents (dbt, reviews, tests)
- Automate frequent tasks

### 5. Autonomous Bug Fixing
1. Paste Slack bug thread
2. Say "fix". Point at logs.
3. Use Claude autonomously.
- Inputs: Slack bug thread + Failing CT tests + Docker logs

### 6. Harsh Reviewer
- Share your changes (diff)
- Ask Claude to "Grill me" / "Prove this works" / "Scrap this and implement elegant version"
- Demand rigorous reviews before PR

### 7. Terminal Setup Matters
- Ghostty terminal
- `/statusline` (Contact Usage + Branch)
- Voice Dictation (~3x faster)
- Optimise environment with tools

### 8. Use Subagents
- Subagent 1 (Narrow Task) + Subagent 2 (Narrow Task) → Main Claude
- Offload tasks to keep context
- Route permissions to Opus via hooks

### 9. Claude for Analytics
- Claude (SQL Skill) → BigQuery CLI, Any DB with CLI/MCP/API
- One engineer hasn't written SQL in 6+ months using this pattern

### 10. Learn with Claude
- Explanatory output (`/config`)
- HTML Presentations
- ASCII Diagrams
- Spaced-Repetition Skill
- Explain understanding; Claude fills gaps, stores result; master new concepts

---

## Cursor vs VS Code — Decision Guide

Source: `MyLearn/AI/rbk-queries-during-ai-discovery-phase.md`

### Why Choose Cursor over VS Code?

Cursor is built on the VS Code codebase — it retains a familiar interface while optimising for AI-first coding. Choose based on your primary workflow:

**Choose Cursor when:**
- You want deep, native AI integration (not extensions bolted on)
- You need project-wide understanding — AI analyzes the entire codebase for multi-file edits
- You want dedicated chat, inline diffs, and "Composer" mode (generate projects from prompts)
- You want multi-model support (switch between OpenAI, Anthropic etc. in one session)
- You want AI-assisted collaboration: shared chats, rules, BugBot code reviews
- You want stronger tab completion (more predictive multi-line suggestions)
- You're a beginner who wants code explained like a coaching session

**Choose VS Code when:**
- You value maximum flexibility through extensions
- You work across many languages/ecosystems with specific extension needs
- You prefer a non-AI-centric workflow with AI as an optional add-on
- Your team has standardised on VS Code tooling

**In short:** VS Code = flexibility + ecosystem. Cursor = streamlined AI-centric workflow.

---

## See Also

- [AI — Claude Code Folder Structure](/wiki/ai-claude-code-folder-structure/) — full .claude/ folder blueprint: rules/, hooks/, commands/, skills/, agents/, team vs personal structure
- [AI — Claude Code Advanced Configuration](/wiki/ai-claude-code-advanced-configuration/) — 6-layer OS system, anti-hallucination protocol, memory/ directory, AAPEV skill pattern, zero-trust hooks, MCP servers, Superpowers plugin
- [AI — Coding Assistants for Financial Domain Evaluation](/wiki/ai-coding-assistants-for-financial-domain-evaluation/) — how to evaluate AI tools for complex projects
- [AI — 30-Day Mastery Mind Map](/wiki/ai-30-day-mastery-mind-map/) — Claude Code tips in context of the broader AI tooling landscape
- [DevOps — IDE Comparison (Cursor vs VS Code)](/wiki/devops-ide-comparison-cursor-vs-vs-code/) — expanded IDE comparison

