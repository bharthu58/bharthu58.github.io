---
layout: page
title: "PKM — Note-Making Philosophy"
domain: "PKM"
---

> The distinction between passive note-taking and active note-making is the key philosophical difference between a vault that compounds and one that stagnates.

---

## Note-Taking vs. Note-Making

| Note-Taking | Note-Making |
|---|---|
| Captures are static; finished when written | Notes are living things; updated over time |
| Filing cabinet: hold until needed | Workbench: actively refined |
| Think → Find (search-first retrieval) | Notes bump into each other; insights emerge |
| Value from individual notes | Value from the network and relationships |
| Focus on content of the active note | Considers connections to all other notes |

**The jeweler vs. the dragon:** The dragon hoards information but sits on it. The jeweler actively works on what he has, making it more valuable. Note-making is the jeweler's practice.

---

## The Three Levels of Knowledge

1. **Having** (Information) — you can find it when you look, but you have to think of it first
2. **Understanding** (Revelation) — you can recall it without looking; you've started connecting it
3. **Doing** (Application) — it changes how you act; visible output exists

The PKM goal is to move knowledge up these levels, not to maximise the volume at level 1.

---

## MOCs: The Cartographer Role

When your notes on a topic feel overwhelming, you've reached the point where you become a cartographer. A Map of Content (MOC) is not an index — it is an opinionated, curated synthesis of what you consider important on a topic. Like a map, it reflects the cartographer's judgement about what matters.

**Key properties of a good MOC:**
- Contains your own opinion notes alongside reference material
- Links to atomic notes — each concept as its own page
- Is in constant development; updated every time you touch the topic
- Reflects your *current* thinking, not just what you've read

Every domain in this vault has an MOC in `MOCs/`. The wiki pages linked from the MOC are the atomic reference layer.

---

## Bidirectional Links: Why They Matter

Wiki-style links (`page`) are one-way: you can navigate from A to B, but not from B back to A without manually adding a return link. Bidirectional links solve this automatically — the relationship is visible in the *Linked Mentions* panel of **both** notes.

This matters because:
- You can start at any note and navigate outward in any direction
- Connections you didn't explicitly plan become discoverable
- The local graph becomes a useful navigation tool (not just aesthetic)

**The test for adding a backlink:** Ask "when do I want to stumble upon this note again?" Only link when that question has a real answer — signal, not noise.

---

## Atomic Notes: The Building Block

An atomic note captures a single irreducible concept — something that can't be broken down further. Examples: `Goodhart's Law`, `RAII in C++`, `Lock-Free SPSC Queue Design`.

**Why atomic notes compound value:**
- Each note is a reusable building block across multiple contexts
- Bidirectional links connect them in ways you didn't anticipate
- The local graph becomes navigable rather than overwhelming

**Trade-off:** Atomic notes require more effort at capture time. The payoff is non-linear — it grows with vault size.

---

## Quality Over Quantity

> "Your job is to collect good ideas. The more good ideas you collect, the more you can choose from to be influenced by." — Austin Kleon

Practical rules:
- Be ruthless at the capture-to-vault threshold: aim for ~1 in 5 captured ideas making it in
- Don't link everything — overlinked vaults lose signal in the noise
- An idea that seemed great at capture often looks weaker after a day's distance
- Five excellent notes are more valuable than 500 mediocre ones

The [LLM Wiki Pattern](/wiki/llm-wiki-pattern/) applies the same principle to AI-assisted ingestion: synthesise and compress, don't transcribe.

---

## The Role of Review

Knowledge you never revisit doesn't compound. Practical review mechanisms:
- **Spaced repetition via Review plugin** — schedule notes for revisit on a future daily note
- **MOC update habit** — every time you touch a topic, ask whether the MOC reflects your current thinking
- **Weekly ingest + capture review** — end of week, review daily note Captures section, ingest anything worth keeping

---

## Related Pages
[LLM Wiki Pattern](/wiki/llm-wiki-pattern/), [Obsidian — Plugin Recommendations](/wiki/obsidian-plugin-recommendations/), [Overview](/wiki/overview/)
