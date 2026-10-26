# Python Fundamentals & Algorithmic Foundations

[![Python Version](https://img.shields.io/badge/Python-3.14%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-green.svg)](https://peps.python.org/pep-0008/)
[![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)]()

A structured, engineering-first laboratory tracking progressive mastery of Python from core syntax to idiomatic, production-grade programming. 

This repository emphasizes **first-principles understanding**—recreating core language constructs, algorithmic patterns, procedural abstractions, and state-machine engines (e.g., accumulators, extreme-value reductions, coordinate matrices, custom modular imports, entropy generators, reactive while-loops, encapsulated sub-routines) from scratch before leveraging high-level abstractions.

---

## Repository Structure & Curriculum Map

```text
.
├── course_notes.md                                  # Consolidated theory & reference manual (Days 1–4)
├── courses_notes_2_Day_5_Loops_in_Python.md         # Deep-dive iteration & entropy reference (Day 5)
├── courses_notes_3_Day_6_Functions_Blocks_While_Loops.md # Functions, scope & indefinite iteration reference (Day 6)
├── day1_Functions_Variables.txt                     # Day 1: I/O, memory assignment & variables
├── day2_Data_Types_Operations.txt                   # Day 2: Primitives, type casting & string formatting
├── day3_Control_Flow_Logic+Operators.txt            # Day 3: Scope, branching & modulo operations
├── day3_Logical_Operators.py                        # Rollercoaster ticketing logic
├── day3b_Exercise1.py                               # Parity checker (Odd/Even)
├── day3b_Exercise2.py                               # BMI 2.0 evaluation with conditional tiers
├── day3b_Exercise3.py                               # Leap Year calendar algorithm
├── day3b_Exercise4_Data_Game.py                     # Multi-branch text adventure (Treasure Island)
├── day4_my_module.py                                # Custom modular import demonstration
├── day4_Randomisation_Lists.py                      # Random floats, scaling & custom modules
├── day4b_Exercise1.py                               # Coin toss simulation (Heads/Tails)
├── day4b_Exercise2.py                               # "Banker Roulette" (Random choice from input)
├── day4b_Exercise3.py                               # 2D list coordinate matrix & treasure map
├── day4b_Exercise3_2_attempt.py                     # Alternative matrix indexing approach
├── day4b_Exercise_Card_Game.py                      # Rock, Paper, Scissors with cyclic evaluation
├── day5_Loops_in_Python.py                          # Loops, range(), accumulator pattern, max/min
├── day5b_Exercise_PyPwdGen_Easy.py                  # PyPassword Generator (Sequential version)
├── day5b_Exercise_PyPwdGen_Hard.py                  # PyPassword Generator (Randomized shuffle version)
└── day6_Functions_Block_While-loops.py              # Functions, indentation blocks & while loops
```

---

## Curriculum Overview

| Phase | Core Concepts | Applied Exercises & Capstones | Reference Docs |
| :--- | :--- | :--- | :--- |
| **Day 1: Variables & I/O** | `print()`, `input()`, string concatenation, memory pointer swapping, PEP 8 variable naming. | Band Name Generator | [`day1_Functions_Variables.txt`](day1_Functions_Variables.txt) |
| **Day 2: Data Types & Operations** | Primitives (`int`, `float`, `str`, `bool`), zero-based subscripting, type conversion, PEMDAS/BODMAS precedence, F-strings. | Tip Calculator, Life in Weeks calculation | [`day2_Data_Types_Operations.txt`](day2_Data_Types_Operations.txt) |
| **Day 3: Control Flow & Logic** | `if` / `elif` / `else` trees, indentation/lexical scope, chained comparisons, `%` modulo parity, boolean operators (`and`, `or`, `not`). | • [Odd/Even Checker](day3b_Exercise1.py)<br>• [BMI 2.0 Calculator](day3b_Exercise2.py)<br>• [Leap Year Engine](day3b_Exercise3.py)<br>• [Treasure Island Adventure](day3b_Exercise4_Data_Game.py) | [`day3_Control_Flow_Logic+Operators.txt`](day3_Control_Flow_Logic+Operators.txt) |
| **Day 4: Randomisation & Lists** | PRNG with `random` module, sequence indexing, negative offsets, mutable operations (`append`, `extend`), 2D nested lists, peer imports. | • [Coin Toss Simulator](day4b_Exercise1.py)<br>• [Banker Roulette](day4b_Exercise2.py)<br>• [2D Matrix Treasure Map](day4b_Exercise3.py)<br>• [Rock, Paper, Scissors](day4b_Exercise_Card_Game.py) | [`course_notes.md`](course_notes.md#day-4-randomisation-custom-modules-and-lists) |
| **Day 5: Loops & Algorithms** | Iteration protocols, loop scope, sequence generation with `range(start, stop, step)`, accumulator patterns, extreme-value reductions, avoiding identifier shadowing, mutability mechanics, in-place shuffling (`random.shuffle`), sequence reassembly (`"".join()`). | • [Manual `sum` & `max` Engine](day5_Loops_in_Python.py)<br>• [FizzBuzz Implementation](day5_Loops_in_Python.py)<br>• [PyPassword Generator (Easy)](day5b_Exercise_PyPwdGen_Easy.py)<br>• [PyPassword Generator (Hard)](day5b_Exercise_PyPwdGen_Hard.py) | [`courses_notes_2_Day_5_Loops_in_Python.md`](courses_notes_2_Day_5_Loops_in_Python.md) |
| **Day 6: Functions & While Loops** | Procedural abstraction (`def`), parameter syntax `()`, code blocks & indentation scope, modular composition, indefinite iteration with `while`, dynamic predicates, structural archetypes (encapsulated while loops, sequential phased pipelines, nested loops), truthiness vs. redundant equality, infinite loop diagnosis & failsafe guards, loop control (`break`, `continue`, `pass`). | • [Reeborg Navigation Engine](day6_Functions_Block_While-loops.py)<br>• [Dynamic Hurdle Traversal](day6_Functions_Block_While-loops.py)<br>• [Maze Wall-Following Engine](day6_Functions_Block_While-loops.py) | [`courses_notes_3_Day_6_Functions_Blocks_While_Loops.md`](courses_notes_3_Day_6_Functions_Blocks_While_Loops.md) |

---

## Featured Implementations

### 1. Recreating Core Reductions from Scratch ([`day5_Loops_in_Python.py`](day5_Loops_in_Python.py))
Rather than treating built-in functions as opaque black boxes, reductions are implemented explicitly using accumulator patterns and conditional comparisons:
- **Accumulator Pattern (`sum` recreation):** Tracking running totals across iteration cycles without shadowing the built-in `sum()` function.
- **Extreme Search (`max` recreation):** Initializing search states to the collection's baseline element (`scores[0]`) to guard against negative integer sets (preventing bugs caused by arbitrary `0` initializations).
- **The FizzBuzz Challenge:** Managing conditional branch precedence by evaluating the combined modulo condition (`% 3 == 0 and % 5 == 0`) before single-factor checks.

### 2. PyPassword Generator: Easy vs. Hard Entropy Architectures
The Day 5 capstone explores the security trade-offs between sequential grouping and true positional randomization:

```text
[Easy Version: Clustered]   -->  Letters: [a, b, c] + Symbols: [!, @] + Numbers: [1, 2]  -->  "abc!@12" (Predictable)
[Hard Version: High Entropy] -->  [a, b, c, !, @, 1, 2] --(Fisher-Yates Shuffle)--> "!b1@a2c" (Cryptographically Strong)
```

- **Easy Implementation ([`day5b_Exercise_PyPwdGen_Easy.py`](day5b_Exercise_PyPwdGen_Easy.py)):** Generates characters sequentially into distinct string partitions and concatenates them (`letters + symbols + numbers`). While satisfying character counts, the predictable clustering lowers password entropy.
- **Hard Implementation ([`day5b_Exercise_PyPwdGen_Hard.py`](day5b_Exercise_PyPwdGen_Hard.py)):** Solves positional clustering by evaluating two distinct architectural paradigms:
  1. **Pattern A (List Accumulator / In-Place Shuffle):** Collects random choices directly into a mutable list via count-controlled `range()` loops with throwaway variables (`for _ in range(N): ...`), executes an in-place Fisher-Yates shuffle (`random.shuffle(list)`), and joins the sequence into a string in $O(N)$ linear time with `"".join()`.
  2. **Pattern B (String Concatenation + Explicit Type Casting):** Generates sliced strings, concatenates them cleanly via grouped parentheses `(...)`, casts the immutable string into a mutable list (`list(password_str)`), performs `random.shuffle()`, and reassembles using `"".join()`.

### 3. Procedural Abstraction & Reactive Navigation ([`day6_Functions_Block_While-loops.py`](day6_Functions_Block_While-loops.py))
Day 6 introduces procedural decomposition and indefinite, sensor-driven iteration:
- **Overcoming Primitive Limits:** Constructing higher-level operations out of primitive constraints (e.g., engineering `turn_right()` via three consecutive `turn_left()` calls).
- **Definite vs. Indefinite Loops:** Transitioning from static, count-controlled iteration (`for _ in range(6): jump()`) to dynamic, goal-seeking loops (`while not at_goal():`).
- **Encapsulated & Phased While Loops:** Encapsulating indefinite loops inside functions to isolate sub-routines (e.g., ascending while wall on right $\rightarrow$ traversing $\rightarrow$ descending while path clear).
- **Binary Decision Simplification & Truthiness:** Refactoring verbose, redundant condition checks (`if wall_in_front() == True:`) into clean, idiomatic boolean branch structures (`if wall_in_front(): jump() else: move()`).
- **Algorithmic Maze Solving:** Implementing the Right-Hand Rule to navigate arbitrary, simply connected 2D mazes with edge-case anchor routines.

### 4. Cyclic Game Matrix ([`day4b_Exercise_Card_Game.py`](day4b_Exercise_Card_Game.py))
An interactive Rock, Paper, Scissors implementation featuring:
- Defensive bounds checking and input sanitization.
- Dynamic ASCII visual state rendering.
- Non-linear, cyclic decision-matrix evaluation (Rock $\rightarrow$ Scissors $\rightarrow$ Paper $\rightarrow$ Rock).

---

## Engineering Standards & Best Practices

1. **Namespace Hygiene:** Strict prevention of Python built-in shadowing. Variables are explicitly named `total_sum` or `highest_score` rather than overriding built-in identifiers (`sum`, `max`, `min`, `list`, `range`, `str`).
2. **Procedural Single Responsibility:** Functions are engineered to execute a single, well-defined task (e.g., `turn_right()` strictly handles orientation; `jump()` coordinates compound movement).
3. **Encapsulated Iteration:** When a discrete task requires internal loops (such as dynamic climbing or polling), encapsulating the `while` loop within a dedicated function isolates complexity and keeps master orchestration loops clean.
4. **Implicit Boolean Truthiness:** Direct evaluation of boolean expressions and predicates (`while not at_goal():`, `if wall_in_front():`) rather than anti-idiomatic equality comparisons (`== True`, `== False`).
5. **Infinite Loop Defense:** Ensuring every indefinite `while` loop mutates state toward a termination threshold or implements a defensive failsafe counter limit.
6. **Mutability Awareness:** Understanding the architectural boundary between **immutable strings** (read-only buffers) and **mutable lists** (in-place editable buffers). `random.shuffle()` requires a mutable sequence, raising `TypeError` if invoked directly on a string.
7. **Sequence Reassembly Optimization:** Utilizing `"".join(sequence)` ($O(N)$ single-pass memory allocation) rather than iterative string addition ($O(N^2)$ repeated memory re-allocation).
8. **Code Cleanliness & Grouped Formatting:** Utilizing parentheses `(...)` for multi-line expressions and concatenations over fragile backslash `\` line continuations.
9. **Throwaway Loop Indices:** Standardizing on `for _ in range(N):` when executing counted loops where the iteration index is intentionally unused.
10. **Zero External Dependencies:** Built entirely with Python's Standard Library to maintain zero overhead, maximum speed, and complete environment portability.

---

## Getting Started

### Prerequisites
- **Python 3.10+** (Tested and verified on **Python 3.14.8**).
- No external packages (`pip`) required.

### Running Any Exercise
Clone the repository and run any script directly using your local Python interpreter:

```bash
# Clone the repository
git clone https://github.com/t0m-a/Python.git
cd Python

# Run Day 6 Functions & While Loop Demonstrations
python day6_Functions_Block_While-loops.py

# Run the PyPassword Generator (Hard Version - Shuffled)
python day5b_Exercise_PyPwdGen_Hard.py

# Run the PyPassword Generator (Easy Version - Sequential)
python day5b_Exercise_PyPwdGen_Easy.py

# Run algorithmic reductions (sum/max from scratch, FizzBuzz)
python day5_Loops_in_Python.py

# Run game implementations (Rock, Paper, Scissors)
python day4b_Exercise_Card_Game.py
```

---

## Documentation Notes

For full theoretical breakdowns, mental models, and detailed code walkthroughs, refer to the accompanying course documentation:
- 📖 [**Consolidated Notes: Days 1–4**](course_notes.md)
- 📖 [**Iteration, Loops & Entropy Architectures: Day 5**](courses_notes_2_Day_5_Loops_in_Python.md)
- 📖 [**Functions, Scope & Indefinite Iteration: Day 6**](courses_notes_3_Day_6_Functions_Blocks_While_Loops.md)
