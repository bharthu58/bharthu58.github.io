---
layout: page
title: "C++ — Modern Features Reference (C++20-23)"
domain: "C++ / Systems"
---

## Overview

A structured reference of C++20 and C++23 features organised by **use case / problem domain**, not by standard version. The aim is to answer *"what should I reach for here?"* rather than *"what was added in which standard?"*

Features marked `*` appear in multiple categories.

**Feature map (categories 1–4):**


**Feature map (categories 5–8):**


**Feature map (categories 9–10):**


Source: Sagar @ Towards Dev (2026-04-14). Companion images in `ingested/assets/`.

---

## Category 1 — Performance & Runtime Optimization

| Feature | Std | Summary |
|---|---|---|
| `std::move_only_function` | C++23 | No copy overhead for callables. Lighter than `std::function` |
| Ranges (Lazy Evaluation) | C++20* | Views lazily evaluated — no intermediate allocations/copies |
| `std::jthread` + `stop_token` | C++20* | Cooperative cancellation avoids wasteful polling & forced termination |
| Coroutines (`co_await`) | C++20 | Stackless suspend/resume without thread overhead. Async I/O gains |
| `std::assume_aligned` | C++20 | Alignment hint to compiler for SIMD vectorisation & cache perf |
| `no_unique_address` | C++20 | Empty base optimisation without inheritance. Smaller object layout |
| `std::flat_map` / `flat_set` | C++23 | Contiguous memory layout for cache-friendly sorted containers |
| `std::unreachable()` | C++23 | UB hint — lets compiler optimise dead branches & switch stmts |
| `likely` / `unlikely` | C++20 | Branch prediction hints for hot paths |

---

## Category 2 — Compile-Time Computation

| Feature | Std | Summary |
|---|---|---|
| `consteval` | C++20 | Guaranteed compile-time execution — immediate functions, no runtime path |
| `constinit` | C++20 | Ensures constant initialisation. Prevents static init order fiasco |
| `constexpr` expanded | C++20 | virtual, try/catch, dynamic_cast, union, new/delete now allowed in constexpr |
| `constexpr` further expanded | C++23 | constexpr unique_ptr, optional, variant, cmath, bitset, more STL |
| `if consteval {}` | C++23 | Branch on compile-time vs runtime context. Replaces `is_constant_evaluated` |
| `static_assert(false, f(...))` | C++23 | Computed messages in static_assert — better diagnostics |
| Class-Type NTTP | C++20* | Structs/strings as template params. Compile-time config & DSLs |
| `constexpr vector/string` | C++20 | Heap allocation at compile time. Transient alloc in constexpr |
| `is_constant_evaluated()` | C++20 | Detect compile-time context to pick optimised code paths |

---

## Category 3 — Readability & Expressiveness

| Feature | Std | Summary |
|---|---|---|
| Ranges pipe `\|` operator | C++20 | Composable, declarative data transformations via `\|` chaining |
| Designated Initializers | C++20 | `.field = value` syntax for aggregates. Self-documenting init |
| `std::format` | C++20* | Python-like formatting. Type-safe, readable alternative to printf/streams |
| `std::print` / `std::println` | C++23 | Direct formatted output. No more `cout` chains or printf |
| `operator<=>` (Spaceship) | C++20 | Auto-generates all 6 comparison operators from one declaration |
| `using enum` | C++20 | Import enum values into scope. Cleaner switch/case on enums |
| Init-stmt in range-for | C++20 | `for(auto v = get(); auto& x : v)` — tighter scoping, less boilerplate |
| Deducing `this` | C++23* | Explicit object parameter. Kills CRTP boilerplate, enables recursion in lambdas |
| Multidim `operator[]` | C++23 | `m[x, y, z]` instead of `m[x][y][z]`. Cleaner matrix/tensor access |
| `auto(x)` / `auto{x}` | C++23 | Explicit decay-copy. Cleaner than static_cast or type repetition |
| Lambda improvements | C++20 | Template lambdas, `[=, this]`, pack expansion in captures |
| auto Params (Abbrev Tmpl) | C++20 | `void foo(auto x)` instead of `template<class T> void foo(T x)` |

---

## Category 4 — Safety & Correctness

