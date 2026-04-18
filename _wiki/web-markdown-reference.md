---
layout: page
title: "WEB — Markdown Reference"
---

## Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

## Text Formatting

```markdown
**Bold**
*Italic*
~~Strikethrough~~
==Highlight Text==      (Obsidian-specific)
```

## Lists

```markdown
- Bullet Item 1
- Bullet Item 2
    - Nested Item
- Bullet Item 3

1. Number one
2. Number two
3. Number three
```

## Links

```markdown
[My First Note](/wiki/my-first-note/)                        (Obsidian wikilink)
[Link Text](https://example.com)         (standard Markdown link)
```

## Tasks

```markdown
- [x] Completed checkbox
- [ ] Incomplete checkbox
```

## Blockquotes & Callouts

```markdown
> Standard blockquote
```

**Obsidian Callout Types:**

| Callout | Aliases |
|---|---|
| `[!note]` | — |
| `[!abstract]` | abstract, summary, tldr |
| `[!info]` | info |
| `[!todo]` | — |
| `[!tip]` | tip, hint, important |
| `[!check]` | success, check, done |
| `[!question]` | question, help, faq |
| `[!warning]` | warning, caution, attention |
| `[!failure]` | failure, fail, missing |
| `[!danger]` | danger, error |
| `[!bug]` | — |
| `[!example]` | — |
| `[!quote]` | quote, cite |

**Usage:**
```markdown
> [!tip] Optional Title
> Callout content goes here.
```

## Code

````markdown
`inline code`

```language
code block
```
````

## Tables

```markdown
| Header 1 | Header 2 |
|---|---|
| Cell 1 | Cell 2 |
```

## Horizontal Rule

```markdown
---
```

---

## See Also

- [LLM Wiki Pattern](/wiki/llm-wiki-pattern/) — wiki pages in this system use standard Markdown with YAML frontmatter

