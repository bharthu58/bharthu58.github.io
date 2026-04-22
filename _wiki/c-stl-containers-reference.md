---
layout: page
title: "C++ — STL Containers Reference"
domain: "C++ / Systems"
---

## Sequence Containers

### `std::array<T, N>`

Fixed-size contiguous array. Size known at compile time; no heap allocation.

- **Access:** `O(1)` random
- **Use when:** size is fixed and known at compile time; want `std::vector` ergonomics without heap overhead

```cpp
std::array<int, 5> arr = {1, 2, 3, 4, 5};
arr[2];           // O(1)
arr.size();       // compile-time constant
```

### `std::vector<T>`

Dynamic array; contiguous memory; grows by reallocating.

- **Access:** `O(1)` random
- **Push back:** amortised `O(1)` (can trigger realloc)
- **Insert/erase middle:** `O(n)` — shifts elements
- **Use when:** default sequential container; cache-friendly; size unknown at compile time

```cpp
std::vector<int> v;
v.reserve(100);       // pre-allocate to avoid realloc
v.push_back(42);      // O(1) amortised
```

### `std::list<T>` / `std::forward_list<T>`

Doubly/singly linked list; non-contiguous memory.

- **Insert/erase anywhere:** `O(1)` given an iterator
- **Random access:** `O(n)`
- **Use when:** frequent insertion/deletion at arbitrary positions; iterators must remain valid across mutations
- **Warning:** poor cache performance vs `vector`; rarely the right choice for modern hardware

### `std::deque<T>`

Double-ended queue; chunk-based storage (not a single contiguous block).

- **Front/back push/pop:** `O(1)`
- **Random access:** `O(1)` (but slower than vector due to chunk indirection)
- **Use when:** need fast push/pop at both ends

---

## String Types

### `std::string`

Heap-allocated, mutable character sequence. Most implementations apply **SSO (Small String Optimisation)** — strings ≤15-22 chars are stored inline without heap allocation.

### `std::string_view`

Non-owning view into a string or character buffer. Zero-copy; no heap allocation.

```cpp
void process(std::string_view sv);  // accepts string, literal, or substring — no copy
process(str.substr(0, 5));          // no allocation — just a view
```

**Warning:** never store `string_view` as a member or return it by value when the underlying string may be destroyed.

---

## Container Adaptors

These are wrappers over sequence containers that restrict the interface:

### `std::stack<T>`

LIFO. Default underlying container: `deque`. Can use `vector` or `list`.

### `std::queue<T>`

FIFO. Default: `deque`.

### `std::priority_queue<T>`

Heap-based. Returns largest element by default (`std::less` comparator).

```cpp
std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;  // min-heap
```

- **Push/pop:** `O(log n)`
- **Top:** `O(1)`

---

## Associative Containers (Tree-Based)

Backed by red-black tree. All operations `O(log n)`. Elements always sorted.

| Container | Keys | Values | Notes |
|---|---|---|---|
| `std::map<K,V>` | Unique | Yes | Ordered key-value store |
| `std::set<T>` | Unique | No | Ordered set of values |
| `std::multimap<K,V>` | Duplicate | Yes | Multiple values per key |
| `std::multiset<T>` | Duplicate | No | Ordered multiset |

**Use when:** need sorted iteration, or `lower_bound`/`upper_bound` range queries.

---

## Unordered Containers (Hash-Based)

Hash table. Average `O(1)` insert/lookup; worst case `O(n)` on collisions.

| Container | Keys | Values |
|---|---|---|
| `std::unordered_map<K,V>` | Unique | Yes |
| `std::unordered_set<T>` | Unique | No |
| `std::unordered_multimap` | Duplicate | Yes |
| `std::unordered_multiset` | Duplicate | No |

**Use when:** fast lookup, no ordering required. Prefer over `map` for most cache-heavy lookup tables.

**Pitfall:** default hash for custom types requires specialising `std::hash<T>` or providing a custom hash function.

```cpp
std::unordered_map<std::string, int> freq;
freq.reserve(1024);  // pre-size to avoid rehashing
freq["key"]++;
```

---

## Decision Guide

```
Need sequence of elements?
├── Fixed size, stack allocation → std::array
├── Dynamic, fast random access, cache-friendly → std::vector (default)
├── Fast push/pop both ends → std::deque
└── Fast insert/delete at arbitrary positions → std::list (rarely best)

Need key-value lookup?
├── Sorted order / range queries → std::map
└── Fast lookup, no ordering needed → std::unordered_map (default)

Need queue semantics?
├── LIFO → std::stack
├── FIFO → std::queue
└── Priority ordering → std::priority_queue

Need lock-free concurrent queue?
→ See [C++ — Lock-Free Ring Buffers](/wiki/c-lock-free-ring-buffers/)
```

---

## See Also

- [C++ — Lock-Free Ring Buffers](/wiki/c-lock-free-ring-buffers/) — concurrent queues not provided by STL
- [C++ — Memory and Cache Performance](/wiki/c-memory-and-cache-performance/) — `vector` is cache-friendly; `list`/`map` cause pointer-chasing cache misses
- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — C++20 ranges, `std::flat_map`/`std::flat_set` (C++23 — contiguous backing for map/set)

