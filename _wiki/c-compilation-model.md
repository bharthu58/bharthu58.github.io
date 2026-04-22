---
layout: page
title: "C++ — Compilation Model"
domain: "C++ / Systems"
---

## The One Definition Rule (ODR)

Every object or function in a C++ program must have **at most one definition** across the entire program (all translation units combined). Multiple declarations are fine; multiple definitions are a linker error:

```cpp
// beverage.cpp — defines GetBestBeverage()
std::string GetBestBeverage() { return "Pepsi!"; }

// main.cpp — defines GetBestBeverage() again → linker error
std::string GetBestBeverage() { return "Coke!"; }
```

---

## `inline` — ODR Dismissal, Not an Optimisation Hint

The common misconception: `inline` hints the compiler to substitute function code at call sites. Modern compilers ignore this hint entirely — they inline based on their own cost models.

**The real purpose:** marking a function (or variable, C++17) as `inline` tells the **linker** that its definition may appear in multiple translation units. The linker picks one definition and discards the rest — as if only one existed.

This is what makes **header-only function definitions** work:

```cpp
// beverage.h — inline function defined in a header
inline std::string GetBestBeverage() { return "Dr Pepper!"; }

// Both beverage.cpp and main.cpp include beverage.h
// Each translation unit sees a definition, but inline suppresses the ODR linker error
```

Without `inline`, including the same header in two `.cpp` files and linking them produces a multiple-definition error.

### Implicitly inline

These are always inline, regardless of the `inline` keyword:

- **Member functions defined inside a class body** (constructors, destructors, methods)
- **Template functions** (not full specialisations — those are subject to ODR)

```cpp
class Beverage {
    std::string GetBrand() const { return mBrand; }  // implicitly inline
};
```

Methods defined *outside* the class body in a header require explicit `inline`:

```cpp
// In header, outside class — requires explicit inline
inline std::string Beverage::GetNetVolume() const { return mNetVolume; }
```

### C++17 inline variables

Extends inline semantics to variables, solving the problem of static member initialization in headers:

```cpp
// Before C++17: mBestBeverage had to be defined in a .cpp file
// C++17: define and initialise static member directly in the header
class Beverage {
    inline static std::string mBestBeverage = "7up";  // fine in multiple TUs
};
```

### The programmer's responsibility

`inline` removes linker enforcement of ODR — it is the programmer's responsibility to ensure all definitions across translation units are identical. Differing definitions compile without error but produce undefined, order-dependent behaviour:

```cpp
// file1.cpp
inline int Foo() { return 1; }

// file2.cpp
inline int Foo() { return 42; }  // different body — UB, output depends on link order
```

---

## Copy/Move Elision — RVO and NRVO

The compiler is permitted (and in C++17, sometimes required) to construct a return value directly in the caller's storage, **eliding** the copy or move constructor entirely.

### Without elision (the naive view)

```cpp
Foo CreateFoo() {
    return Foo();  // without elision: construct temp → copy to return slot → copy to caller
}
Foo x = CreateFoo();  // up to 3 constructor calls without elision
```

With copy elision enabled (default), this reduces to exactly **one default constructor call** — the object is constructed directly in `x`.

### RVO (Return Value Optimisation)

Applies when a function returns a **temporary** (unnamed) object:

```cpp
Foo CreateFooA() {
    return Foo();  // RVO: Foo constructed directly in caller's variable
}
```

**C++17 guarantees RVO** — it is mandatory, even if `-fno-elide-constructors` is passed. The compiler has no choice.

### NRVO (Named Return Value Optimisation)

Applies when a function returns a **named local variable**:

```cpp
Foo CreateFooB() {
    Foo temp;
    temp.x = 42;
    return temp;  // NRVO: temp may be constructed directly in caller's variable
}
```

NRVO is **not guaranteed** by the standard — it is a quality-of-implementation optimisation. Most modern compilers perform it, but do not rely on it for correctness.

### Move semantics as fallback

When NRVO doesn't apply, C++ standard §12.8 mandates that returning a named local variable **treats it as an rvalue** when selecting the constructor — so the move constructor is used instead of copy, even though `temp` is technically an lvalue. This is why `std::unique_ptr` can be returned by value:

```cpp
std::unique_ptr<int> CreatePtr() {
    auto ptr = std::make_unique<int>(0);
    return ptr;  // ptr treated as rvalue — move constructor called (or NRVO applies)
}
```

### Critical invariant

**Elision can suppress constructor side-effects.** If copy/move constructors contain logic (logging, resource acquisition), that code may not run. Never put critical logic inside copy/move constructors that depends on being called at function return.

### Summary

| Scenario | C++14 | C++17 |
|---|---|---|
| Return unnamed temporary (RVO) | Permitted, usually applied | **Mandatory** — guaranteed |
| Return named local (NRVO) | Permitted, not guaranteed | Permitted, not guaranteed |
| Return named local, no elision | Copy constructor | Move constructor (lvalue treated as rvalue) |

---

## See Also

- [C++ — auto Type Deduction Reference](/wiki/c-auto-type-deduction-reference/) — `auto` and template type deduction interact with how return types are deduced
- [C++ — pImpl Idiom](/wiki/c-pimpl-idiom/) — pImpl with `unique_ptr` relies on move semantics and NRVO behaviour
- [C++ — Modern Features Reference (C++20-23)](/wiki/c-modern-features-reference-c20-23/) — C++20 adds consteval, constinit; C++23 updates to RVO guarantees

