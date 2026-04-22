---
layout: page
title: "Python — Core Language Concepts"
domain: "Python"
---

## Mutable vs Immutable Objects

**Immutable types** — `int`, `float`, `str`, `tuple`: operations produce a new object, the original is unchanged.

**Mutable types** — `list`, `dict`, `set`: operations modify the original object in place.

```python
def add_item(items, value):
    items.append(value)   # modifies the original list — no return needed

my_list = [1, 2, 3]
add_item(my_list, 4)
print(my_list)  # [1, 2, 3, 4] — mutated in place
```

Understanding this explains most "why did my variable change?" bugs.

---

## Default Mutable Arguments — Classic Bug

Default argument values are evaluated **once at function definition time**, not on each call. A mutable default accumulates state across calls:

```python
def add_to_list(value, items=[]):  # WRONG — items is shared across all calls
    items.append(value)
    return items

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2] — not a fresh list!
```

**Fix:** use `None` as sentinel and create the mutable object inside the function:

```python
def add_to_list(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items
```

---

## Pass-by-Object-Reference

Python is neither "pass by value" nor "pass by reference" — it is **pass-by-object-reference**. Variables are labels pointing to objects; function arguments receive new labels for the same objects.

```python
def modify(num):
    num += 1   # num is rebound to a new int — original x is untouched

x = 5
modify(x)
print(x)  # 5 — immutable int, x still points to 5
```

For mutable objects, the function and caller share the same object — mutation inside the function is visible outside. For immutable objects, rebinding inside the function has no effect outside.

---

## `is` vs `==`

| Operator | What it checks |
|---|---|
| `==` | Value equality (calls `__eq__`) |
| `is` | Object identity (same object in memory) |

```python
a = [1, 2]
b = [1, 2]
print(a == b)  # True  — same values
print(a is b)  # False — different objects
```

**Rule:** always use `is None` / `is not None`, never `== None`. `None` is a singleton — identity check is correct and slightly faster.

---

## Iterators and Generators

An **iterator** is any object with `__iter__` and `__next__`. Calling `next()` advances it one step; it raises `StopIteration` when exhausted.

```python
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
```

A **generator function** creates an iterator using `yield` — values are produced lazily, one at a time, without storing the full sequence in memory:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)   # 3, 2, 1
```

**Use generators when:** iterating over large sequences, reading large files line-by-line, or implementing infinite streams.

---

## List Comprehensions vs Generator Expressions

```python
# List comprehension — builds and stores full list in memory
squares = [x*x for x in range(1_000_000)]   # allocates entire list

# Generator expression — lazy, one value at a time, no full allocation
squares_gen = (x*x for x in range(1_000_000))  # no memory overhead until iterated
```

Use list comprehensions when you need random access, `len()`, or multiple iterations. Use generator expressions when you iterate once over large data.

---

## Context Managers (`with`)

The `with` statement guarantees resource cleanup even if an exception occurs — no manual `try/finally` needed:

```python
# Risky: file may never close if an exception is raised before f.close()
f = open("data.txt")
data = f.read()
f.close()

# Correct: guaranteed close on exit, exception or not
with open("data.txt") as f:
    data = f.read()
```

Custom context managers implement `__enter__` and `__exit__`, or use `contextlib.contextmanager`:

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.perf_counter()
    yield
    print(f"Elapsed: {time.perf_counter() - start:.3f}s")

with timer():
    expensive_operation()
```

---

## `*args` and `**kwargs`

```python
def demo(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)       # tuple of positional extras
    print("kwargs:", kwargs)   # dict of keyword extras

demo(1, 2, 3, x=4, y=5)
# a: 1
# args: (2, 3)
# kwargs: {'x': 4, 'y': 5}
```

**Common patterns:**

```python
# Forward all arguments to a wrapped function
def wrapper(*args, **kwargs):
    log("called")
    return original(*args, **kwargs)

# Unpack a list/dict as arguments
nums = [1, 2, 3]
print(max(*nums))           # same as max(1, 2, 3)

opts = {"sep": ", ", "end": "!\n"}
print(1, 2, 3, **opts)      # same as print(1, 2, 3, sep=", ", end="!\n")
```

---

## Decorators

A decorator is a function that takes a function and returns a function. The `@` syntax is syntactic sugar for `func = decorator(func)`:

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done")
        return result
    return wrapper

@log
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
# Calling greet
# Hello, Alice
# Done
```

Use `functools.wraps(func)` on the wrapper to preserve the original function's `__name__` and `__doc__`.

Common decorator use cases: logging, timing, retry logic, access control, caching (`@functools.lru_cache`).

---

## `if __name__ == "__main__"`

When Python runs a file directly, `__name__` is set to `"__main__"`. When the file is imported as a module, `__name__` is set to the module name. This guard prevents top-level code from running on import:

```python
def main():
    print("Running as script")

if __name__ == "__main__":
    main()
```

Without this guard, any code at module level runs on import — causing side effects, slow imports, and hard-to-test code.

---

## See Also

- [Python — Package Management (uv and pipx)](/wiki/python-package-management-uv-and-pipx/) — uv and pipx for managing Python environments
- [Python — Engineering Tools](/wiki/python-engineering-tools/) — tools that enforce and automate these concepts at scale

