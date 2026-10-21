# Python Fundamentals & Algorithmic Foundations

[![Python Version](https://img.shields.io/badge/Python-3.14%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-green.svg)](https://peps.python.org/pep-0008/)
[![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)]()

A structured, engineering-first laboratory tracking progressive mastery of Python from core syntax to idiomatic, production-grade programming. 

This repository emphasizes **first-principles understanding**—recreating core language constructs and algorithms (e.g., accumulators, extreme-value reductions, coordinate matrices, custom modular imports) from scratch before leveraging high-level abstractions.

---

## Repository Structure & Curriculum Map

```text
.
├── course_notes.md                              # Deep-dive theory and reference (Days 1–4)
├── courses_notes_2_Day_5_Loops_in_Python.md     # Deep-dive theory and reference (Day 5)
├── day1_Functions_Variables.txt                 # Day 1: I/O, memory assignment & variables
├── day2_Data_Types_Operations.txt               # Day 2: Primitives, type casting & formatting
├── day3_Control_Flow_Logic+Operators.txt        # Day 3: Scope, branching & modulo operations
├── day3_Logical_Operators.py                    # Rollercoaster ticketing logic
├── day3b_Exercise1.py                           # Parity checker (Odd/Even)
├── day3b_Exercise2.py                           # BMI 2.0 evaluation with conditional tiers
├── day3b_Exercise3.py                           # Leap Year calendar algorithm
├── day3b_Exercise4_Data_Game.py                 # Multi-branch text adventure (Treasure Island)
├── day4_my_module.py                            # Custom modular import demonstration
├── day4_Randomisation_Lists.py                  # Random floats, scaling & custom modules
├── day4b_Exercise1.py                           # Coin toss simulation (Heads/Tails)
├── day4b_Exercise2.py                           # "Banker Roulette" (Random choice from input)
├── day4b_Exercise3.py                           # 2D list coordinate matrix & treasure map
├── day4b_Exercise3_2_attempt.py                 # Alternative matrix indexing approach
├── day4b_Exercise_Card_Game.py                  # Rock, Paper, Scissors with cyclic evaluation
├── day5_Loops_in_Python.py                      # Loops, range(), accumulator pattern, max/min
├── day5b_Exercise_PyPwdGen_Easy.py              # PyPassword Generator (Sequential version)
└── day5b_Exercise_PyPwdGen_Hard.py              # PyPassword Generator (Randomized shuffle version)
```

---

## Curriculum Overview

| Phase | Core Concepts | Applied Exercises & Capstones | Reference Docs |
| :--- | :--- | :--- | :--- |
| **Day 1: Variables & I/O** | `print()`, `input()`, string concatenation, memory pointer swapping, PEP 8 variable naming. | Band Name Generator | [`day1_Functions_Variables.txt`](day1_Functions_Variables.txt) |
| **Day 2: Data Types & Operations** | Primitives (`int`, `float`, `str`, `bool`), zero-based subscripting, type conversion, PEMDAS/BODMAS precedence, F-strings. | Tip Calculator, Life in Weeks calculation | [`day2_Data_Types_Operations.txt`](day2_Data_Types_Operations.txt) |
| **Day 3: Control Flow & Logic** | `if` / `elif` / `else` trees, indentation/lexical scope, chained comparisons, `%` modulo parity, boolean operators (`and`, `or`, `not`). | • [Odd/Even Checker](day3b_Exercise1.py)<br>• [BMI 2.0 Calculator](day3b_Exercise2.py)<br>• [Leap Year Engine](day3b_Exercise3.py)<br>• [Treasure Island Adventure](day3b_Exercise4_Data_Game.py) | [`day3_Control_Flow_Logic+Operators.txt`](day3_Control_Flow_Logic+Operators.txt) |
| **Day 4: Randomisation & Lists** | PRNG with `random` module, sequence indexing, negative offsets, mutable operations (`append`, `extend`), 2D nested lists, peer imports. | • [Coin Toss Simulator](day4b_Exercise1.py)<br>• [Banker Roulette](day4b_Exercise2.py)<br>• [2D Matrix Treasure Map](day4b_Exercise3.py)<br>• [Rock, Paper, Scissors](day4b_Exercise_Card_Game.py) | [`course_notes.md`](course_notes.md#day-4-randomisation-custom-modules-and-lists) |
| **Day 5: Loops & Algorithms** | Iteration protocols, loop scope, sequence generation with `range()`, accumulator patterns, extreme-value reductions, avoiding identifier shadowing. | • [Manual `sum` & `max` Engine](day5_Loops_in_Python.py)<br>• [FizzBuzz Implementation](day5_Loops_in_Python.py)<br>• [PyPassword Generator (Easy)](day5b_Exercise_PyPwdGen_Easy.py)<br>• [PyPassword Generator (Hard)](day5b_Exercise_PyPwdGen_Hard.py) | [`courses_notes_2_Day_5_Loops_in_Python.md`](courses_notes_2_Day_5_Loops_in_Python.md) |

---

## Featured Implementations

### 1. Recreating Core Reductions from Scratch ([`day5_Loops_in_Python.py`](day5_Loops_in_Python.py))
Rather than treating built-in functions as opaque black boxes, reductions are implemented explicitly using accumulator patterns and conditional comparisons:
- **Accumulator Pattern (`sum` recreation):** Tracking a running sum across iteration cycles without shadowing the built-in `sum()` function.
- **Extreme Search (`max` recreation):** Initializing search states to the collection's baseline element (`scores[0]`) to guard against negative integer sets.

### 2. PyPassword Generator ([`day5b_Exercise_PyPwdGen_Hard.py`](day5b_Exercise_PyPwdGen_Hard.py))
A password generator implementing multi-stage entropy:
- **Character Pool Segregation:** Separate sets for lowercase/uppercase alphabets, numeric digits, and punctuation symbols.
- **Controlled Generation:** User-defined quotas per character class.
- **Randomization Architecture:** Comparative evaluation of iterative string truncation vs. in-place list shuffling (`random.shuffle()`) to eliminate character-type clustering.

### 3. Cyclic Game Matrix ([`day4b_Exercise_Card_Game.py`](day4b_Exercise_Card_Game.py))
An interactive Rock, Paper, Scissors implementation featuring:
- Input sanitization and bounds checking.
- Dynamic ASCII visual state rendering.
- Non-linear, cyclic decision-matrix evaluation (Rock $\rightarrow$ Scissors $\rightarrow$ Paper $\rightarrow$ Rock).

---

## Engineering Standards & Best Practices

1. **Namespace Hygiene:** Strict prevention of Python built-in shadowing (e.g., avoiding variable declarations like `sum`, `max`, `min`, `list`, or `str`).
2. **PEP 8 Compliance:** Idiomatic snake_case variable and function naming, standard 4-space indentation, and clean whitespace boundaries.
3. **Defensive Validation:** Guarding against common runtime errors (`IndexError`, `ValueError`, type mismatch) via explicit input normalization and pre-condition validation.
4. **Zero External Dependencies:** Built entirely with Python's Standard Library to maintain zero overhead and complete environment portability.

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

# Run an interactive exercise (e.g., Password Generator)
python day5b_Exercise_PyPwdGen_Hard.py

# Run a game implementation (e.g., Rock Paper Scissors)
python day4b_Exercise_Card_Game.py

# Run algorithmic reductions
python day5_Loops_in_Python.py
```

---

## Documentation Notes

For full theoretical breakdowns, mental models, and detailed code walkthroughs, refer to the accompanying course documentation:
- 📖 [**Consolidated Notes: Days 1–4**](course_notes.md)
- 📖 [**Iteration & Algorithmic Patterns: Day 5**](courses_notes_2_Day_5_Loops_in_Python.md)

