---
layout: page
title: "Obsidian — Dataview Queries"
---

# Obsidian — Dataview Queries

> Dataview turns your vault into a live database. Every wiki page already has `title`, `version`, `date`, and `changes` YAML frontmatter — all queryable now.

---

## Installation

Community Plugins → Browse → search "Dataview" → Install → Enable.
No additional config required.

---

## How It Works

Add a fenced code block with language `dataview` anywhere in a note. Dataview renders it as a live table/list when the note is in reading view.

```
```dataview
TABLE version, date FROM "folder"
SORT date DESC
```
```

The query re-runs every time the note opens — it's always current.

---

## Ready-to-Use Queries for This Wiki

### Recently Updated Pages
```dataview
TABLE version, date, changes FROM "Agent Access/rbk-pkm-wiki/rbk-main-wiki"
WHERE file.name != "Overview" AND file.name != "index" AND file.name != "log"
SORT date DESC
LIMIT 10
```

### All Pages by Domain Folder
```dataview
TABLE file.folder AS Domain, version, date FROM "Agent Access/rbk-pkm-wiki/rbk-main-wiki"
WHERE file.name != "Overview" AND file.name != "index" AND file.name != "log"
SORT file.folder ASC
```

### AI Domain Pages Only
```dataview
LIST FROM "Agent Access/rbk-pkm-wiki/rbk-main-wiki/ai"
SORT date DESC
```

### C++ Domain Pages Only
```dataview
LIST FROM "Agent Access/rbk-pkm-wiki/rbk-main-wiki/cpp"
SORT date DESC
```

### Pages Created This Month
```dataview
TABLE title, date FROM "Agent Access/rbk-pkm-wiki/rbk-main-wiki"
WHERE date >= date(2026-04-01)
SORT date DESC
```

### Pages Not Updated in 60+ Days (Stale Review Candidates)
```dataview
TABLE date FROM "Agent Access/rbk-pkm-wiki/rbk-main-wiki"
WHERE date < date(today) - dur(60 days)
AND file.name != "Overview" AND file.name != "index" AND file.name != "log"
SORT date ASC
```

---

## YAML Fields Available on Wiki Pages

Every wiki page created by wiki-ingest has these queryable fields:

| Field | Example value | Use |
|---|---|---|
| `title` | `C++ — Lock-Free Ring Buffers` | Display name |
| `version` | `1.1` | Track revisions |
| `date` | `2026-04-17` | Sort by recency |
| `changes` | `Created by wiki-ingest from...` | Trace source |

---

## Query Syntax Reference

```
TABLE field1, field2 FROM "folder/path"
WHERE condition
SORT field ASC/DESC
LIMIT N
```

| Keyword | Description |
|---|---|
| `TABLE` | Renders a table. Use `LIST` for a bullet list. |
| `FROM "path"` | Scope to a folder. Quotes required. |
| `FROM #tag` | Scope by tag |
| `WHERE` | Filter condition. Supports `AND`, `OR`, `<`, `>`, `=` |
| `SORT` | Order results. `date DESC` = newest first |
| `LIMIT N` | Cap results |
| `file.name` | The filename without extension |
| `file.folder` | The folder containing the file |
| `date(today)` | Dynamic today reference |
| `dur(60 days)` | Duration for arithmetic on dates |

---

## Placing Queries

These queries are already live in `Overview.md`. You can also add them to:
- MOC pages (e.g. `CPP.md` — show only cpp/ pages)
- A dedicated `Dashboard.md` at vault root
- Any Daily Note (Dataview works anywhere)

---

## Related Pages
[Obsidian — Plugin Recommendations](/wiki/obsidian-plugin-recommendations/), [LLM Wiki Pattern](/wiki/llm-wiki-pattern/), [Overview](/wiki/overview/)

