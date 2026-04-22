---
layout: page
title: "Obsidian — Word and Google Docs Integration"
domain: "Obsidian"
---

## Overview

No single plugin handles both Word and Google Docs natively inside Obsidian. The best approach depends on whether you want to **embed/preview** the live document or **convert** it to Markdown for native editing.

## Microsoft Word (.docx)

**Docxer** — the most streamlined option for most users.
- Previews `.docx` files directly inside Obsidian (no external app needed).
- Includes a one-click "Convert" button to turn the Word doc into a standard Markdown note.

**Obsidian Pandoc** — the gold standard for high-fidelity conversion.
- Handles complex formatting (tables, styles, footnotes) more accurately than Docxer.
- Requires installing the Pandoc binary on your system first (extra setup step).
- Best for documents where formatting precision matters.

**Prerequisite:** Enable **"Detect all file extensions"** in Obsidian Settings → Files & Links so `.docx` files appear in the sidebar at all.

## Google Docs

No plugin renders a fully editable Google Doc as a native Obsidian note. Two viable approaches:

**Live embed via iframe (no plugin required):**
1. In Google Docs: File → Share → Publish to web → copy link
2. In your Obsidian note: `<iframe src="YOUR_LINK" width="100%" height="500px"></iframe>`
- Result: a scrollable, live view of the published doc inside Obsidian.
- Limitation: read-only; doc must be published to web.

**Google Drive Sync plugin (Richard Xiang, 2026 edition):**
- Keeps Google Drive and Obsidian vault in sync.
- Focused on file synchronisation, not live inline editing of `.gdoc` files.
- Best for cross-platform access and backup rather than live editing.

## Quick Reference

| Goal | Tool | Notes |
|---|---|---|
| Preview Word (.docx) | **Docxer** | Inline preview + one-click convert |
| Convert Word to Markdown | **Pandoc Plugin** | Highest fidelity; requires Pandoc binary |
| Embed Google Docs live | **iframe** (no plugin) | Publish-to-web required |
| Sync with Google Drive | **Google Drive Sync** | File sync, not live editing |

## Relevance to the LLM Wiki Pattern

Getting external documents into raw/ is a prerequisite for [LLM Wiki Pattern](/wiki/llm-wiki-pattern/) ingest. The above tools bridge the gap between cloud document workflows (Google Docs, Word) and the local Markdown-first wiki system. The preferred path for long-term knowledge is: export/convert → drop in raw/ → wiki-ingest synthesises → native Markdown page in the wiki.

