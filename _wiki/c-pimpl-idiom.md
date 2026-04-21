---
layout: page
title: "C++ — pImpl Idiom"
---

## What pImpl Solves

The **pointer to implementation** idiom (pImpl, also "Cheshire Cat" or "opaque pointer") separates a class's public interface from its private implementation details. The header exposes only a pointer to a forward-declared `Impl` struct; the implementation lives entirely in the `.cpp` file.

**Problems it solves:**

1. **ABI stability** — adding/removing private members changes the class layout, breaking binary compatibility for library users. With pImpl, layout is always `sizeof(pointer)` + public members.
2. **Compile-time isolation** — changes to private implementation do not cause recompilation of all translation units that include the header (the header doesn't change).
3. **Information hiding** — private implementation details (and their dependencies) are invisible to header consumers.

---

## Classic pImpl with `unique_ptr`

```cpp
// Widget.h — only forward declaration, no implementation details
class Widget {
public:
    Widget();
    ~Widget();
    Widget(Widget&&) noexcept;
    Widget& operator=(Widget&&) noexcept;

    void do_something();

private:
    struct Impl;
    std::unique_ptr<Impl> pImpl;
};
```

```cpp
// Widget.cpp — Impl defined here; consumers never see this
#include "Widget.h"

struct Widget::Impl {
    int counter = 0;
    std::string name;
    // ... heavy headers, private state
};

Widget::Widget() : pImpl(std::make_unique<Impl>()) {}
Widget::~Widget() = default;  // must be in .cpp — Impl must be complete here
Widget::Widget(Widget&&) noexcept = default;
Widget& Widget::operator=(Widget&&) noexcept = default;

void Widget::do_something() { pImpl->counter++; }
```

**Why `~Widget()` must be in `.cpp`:** `unique_ptr<Impl>` destructor requires `Impl` to be a complete type. If the destructor is compiler-generated in the header, `Impl` is still incomplete there → compile error.

**Cost:** one heap allocation per `Widget` construction; one pointer indirection per method call.

---

## Fast pImpl — Stack-Allocated Implementation

The classic pImpl allocates `Impl` on the heap. **Fast pImpl** pre-allocates a fixed-size buffer in the object itself:

```cpp
// Widget.h
class Widget {
public:
    Widget();
    ~Widget();
    Widget(Widget&&) noexcept;
    Widget& operator=(Widget&&) noexcept;

    void do_something();

private:
    static constexpr std::size_t kImplSize      = 64;
    static constexpr std::size_t kImplAlignment = alignof(std::max_align_t);

    alignas(kImplAlignment) std::byte storage[kImplSize];

    Impl*       impl()       { return std::launder(reinterpret_cast<Impl*>(storage)); }
    const Impl* impl() const { return std::launder(reinterpret_cast<const Impl*>(storage)); }
};
```

```cpp
// Widget.cpp
struct Widget::Impl {
    int counter = 0;
    // ... must fit in kImplSize bytes
};

static_assert(sizeof(Widget::Impl)  <= Widget::kImplSize,      "Impl too large");
static_assert(alignof(Widget::Impl) <= Widget::kImplAlignment, "Impl alignment too strict");

Widget::Widget() {
    new (storage) Impl{};           // placement new — constructs Impl in pre-allocated storage
}

Widget::~Widget() {
    std::destroy_at(impl());        // explicit destructor call (does NOT free memory)
}

Widget::Widget(Widget&& other) noexcept {
    new (storage) Impl{std::move(*other.impl())};
    std::destroy_at(other.impl());
}

Widget& Widget::operator=(Widget&& other) noexcept {
    if (this != &other) {
        std::destroy_at(impl());
        new (storage) Impl{std::move(*other.impl())};
        std::destroy_at(other.impl());
    }
    return *this;
}

void Widget::do_something() { impl()->counter++; }
```

### Key mechanisms

- `alignas(std::max_align_t)` — ensures `storage` is aligned for any fundamental type
- **Placement new** `new (storage) Impl{}` — constructs object at given address without allocation
- `std::launder` — tells the compiler that `storage` now holds an `Impl` object, suppressing UB from pointer provenance rules (required when accessing an object through storage that was not originally created as that type)
- `std::destroy_at(ptr)` — calls the destructor without freeing memory (since there is no heap allocation to free)

### Trade-offs

| | Classic pImpl | Fast pImpl |
|---|---|---|
| Allocation | Heap (`make_unique`) | None — inline storage |
| Latency | + pointer indirection + cache miss | Better cache locality |
| `Widget` size | `sizeof(pointer)` | Fixed `kImplSize` |
| Impl size constraint | Unlimited | Must fit in `kImplSize` |
| Move semantics | Free (pointer swap) | Must move-construct Impl fields |
| Risk | None | `static_assert` needed; layout changes require updating `kImplSize` |

**Use Fast pImpl for hot-path objects where heap allocation latency is unacceptable** (e.g. per-message state in HFT, per-packet handlers). Use classic pImpl for stability and simplicity.

---

## See Also

- [C++ — Compilation Model](/wiki/c-compilation-model/) — pImpl is the canonical solution to the ABI-stability problem that arises from C++ compilation rules
- [C++ — Memory and Cache Performance](/wiki/c-memory-and-cache-performance/) — fast pImpl's inline storage improves cache locality vs heap pImpl
- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — `std::is_implicit_lifetime` (C++23) simplifies some placement-new use cases