| Feature | Std | Summary |
|---|---|---|
| `std::span` | C++20 | Non-owning view over contiguous memory. No raw ptr + size pairs |
| Concepts (Constraint Safety) | C++20 | Catch type errors at call site, not deep in template instantiation |
| `constinit` (safety) | C++20 | Prevents accidental dynamic init of global/static variables |
| `std::expected<T, E>` | C++23 | Type-safe error handling without exceptions. Value-or-error pattern |
| `nodiscard("reason")` | C++20 | Custom warning messages when return values are discarded |
| `std::bit_cast` | C++20 | Safe type punning — replacement for `reinterpret_cast` / memcpy |
| Paren Init for Aggregates | C++20 | `make_shared` and emplace work with aggregates — no narrowing bugs |
| `optional::and_then/or_else` | C++23 | Monadic ops — chain operations on optional without null checks |
| `std::source_location` | C++20 | Type-safe `__FILE__` / `__LINE__`. Better logging & diagnostics |
| `std::stacktrace` | C++23 | Portable stack traces for debugging & error reporting |
| `assume(expr)` | C++23 | Assert invariants to compiler. Enables optimiser, documents intent |
| Implicit Move / NRVO | C++20 | More contexts trigger implicit move — fewer accidental copies |

---

## Category 5 — Concurrency & Parallelism

| Feature | Std | Summary |
|---|---|---|
| Coroutines Framework | C++20 | `co_await`, `co_yield`, `co_return`. Async without callback hell |
| `std::jthread` | C++20 | RAII thread — auto-joins on destruction. No more detach bugs |
| `stop_token` / `stop_source` | C++20 | Cooperative cancellation protocol. Thread-safe request/check pattern |
| `std::atomic<shared_ptr>` | C++20 | Lock-free shared_ptr operations. Safe concurrent shared ownership |
| `counting/binary_semaphore` | C++20 | Lightweight synchronisation primitive. Faster than mutex |
| `std::latch` / `std::barrier` | C++20 | One-shot (latch) or reusable (barrier) thread synchronisation |
| `std::atomic_ref` | C++20 | Atomic ops on non-atomic objects. Flexible lock-free access |
| `atomic::wait` / `notify` | C++20 | Futex-style wait on atomics. Efficient spin-free waiting |
| `std::osyncstream` | C++20 | Synchronized output stream. No interleaved `cout` from threads |

---

## Category 6 — Metaprogramming & Type System

| Feature | Std | Summary |
|---|---|---|
| Concepts & Constraints | C++20 | Named type requirements. Replace SFINAE with readable `requires` |
| `requires {}` expressions | C++20 | Inline constraint checks: valid expressions, type requirements |
| Deducing `this` (CRTP killer) | C++23* | Replaces CRTP pattern. Recursive lambdas, simplified mixins |
| `std::type_identity` | C++20 | Prevent deduction on specific parameters. Control template args |
| `std::remove_cvref` | C++20 | Combined cv + ref removal trait. Simpler than chained traits |
| `std::common_reference` | C++20 | Foundation for ranges/concepts. Unifies proxy & value references |
| Class-Type NTTP (meta) | C++20* | Compile-time strings, regex, FSMs as template arguments |
| Lambdas in unevaluated ctx | C++20 | Lambdas in decltype, sizeof. Enables new metaprogramming idioms |
| `std::to_underlying` | C++23 | Convert enum to underlying type. Replaces static_cast patterns |

---

## Category 7 — Generic Programming & Ranges

| Feature | Std | Summary |
|---|---|---|
| `std::ranges` library | C++20* | Views, adaptors, projections. Composable algorithm pipelines |
| Range views (20 types) | C++20 | filter, transform, take, drop, split, join, reverse, elements… |
| Standard Concepts Library | C++20 | same_as, derived_from, integral, invocable, sortable, ranges::… |
| New range views | C++23 | zip, chunk, slide, stride, repeat, cartesian_product, as_rvalue… |
| `ranges::to<Container>` | C++23 | Materialise a view into a concrete container — completes the pipeline |
| `ranges::fold_left/right` | C++23 | Proper fold algorithms. Explicit initial value, replaces accumulate |
| Constrained algorithms | C++20 | `ranges::sort`, `find` etc. take ranges directly + projections |
| Sentinel & Subrange | C++20 | End iterator can differ from begin. Null-term strings, infinite ranges |
| `ranges::contains/starts_with` | C++23 | Long-missing algorithms. No more `find != end` patterns |

---

## Category 8 — Library & Utilities

