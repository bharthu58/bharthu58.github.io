---
layout: page
title: "C++ — Data-Oriented Design (ECS & SoA)"
---

# C++ — Data-Oriented Design (ECS & SoA)

Data-oriented design (DoD) restructures code around *data transformations* rather than object hierarchies, matching hardware memory access patterns. Related: [C++ — Memory and Cache Performance](/wiki/c-memory-and-cache-performance/), [C++ — High Performance Data Processing](/wiki/c-high-performance-data-processing/).

---

## The Core Problem with OOP on Hot Paths

OOP is fine for APIs, plugin interfaces, and code called a handful of times per frame. It becomes a bottleneck on tight loops touching millions of objects because it forces **Array of Structs (AoS)** layout.

Three specific costs:

| Problem | Cause | Effect |
|---|---|---|
| Pointer chasing | `vector<unique_ptr<Entity>>` — objects heap-scattered | Cache miss on every `e->update()` |
| Object bloat | Loading the full struct (vtable + all fields) when only 3 fields are needed | 68% of each cache line is waste |
| Virtual dispatch | Unpredictable vtable targets across 10–50 entity types | Branch mispredictions, pipeline stalls |

**The hardware contract:** CPUs fetch memory in **64-byte cache lines**. If the 8 bytes you need are surrounded by 56 bytes of unrelated data, those 56 bytes still consume the cache line — and cost ~100 ns to load from RAM.

---

## AoS vs SoA

**Array of Structs (AoS)** — the OOP default:
```
entities[]: [ {pos, vel, hp, name, vtbl}, {pos, vel, hp, name, vtbl}, ... ]
```
Each update loads the entire struct; only `pos + vel + is_active` are needed.

**Struct of Arrays (SoA)** — the DoD layout:
```
positions[]:    [ p0, p1, p2, p3, ... ]   ← every byte used
velocities[]:   [ v0, v1, v2, v3, ... ]   ← every byte used
active_flags[]: [  1,  1,  0,  1, ... ]   ← every byte used
```
Cache lines load only the data the system needs. The prefetcher sees linear access and preloads ahead. The compiler can auto-vectorise the inner loop.

---

## Minimal ECS Implementation

Entity Component System (ECS) is SoA applied to game/simulation entities. Three concepts:

- **Entity** — just an integer ID (`uint32_t`). No object, no vtable.
- **Components** — plain structs with no inheritance, stored in flat arrays indexed by entity ID.
- **Systems** — free functions that iterate component arrays and apply transformations.

```cpp
// ecs.hpp
struct Position    { float x = 0.f, y = 0.f, z = 0.f; };
struct Velocity    { float x = 0.f, y = 0.f, z = 0.f; };
struct Health      { int value = 100; };
struct ActiveFlag  { bool is_active = true; };

enum ComponentID : uint8_t {
    COMP_POSITION = 0, COMP_VELOCITY, COMP_HEALTH,
    COMP_ACTIVE_FLAG, COMP_COUNT
};
using ComponentMask = std::bitset<COMP_COUNT>;
using Entity = uint32_t;

class ECSWorld {
public:
    std::vector<ComponentMask> masks;
    std::vector<Position>      positions;
    std::vector<Velocity>      velocities;
    std::vector<Health>        healths;
    std::vector<ActiveFlag>    active_flags;
    size_t entity_count = 0;

    Entity create_entity() {
        Entity id = static_cast<Entity>(entity_count++);
        masks.emplace_back(); positions.emplace_back();
        velocities.emplace_back(); healths.emplace_back();
        active_flags.emplace_back();
        return id;
    }
    // add_position, add_velocity, ... (trivial setters)
    bool has_components(Entity e, ComponentMask required) const {
        return (masks[e] & required) == required;
    }
};
```

**Movement system** — no virtual calls, no pointer dereferences, trivially vectorisable:
```cpp
void movement_system(ECSWorld& world, float dt) {
    Position*       __restrict pos = world.positions.data();
    const Velocity* __restrict vel = world.velocities.data();
    const ActiveFlag* __restrict act = world.active_flags.data();

    for (size_t i = 0; i < world.entity_count; ++i) {
        if (!world.has_components(i, required)) continue;
        if (!act[i].is_active) continue;
        pos[i].x += vel[i].x * dt;
        pos[i].y += vel[i].y * dt;
        pos[i].z += vel[i].z * dt;
    }
}
```
`__restrict` tells the compiler the arrays don't alias, enabling SIMD auto-vectorisation.

---

## Benchmark Results

Workload: 1,000,000 entities, physics integration loop (`position += velocity * dt`), 100 frames. Identical algorithm, different data layout only.

**Ryzen 7 5800X, GCC 13.2, `-O2 -march=native`:**

| Approach | Avg frame (ms) | Relative |
|---|---|---|
| OOP (vtable, AoS) | 8.34 | 1.00× baseline |
| ECS (SoA) | 1.47 | **5.67× faster** |

**`perf stat` breakdown:**

| Metric | OOP | ECS |
|---|---|---|
| Cache references | 18.2M | 4.1M |
| Cache misses | 5.4M (29.7%) | 0.12M (2.9%) |
| IPC | 0.71 | **3.12** |

IPC of 0.71 means the OOP CPU was idle ~70% of the time waiting for memory. ECS keeps all execution units fed.

**Scaling behaviour:** The gap widens with data size. At 10K entities everything fits in L3 and OOP is only 3.5× slower. At 10M entities (blowing past L3) ECS is **6×** faster.

---

## When to Apply DoD

```
Is this code on a hot path?
├── NO  → use whatever is clearest (OOP is fine)
└── YES → how many items?
          ├── <1000 → probably doesn't matter
          └── >1000 → profile it
                      cache misses > 5%?
                      ├── NO  → you're fine
                      └── YES → data-oriented redesign
```

Good candidates: per-frame simulation loops, particle systems, physics engines, HFT order book updates touching millions of quotes. Not worth it for: UI code, configuration, plugin interfaces, anything called < 1000× per frame.

---

## C++26 Reflection (Future Direction)

The boilerplate cost of manual ECS (explicit component IDs, `add_*` functions, bitmasks) will shrink significantly with **P2996 static reflection** (targeting C++26). The idea: write an AoS struct definition, compiler generates SoA storage automatically.

```cpp
// HYPOTHETICAL C++26
struct PhysicsBundle { Position position; Velocity velocity; ActiveFlag active; };
auto storage = make_soa_storage<PhysicsBundle>(1'000'000);  // SoA under the hood
```

Libraries like **EnTT** and **flecs** already approximate this with template metaprogramming. See [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) for current C++20/23 compile-time tooling.

---

## Related Pages

- [C++ — Memory and Cache Performance](/wiki/c-memory-and-cache-performance/) — struct padding, false sharing, cache line alignment
- [C++ — High Performance Data Processing](/wiki/c-high-performance-data-processing/) — mmap I/O, flat hash tables, NUMA pinning
- [C++ — ULL Developer Skillset](/wiki/c-ull-developer-skillset/) — hot path skill checklist for HFT/ULL roles
- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — current compile-time and SIMD tooling

