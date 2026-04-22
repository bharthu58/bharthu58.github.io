---
layout: page
title: "C++ — Atomics and Memory Model"
domain: "C++ / Systems"
---

## Core Rule

> **Concurrent access to any variable must be either synchronised (mutex/lock) or atomic. Anything else is a data race — undefined behaviour.**

---

## `std::atomic<T>` Basics

An atomic operation is guaranteed to execute as a single, indivisible transaction. No other thread sees an intermediary state.

### What can be made atomic

Only **trivially copyable** types (copyable with `memcpy`). Types with virtual functions or non-contiguous memory cannot be made atomic. Whether the implementation is lock-free depends on the platform and alignment:

```cpp
std::atomic<int> x{0};
bool lf = x.is_lock_free();               // runtime check
bool always = decltype(x)::is_always_lock_free; // compile-time (C++17)
```

Lock-free requires proper alignment — e.g. a 16-byte struct may not be lock-free unless `alignas(16)` is applied.

### The read-modify-write problem

`sum = sum + 1` on `std::atomic<int>` is NOT atomic — it performs an atomic read then an atomic write with a gap between them:

```cpp
// WRONG: two separate atomic ops, still a race
sum = sum + 1;

// CORRECT: single atomic RMW operation
sum++;          // operator++ overload — atomic increment
sum.fetch_add(1);  // explicit form — preferred for clarity
```

Prefer explicit member functions (`fetch_add`, `fetch_sub`, `load`, `store`) over operators to make intent clear and avoid accidental non-atomic expressions.

```cpp
int x = atomic_var.load();     // atomic read
atomic_var.store(42);          // atomic write
```

---

## Compare-And-Swap (CAS)

The fundamental primitive for lock-free algorithms.

### `exchange()`

Atomically swap the current value for a new one; returns the old value:

```cpp
std::atomic<int> x{0};
int old = x.exchange(42);  // old = 0, x = 42 (done atomically)
```

### `compare_exchange_strong` / `compare_exchange_weak`

```cpp
std::atomic<int> x{0};
int expected = x.load();
int desired  = 42;

// If x == expected → x = desired, returns true
// If x != expected → expected = x, returns false
while (!x.compare_exchange_strong(expected, desired));
```

The retry loop is the core of most lock-free algorithms: read current value, compute desired value, CAS — retry if another thread interfered.

**Strong vs Weak:**

| | `compare_exchange_strong` | `compare_exchange_weak` |
|---|---|---|
| Failure condition | Only when value differs | May fail spuriously even if equal |
| Platform cost | Full exclusive acquire | May use timed-acquire (cheaper on some ARM) |
| When to use | Expensive-to-reconstruct state | Simple retry loops (spin counters, flags) |

Note: x86 has no weak CAS — all CAS operations are brute-force exclusive acquire.

### Lock-Free List Example

```cpp
struct Node { int value; Node* next{nullptr}; };
std::atomic<Node*> head{nullptr};

void push_front(int val) {
    Node* node = new Node{val};
    Node* expected = head.load();
    do {
        node->next = expected;
    } while (!head.compare_exchange_strong(expected, node));
}
```

---

## Memory Order

Atomics provide ordering guarantees beyond just atomicity. Without memory barriers, the CPU and compiler are free to reorder writes to main memory.

```
a = 1;  // writes to core-local cache
b = 2;  // writes to core-local cache
// hardware may flush b before a — other threads see b=2 before a=1
```

`std::memory_order` constrains this reordering:

| Order | Guarantee | Cost |
|---|---|---|
| `relaxed` | Atomicity only — no ordering guarantees | Free on x86 |
| `acquire` | Nothing after this barrier can move before it (loads) | Free on x86 |
| `release` | Nothing before this barrier can move after it (stores) | Free on x86 |
| `acq_rel` | Combines acquire + release (for RMW operations) | Free on x86 |
| `seq_cst` | Total global ordering across all threads, all atomics | Can require memory fence on x86 |

### Acquire-Release Pair

Thread A `release`-stores to publish changes; Thread B `acquire`-loads to see them. Guarantee only holds if A and B refer to the **same atomic**:

```cpp
// Spinlock using acquire-release
struct SpinLock {
    std::atomic<bool> locked{false};
    void lock()   { while (locked.exchange(true,  std::memory_order_acquire)); }
    void unlock() { locked.store(false, std::memory_order_release); }
};
```

### When to use each

- `relaxed` — counters where ordering doesn't matter (e.g. `shared_ptr` reference count *increment*)
- `acquire`/`release` pair — standard lock/unlock, producer-consumer handoff
- `acq_rel` — RMW where you both publish and acquire (e.g. `shared_ptr` reference count *decrement* — must see other threads' final stores before destruction)
- `seq_cst` — default; use when you need a single global order visible to all threads across multiple atomics

### x86 vs ARM cost

On x86 (strong memory model): loads are acquire, stores are release, RMW is acq_rel — all essentially free. On ARM (weak memory model), explicit barriers can be expensive. Always specify the intended order even on x86 — it communicates intent to readers and prevents compiler reordering.

---

## Atomics vs Locks

| | Atomics | Mutex/Lock |
|---|---|---|
| Speed | Faster for simple RMW, CAS loops | Higher overhead per acquisition |
| Deadlock risk | None | Possible with multiple locks |
| Code complexity | Hard to write correctly | Easier to reason about |
| Use case | Lock-free data structures, counters, flags | General shared state |

Lock-free doesn't mean "always faster" — measure. A well-tuned lock can outperform a poorly designed CAS loop. Use lock-free code for hot paths where lock contention is the measured bottleneck.

---

## See Also

- [C++ — Lock-Free Ring Buffers](/wiki/c-lock-free-ring-buffers/) — practical implementations using these primitives (MoodyCamel, rigtorp)
- [C++ — Memory and Cache Performance](/wiki/c-memory-and-cache-performance/) — alignment affects `is_lock_free()`, false sharing degrades concurrent performance
- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — C++20 additions: `atomic_ref`, `atomic::wait/notify`, `atomic<shared_ptr>`

