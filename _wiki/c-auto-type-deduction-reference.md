---
layout: page
title: "C++ — auto Type Deduction Reference"
domain: "C++ / Systems"
---

## Quick Reference: `auto` Type Deduction

| Declaration | Deduced Type | Notes |
|---|---|---|
| `auto x = expr;` | Type of `expr` | Drops reference and top-level const |
| `const auto x = expr;` | `const` type of `expr` | Still drops reference |
| `auto& x = expr;` | Reference to type of `expr` | Useful for binding to lvalues |
| `const auto& x = expr;` | Const reference | Useful for binding to temporaries (extends lifetime) |
| `auto x {expr}` (C++11/14) | Universal reference | May deduce `std::initializer_list` |
| `auto x = {a, b};` | `std::initializer_list<T>` | Use with caution — not intuitive |
| `auto x = {42};` | `std::initializer_list<int>` | Note: **not** `int` |
| `auto x = 42;` | `int` | Safe and recommended for simple values |
| `auto func();` | Return type (C++14+) | Use trailing return types if ambiguity exists |

---

## Key Rules

- `auto` always drops top-level `const` and references — add them back explicitly (`const auto&`)
- `auto x = {42}` gives `std::initializer_list<int>`, NOT `int` — a common surprise
- `auto&` creates a reference to the deduced type — won't copy
- `const auto&` is the universal read-only binding — works with both lvalues and rvalues, extends temporary lifetime
- For function return types, `auto` (C++14) works but be explicit when returning references to avoid dangling

---

## Common Patterns

```cpp
// Copy (safe for scalars and small types)
auto x = 42;
auto s = someString;  // copies the string

// Reference (no copy — use for large objects or when you need to modify)
auto& ref = container[i];

// Const reference (read-only — works with rvalues)
const auto& val = expensiveComputation();

// Range-for idioms
for (auto& elem : vec) { /* modify */ }
for (const auto& elem : vec) { /* read-only */ }
for (auto elem : vec) { /* copy each element — use for small/trivial types */ }

// Structured bindings (C++17)
auto [key, value] = *map.begin();
const auto& [k, v] = *map.begin();  // read-only binding
```

---

## Relationship to `decltype`

- `auto` deduces like a function template parameter — drops ref and cv-qualifiers
- `decltype(auto)` (C++14) preserves the exact declared type including references
- Use `decltype(auto)` as a return type when you need to perfectly forward the return expression's type

---

---

## Template Type Deduction

`auto` deduction rules are identical to template type deduction. The `ParamType` (how the parameter is declared) determines what `T` becomes.

### Three ParamType categories

**1. Reference or pointer (`T&`, `T*`, `const T&`)**

`T` is deduced as the exact type of the argument; reference-ness of the argument is stripped (already captured by ParamType):

```cpp
template<class T> void f(T& p);
int a = 0;          f(a);   // T = int,       param = int&
const int ca = 0;   f(ca);  // T = const int, param = const int&
const int& r = ca;  f(r);   // T = const int, param = const int&  (ref stripped)
```

If ParamType already has `const`, it doesn't need to be part of T:
```cpp
template<class T> void f(const T& p);
f(a);   // T = int,  param = const int&
f(ca);  // T = int,  param = const int&
```

**2. By value (`T`) — copy semantics**

Any reference-ness and top-level cv-qualifiers are stripped (making a fresh independent copy):

```cpp
template<class T> void f(T p);
f(a);    // T = int,  param = int
f(ca);   // T = int,  param = int    (const dropped — new copy)
f(r);    // T = int,  param = int    (ref and const dropped)
```

Exception: if the argument is `const T* const`, the pointer-target const is preserved (only the pointer's own const is stripped):
```cpp
const int* const cpa = &a;
f(cpa);  // T = const int*, param = const int*
```

**3. Universal/forwarding reference (`T&&`)**

The only category that can deduce to a reference type. Preserves lvalue vs rvalue:

```cpp
template<class T> void f(T&& p);
int a = 0;
f(a);   // T = int&,       param = int&      (lvalue → lvalue ref)
f(42);  // T = int,        param = int&&     (rvalue → rvalue ref)
```

### Perfect forwarding

Universal references enable perfect forwarding — preserving lvalue/rvalue nature of arguments into deeper calls:

```cpp
template<class T>
class Wrapper {
    template<class U>
    Wrapper(U&& v) : data(std::forward<U>(v)) {}  // lvalue → copy ctor; rvalue → move ctor
    T data;
};
```

### `auto` deduction mirrors template rules

| Template | Equivalent auto |
|---|---|
| `T&` param | `auto&` |
| `const T&` param | `const auto&` |
| `T` param (copy) | `auto` |
| `T&&` param (universal) | `auto&&` (forwarding) |

One difference: `auto x = {1,2,3}` deduces `std::initializer_list<int>` — template functions do not accept brace-init lists directly.

---

## See Also

- [C++ — Compilation Model](/wiki/c-compilation-model/) — RVO/NRVO interacts with deduced return types
- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — C++20/23 feature reference including `auto` params (abbreviated function templates), deducing `this`, and `auto(x)`/`auto{x}` (C++23)

