# Python Course Notes: Day 5 — Loops in Python & the `range()` Function

A comprehensive, structured reference guide covering iteration, loop scope, algorithm recreation (`sum`, `max`, `min`), variable shadowing, and sequence generation with `range()`.

---

## Table of Contents
1. [Core Concepts of Iteration](#1-core-concepts-of-iteration)
   - [What is a `for` Loop?](#what-is-a-for-loop)
   - [Syntax & Mechanics](#syntax--mechanics)
   - [Temporary vs. Persistent Variables](#temporary-vs-persistent-variables)
2. [Indentation & Loop Scope](#2-indentation--loop-scope)
   - [Inside vs. Outside the Loop Body](#inside-vs-outside-the-loop-body)
   - [Common Indentation Pitfalls](#common-indentation-pitfalls)
3. [Algorithmic Patterns: Accumulators & Reductions](#3-algorithmic-patterns-accumulators--reductions)
   - [The Accumulator Pattern (Recreating `sum()`)](#the-accumulator-pattern-recreating-sum)
   - [Critical Best Practice: Avoiding Built-in Variable Shadowing](#critical-best-practice-avoiding-built-in-variable-shadowing)
4. [Finding Extreme Values: `max()` & `min()`](#4-finding-extreme-values-max--min)
   - [Recreating `max()` from Scratch](#recreating-max-from-scratch)
   - [Edge Case: Why Initializing to `0` Can Fail](#edge-case-why-initializing-to-0-can-fail)
   - [Extending the Algorithm: Recreating `min()`](#extending-the-algorithm-recreating-min)
5. [The `for` Loop with `range()`](#5-the-for-loop-with-range)
   - [Understanding `range(start, stop, step)`](#understanding-rangestart-stop-step)
   - [Calculating Sums of Numerical Ranges (Gauss Challenge)](#calculating-sums-of-numerical-ranges-gauss-challenge)
6. [Practical Synthesis: The Classic FizzBuzz Problem](#6-practical-synthesis-the-classic-fizzbuzz-problem)
7. [Quick Reference & Best Practices Summary](#7-quick-reference--best-practices-summary)

---

## 1. Core Concepts of Iteration

### What is a `for` Loop?
In programming, **iteration** is the process of executing a block of code repeatedly for each item in a collection or sequence. 

Instead of manually duplicating code for every element:
```python
fruits = ["apple", "peach", "pear"]

# Without loops (tedious and inflexible):
print(fruits[0])
print(fruits[1])
print(fruits[2])
```

A `for` loop automates this process cleanly and dynamically handles lists of any length:
```python
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
```

### Syntax & Mechanics
```text
for <target_variable> in <iterable_collection>:
    <statement_1>
    <statement_2>
```

#### Step-by-Step Execution Lifecycle
1. Python inspects the collection (`fruits`).
2. **Iteration 1**: `fruit` is assigned `"apple"`. The indented body runs $\rightarrow$ prints `"apple"`.
3. **Iteration 2**: `fruit` is reassigned to `"peach"`. The body runs $\rightarrow$ prints `"peach"`.
4. **Iteration 3**: `fruit` is reassigned to `"pear"`. The body runs $\rightarrow$ prints `"pear"`.
5. The list has no more items. The loop terminates, and execution continues with the subsequent unindented lines.

```python
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

**Output:**
```text
apple
apple pie
peach
peach pie
pear
pear pie
```

### Temporary vs. Persistent Variables
- **Temporary Loop Variable** (`fruit`): Re-assigned automatically at the beginning of each iteration to the next item in the collection.
- **Persistent Data Structure** (`fruits`): The original list remains unmodified throughout the iteration.

---

## 2. Indentation & Loop Scope

In Python, **whitespace and indentation define code blocks and execution scope**. Whether a line is indented or not dictates how many times it executes.

### Inside vs. Outside the Loop Body

#### Scenario A: Statement Inside the Loop Body
```python
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruits)  # Indented: Executes once per iteration (3 times total)
```
**Output:**
```text
apple
['apple', 'peach', 'pear']
peach
['apple', 'peach', 'pear']
pear
['apple', 'peach', 'pear']
```

#### Scenario B: Statement Outside the Loop Body
```python
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)  # Inside loop: executes 3 times

print(fruits)     # Unindented: executes once after the loop finishes completely
```
**Output:**
```text
apple
peach
pear
['apple', 'peach', 'pear']
```

### Common Indentation Pitfalls

| Mistake | Manifestation | Resulting Behavior |
| :--- | :--- | :--- |
| **Premature Output** | Placing a summary print statement *inside* the loop | Outputs incomplete intermediate states on every iteration instead of a final result. |
| **Accidental In-Loop Logic** | Resetting an accumulator variable *inside* the loop | Wipes out accumulated progress on each pass, retaining only the last element's value. |
| **Inconsistent Indentation** | Mixing tabs and spaces, or varying space counts | Raises `IndentationError: unindent does not match any outer indentation level`. |

---

## 3. Algorithmic Patterns: Accumulators & Reductions

Python provides built-in convenience functions such as `sum()`. However, understanding how to construct algorithms from first principles using loops and conditional logic is foundational to data manipulation and computer science.

### The Accumulator Pattern (Recreating `sum()`)

The **Accumulator Pattern** consists of three steps:
1. **Initialize** a variable before the loop to hold a baseline starting total (typically `0` for additions).
2. **Iterate** through the collection, adding each item's value into the accumulator using the addition assignment operator (`+=`).
3. **Inspect / Output** the accumulated total once the loop has completed.

```python
scores = [150, 120, 110, 130, 90, 60]

# Built-in baseline:
built_in_total = sum(scores)
print(built_in_total)  # 660

# Algorithmic recreation:
total_score = 0  # 1. Initialize accumulator

for score in scores:
    total_score += score  # 2. Accumulate: total_score = total_score + score

print(total_score)  # 3. Output final result outside loop: 660
```

### Critical Best Practice: Avoiding Built-in Variable Shadowing

> [!WARNING]
> **Never name a custom variable after built-in Python functions** such as `sum`, `max`, `min`, `list`, `type`, or `str`.

```python
# POOR PRACTICE (Shadows built-in function):
sum = 0
for score in scores:
    sum += score

# CONSEQUENCE:
# 'sum' is now an integer, not a function!
# Calling sum([1, 2, 3]) later in the same script will crash with:
# TypeError: 'int' object is not callable
```

**Recommended Alternative**: Use descriptive variable names such as `total_score`, `score_sum`, or `running_total`.

---

## 4. Finding Extreme Values: `max()` & `min()`

Python's built-in `max()` finds the highest value in an iterable, while `min()` finds the lowest.

### Recreating `max()` from Scratch

To determine the largest value without relying on `max()`:
1. Define a persistent tracking variable initialized to the **first item** in the list (`scores[0]`).
2. Iterate through every item in the list.
3. Compare the current item against the current champion: `if score > highest_score:`.
4. If the condition is met, update `highest_score` to the new value.
5. Once all items have been evaluated, `highest_score` holds the greatest number.

```python
scores = [150, 120, 110, 130, 350, 90, 60, 299]

# 1. Initialize tracker to the first item
highest_score = scores[0]

# 2. Iterate through each item
for score in scores:
    # 3. Selective state update: update only when a strictly greater value appears
    if score > highest_score:
        highest_score = score

# 4. Output final result
print(f"The highest value is: {highest_score}")  # 350
```

### Edge Case: Why Initializing to `0` Can Fail

A frequent mistake is initializing the maximum tracker to `0`:
```python
# DANGEROUS INITIALIZATION:
highest_score = 0
negative_scores = [-50, -20, -110, -5]

for score in negative_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)  # Incorrectly prints 0, which wasn't even in the list!
```

**Why initializing to `scores[0]` is superior:**
- By anchoring your baseline to the first actual element of the collection, the algorithm remains robust regardless of whether numbers are all positive, all negative, or zeroes.
- Alternatively, for completely arbitrary collections, you can initialize to negative infinity: `highest = float("-inf")`.

### Extending the Algorithm: Recreating `min()`
By inverting the comparison operator from `>` to `<`, the same structural pattern finds the minimum value:

```python
scores = [150, 120, 110, 130, 350, 90, 60, 299]

lowest_score = scores[0]

for score in scores:
    if score < lowest_score:
        lowest_score = score

print(f"The lowest value is: {lowest_score}")  # 60
```

---

## 5. The `for` Loop with `range()`

Often, you need to loop a specific number of times or generate a sequence of integers rather than looping through a pre-existing list. This is where Python's built-in `range()` function is used.

### Understanding `range(start, stop, step)`

The `range()` function produces an immutable sequence of integers:
- **`start`** *(optional, default 0)*: First number of the sequence.
- **`stop`** *(required)*: Generates numbers up to, but **not including**, this value (exclusive upper bound).
- **`step`** *(optional, default 1)*: Increment between each successive number.

```python
# 1. Single argument: range(stop) -> 0 to stop - 1
for number in range(5):
    print(number)  # Prints 0, 1, 2, 3, 4

# 2. Two arguments: range(start, stop) -> start to stop - 1
for number in range(1, 6):
    print(number)  # Prints 1, 2, 3, 4, 5

# 3. Three arguments: range(start, stop, step) -> counts with custom stride
for number in range(1, 10, 2):
    print(number)  # Prints 1, 3, 5, 7, 9
```

### Calculating Sums of Numerical Ranges (Gauss Challenge)
A famous mathematical challenge (attributed to Carl Friedrich Gauss) is summing all integers from 1 to 100 ($1 + 2 + 3 + \dots + 100 = 5050$).

Using a `for` loop with `range()`:
```python
# Remember: to include 100, the stop parameter must be 101!
total_sum = 0

for number in range(1, 101):
    total_sum += number

print(f"The sum of numbers from 1 to 100 is: {total_sum}")  # 5050
```

Summing only even numbers from 1 to 100:
```python
# Approach 1: Using the step parameter in range
even_total = 0
for number in range(2, 101, 2):
    even_total += number
print(even_total)  # 2550

# Approach 2: Using a condition with the modulo operator %
even_total_mod = 0
for number in range(1, 101):
    if number % 2 == 0:
        even_total_mod += number
print(even_total_mod)  # 2550
```

---

## 6. Practical Synthesis: The Classic FizzBuzz Problem

The **FizzBuzz** coding interview challenge seamlessly brings together `for` loops, `range()`, modulo arithmetic (`%`), and conditional branching (`if`/`elif`/`else`):

### The Rules
For numbers from 1 to 100:
1. If divisible by both 3 and 5, print `"FizzBuzz"`.
2. If divisible only by 3, print `"Fizz"`.
3. If divisible only by 5, print `"Buzz"`.
4. Otherwise, print the number itself.

### Implementation
```python
for number in range(1, 101):
    # CRITICAL: Check the combined condition (15) FIRST.
    # If checked after 3 or 5, divisible-by-15 numbers would match prematurely.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

---

## 7. Quick Reference & Best Practices Summary

| Goal | Technique | Example Code |
| :--- | :--- | :--- |
| **Iterate over elements** | `for item in collection:` | `for f in fruits: print(f)` |
| **Loop $N$ times** | `for i in range(n):` | `for i in range(10): print(i)` |
| **Accumulate sum** | Accumulator variable + `+=` | `total += val` outside loop `total = 0` |
| **Find Maximum** | Initialize to `items[0]` + `>` check | `if x > max_val: max_val = x` |
| **Find Minimum** | Initialize to `items[0]` + `<` check | `if x < min_val: min_val = x` |
| **Step / Skip values** | `range(start, stop, step)` | `range(0, 100, 5)` |
| **Check Parity / Divisibility** | Modulo `%` operator | `if num % 2 == 0:` |

### Golden Rules
1. **Scope by Indentation**: Ensure aggregation steps occur *inside* the loop and final outputs occur *outside* the loop.
2. **Avoid Name Collisions**: Do not name variables after built-in keywords (`sum`, `max`, `min`, `list`, `range`).
3. **Upper Bound is Exclusive**: `range(1, 10)` stops at 9. Always use `n + 1` as the `stop` argument if $n$ must be included.
4. **Initialize Sensibly**: Anchor comparative trackers (`max`/`min`) to an existing element in the data (`collection[0]`) rather than arbitrary numbers like `0`.
