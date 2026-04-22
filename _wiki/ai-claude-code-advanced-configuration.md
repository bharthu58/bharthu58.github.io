---
layout: page
title: "AI — Claude Code Advanced Configuration"
domain: "AI / LLM"
---

Advanced configuration patterns treating Claude Code as a programmable OS: CLAUDE.md as kernel, memory/ for state, skills for commands, agents for workers, hooks for security, and MCP servers for I/O.

See also: [AI — Claude Code Folder Structure](/wiki/ai-claude-code-folder-structure/), [AI — Claude Code Tips](/wiki/ai-claude-code-tips/), [AI — Agent Systems](/wiki/ai-agent-systems/)

---

## The 6-Layer System

| Layer | Analogy | What it does |
|-------|---------|--------------|
| CLAUDE.md | OS kernel | Defines agent identity, constraints, anti-hallucination rules |
| memory/ | RAM / persistent state | Stores cross-session facts in indexed satellite files |
| Skills (32) | System programs | Lazy-loaded procedures invoked by slash command |
| Agents (10) | Worker processes | Specialised subagents with model + tools + description |
| Hooks + permissions | Kernel security | PreToolUse/PostToolUse intercept every tool call |
| MCP servers (6) | I/O drivers | External integrations (context7, search, filesystem, etc.) |

---

## Layer 1: CLAUDE.md as Kernel

### Anti-Hallucination Protocol
Force the model to label its own confidence before answering:
- **High** — directly verified from source
- **Medium** — inferred with reasonable confidence
- **Low** — guessed or uncertain
- **Unknown** — not enough information to assess

This surfaces hedging explicitly rather than burying it in fluent-sounding prose.

### /compact Preservation Rules
Specify which information must survive context compression:
- Active task state and current sub-goal
- Decisions made and their rationale
- Constraints that must not be forgotten (e.g. "never write to X")
- In-progress file edits

### Behaviour Constraints
CLAUDE.md is the right place for hard constraints that should never be overridden:
- Blacklisted paths (never write here)
- Required confirmation before destructive operations
- Mandatory frontmatter fields on all new files

---

## Layer 2: memory/ Directory

The memory/ directory provides cross-session persistence independent of context compression.

### Structure
```
memory/
├── MEMORY.md          ← index file, ≤200 lines, always loaded
├── user_role.md       ← user background, preferences
├── feedback_*.md      ← corrections and validated approaches
├── project_*.md       ← ongoing work, decisions, deadlines
└── reference_*.md     ← pointers to external systems
```

### Memory Types
| Type | What to store |
|------|--------------|
| `user` | Role, expertise, preferences |
| `feedback` | Corrections and validated non-obvious approaches |
| `project` | Ongoing work, decisions, deadlines |
| `reference` | Pointers to external systems (Linear, Slack channels, dashboards) |

### MEMORY.md Index Pattern
Each entry is one line under 150 characters:
```
- [Title](file.md) — one-line hook about what's in this file
```
The index is always loaded; satellite files are loaded on demand when relevant.

---

## Layer 3: Skills

### AAPEV Pattern (5-Phase Mandatory)
Every skill should follow:
1. **Acquire** — gather all needed context before acting
2. **Analyze** — understand the current state
3. **Plan** — decide what to do (and surface the plan for review if non-trivial)
4. **Execute** — act
5. **Verify** — confirm the action achieved the intended result

### Skill Categories (9)
1. Research & knowledge synthesis
2. Code generation
3. Code review & quality
4. Testing
5. Debugging
6. Git & version control
7. Documentation
8. Project management
9. System operations

### Key Gotchas
- **description field is the routing trigger** — Claude uses `description:` to decide whether to lazy-load a skill. A vague or absent description means the skill never fires.
- **Hooks-on-demand** — skills can register hooks dynamically; do not wire all hooks globally if only needed in specific skill contexts
- **`${CLAUDE_PLUGIN_DATA}`** — environment variable for skill-level persistence (state that should outlive a skill invocation but not go into memory/)
- **Skill marketplace** — skills can be published and installed from a shared registry (`/plugin marketplace add` → `/plugin install`)

---

## Layer 4: Agent Anatomy

Each of the 10 specialised agents has:
```yaml
model:       # e.g. claude-opus-4-7 (expensive, for reasoning) or claude-haiku-4-5 (fast, cheap)
tools:       # subset of available tools relevant to this agent's domain
description: # routing string — determines when this agent is selected
color:       # terminal colour for output identification
```

Agent specialisation reduces context contamination: a code-review agent sees only code; a research agent has web tools but no write access.

---

## Layer 5: Zero-Trust Security

### Permission Rule Framework
78 explicit rules covering: which tools each agent/skill can use, which paths are writable, which commands are permitted.

Design principle: **fail-closed** — anything not explicitly allowed is denied by default.

### Hook Types
| Hook | Trigger | Use |
|------|---------|-----|
| PreToolUse | Before any tool executes | Validate, block, log |
| PostToolUse | After tool execution | Auto-format, audit, alert |

### bash-guard (PreToolUse)
Intercepts all Bash tool calls. Blocks:
- Commands matching a deny-list (rm -rf, curl to external hosts, etc.)
- Commands outside the project directory
- Commands not matching an allowlist pattern

### write-guard (PreToolUse)
Intercepts all file write/edit calls. Blocks:
- Writes to paths in the blacklist
- Writes outside the agent access boundary
- Writes without the required frontmatter fields (for .md files)

### Fail-Closed Trap
```
if tool_not_in_allowlist:
    deny()
    log("blocked: {tool} {args}")
    return error_to_agent
```
The agent receives an explicit denial, not a silent failure.

---

## Layer 6: MCP Servers

| Server | Role |
|--------|------|
| context7 | Anti-hallucination cornerstone — verifies claims against live documentation |
| Search | Web search integration |
| Filesystem | Controlled file system access |
| + 3 others | Domain-specific integrations |

**context7** is the most important. It intercepts responses that reference external APIs/libraries and cross-checks against current documentation, surfacing version drift or hallucinated method signatures.

---

## Superpowers Plugin (by obra)

An installable plugin that enforces a senior-engineer workflow:

```
/plugin marketplace add opera/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

### Enforced Workflow
1. **Brainstorm-first** — `/superpowers:brainstorm` forces question-asking before any code is written; extracts specs and edge cases
2. **Implementation plan** — `/superpowers:execute-plan` creates a task list (2–5 min each) before execution
3. **Sacred principles** — TDD (test first), YAGNI (no speculative code), DRY (no repetition)
4. **Subagent-driven execution** — main agent acts as manager; subagents execute individual tasks and self-verify
5. **Red-Green-Refactor** — enforced cycle: write failing test → pass it → clean it up → commit

### Built-in Skills
- **Systematic Debugging** — 4-phase root cause process (observe, isolate, hypothesise, verify)
- **Git Worktrees** — isolated workspaces per task for clean branch management
- **Automated Code Review** — checks code against the plan and quality standards before task close
