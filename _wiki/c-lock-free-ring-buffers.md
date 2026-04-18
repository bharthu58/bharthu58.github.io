---
layout: page
title: "C++ — Lock-Free Ring Buffers"
---

## Summary

"Best" depends on your threading model (SPSC vs MPMC) and constraints (latency vs throughput). The default recommendation is **MoodyCamel::ConcurrentQueue** — it offers the best balance of correctness, performance, and ease of use.

---

## Top Implementations by Use Case

### 1. General-Purpose MPMC — MoodyCamel::ConcurrentQueue

The state-of-the-art for general-purpose lock-free queues in C++.

- **Threading model:** Multi-Producer, Multi-Consumer (MPMC)
- **Allocation:** Dynamic (block-based) — no fixed-size constraint
- **Integration:** Header-only, drop into any project
- **Performance:** Consistently outperforms `boost::lockfree` in benchmarks
- **License:** Simplified BSD / MIT

**When to use:** Default choice for most production MPMC scenarios.

### 2. SPSC — MoodyCamel::ReaderWriterQueue

If you have exactly one writer thread and one reader thread, do not use a generic MPMC queue. The synchronisation overhead is unnecessary.

- **Threading model:** Single-Producer, Single-Consumer only
- **Why it wins:** Raw ring buffer — avoids CAS loops, uses lighter memory fences instead
- **Latency:** Extremely low — the lowest of the MoodyCamel family
- **Integration:** Header-only

**When to use:** 1:1 thread topology where latency matters (audio pipelines, single-producer event queues).

### 3. Ultra-Low Latency / HFT — rigtorp::MPMCQueue

For scenarios where **no dynamic allocation is acceptable at runtime** and bounded latency is required.

- **Threading model:** MPMC or SPSC
- **Allocation:** Fixed — entire buffer pre-allocated upfront (strict ring buffer)
- **Trade-off:** If the queue fills, you must block or drop — it cannot grow
- **Performance:** Often beats MoodyCamel in throughput for fixed-size scenarios due to simplicity and cache-friendliness
- **Integration:** Header-only, C++11

**When to use:** HFT order paths, audio processing, any hot loop where dynamic allocation is banned.

### 4. Boost.Lockfree

- **Threading model:** MPMC and SPSC variants
- **When to use:** Already heavily invested in the Boost ecosystem
- **Pros:** Battle-tested, stable API, part of a standard distribution
- **Cons:** Generally slower than the specialised libraries above. `boost::lockfree::queue` requires trivially copyable payloads for some operations

### 5. Folly::ProducerConsumerQueue (Facebook/Meta)

- **Threading model:** SPSC
- **Pros:** Extremely optimised for cache locality
- **Cons:** Folly is a massive dependency — do not import it just for this queue
- **When to use:** Only if already using the Folly library

---

## Summary Table

| Library | Type | Allocation | Best Use Case | Dependencies |
|---|---|---|---|---|
| **MoodyCamel ConcurrentQueue** | MPMC | Dynamic (block) | General purpose, high throughput | None (header-only) |
| **MoodyCamel ReaderWriterQueue** | SPSC | Dynamic (block) | 1:1 threading, lowest latency | None (header-only) |
| **rigtorp::MPMCQueue** | MPMC/SPSC | Fixed (static) | Ultra-low latency, HFT, audio | None (header-only C++11) |
| **Boost.Lockfree** | MPMC/SPSC | Fixed/dynamic | Boost-ecosystem projects | Boost |
| **Folly PCQueue** | SPSC | Fixed | Cache-optimised, inside Folly | Folly (heavy) |

---

## Decision Guide

```
Need zero runtime allocation (HFT/audio)?
  → rigtorp::MPMCQueue

SPSC topology (1 writer, 1 reader)?
  → MoodyCamel::ReaderWriterQueue

MPMC, general use?
  → MoodyCamel::ConcurrentQueue

Already on Boost?
  → Boost.Lockfree (acceptable, not fastest)
```

---

## Key Concepts

- **SPSC** — Single-Producer Single-Consumer: simplest case, no CAS needed, just memory fences
- **MPMC** — Multi-Producer Multi-Consumer: requires atomic CAS loops, more overhead
- **CAS** — Compare-And-Swap: the atomic primitive that makes lock-free queues work; avoid when topology allows
- **Ring buffer** — fixed-size circular array; when full, either blocks or drops; no heap allocation after init

---

## See Also

- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — C++20 atomics (`atomic_ref`, `atomic::wait/notify`, `atomic<shared_ptr>`) relevant to lock-free programming
- [C++ — auto Type Deduction Reference](/wiki/c-auto-type-deduction-reference/)

