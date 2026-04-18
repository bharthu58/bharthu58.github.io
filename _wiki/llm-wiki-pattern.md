---
layout: page
title: "LLM Wiki Pattern"
---

## What It Is

The LLM Wiki pattern (articulated by Andrej Karpathy) is an approach to personal knowledge management where an LLM **incrementally builds and maintains a persistent wiki** rather than doing one-shot retrieval from raw documents. The wiki is a compiled, compounding artefact: the LLM synthesises sources into it, cross-references accumulate, and contradictions get flagged. Every new source and every good question makes it richer.

This is distinct from RAG: RAG re-derives knowledge from scratch on every query. The wiki compiles knowledge once and keeps it current.

## The Three-Layer Architecture

| Layer | Who owns it | What it is |
|---|---|---|
| **Raw sources** | You | Immutable documents (articles, papers, clippings). LLM reads but never modifies. Source of truth. |
| **The wiki** | The LLM | Synthesised markdown pages: summaries, entity pages, concept pages, comparisons. LLM creates, updates, cross-references. You read it. |
| **The schema** | You + LLM | CLAUDE.md / AGENTS.md — tells the LLM the conventions, structure, and workflows. Co-evolved over time. |

## Core Operations

**Ingest** — Drop a source into raw/, ask LLM to process it. LLM reads, synthesises, writes/updates wiki pages, updates index, appends to log. A single rich source may touch 10–15 wiki pages.

**Query** — Ask questions; LLM reads index → relevant pages → synthesises answer with citations. Good answers can be filed back as new wiki pages — explorations compound just like ingested sources.

**Lint** — Periodic health-check: contradictions, stale claims, orphan pages, missing cross-references, concepts lacking their own page.

## Navigation Files

**index.md** — Content-oriented catalogue. Every page listed with a link and one-line summary, organised by category. LLM reads this first on every query to find relevant pages. Works well up to ~hundreds of pages without embedding-based RAG.

**log.md** — Append-only chronological record of ingests, queries, lint passes. Each entry starts with a consistent prefix (e.g. `## [YYYY-MM-DD] ingest | Source`) so it's parseable with grep.

## Why It Works

The bottleneck in knowledge management is not reading or thinking — it is bookkeeping: updating cross-references, keeping summaries current, noting contradictions, maintaining consistency. Humans abandon wikis because maintenance cost grows faster than value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because maintenance cost is near zero.

Human role: curate sources, direct analysis, ask good questions.  
LLM role: summarizing, cross-referencing, filing, bookkeeping.

## Workflow Tips (from Karpathy)

- Stay involved during ingest — read summaries, check updates, guide emphasis. Batch-ingest is possible but less valuable.
- File good query answers back into the wiki — they compound.
- Use **Obsidian Web Clipper** to get web articles into raw/ quickly.
- Download images locally (Obsidian: Settings → Files and links → Attachment folder = `raw/assets/`).
- **Obsidian graph view** shows wiki shape — hubs, orphans, cluster density.
- **Marp** (Obsidian plugin) generates slide decks from wiki content.
- **Dataview** (Obsidian plugin) queries YAML frontmatter for dynamic tables.
- The wiki is just a git repo — version history and collaboration come for free.
- At scale, consider a local search engine (e.g. qmd) with BM25/vector hybrid search for the index.

## Relationship to the Memex

Conceptually close to Vannevar Bush's Memex (1945) — a private, curated knowledge store with associative trails. The LLM solves the part Bush couldn't: who does the maintenance.

## See Also

- [PKM — Note-Making Philosophy](/wiki/pkm-note-making-philosophy/) — human note-making practices that complement the LLM wiki pattern; atomic notes, MOCs, bidirectional links
- [Obsidian — Word and Google Docs Integration](/wiki/obsidian-word-and-google-docs-integration/) — tooling for getting external documents into Obsidian/raw/

