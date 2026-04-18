---
layout: page
title: "AI — Coding Assistants for Financial Domain Evaluation"
---

## Context

Comparing AI coding assistants (Claude Code, Jules, Codex, GitHub Copilot) for complex financial systems: equities trading systems, OMS, matching engines, smart order routers, algo trading platforms. Source: Perplexity analysis.

**Key framing:** Present-day assistants are best as design aides, code generators for local components, refactoring copilots, and test writers — **not** primary system architects or final authorities on market structure, regulation, or microstructure edge cases.

Human engineers must still own: overall architecture, latency budgets, failure modes, microstructure edge cases, regulatory obligations (MiFID II, Reg NMS, CAT reporting, best execution).

---

## Capability Dimensions That Matter

### 1. Codebase-Scale Reasoning
- Can it understand and modify a multi-service codebase (50–200 kLOC) with shared domain models?
- Does it respect module boundaries, domain language, existing patterns?
- Does it handle multi-file changes and keep them coherent?

### 2. Domain Modeling & Correctness
- Can it work with FIX/FAST, market data feeds, order lifecycle states, risk controls without hallucinating?
- Does it keep exchange-specific behavior straight (time-in-force, auction types)?
- Does it handle numerical precision and time correctly (rounding, time zones, clocks, sequence numbers)?

### 3. Latency & Performance Awareness
- Does it suggest sane data structures for low-latency contexts (minimising GC, avoiding unnecessary allocation or reflection, lock-free structures)?
- Does it avoid obviously bad patterns (chatty network calls on hot paths, heavy ORM in matching engine loops)?

### 4. Security, Safety & Compliance
- Handling of auth, secrets, logging, PII
- Graceful handling of failure: circuit breakers, backpressure, replay logic for dropped messages
- Generates tests for risk controls, position limits, kill switches

### 5. Testing & Verification Support
- Quality of unit, integration, property-based tests generated
- Ability to build deterministic simulations and backtest harnesses for algos
- Ability to derive edge-case scenarios from specs

### 6. Workflow Integration
- How well it lives in your actual workflow: IDE, terminal, code review, CI
- Keeping it "aware" of configs, topology, runbooks, production incidents

### 7. Reliability & Steerability
- How often you need to "fight" it to follow instructions
- Whether you can reliably impose constraints: "no external libraries", "no dynamic allocation in this loop", "must be MiFID II compliant"

---

## Evaluation Framework: How to Measure Objectively

### A. Define a Scenario Set (10–20 tasks)

**Architecture / Design:**
- "Propose 2 viable architectures for a low-latency equities matching engine with separate risk and market data services; compare pros/cons and failure modes."
- "Refine this SOR architecture to support an additional dark venue with specific routing constraints."

**Implement / Extend Components:**
- "Implement an order state machine supporting partial fills, cancels, busts, and exchange rejects, with exhaustive tests."
- "Add a new exchange adapter following existing patterns, including FIX message mapping and recovery logic."

**Algo & Backtesting:**
- "Implement an execution algo with POV and VWAP modes; add backtest harness and metrics (slippage, shortfall, participation)."
- "Given this historical order book format, implement a replay engine to test routing logic deterministically."

**Risk & Controls:**
- "Implement pre-trade risk checks (max notional, max size, per-symbol limits) with tests, logs, and admin overrides."
- "Add a kill-switch mechanism that can stop all trading per account and symbol, with persistence and recovery."

**Non-Functional:**
- "Optimise this hot loop in the matching engine under a 99.9% latency budget; explain the trade-offs."
- "Add observability (metrics, traces) to this microservice while respecting latency constraints."

**Task requirements:**
- Non-trivial (must touch multiple files/layers)
- Hidden acceptance tests and performance constraints for objective scoring
- Representative of your actual tech stack

### B. Experimental Protocol

- Same curated repo for all tools — simplified but realistic
- Same time budget per task (60–90 min)
- Same level of human interaction allowed
- Choose one interaction pattern consistently: "assistant coding" (AI writes most) or "copilot mode" (you lead, AI suggests)

### C. Scoring Rubric (per task, 0–5 each)

| Dimension | Weight | What to Assess |
|---|---|---|
| **Functional correctness** | 30% | Passes all tests including edge/failure cases |
| **Latency/perf adherence** | 15% | No blocking IO on hot paths, sane allocations |
| **Code quality** | 15% | Readability, style adherence, test quality, logging, separation of concerns |
| **Security/safety** | 10% | Error handling, no sensitive data in logs, sane defaults, failure behaviour |
| **Productivity gain** | 20% | (Human-only time – AI-assisted time) / Human-only time |
| **Steerability/compliance** | 10% | Constraint adherence, hallucinated API count, corrections required |

**Hard metrics to track:**
- Number of human edit iterations per task
- Lines changed to fix AI-generated code
- Number of production-like defects found in review/tests

---

## Interpreting Results for Trading Systems

**Weight priorities:**
- Correctness & safety > pure productivity
- Latency and resource usage > cosmetic code style
- Steerability (obeying constraints, not hallucinating) > "wow" moments

**Typical outcome:** Pick two different tools:
- One "heavyweight" assistant for architecture, complex refactors, cross-module work
- One "inline copilot" for day-to-day small suggestions

**Guardrails for AI-generated code:**
- Must be covered by tests (AI or human written)
- Must go through human review with explicit checklist (latency, risk, logging, failure modes)
- Must never touch ultra-critical components directly (matching engine core) without additional scrutiny

---

## Concrete Next Steps

1. Pick one system type (e.g. SOR) and extract a sanitised internal or synthetic repo
2. Define 8–10 tasks with hidden tests
3. Run a 2–3 week bake-off with a small team, logging: time per task, correction count, rubric scores
4. Use results to choose:
   - "Primary architecture assistant"
   - "Inline coding copilot(s)"
   - Policy for where AI can/cannot be used

---

## See Also

- [AI — Claude Code Tips](/wiki/ai-claude-code-tips/) — Claude Code-specific workflow optimisations
- [AI — Learning Resources & Roadmap](/wiki/ai-learning-resources-roadmap/) — foundational AI knowledge for practitioners
- [DevOps — IDE Comparison (Cursor vs VS Code)](/wiki/devops-ide-comparison-cursor-vs-vs-code/) — tooling decision for development environment

