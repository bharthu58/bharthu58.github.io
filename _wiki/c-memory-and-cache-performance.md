---
layout: page
title: "C++ — Memory and Cache Performance"
domain: "C++ / Systems"
---

## Memory Alignment

### What it is

Modern CPUs fetch memory in parallel banks (32/64-bit word-width). An `N`-byte type is naturally aligned when its address is divisible by `N`. Misaligned data spans two memory rows → two read cycles instead of one.

### Alignment requirements in C++

Every type has an alignment requirement: the minimum address boundary it must be placed on. Use `alignof(T)` to query it.

The compiler automatically satisfies alignment by inserting **padding bytes** between struct members:

```cpp
struct A { char c; int i; };
// Layout: [c][pad pad pad][i i i i] = 8 bytes (alignof = 4)

struct B { char c; double d; int i; };
// Layout: [c][7 padding][d d d d d d d d][i i i i][4 padding] = 24 bytes (alignof = 8)

struct C { double d; int i; char c; };
// Layout: [d d d d d d d d][i i i i][c][3 padding] = 16 bytes (alignof = 8)
```

**B and C have the same fields but different sizes: member order matters.**

### Rule: struct alignment = largest member alignment

The struct itself must be padded to a multiple of its alignment so that arrays of it keep all elements properly aligned:

```
Struct B: needs final padding to reach next 8-byte boundary → 24 bytes total
Struct C: only 3 bytes of tail padding needed → 16 bytes total
```

**Optimisation:** order struct members from largest to smallest alignment to minimise padding.

### Misaligned access is undefined behaviour

```cpp
uint64_t a = 42;
char* x = reinterpret_cast<char*>(&a);
uint32_t* b = reinterpret_cast<uint32_t*>(x + 1);  // misaligned!
std::cout << *b;  // UB — undefined behaviour
```

x86 CPUs handle misaligned access in hardware (with a performance penalty), but other platforms (ARM, RISC-V) may fault. Use `-fsanitize=undefined` (UBSan) to catch this.

### `#pragma pack` / `alignas`

```cpp
#pragma pack(1)         // GCC/MSVC: suppress padding (use for serialisation, not performance)
struct Packed { char c; int i; };  // 5 bytes, but misaligned int

alignas(16) struct SIMD { float x, y, z, w; };  // enforce 16-byte boundary for SSE
```

---

## Cache Line Alignment

### Cache lines

Data moves between CPU cache and main memory in 64-byte **cache lines**. When a core loads any byte in a cache line, the entire 64-byte block is loaded.

```cpp
// C++17: portable cache line size constant
#include <new>
constexpr size_t cache_line = std::hardware_destructive_interference_size;  // typically 64
```

### False sharing

When two threads access **different variables that happen to share a cache line**, modifying one variable invalidates the other's cache entry — forcing expensive cache bouncing:

```cpp
struct Counter { int value = 0; };  // 4 bytes
Counter arr[2];  // arr[0] and arr[1] likely on the same 64-byte cache line

// Thread 1 writes arr[0].value — invalidates arr[1]'s cache line on Thread 2's core
// Thread 2 writes arr[1].value — invalidates arr[0]'s cache line on Thread 1's core
// Result: cores constantly fight over the same cache line despite no shared data
```

This is **false sharing** — cores see completely independent data but waste cycles due to physical proximity.

### Solution: cache line alignment

Force each hot object onto its own cache line:

```cpp
struct alignas(64) Counter {
    int value = 0;
    // compiler adds 60 bytes of padding to fill the cache line
};
static_assert(alignof(Counter) == 64);

Counter arr[2];  // arr[0] on cache line 0, arr[1] on cache line 1 — no conflict
```

**Benchmark (100M increments, 2 threads):**
- Without alignment: ~518 ms (constant cache bouncing)
- With `alignas(64)`: ~265 ms — roughly **2× speedup**, improvement scales with number of concurrent threads

### When to apply cache line alignment

1. **Hot variables written by different threads** — the primary use case for false sharing avoidance
2. **Lock-free data structures** — separate producer/consumer state to different cache lines
3. **Critical per-core state** (thread-local statistics, locks)

Padding wastes memory — do not apply blindly to all structs. Profile first.

---

## Alignment and SIMD

SIMD intrinsics (SSE, AVX) require specific alignment (16 / 32 / 64 bytes) to use the fastest load/store instructions:

```cpp
alignas(32) float data[8];  // 32-byte aligned — safe for AVX 256-bit loads
```

Misaligned SIMD data causes either hardware faults or silent fallback to slower unaligned variants.

---

## Quick Decision Guide

| Situation | Action |
|---|---|
| Struct too large | Reorder members: large → small alignment |
| Two threads write separate fields in same struct | Add `alignas(64)` to the struct |
| SIMD operations on float arrays | `alignas(16)` (SSE) or `alignas(32)` (AVX) |
| Serialisation (wire format) | `#pragma pack(1)` — suppress padding, handle misalignment explicitly |
| Check atomic lock-free status | Alignment must satisfy atomic instruction requirements |

---

## See Also

- [C++ — Atomics and Memory Model](/wiki/c-atomics-and-memory-model/) — alignment determines whether `std::atomic<T>` is lock-free
- [C++ — STL Containers Reference](/wiki/c-stl-containers-reference/) — `std::vector` guarantees alignment for element type; custom allocators needed for over-aligned types
- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — `std::hardware_destructive_interference_size` (C++17), `std::assume_aligned` (C++20)
- [C++ — Data-Oriented Design (ECS & SoA)](/wiki/c-data-oriented-design-ecs-soa/) — applying cache line knowledge to data layout: AoS vs SoA, 5.67× benchmark, ECS pattern

