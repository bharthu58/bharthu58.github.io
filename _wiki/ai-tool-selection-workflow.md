---
layout: page
title: "AI — Tool Selection & Workflow"
domain: "AI / LLM"
---

> Optimised for a C++ / financial systems engineering context.
> [AI — Coding Assistants for Financial Domain Evaluation](/wiki/ai-coding-assistants-for-financial-domain-evaluation/) | [AI — 30-Day Mastery Mind Map](/wiki/ai-30-day-mastery-mind-map/)

---

## Tool Roles

| Tool | Tier | Role | Primary Use Cases |
|---|---|---|---|
| **ChatGPT** | Free | The "Broad Triage" Assistant | Quick syntax checks, drafting/polishing prompts, general FAQs, administrative queries |
| **Gemini** | Plus | The "Big Context" Librarian | Massive codebase/doc analysis (1M+ tokens), Google Workspace integration, multi-modal research (PDFs, logs) |
| **Claude Code** | Pro | The "Senior Architect" Engineer | Complex C++ implementation, hard-core debugging, low-latency architecture refactoring, agentic terminal work |

---

## The Low-Latency Workflow

Always escalate from cheapest to most powerful:

1. **TRIAGE (ChatGPT Free)** — Clarify requirements, rough-draft the solution, refine your thought process. Do 80% of conversational back-and-forth here.
2. **CONTEXT (Gemini Plus)** — Feed large files, logs, codebases. Extract patterns, ground facts. Use when the problem requires reading a lot of material at once.
3. **EXECUTE (Claude Code Pro)** — Bring the refined prompt + grounded facts here for final, high-stakes code production.

---

## Quick-Select Rules

| Task | Tool |
|---|---|
| Quick C++20 syntax example | ChatGPT Free |
| Analyze 500 lines of trading logs | Gemini Plus |
| Refactor a thread-safe OMS component | Claude Code |
| Summarize a long SEC filing | Gemini Plus |
| Update professional resume/CV | Claude Pro |
| Complex low-latency architecture work | Claude Code |

---

## Token Conservation

- **Start a NEW chat** for unrelated tasks — long histories consume paid token limits
- **Draft in Free, Execute in Pro** — refine the prompt in ChatGPT before bringing it to Claude
- **Ecosystem rule:** Use Gemini for anything touching Google Keep/Docs/Gmail to avoid round-tripping

---

## Related

- [AI — Coding Assistants for Financial Domain Evaluation](/wiki/ai-coding-assistants-for-financial-domain-evaluation/) — Detailed evaluation framework for AI coding tools on OMS, matching engine, algo trading
- [AI — 30-Day Mastery Mind Map](/wiki/ai-30-day-mastery-mind-map/) — Broader tool/model/workflow reference
- [AI — Claude Code Tips](/wiki/ai-claude-code-tips/) — Claude Code-specific usage tips
