---
layout: page
title: "AI — Claude Code .claude/ Folder Structure"
domain: "AI / LLM"
---

## Purpose

The `.claude/` folder is the **operating layer** of a Claude Code project. A poorly organised one creates the same friction as a messy codebase — buried rules, scattered scripts, no shared conventions. A well-structured one makes Claude easier to guide, trust, and scale.

---

## Full Blueprint

```
your-project/
├── CLAUDE.md                   ← Project-wide instructions (committed)
├── CLAUDE.local.md             ← Personal overrides (not committed)
└── .claude/
    ├── settings.json           ← Permissions, hooks, operational behaviour
    ├── settings.local.json     ← Personal permission overrides (not committed)
    ├── rules/                  ← Modular, area-specific guidance
    ├── hooks/                  ← Automation scripts (run at lifecycle events)
    ├── commands/               ← Reusable prompt workflows
    ├── skills/                 ← Packaged multi-step capabilities
    └── agents/                 ← Specialised subagent personas
```

---

## Layer-by-Layer Reference

### CLAUDE.md — Global Context

Entry point for every session. Keep it to the **essential context that applies across all tasks**:

- What the project is and how it's organised
- Main development commands
- Broad code conventions
- Project-wide constraints or warnings

> Rule: if an instruction is area-specific (frontend, testing, security), move it to `rules/`. If it needs to be in every session, it stays in `CLAUDE.md`.

### settings.json — Control Layer

Permissions, hook wiring, and operational behaviour. Sits at the top level of `.claude/` because it defines **what Claude is allowed to do**, not what it should know. Keep it findable — don't bury it.

### rules/ — Modular Guidance

When `CLAUDE.md` starts feeling crowded, split by domain:

```
.claude/rules/
├── frontend.md
├── backend-api.md
├── testing.md
└── security.md
```

Each file owns one area. The team responsible for that area updates only their file. `CLAUDE.md` stays slim; rules/ absorbs the detail.

**Split trigger:** CLAUDE.md feels noisy, different areas need different standards, or conventions change often.

### hooks/ — Automation Scripts

Scripts that run automatically at specific lifecycle events (before a tool call, after a file edit, before session stop). Their purpose is always one of:

- Prevent risky actions (`block-dangerous-commands.sh`)
- Validate or clean output (`format-edits.sh`)
- Enforce a workflow requirement (`run-tests-before-stop.sh`)

Even a small hook should live in `hooks/` — the folder name makes its purpose self-evident.

### commands/ — Reusable Prompt Workflows

Markdown files that package repeated prompt tasks:

```
.claude/commands/
├── review-pr.md
├── write-tests.md
└── summarize-changes.md
```

Not automatic (unlike hooks) — invoked intentionally. Use when a prompt is repeated often but fits neatly into one file.

### skills/ — Packaged Workflows

For workflows too complex for a single command file. Each skill is a self-contained directory:

```
.claude/skills/
├── release-prep/
│   ├── SKILL.md
│   └── release-template.md
└── api-audit/
    ├── SKILL.md
    └── api-checklist.md
```

**Use a skill when:** a workflow has multiple steps, needs companion documents, or is important enough to standardise carefully.

**Stay with commands/ when:** the task is short, direct, and prompt-driven.

### agents/ — Specialised Personas

Narrowly focused role-based subagents:

```
.claude/agents/
├── code-reviewer.md
├── security-auditor.md
└── docs-writer.md
```

Each agent owns one specialised role. Don't add agents speculatively — only when a specialised lens genuinely improves results.

---

## Team vs Personal Structure

| Layer | Location | What goes here |
|---|---|---|
| Shared project | `CLAUDE.md`, `.claude/` (committed) | Rules, hooks, commands, skills that help the whole team |
| Personal project overrides | `CLAUDE.local.md`, `.claude/settings.local.json` | Local permissions, personal phrasing, machine-specific behaviour |
| Personal global | `~/.claude/CLAUDE.md`, `~/.claude/skills/`, `~/.claude/agents/` | Workflows that apply across repos, private skills |

> Rule: if it improves team consistency → project. If it reflects personal style → personal.

---

## Progressive Blueprint

Don't build the full structure upfront. Add folders only when the workflow demands them:

1. **Start with** `CLAUDE.md` + `settings.json`
2. **Add `rules/`** when one instruction file stops scaling
3. **Add `hooks/`** when you need automation or enforcement
4. **Add `commands/`** when prompts become repetitive
5. **Add `skills/`** when workflows become deeper than a single file
6. **Add `agents/`** when specialisation clearly improves results

A minimal project may only need:
```
CLAUDE.md
.claude/settings.json
.claude/rules/testing.md
.claude/hooks/format-edits.sh
```
That is still a strong structure.

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Overloaded CLAUDE.md | Move area-specific guidance to `rules/` |
| Adding folders before needed | Only add structure when workflow justifies it |
| Team standards mixed with personal habits | Use `.local` files for personal overrides |
| Vague filenames (`misc.md`, `helper.sh`) | Names should make purpose obvious at a glance |
| Stale files never cleaned up | Treat `.claude/` like the codebase — prune periodically |
| Claude instructions duplicating tool configs | If it belongs in `.eslintrc` or `pyproject.toml`, put it there |

---

## See Also

- [AI — Claude Code Tips](/wiki/ai-claude-code-tips/) — usage patterns: plan mode, subagents, CLAUDE.md as memory, skills for repeat tasks
- [AI — Claude Code Advanced Configuration](/wiki/ai-claude-code-advanced-configuration/) — advanced OS-level patterns: anti-hallucination protocol, memory/ satellite files, AAPEV skill pattern, zero-trust hooks, Superpowers plugin
- [AI — Tool Selection & Workflow](/wiki/ai-tool-selection-workflow/) — where Claude Code fits in the daily tool chain
- [PKM — Personal Workflow Reference](/wiki/pkm-personal-workflow-reference/) — applying the same modularity principle to personal knowledge management

