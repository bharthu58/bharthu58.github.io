---
layout: page
title: "Wiki Overview"
---

# RBK PKM Wiki — Overview

*Start every new session here. This page is the persistent context — read it before doing anything else.*

---

## What This Wiki Is

A personal knowledge base maintained by LLM agents using the [LLM Wiki Pattern](/wiki/llm-wiki-pattern/). Sources are dropped into `raw/`, ingested into synthesised wiki pages, and queried against as a compounding knowledge base. The wiki gets richer with every source and every session.

The wiki lives inside an Obsidian vault. It is version-controlled via git. Agent access is scoped to `Agent Access/rbk-pkm-wiki/` — everything outside is private and off-limits unless explicitly requested.

---

## Directory Layout

```
Agent Access/rbk-pkm-wiki/
├── wiki-config.md          ← configuration (wiki_root, blacklist, log_format)
├── raw/                    ← drop sources here; wiki-ingest processes them
│   ├── web-clippings/      ← browser clips, Obsidian Web Clipper output
│   └── assets/             ← images and binary assets accompanying clippings
├── ingested/               ← processed sources archived here (move = the commit)
│   ├── clippings/
│   ├── articles/
│   ├── documentation/
│   ├── notes/
│   ├── data/
│   └── assets/             ← images and unreadable files
├── rbk-main-wiki/          ← ALL wiki pages live here (this file's location)
│   ├── Overview.md         ← this file
│   ├── index.md            ← page catalogue
│   ├── log.md              ← append-only audit trail
│   ├── ai/                 ← AI / LLM pages
│   ├── cpp/                ← C++ / Systems pages
│   ├── devops/             ← DevOps / Tooling pages
│   ├── linux/              ← Linux pages
│   ├── python/             ← Python pages
│   ├── obsidian/           ← Obsidian tooling pages
│   ├── web/                ← Web / Markup pages
│   └── meta/               ← Wiki infrastructure pages (LLM Wiki Pattern, etc.)
```

**Key structural note:** `wiki_root` in `wiki-config.md` points to the `rbk-pkm-wiki/` directory (where `raw/` and `ingested/` live), not to `rbk-main-wiki/`. Wiki pages go in `rbk-main-wiki/`.

---

## Wiki Skills

| Skill | Command | What it does |
|---|---|---|
| wiki-ingest | `/wiki-ingest` | Reads `raw/`, synthesises wiki pages, moves sources to `ingested/` |
| wiki-query | `/wiki-query` | Answers questions from wiki pages with `[wikilink](/wiki/wikilink/)` citations |
| wiki-lint | `/wiki-lint` | Health-checks links, orphans, stale index entries |
| wiki-integrate | `/wiki-integrate` | Weaves a new/updated page into the knowledge graph |
| wiki-crystallize | `/wiki-crystallize` | Distils a session into a structured wiki page |

---

## Current Knowledge Domains

### Wiki Infrastructure / Meta (3 pages)
- [LLM Wiki Pattern](/wiki/llm-wiki-pattern/) — the Karpathy compounding wiki pattern; the architecture behind this vault
- [PKM — Note-Making Philosophy](/wiki/pkm-note-making-philosophy/) — note-making vs note-taking, MOCs, atomic notes, bidirectional links, quality over quantity

### AI / LLM (6 pages)
- [AI — Learning Resources & Roadmap](/wiki/ai-learning-resources-roadmap/) — curated videos, books, courses, newsletters, papers; 20-step GenAI learning roadmap
- [AI — 30-Day Mastery Mind Map](/wiki/ai-30-day-mastery-mind-map/) — model selection, prompt/context engineering, image/video gen, automation, open source models
- [AI — Agent Frameworks (N8N vs LangGraph)](/wiki/ai-agent-frameworks-n8n-vs-langgraph/) — visual workflow builder vs graph-based multi-agent Python framework
- [AI — Open Source RAG Stack](/wiki/ai-open-source-rag-stack/) — 7-layer open source RAG stack with tool options at each layer
- [AI — Coding Assistants for Financial Domain Evaluation](/wiki/ai-coding-assistants-for-financial-domain-evaluation/) — evaluation framework for AI tools on OMS/matching engine/SOR/algo trading
- [AI — Claude Code Tips](/wiki/ai-claude-code-tips/) — 10 team tips + Cursor vs VS Code guide