| Feature | Std | Summary |
|---|---|---|
| `std::mdspan` | C++23 | Multidimensional array view. Customisable layouts for HPC/ML |
| `std::generator<T>` | C++23 | Coroutine-based lazy sequence. First standard coroutine type |
| chrono Calendar & TZ | C++20 | year, month, day, time zones, UTC, TAI clocks. Full date/time API |
| `<bit>` utilities | C++20 | popcount, countl_zero, rotl, rotr, has_single_bit, bit_ceil/floor |
| `std::byteswap` | C++23 | Portable byte order reversal. Endianness conversion utility |
| `string::contains()` | C++23 | Finally: `str.contains("sub")` instead of `find != npos` |
| `starts_with` / `ends_with` | C++20 | String and string_view prefix/suffix checks |
| `std::endian` | C++20 | Compile-time byte order detection. Portable network/file I/O |
| `std::bind_back` | C++23 | Bind trailing arguments. Companion to `std::bind_front` (C++20) |

---

## Category 9 — I/O, Formatting & Text

| Feature | Std | Summary |
|---|---|---|
| `std::format` | C++20* | Type-safe, extensible formatting. `"{:>10.2f}"` with custom formatters |
| `std::print` / `println` | C++23 | Direct UTF-8 output to stdout. Handles Unicode correctly on Windows |
| `format_to` / `format_to_n` | C++20 | Format directly to output iterator. Avoids temp string allocation |
| `std::osyncstream` (I/O) | C++20 | Atomic output operations. Thread-safe formatted output |
| Formatted range output | C++23 | `std::format("{}", vec)` — auto-formats containers & ranges |
| `char8_t` / `u8string` | C++20 | Distinct UTF-8 type. Prevents mixing encodings accidentally |

---

## Category 10 — Modularity & Build System

| Feature | Std | Summary |
|---|---|---|
| Modules (`import`/`export`) | C++20 | Replace `#include`. Faster builds, isolation, no macro leakage |
| Module Partitions | C++20 | Split large modules into internal units. Incremental compilation |
| Header Units | C++20 | `import <iostream>;` — bridge to modules from legacy headers |
| `import std;` | C++23 | One import for entire standard library. Massive compile speedup |
| `import std.compat;` | C++23 | Includes C library names in global namespace. Smooth migration |
| Feature Test Macros | C++20 | `__cpp_concepts`, `__cpp_modules` etc. Portable feature detection |

---

## Cross-Category Features (appear in 3+ categories)



From the cross-category diagram:
- **Concepts** — touches Performance, Compile-Time, Safety, Metaprogramming, Generic Prog.
- **Ranges** — touches Performance, Readability, Generic Prog., Library/Utilities
- **Coroutines** — touches Performance, Concurrency, Library/Utilities
- **Deducing this** — touches Readability, Metaprogramming, Generic Prog.
- **Formatting (std::format)** — touches Readability, I/O & Formatting, Modularity/Build
- **constexpr family** — touches Compile-Time, Safety, Metaprogramming

---

## Decision Flowchart (C++20/23 Feature Selection)



The source includes a flowchart for choosing features. Decision tree summary:

1. **Performance problem?** → Ranges (lazy), `flat_map`, `assume_aligned`, `likely`, coroutines (async I/O)
2. **Compile-time computation?** → `consteval` > `constexpr` > `constinit`
3. **Error handling without exceptions?** → `std::expected<T,E>` + monadic ops
4. **Thread management?** → `std::jthread` + `stop_token` + `std::latch/barrier`
5. **Type constraints on templates?** → Concepts + `requires` expressions
6. **Generic algorithms over containers?** → `std::ranges` + constrained algorithms
7. **Formatted output?** → `std::format` (C++20) / `std::print` (C++23)
8. **Multidimensional data?** → `std::mdspan`
9. **Lazy sequences?** → `std::generator<T>` (C++23)
10. **Build isolation / compile speed?** → Modules (`import std;`)

---

## Further Reading (from source)

Key deep-dive articles by Sagar @ Towards Dev covering features in this map:
- Concepts & Templates, `std::span`, Modules migration, Ranges/Views, Coroutines (parts 1-3), `std::expected`, `std::mdspan`, `std::flat_map`, Deducing this / CRTP, `std::jthread`, atomic improvements, `std::format/print`, constexpr evolution, `<bit>` header, branch prediction hints

---

## See Also

- [LLM Wiki Pattern](/wiki/llm-wiki-pattern/) — methodology for building this knowledge base

