---
layout: page
title: "AI — 30-Day Mastery Mind Map"
---



## Overview

Comprehensive mind map by @MindBranches — "How to Master AI in 30 Days (The Exact Roadmap)". Covers model selection, prompt engineering, context engineering, image/video generation, coding with AI, automation infrastructure, high-value workflows, open source models, custom knowledge systems, and personal AI assistants.

---

## Foundational Mental Models — Understanding AI Processing

- Context window: weights context to interpret words; give clear context for better results
- Tokenisation: ~1 token = 3.5 chars or 0.75 words — affects costs and limits
- Temperature: parameter (0-1) — set low (0) for factual/analytical, high (1) for creative
- Hallucination: structural, not a bug — verify claims, use low temperature for facts, implement RAG systems

---

## Model Selection Framework (January 2026)

| Model | Best For |
|---|---|
| **Claude (Anthropic)** | Coding (Claude Opus 4.5+ reads codebase), Marketing/long-form writing, Spreadsheet/business analysis, Excel integration |
| **Gemini 3 Pro (Google)** | Research with 1M token context window, Native Google Search integration, Tasks requiring recent data or creative document analysis |
| **Grok** | Real-time X social analysis |
| **Nano Banana Pro** | Image generation |
| **VEO 3.1** | Video generation |
| **GPT-5** | General AI-sounding output |

**Format by Model:**
- Claude/Gemini: use JSON for structured data
- Markdown: works well overall
- Chain-of-Thought: "Let's think through this step by step" for complex problems

---

## Prompt Engineering 2026

**System Prompt Formula:**
- Role — who the AI should be
- Behaviour — how it should interact
- Constraints — what to avoid
- Output structure — format specifications

**Four Strategies:**
1. Write: save context in knowledge/code/reference files
2. Select: use RAG and dynamic retrieval vs dumping everything
3. Compress: summarise verbatim into before including
4. Isolate: separate threads/sub-agents for different contexts

---

## Context Engineering (The 2025-2026 Skill)

**Claude Projects in Practice:**
- Create persistent workspaces with uploaded documents accessible across conversations
- One focused project per task beats one-size-fits-all
- Upload files, write custom instructions, reuse hundreds of times

**RAG for Non-Technical Users:**
- NotebookLM (Google) — free, no-code RAG
- Upload PDFs, docs, YouTube videos for AI expert on specific content with citations
- Grounds responses in actual data vs training data

---

## Image Generation

**Nano Banana Pro:**
- Perfect text rendering in images
- Reasoning before rendering for intentional compositions
- Self-grounding for factually accurate infographics
- Natural language prompts: describe like briefing a photographer
- Include subject, details, action, environment, composition, lighting, text requirements

**Alternatives:**
- Midjourney V7 — most artistic/cinematic for stylised work
- Flux — open-source for local generation

---

## Video Generation

**VEO 3.1 (Google):**
- Up to 60 seconds, 4K output, vertical format support
- Use for finished clips with audio

**Kling 2.6:** Best cinematic realism

**Best Practices:**
- 5-10 seconds is reliable range
- Budget 8-10 attempts per viable clip
- Prompt like a director describing camera view, not narrative storytelling
- Sweet spot: social shorts under 15 seconds, B-roll, product reviews

---

## Coding with AI

**For Developers:**
- Claude Code — runs in terminal, reads codebase, multi-file edits, creates commits
- Cursor — AI-first IDE built on VS Code

**For Non-Developers:**
- Lovable — natural language to complete web application without code
- Bolt.new — rapid prototyping from plain English
- Replit — browser-based development with AI assistance
- "Vibe coding" — describe what you want, iterate based on results

---

## n8n Platform (Automation & Infrastructure)

- Open source, self-hostable, unlimited free workflows
- Claude Code generates n8n configurations from natural language
- Describe workflow → Claude Code generates config → deploy
- Universal adapter for AI systems to connect external tools/APIs
- Pre-built MCP servers for common services
- n8n creates custom MCP servers from workflows

---

## MCP (Model Context Protocol)

- Universal adapter for AI systems to connect external tools/APIs
- Pre-built MCP servers for common services
- Create custom MCP servers from workflows

---

## High-Value Workflows

- Content repurposing — one post becomes multiple platform-specific versions
- Customer feedback routing — sentiment analysis → automated ticketing system

---

## Open Source Models (Current Leaders)

- **Kimi K2.5** (MoonshotAI) — 1 trillion parameters, 1/10th GPT cost
- **DeepSeek V3.2** — matches GPT-5, 90% lower training costs, self-hostable
- **GLM 4** (ZhipuAI) — strong coding
- **Mistral** — fast, 1M token context at fraction of Claude price

**Timeline:**
- 6-12 months: consumer hardware runs capable local models
- 12-24 months: open source likely matches/exceeds closed models

---

## Custom Knowledge Systems

**Claude Projects Alternative:**
- Upload documents, reference automatically in conversations
- More flexible for creating outputs vs just querying

**Vector Database Approach:**
- Documents split into chunks → converted to embeddings → stored in vector database
- Query becomes embedding → find similar chunks → LLM produces grounded answer

---

## Personal AI Assistants

**Clawbot:**
- Runs entirely on hardware (Mac/Windows/Linux or R2me VPS)
- Connects to WhatsApp, Telegram, Slack, Discord, Signal, iMessage
- Persistent memory across conversations
- Can read/write files, control browsers, execute scripts, build extensions
- Self-modifying: writes code to expand its own capabilities

---

## The 30-Day Implementation Roadmap

**Days 1-7 (Fundamentals):**
- Mental models, how AI processes information

**Days 8-14 (Power & Context Engineering):**
- Multiply value of every interaction

**Days 15-21 (Creative & Technical Tools):**
- Image/video/coding with immediate feedback

**Days 22-30 (Advanced Integration):**
- Automation, RAG, personal knowledge systems

**Single Highest-Leverage Move:**
- Build a Claude Project for a repetitive task
- Upload relevant documents, write custom instructions
- Run it 5+ hours weekly

---

## Key Resources

- Anthropic Prompt Guide (official docs)
- OpenAI Tokenizer (visualise text to tokens)
- Andrej Karpathy's LLM videos
- TypingMind/Typing AI
- NotebookLM — free RAG system
- OpenRouter — unified access to all major models
- ClawBot (GitHub) — open-source personal assistant

---

## Critical Insight

> "The gap between AI-fluent and AI-confused widens monthly. The window is time-sensitive — compound over time. The window is time-aware: 30 days from now, students using AI autonomously are still collecting bookmarks. The roadmap exists, the choice is yours."

---

## See Also

- [AI — Learning Resources & Roadmap](/wiki/ai-learning-resources-roadmap/) — structured learning path and resource list
- [AI — Agent Frameworks (N8N vs LangGraph)](/wiki/ai-agent-frameworks-n8n-vs-langgraph/) — agentic automation tools
- [AI — Claude Code Tips](/wiki/ai-claude-code-tips/) — Claude Code-specific workflow tips
- [AI — Open Source RAG Stack](/wiki/ai-open-source-rag-stack/) — RAG tooling landscape

