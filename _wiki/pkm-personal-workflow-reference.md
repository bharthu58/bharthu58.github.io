---
layout: page
title: "PKM — Personal Workflow Reference"
---

# PKM — Personal Workflow Reference

*Your system, your rules. Read this until the habits are automatic.*

---

## The One Rule

> **Capture → Process → Connect → Review.**
> A note that is never reviewed is just an archive. An archive you never query is just clutter.

---

## Daily (5 min)

Open Daily Notes. Write 3–5 bullets — anything you learned, noticed, or want to follow up on. No formatting required. Examples:
- *"lock-free queues: false sharing kills perf on multi-socket"*
- *"look up NUMA-aware allocation in jemalloc"*
- *"mise over nvm — add to DevOps wiki"*

Do not let daily notes accumulate. Process them weekly.

---

## Weekly (Saturday — already in your bootcamp rules)

**Step 1 — Process daily notes**
Scan the week's daily bullets. For each one:
- Worth a wiki page → drop into `raw/`, run `/wiki-ingest`
- Quick addition to existing page → run `/wiki-integrate`
- Not worth keeping → delete

**Step 2 — Write HFT weekly review**
Use `03_Reviews/Week_XX_Review.md`. Be honest: what worked, what didn't, biggest mistake, key insight.

**Step 3 — Crystallize learnings into the wiki**
For anything in the review that has lasting value (a pattern, a technique, a design decision), open `_templates/HFT-Crystallize.md`, fill it out, run `/wiki-crystallize`. Link the result from the CPP MOC.

---

## The Recall Habit

**Before you Google or ask an LLM → run `/wiki-query` first.**

This is the habit that makes your knowledge base compound. If the wiki answers it, you've recalled and reinforced. If it doesn't, find the answer externally then ingest it.

---

## Spaced Review (Obsidian Review Plugin)

Add `review: true` to the frontmatter of any wiki page you want to retain — not just reference. Key candidates:
- All `cpp/` pages
- `AI — Open Source RAG Stack`
- `AI — Agent Frameworks`
- `PKM — Note-Making Philosophy`

The Review plugin will surface these on a spaced schedule. Spend 2 minutes re-reading when it prompts. No flashcards needed — reading your own synthesised notes is enough.

---

## Monthly (30 min)

1. Run `/wiki-lint` — fix broken links, orphaned pages
2. Scan `index.md` — any pages you haven't touched in 30 days?
3. Ask: *"Is there a domain growing too large for its MOC?"* → create a new MOC if yes
4. Check `raw/` — anything sitting there unprocessed?

---

## The Bootcamp → Wiki Pipeline

```
Build something in bootcamp
        ↓
Weekly review: extract key insight
        ↓
Fill out _templates/HFT-Crystallize.md
        ↓
Run /wiki-crystallize
        ↓
Link new page from CPP MOC
```

The bootcamp is where you learn. The wiki is where you keep it.

---

## Warning Signs (ask Claude to flag these)

| Sign | What it means |
|---|---|
| Pages piling up without MOC links | Domain growing without structure |
| `raw/` has files older than 1 week | Capture without processing |
| Daily notes older than 7 days unprocessed | Pipeline is stalled |
| A MOC has 10+ items in one section | Time to split |
| You're Googling something you've ingested | Review cadence too slow |

---

## Related
[PKM — Note-Making Philosophy](/wiki/pkm-note-making-philosophy/) · [LLM Wiki Pattern](/wiki/llm-wiki-pattern/) · [Overview](/wiki/overview/) · [Obsidian — iPhone Capture Pipeline](/wiki/obsidian-iphone-capture-pipeline/)

