---
layout: page
title: "AI — Agent Systems"
---

# AI — Agent Systems

Covers the architecture, design patterns, and production concerns for LLM-powered agents.

See also: [AI — Agent Frameworks (N8N vs LangGraph)](/wiki/ai-agent-frameworks-n8n-vs-langgraph/), [AI — Claude Code Advanced Configuration](/wiki/ai-claude-code-advanced-configuration/), [AI — Open Source RAG Stack](/wiki/ai-open-source-rag-stack/)

---

## Core Concepts

### What is an Agent
An agent is an LLM + a loop + tools. The loop observes the environment, reasons about the next action, executes a tool call, and incorporates the result — repeating until the task is complete or a stopping condition is met.

### ReAct Pattern (Reason-Act-Observe)
The foundational loop:
1. **Reason** — LLM thinks through the current state
2. **Act** — executes a tool (web search, code execution, DB query, API call)
3. **Observe** — result appended to context
4. Repeat until goal reached

Transparency is a key benefit: every intermediate step is visible and auditable.

### Context Engineering
The actual lever of agent performance — not prompt engineering alone. Context engineering controls what information is in the context window at each step:
- Which prior steps to include or summarise
- What tool results to truncate or compress
- When to flush and restart context vs. accumulate

---

## Memory vs. Knowledge

| Dimension | Memory | Knowledge |
|-----------|--------|-----------|
| Definition | Dynamic task state | Static facts |
| Scope | Tied to a session or agent instance | Shared, persistent |
| Storage | Short-term (context) or long-term (DB/file) | Vector DB, wiki, config |
| Changes | Frequently updated during execution | Rarely changes |

**Short-term memory** = the active context window during a session.
**Long-term memory** = files, databases, or vector stores persisted between sessions.

---

## Task Decomposition Strategies

| Strategy | Split by | When to use |
|----------|----------|-------------|
| Functional | Purpose / concern | Clear separation of responsibilities |
| Spatial | Geography / partition / shard | Data is naturally partitioned |
| Temporal | Time window / sequence | Tasks have natural ordering |
| Data-driven | Input data shape or type | Different handlers per format |

Decomposing tasks into 2–5 minute sub-units is a strong heuristic for both human and LLM agents — it bounds error propagation and enables parallelism.

---

## Design Patterns

### 1. Reflection
The agent produces output, then reviews it against a critique framework before finalising.
- Critique dimensions: correctness, completeness, style, security, edge cases
- Self-review cycle: draft → critique → revise → (repeat)
- Can use a second LLM call (a "critic") rather than self-critique

### 2. Tool Use
LLM requests tool execution but does not execute directly — the orchestrator handles execution.
- Tools are **dynamic** (selected per query) and **composable** (chained)
- Key principle: the LLM describes *what* to do; the runtime decides *how* to do it safely
- Prevents direct code execution from arbitrary LLM output

### 3. Planning
Agent decomposes the full task upfront before any execution begins.
- Upfront plan = lower risk of mid-task context divergence
- **Adaptive planning** replans when tool results contradict assumptions
- Best for long-horizon tasks where order of operations matters

### 4. Multi-Agent
Multiple specialised agents collaborate, each with a focused role:
- **Specialist** — expert in a domain (coder, researcher, critic)
- **Critic** — evaluates other agents' output
- **Coordinator** — routes tasks and merges results
- **Manager** — breaks tasks, delegates to subagents, integrates results

---

## Multi-Agent Coordination Patterns

| Pattern | Description | Best for |
|---------|-------------|----------|
| Sequential (pipeline) | Agent A output → Agent B input | Dependent, ordered steps |
| Parallel (fan-out) | Multiple agents work independently, results merged | Independent subtasks |
| Manager hierarchy | Central manager delegates to specialist subagents | Complex tasks needing orchestration |
| All-to-all (mesh) | Any agent can call any other | Highly dynamic collaboration |

---

## Guardrails

### Code-Based
- Input validation: schema checks, length limits, content filters
- Output validation: format checks, regex, structured output parsing

### LLM Judge
- A second LLM call evaluates output quality or safety
- Slower but can catch semantic issues code validators miss
- Useful for tone, accuracy, policy compliance

### Human-in-the-Loop
- Pause at decision points for human confirmation
- Mandatory for irreversible or high-risk actions
- Can be asynchronous (async approval queue) or synchronous (blocking confirmation)

---

## Production Concerns

### Quality
- Reflection loops: self-critique before finalising output
- Multiple samples (temperature > 0) and majority vote for critical decisions
- Automated test assertions on structured outputs

### Latency
- Parallel execution of independent subtasks
- Streaming responses to reduce time-to-first-token perception
- Smaller models for simple subtasks in a pipeline

### Cost
- Route simple queries to smaller/cheaper models
- Prompt caching (Anthropic / OpenAI APIs) for repeated context prefixes
- Set max_tokens aggressively for classification/routing calls

### Observability
- Trace every step: input, tool call, output, latency, tokens
- Correlation IDs across multi-agent calls
- Capture tool failure rates and retry counts separately

### Security
- **Sandbox all code execution** — agents that write and run code must be isolated (container, VM, subprocess with no network/FS access by default)
- **Prompt injection defence** — treat all external data (web scrapes, user files) as untrusted; never inject raw external content directly into the system prompt
- Tool permissions: grant least privilege; a search tool should not have write access

