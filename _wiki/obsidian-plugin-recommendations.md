---
layout: page
title: "Obsidian — Plugin Recommendations"
domain: "Obsidian"
---

> Curated plugin list for an engineering/technical Obsidian setup. Covers navigation, task tracking, knowledge management, and daily planning.

---

## Already Installed

| Plugin | Purpose | Notes |
|---|---|---|
| `image-converter` | Convert image formats on paste | Passive — no config needed |
| `obsidian-image-gallery` | Gallery view for images | Useful for browsing `ingested/assets/` |
| `docxer` | Preview Word (.docx) files in Obsidian | Required for [Obsidian — Word and Google Docs Integration](/wiki/obsidian-word-and-google-docs-integration/) |
| `marp-slides` | Generate slide decks from Markdown | Remove if not actively used — adds startup overhead |

---

## High Priority — Install Next

### Dataview
**What it does:** Turns your vault into a queryable database. Pull tables, lists, and task views from YAML frontmatter across all notes.

**Why now:** Every wiki page already has `title`, `version`, `date` frontmatter — Dataview can query them immediately.

See: [Obsidian — Dataview Queries](/wiki/obsidian-dataview-queries/) for ready-to-use query examples.

### Calendar
**What it does:** Sidebar calendar for navigating Daily Notes — click any date to open or create that day's note.

**Why:** Dots appear under dates indicating unfinished tasks. Makes the daily note habit frictionless.

### Review
**What it does:** Schedule any note to appear in a future Daily Note for review. Uses natural language ("next Friday", "in 2 weeks").

**Why:** Spaced repetition for notes. Essential for surfacing wiki pages that need updating.

Requires: Natural Language Dates plugin (install alongside Review).

---

## Worth Considering

### Kanban
**What it does:** Kanban board inside Obsidian, backed by plain Markdown. Cards are draggable between swim lanes.

**Use case:** Track learning projects, feature work, reading lists. Cards can link to Daily Notes.

### Obsidian Git
**What it does:** Automated push/pull to a GitHub repo on a schedule or via keyboard shortcut.

**Why relevant:** Your vault is already git-controlled. This would let Obsidian auto-commit on Windows without WSL.

**Caution:** Backup conflicts possible if WSL-side Claude Code and Windows-side Obsidian Git both commit. Coordinate workflow before enabling.

---

## Core Plugins — Enable These (Currently Disabled)

| Plugin | Why Enable |
|---|---|
| `slash-command` | `/` in editor opens command palette — faster than Cmd+P |
| `outline` | Right sidebar shows headings of current note — useful for long wiki pages |

Enable via: Settings → Core plugins → toggle on.

---

## Keyboard Shortcuts Worth Setting Up

| Shortcut | Action | Why |
|---|---|---|
| `Ctrl+Shift+D` | Open today's Daily Note | Already set (download-attachments) — consider reassigning to daily note |
| `Ctrl+E` | Toggle edit/preview | Default — keep it |
| `Ctrl+P` | Command palette | Default — use heavily |
| `Ctrl+O` | Quick switcher (open note by name) | Default — fastest navigation |
| `Ctrl+Shift+F` | Search across vault | Default — use for wiki queries |
| `Ctrl+G` | Open graph view | Default — useful for MOC navigation |

**Daily Note shortcut:** Open Settings → Hotkeys → search "Daily Note" → set to `Ctrl+Shift+D`.

---

## Timeblocking with Day Planner

For engineering focus work, the Day Planner plugin adds time-blocked schedules to Daily Notes:

1. Install Day Planner community plugin
2. Set *File Mode* to *Command Mode* (so blocks appear inside your daily note, not a separate file)
3. Enable: Complete past planner items ON, Status Bar Now & Next ON
4. In your daily note, use `Cmd+P` → *Add a Day Planner template* then fill in:
```
- [ ] 09:00 Deep work — [current focus]
- [ ] 12:00 Lunch
- [ ] 13:00 Reviews / PRs
- [ ] 15:00 [next focus block]
- [ ] 17:00 Daily note — captures review
```

Status bar shows current block and next block at all times.

---

## Related Pages
[Obsidian — Dataview Queries](/wiki/obsidian-dataview-queries/), [Obsidian — Word and Google Docs Integration](/wiki/obsidian-word-and-google-docs-integration/), [PKM — Note-Making Philosophy](/wiki/pkm-note-making-philosophy/)