### C++ / Systems Programming (3 pages)
- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — 10-category feature reference + decision flowchart
- [C++ — auto Type Deduction Reference](/wiki/c-auto-type-deduction-reference/) — quick reference for auto, const auto&, initializer-list deduction
- [C++ — Lock-Free Ring Buffers](/wiki/c-lock-free-ring-buffers/) — MoodyCamel vs rigtorp vs Boost.Lockfree vs Folly comparison by threading model

### DevOps / Tooling (4 pages)
- [DevOps — GitHub vs GitLab](/wiki/devops-github-vs-gitlab/) — comparison and decision matrix
- [DevOps — Tool Version Management (mise)](/wiki/devops-tool-version-management-mise/) — cross-platform tool version manager (replaces asdf, nvm, pyenv)
- [DevOps — IDE Comparison (Cursor vs VS Code)](/wiki/devops-ide-comparison-cursor-vs-vs-code/) — AI-first IDE vs flexible extension-based IDE
- [DevOps — Git Cheat Sheet](/wiki/devops-git-cheat-sheet/) — core git commands: setup, staging, branching, remote, stash, rebase

### Linux (2 pages)
- [Linux — Commands Reference](/wiki/linux-commands-reference/) — most-used commands by category (file, networking, process, permissions, etc.)
- [Linux — WSL2 Obsidian Vault Access](/wiki/linux-wsl2-obsidian-vault-access/) — accessing WSL2-hosted vaults from Windows

### Python (1 page)
- [Python — Package Management (uv and pipx)](/wiki/python-package-management-uv-and-pipx/) — uv (all-in-one fast manager) and pipx (global CLI tools)

### Obsidian Tooling (4 pages)
- [Obsidian — Word and Google Docs Integration](/wiki/obsidian-word-and-google-docs-integration/) — Docxer, Pandoc, iframe, Google Drive Sync
- [Obsidian — Plugin Recommendations](/wiki/obsidian-plugin-recommendations/) — Dataview, Calendar, Review, Kanban, Day Planner; core plugins and hotkeys
- [Obsidian — Dataview Queries](/wiki/obsidian-dataview-queries/) — ready-to-use queries for the wiki; YAML field reference; syntax cheat sheet
- [Linux — WSL2 Obsidian Vault Access](/wiki/linux-wsl2-obsidian-vault-access/) — also relevant here

### Web / Markup (1 page)
- [WEB — Markdown Reference](/wiki/web-markdown-reference/) — Obsidian Markdown syntax and callout types

---

## Source Notes

- **MyLearn/** — personal learning notes, bulk-ingested 2026-04-16. Folder subsequently deleted. All readable sources synthesised into wiki pages; images moved to `ingested/assets/`.
- **Uningested sources (deleted, contents not captured):** `Claude-Code-PromptContract.gdoc`, `RBK useful prompts.gdoc` — Google Docs format, never exported.

## Operational Notes (from initialization session)

- **Images in `raw/assets/`** can be read via vision during ingest — do not skip them; they often carry the main content of a clipping (e.g. feature maps, diagrams).
- **`raw/` has subdirs** (`web-clippings/`, `assets/`) — ingest must traverse them, not just the flat root.
- **Ingest atomic commit:** move the source file to `ingested/[subdir]/` only after the wiki page is written. If the move fails, leave the file in `raw/` for retry.
- **`changes:` frontmatter** on every wiki page is the traceability link — wiki-lint uses it to confirm sources are not orphaned.
- **`log.md` is append-only** — new entries at the top; never edit existing entries.

---

## Live Dashboard

*Requires Dataview plugin. Install via Community Plugins if not yet installed.*

**Recently updated pages:**
```dataview
TABLE version, date FROM "Agent Access/rbk-pkm-wiki/rbk-main-wiki"
WHERE file.name != "Overview" AND file.name != "index" AND file.name != "log"
SORT date DESC
LIMIT 10
```

**Pages by domain:**
```dataview
TABLE file.folder AS Domain, version, date FROM "Agent Access/rbk-pkm-wiki/rbk-main-wiki"
WHERE file.name != "Overview" AND file.name != "index" AND file.name != "log"
SORT file.folder ASC
```

---

## Session Bootstrap Checklist

When starting a new session:
1. Read this `Overview.md`
2. Read `index.md` for the current page catalogue
3. Check `raw/` for any new sources to ingest
4. Check `log.md` top entry to see what was done last

---

## Related Pages

[LLM Wiki Pattern](/wiki/llm-wiki-pattern/) — the methodology behind this wiki  
[C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — primary technical reference  
[Obsidian — Word and Google Docs Integration](/wiki/obsidian-word-and-google-docs-integration/) — tooling for getting external docs into raw/

