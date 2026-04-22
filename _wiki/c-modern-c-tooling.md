---
layout: page
title: "C++ — Modern C++ Tooling"
domain: "C++ / Systems"
---

## Mental Model

> "Senior C++ developers don't fight the language — they automate around it. Libraries give leverage; leverage is what separates developers who survive large systems from those who burn out fixing the same category of bug for the tenth time."

If you've fixed the same class of bug twice, the third fix should be a library or a tool.

---

## Build and Dependency Management

### Conan — reproducible dependency management

```bash
conan install . --build=missing
```

```ini
# conanfile.txt
[requires]
boost/1.83.0
fmt/10.1.1

[generators]
CMakeDeps
CMakeToolchain
```

- Eliminates "works on my machine" — dependencies are pinned and reproducible
- Makes CI deterministic; stops writing fallback code for missing features

### CMake Toolchain Files — consistent build config

Centralise all build flags in a toolchain file instead of scatter-shot per-developer setups:

```cmake
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
```

Same flags for debug, release, CI, and every developer machine.

### ccache — build caching

```bash
export CC="ccache clang++"
```

Caches compilation outputs. Cuts build times by 50%+ on large projects with no code changes. **Long builds punish curiosity; short builds reward it** — developers avoid touching code when rebuilds are painful.

---

## Code Quality and Safety

### AddressSanitizer (ASan)

```bash
g++ -fsanitize=address -g -O1 main.cpp
```

Runtime detection of:
- Use-after-free
- Stack/heap buffer overflows
- Stack corruption

ASan in dev eliminates defensive "just in case" bounds checks — the runtime is the safety net. Always run in CI.

**ThreadSanitizer:** `-fsanitize=thread` — detects data races  
**UBSanitizer:** `-fsanitize=undefined` — detects UB including misaligned access

### clang-tidy — as a law, not a suggestion

```yaml
# .clang-tidy
Checks: '-*,modernize-*,performance-*'
WarningsAsErrors: '*'
```

Run as part of CI — not just as a warning. Automates:
- Modern C++ idiom enforcement
- Performance anti-pattern detection
- Consistent style across the team

Once style and correctness are enforced automatically, humans focus on logic.

### clang-format — automated style

```bash
clang-format -i src/*.cpp
```

Eliminates style debates entirely. Use with `--style=file` and a committed `.clang-format`.

---

## Libraries for Common Pain Points

### fmt — type-safe, fast formatting

```cpp
#include <fmt/core.h>
fmt::print("User {} logged in at {}\n", user_id, timestamp);
```

- Type-safe: no UB from mismatched printf specifiers
- Faster than `std::cout` and `printf`
- `fmt::format` returns `std::string` for string building

The standard library's `std::format` (C++20) is based on fmt.

### tl::expected / Boost.Outcome — explicit error handling

For performance-critical paths where exceptions are too expensive:

```cpp
// tl::expected — caller MUST handle failure
tl::expected<Config, std::string> parse_config(std::string_view path);

auto result = parse_config("config.json");
if (!result) { return handle_error(result.error()); }
use(result.value());
```

```cpp
// Boost.Outcome — similar semantics
outcome::result<int> load_config();
auto r = load_config();
if (r.has_error()) return outcome::failure(r.error());
```

Both force callers to handle failures — no silent exception paths, no unchecked returns. If a function can fail but the type doesn't say so, the lies surface in production.

### std::span (C++20) — safe array passing

```cpp
void normalize(std::span<float> data) {
    for (auto& v : data) v /= 255.0f;
}

// Works with vector, array, raw pointer+size — no copies
normalize(vec);
normalize(std::span{ptr, size});
```

Replaces `(float* data, size_t len)` — bounds are encoded in the type, manual size mismatch errors vanish.

### std::chrono — type-safe time

```cpp
using namespace std::chrono;
auto start   = steady_clock::now();
// ... work ...
auto elapsed = duration_cast<milliseconds>(steady_clock::now() - start);
```

Time units enforced by the type system — no accidental milliseconds-vs-seconds bugs.

### moodycamel::ConcurrentQueue — lock-free MPMC without the pain

```cpp
moodycamel::ConcurrentQueue<Task> queue;
queue.enqueue(task);
Task t; queue.try_dequeue(t);
```

Provides 95% of hand-rolled lock-free queue performance without the correctness hazards. See [C++ — Lock-Free Ring Buffers](/wiki/c-lock-free-ring-buffers/) for the full decision guide.

### std::unique_ptr with custom deleters — RAII for C resources

```cpp
auto file = std::unique_ptr<FILE, decltype(&fclose)>(
    fopen("data.txt", "r"), &fclose
);
// file closed automatically on scope exit — no cleanup comments needed
```

Encodes ownership and lifetime in the type. Use for C API resources (file handles, sockets, OpenSSL contexts).

---

## Quick Selection Table

| Problem | Tool |
|---|---|
| Reproducible dependencies | Conan |
| Consistent build flags | CMake toolchain file |
| Slow iterative builds | ccache |
| Memory bugs (use-after-free, overflow) | AddressSanitizer |
| Data races | ThreadSanitizer |
| Enforce modern C++ in CI | clang-tidy (WarningsAsErrors) |
| Logging / string formatting | fmt (or C++20 std::format) |
| Error handling without exceptions | tl::expected / Boost.Outcome |
| Safe array passing | std::span |
| Time measurement | std::chrono |
| Lock-free MPMC queue | moodycamel::ConcurrentQueue |
| RAII for C-style resources | unique_ptr with custom deleter |

---

## See Also

- [C++ — Lock-Free Ring Buffers](/wiki/c-lock-free-ring-buffers/) — full comparison of concurrent queue implementations
- [C++ — Atomics and Memory Model](/wiki/c-atomics-and-memory-model/) — understanding what moodycamel abstracts away
- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — std::format (C++20), std::span (C++20), std::expected (C++23)
- [C++ — ULL Developer Skillset](/wiki/c-ull-developer-skillset/) — tooling requirements for HFT/ULL roles

