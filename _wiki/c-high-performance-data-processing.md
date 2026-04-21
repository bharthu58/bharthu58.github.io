---
layout: page
title: "C++ — High Performance Data Processing"
---

## The 1 Billion Row Challenge — Optimisation Progression

A case study in iterative C++ performance engineering. Goal: aggregate min/mean/max temperatures for 1 billion rows from a 13 GB CSV file (`STATION;12.3` format).

Hardware: AMD Ryzen 9 7950X (16 cores), 64 GB DDR5, NVMe SSD, GCC 14 `-O3 -march=native`

| Technique | Wall time | Speedup |
|---|---|---|
| Baseline: `ifstream` + `string` + `unordered_map` | ~11 min | — |
| Memory-mapped I/O (`mmap`) | ~4 min | 2.7× |
| 16-thread parallel scan (thread-local maps) | 46 s | 5.2× |
| Flat open-addressing hash table (Robin Hood) | 9.1 s | 5× |
| Branchless SWAR float parser | 3.6 s | 2.5× |
| Zstd-compressed I/O + ring buffer | 1.2 s | 3× |
| NUMA pinning + huge pages + relaxed atomics | **0.93 s** | final |

---

## Technique Deep-Dives

### 1. Memory-Mapped I/O

Standard `ifstream` copies data into userspace buffers. `mmap()` lets the kernel page-fault chunks lazily — zero-copy access to the file:

```cpp
int fd = ::open(fname, O_RDONLY);
size_t len = ::lseek(fd, 0, SEEK_END);
char* data = static_cast<char*>(
    ::mmap(nullptr, len, PROT_READ, MAP_PRIVATE, fd, 0)
);
// Parse data[0..len-1] directly — no memcpy
::munmap(data, len);
```

Use `std::string_view` to reference substrings within the mapped region — no allocations during parsing.

**Gain:** eliminates repeated userspace buffer copies; enables parallel slicing.

### 2. File Partitioning for Parallel Scan

Split the memory-mapped file into N line-aligned chunks, one per thread:

```cpp
std::vector<size_t> offsets(workers + 1);
for (size_t i = 1; i < workers; ++i) {
    size_t p = i * (len / workers);
    while (p < len && mmap_ptr[p] != '\n') ++p;  // advance to line boundary
    offsets[i] = p + 1;
}
```

Each thread scans its slice independently into a **thread-local** aggregation structure, eliminating all cross-thread synchronisation during the hot path. Merge at the end.

### 3. Flat Open-Addressing Hash Table

`std::unordered_map` is too slow: separate chaining → pointer-chasing cache misses + allocator contention. Replace with a **contiguous flat table**:

```cpp
struct Entry { uint64_t hash; uint32_t station_idx; Stats stats; };
std::vector<Entry> table(capacity);  // cache-friendly: all data in one array

// Linear-probe lookup/insert
size_t slot = hash & mask;
while (table[slot].hash != 0 && table[slot].hash != hash) ++slot;
```

Key improvements:
- Store station **indices** (into a string pool) rather than keys inline — keeps entry small
- Pre-size table to `num_stations × 1.3` to minimise collisions
- String pool aligned to 64-byte cache lines

**Gain:** eliminates pointer chasing, removes allocator contention between threads.

### 4. Branchless / SWAR Number Parsing

`std::strtod` is slow for the fixed-format numbers (`-99.9` to `99.9`). Custom branchless parser:

- Read sign, integer digits, decimal point, fractional digit in a single register operation (SIMD-Within-A-Register)
- Use `std::bit_cast` + power-of-ten lookup table for final scaling
- Entirely branch-free → highly predictable pipeline

**Gain:** 2.5× over `strtod` for this constrained format.

### 5. Compressed I/O Pipeline

Compressing the dataset with Zstandard level 1 (13 GB → 980 MB) allows reading 9 GB/s from disk (decompression bandwidth) vs 2 GB/s raw NVMe sequential throughput:

```
Producer thread: pread() 8 MiB blocks → ring buffer
Worker threads: ZSTD_decompress() in-memory → parse lines
```

Counter-intuitive: compression *reduces* elapsed time by reducing I/O stalls. Only viable because decompression is faster than the I/O bottleneck.

### 6. Micro-Optimisations

```cpp
// NUMA pinning: bind threads to physical cores for memory locality
pthread_setaffinity_np(thread.native_handle(), sizeof(cpuset), &cpuset);

// Huge pages: reduce TLB misses for the large mmap region
mmap(nullptr, len, PROT_READ, MAP_PRIVATE | MAP_HUGETLB, fd, 0);

// Relaxed atomics for final stats merge: ordering irrelevant, just atomicity
counter.fetch_add(1, std::memory_order_relaxed);
```

---

## Key Principles Extracted

1. **Identify the true hot path first.** For CSV processing: read bytes → find delimiter → parse number → aggregate. Everything else is noise.

2. **Zero-copy I/O eliminates the biggest waste.** `mmap` vs `ifstream` is a 2.7× gain from changing nothing but the read strategy.

3. **Eliminate shared state on the hot path.** Thread-local data structures + single merge is always faster than fine-grained locking.

4. **Flat data structures beat pointer-based ones.** A custom open-addressing hash table eliminates cache misses that dominate `unordered_map` performance.

5. **Parsing cost eventually dwarfs I/O.** Once I/O is optimised, number parsing becomes the bottleneck — write domain-specific parsers for constrained formats.

6. **Compression can improve throughput.** When CPU is faster than disk, compress to reduce bytes-from-disk; decompression cost is paid back in I/O savings.

7. **NUMA and TLB effects matter at scale.** Huge pages + NUMA pinning are single-digit percentage wins but easy to apply.

---

## Applicability to Financial Systems

These techniques directly map to HFT/financial data processing:

| 1BRC Technique | HFT Application |
|---|---|
| `mmap` for file I/O | Market data replay, tick database reads |
| Thread-local aggregation | Per-core order books, per-thread statistics |
| Flat hash tables | Symbol → order book lookup, session ID maps |
| Branchless parsers | FIX/FAST/ITCH protocol parsers |
| Ring buffer + worker threads | Feed handler → strategy thread pipeline |
| Relaxed atomics | Reference counting, non-order-sensitive metrics |

---

## See Also

- [C++ — Atomics and Memory Model](/wiki/c-atomics-and-memory-model/) — relaxed atomics, memory ordering for merge step
- [C++ — Memory and Cache Performance](/wiki/c-memory-and-cache-performance/) — cache line alignment for thread-local structures, false sharing
- [C++ — STL Containers Reference](/wiki/c-stl-containers-reference/) — why `unordered_map` underperforms for high-volume workloads
- [C++ — Lock-Free Ring Buffers](/wiki/c-lock-free-ring-buffers/) — the ring-buffer pattern used in the decompression pipeline

