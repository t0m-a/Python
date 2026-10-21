# Python Course Notes

A consolidated, structured reference compiled from course notes, exercises, and practical implementations covering Python fundamentals from Day 1 to Day 4.

---

## Table of Contents
1. [Day 1: Functions, Variables, and User Input](#day-1-functions-variables-and-user-input)
   - [Basic Functions & Nested Execution](#basic-functions--nested-execution)
   - [Variables & Memory Assignment](#variables--memory-assignment)
   - [Swapping Variable Values](#swapping-variable-values)
   - [Naming Conventions & Best Practices](#naming-conventions--best-practices)
   - [Sample Application: Band Name Generator](#sample-application-band-name-generator)
2. [Day 2: Data Types, Operations, and String Formatting](#day-2-data-types-operations-and-string-formatting)
   - [Primitive Data Types](#primitive-data-types)
   - [String Subscripting & Indexing](#string-subscripting--indexing)
   - [Type Inspection & Type Casting](#type-inspection--type-casting)
   - [String Sanitization & Validation Methods](#string-sanitization--validation-methods)
   - [Dynamic Type Parsing (`ast.literal_eval`)](#dynamic-type-parsing-astliteral_eval)
   - [Mathematical Operators & Precedence (PEMDAS / BODMAS)](#mathematical-operators--precedence-pemdas--bodmas)
   - [Number Manipulation & Rounding](#number-manipulation--rounding)
   - [Assignment Operators](#assignment-operators)
   - [String Formatting: F-Strings & Multi-line Strings](#string-formatting-f-strings--multi-line-strings)
   - [Raw Strings (`r"..."`) vs. Escape Sequences](#raw-strings-r-vs-escape-sequences)
3. [Day 3: Control Flow and Logical Operators](#day-3-control-flow-and-logical-operators)
   - [Conditional Statements (`if`, `elif`, `else`)](#conditional-statements-if-elif-else)
   - [Indentation & Scope](#indentation--scope)
   - [Comparison Operators & Chained Comparisons](#comparison-operators--chained-comparisons)
   - [Common Pitfall: Chained Comparison Directionality](#common-pitfall-chained-comparison-directionality)
   - [The Modulo Operator (`%`)](#the-modulo-operator-)
   - [Logical Operators (`and`, `or`, `not`)](#logical-operators-and-or-not)
   - [Architectural Pattern: Mutually Exclusive vs. Additive Conditions](#architectural-pattern-mutually-exclusive-vs-additive-conditions)
   - [Multi-Stage Decision Trees & Input Normalization](#multi-stage-decision-trees--input-normalization)
4. [Day 4: Randomisation, Custom Modules, and Lists](#day-4-randomisation-custom-modules-and-lists)
   - [The `random` Module Functions](#the-random-module-functions)
   - [Random Selection: Index vs. `random.choice()`](#random-selection-index-vs-randomchoice)
   - [Built-in `range()` Function](#built-in-range-function)
   - [Custom Modules & Imports](#custom-modules--imports)
   - [Lists: Fundamentals & Modification](#lists-fundamentals--modification)
   - [Common List Methods](#common-list-methods)
   - [Preventing `IndexError` via Validation Guards](#preventing-indexerror-via-validation-guards)
   - [Nested Lists (2D Lists)](#nested-lists-2d-lists)
   - [Case Study: List-Driven Games & ASCII Visuals](#case-study-list-driven-games--ascii-visuals)
   - [Decision Matrix Architectures: Cyclic vs. Monotonic Hierarchies](#decision-matrix-architectures-cyclic-vs-monotonic-hierarchies)

---

## Day 1: Functions, Variables, and User Input

### Basic Functions & Nested Execution
Python executes nested functions from the inside out (innermost function first, passing its return value outward):

```python
# The input() prompt executes first, len() measures the resulting string, and print() outputs it.
print(len(input("What is your name? ")))
```

Breaking down steps into variables improves readability and debugging:
```python
username = input("Enter your username: ")
length = len(username)
print(username)
print(length)
```

### Variables & Memory Assignment
Variables act as labeled containers for data in memory:
```python
name = input("Enter your name: ")
print("Hello " + name + "!")
print(len(name))
```

### Swapping Variable Values
Python provides multiple assignment shorthand to swap variable values cleanly without requiring a temporary intermediate variable:
```python
a = 5
b = 4

# Tuple unpacking swap
a, b = b, a

print(a)  # 4
print(b)  # 5
```

### Naming Conventions & Best Practices
- **Case Sensitivity**: Python variables are strictly case-sensitive (`Score` $\neq$ `score`).
- **Naming Style**: Use `snake_case` (lowercase letters separated by underscores) for variables and functions.
- **Rules**:
  - Cannot begin with a number (e.g., `1variable` is invalid; `variable_1` is valid).
  - Cannot use reserved keywords or built-in function names (e.g., avoid naming variables `print`, `len`, `input`, `str`, or `list`).
- **Initialization**: Variables must be defined/assigned before they can be referenced.

### Sample Application: Band Name Generator
```python
print("Welcome to the band name generator")
city_name = input("What is the name of your city?\n")
pet_name = input("What is the name of your pet?\n")
print("Your band name could be " + city_name + " " + pet_name)
```

---

## Day 2: Data Types, Operations, and String Formatting

### Primitive Data Types
Python has four primary primitive data types:
1. **String (`str`)**: Sequence of characters enclosed in quotes (`"hello"` or `'hello'`).
2. **Integer (`int`)**: Whole numbers without decimal points (`42`). Large integers can use underscores for readability (`123_456_789`).
3. **Float (`float`)**: Real numbers containing decimal points (`3.14`, `3.0`).
4. **Boolean (`bool`)**: Logical state (`True` or `False`, strictly capitalized).

### String Subscripting & Indexing
Characters in strings can be accessed using zero-based bracket notation (`[]`):
```python
text = "hello"

# Positive index: starts from the beginning (0 to length - 1)
print(text[0])   # 'h'
print(text[4])   # 'o'

# Negative index: counts backwards from the end (-1 is the last character)
print(text[-1])  # 'o'
print(text[-2])  # 'l'
```

### Type Inspection & Type Casting

#### Checking Types
Use `type()` to inspect the runtime data type of an object:
```python
print(type("string"))  # <class 'str'>
print(type(3))         # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
```

#### Explicit Type Casting (Conversion)
- `int(value)`: Converts to integer (truncates floats toward zero, removing the decimal portion).
- `float(value)`: Converts to float (e.g., `float(3)` becomes `3.0`).
- `str(value)`: Converts to string representation.
- `bool(value)`: Converts to boolean based on truthiness (`0`, `""`, and empty collections evaluate to `False`; non-zero numbers and non-empty strings evaluate to `True`).

```python
# Converting float to int truncates the decimal:
print(int(3.14))  # 3

# String conversion required for string concatenation:
length = len(input("Enter your name: "))
print("Number of letters in your name: " + str(length))

# Boolean evaluation truth table examples:
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("hello"))  # True
print(bool(3.14))     # True
```

### String Sanitization & Validation Methods
When working with user input, built-in string methods help validate and sanitize values prior to processing or casting:

```python
raw_input = "  Yes \n"

# .strip(): Removes leading and trailing whitespace/newlines
clean_input = raw_input.strip()  # "Yes"

# .lower() / .upper(): Normalizes case for resilient comparisons
print(clean_input.lower())  # "yes"
print(clean_input.upper())  # "YES"

# .isnumeric(): Checks if all characters in the string are numeric digits
num_str = "12345"
print(num_str.isnumeric())      # True
print("123a".isnumeric())       # False
```

### Dynamic Type Parsing (`ast.literal_eval`)
To safely evaluate user input into its native Python type (`int`, `float`, `list`, etc.) without the security risks of `eval()`, standard library `ast.literal_eval` can be combined with error handling:

```python
import ast

user_input = input("Enter any literal data: ")

try:
    # Parses valid Python literals safely into their native type
    parsed_value = ast.literal_eval(user_input)
except (ValueError, SyntaxError):
    # Falls back to plain string if evaluation fails
    parsed_value = user_input

print(f"Value: {parsed_value} | Type: {type(parsed_value)}")

# Type comparison and membership check
if type(parsed_value) == int:
    print("Detected integer input")
elif type(parsed_value) not in [str, int, float]:
    print("Complex or collection data type")
```

### Mathematical Operators & Precedence (PEMDAS / BODMAS)

| Operator | Name | Example | Result / Behavior |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraction | `3 - 2` | `1` |
| `*` | Multiplication | `3 * 2` | `6` |
| `/` | Division | `3 / 2` | `1.5` (*Always returns a `float` — implicit casting*) |
| `//` | Floor Division | `3 // 2` | `1` (*Rounds down to nearest integer*) |
| `**` | Exponentiation | `3 ** 2` | `9` ($3^2 = 3 \times 3$) |
| `%` | Modulo | `10 % 3` | `1` (*Returns remainder*) |

#### Order of Operations
Python follows standard mathematical precedence:
1. **P**arentheses `()`
2. **E**xponents `**`
3. **M**ultiplication & **D**ivision `*`, `/`, `//`, `%` (evaluated left-to-right)
4. **A**ddition & **S**ubtraction `+`, `-` (evaluated left-to-right)

> **Rule of Thumb**: When expressions combine multiple operations, group terms using parentheses to make evaluation order unambiguous.

### Number Manipulation & Rounding
```python
weight = 84
height = 1.65
bmi = weight / (height ** 2)

print(int(bmi))       # Truncates decimal completely (30)
print(round(bmi))     # Rounds to nearest integer (31)
print(round(bmi, 2))  # Rounds to 2 decimal places (30.85)
```

### Assignment Operators
Accumulate and update variable values directly:
```python
score = 0
score += 1  # score = score + 1 (1)
score += 3  # score = score + 3 (4)
score -= 1  # score = score - 1 (3)
```

### String Formatting: F-Strings & Multi-line Strings

#### F-Strings (`f"..."`)
Prefix the string with `f` and embed expressions or variables within curly braces `{}` without manual type conversions:
```python
score = 0
height = 1.65
is_winning = True

print(f"Your score is {score}, your height is {height}, winning: {is_winning}.")
```

#### Multi-line Strings & Escaping Quotes
```python
# Triple quotes preserve newlines and indentation:
multiline = '''
Multi-line strings can span several lines
without newline escape characters.
'''

# Quoting variations:
print('A string with a "double quote" inside')
print('Escaping a single quote \' with a backslash')
```

### Raw Strings (`r"..."`) vs. Escape Sequences
In standard Python strings, the backslash `\` character acts as an escape indicator to create special characters (such as `\n` for newline or `\t` for tab). 

However, in multi-line ASCII art, regular expressions, or file system paths, backslashes are frequently used as visual symbols (e.g. `\ 'V' /`, `\ /`, `\_-_/`) or directory separators (`C:\test`). In regular strings, an unescaped backslash can corrupt the text or trigger a `SyntaxWarning: invalid escape sequence`.

Prefixing a string with `r` or `R` creates a **raw string literal**, instructing Python to treat backslashes as plain, literal characters:

```python
# Standard string: requires manual escaping with double backslashes
path = "C:\\test\\notes.txt"

# Raw string: backslashes are preserved as literal characters
raw_path = r"C:\test\notes.txt"

# ASCII Art with raw multi-line strings r"""..."""
# Backslashes in the card graphics are preserved without manual double-escaping:
jack_card = r"""
.-----------.
| J         |
|   .---.   |
|  /     \  |
|  | ^ ^ |  |
|  \ 'V' /  |
|   `---'   |
|         J |
`-----------'
"""
```

> **Note on `re.escape()`**: While the standard library `re` module provides `re.escape()` to programmatically escape special metacharacters for regular expressions, using raw string literals (`r"..."` or `r"""..."""`) is the idiomatic solution for declaring static strings and ASCII art directly in your source code without altering formatting or requiring manual escape characters.

---

## Day 3: Control Flow and Logical Operators

### Conditional Statements (`if`, `elif`, `else`)
Conditional structures execute blocks of code depending on boolean expressions:
```python
if condition:
    # Executes when condition is True
elif another_condition:
    # Executes when another_condition is True
else:
    # Executes when all preceding conditions are False
```

### Indentation & Scope
Python relies on strict indentation (typically 4 spaces) to define code blocks. Nested conditionals require an additional level of indentation:
```python
if score >= 50:
    if score >= 90:
        print("Excellent")
    else:
        print("Passed")
else:
    print("Failed")
```

### Comparison Operators & Chained Comparisons
Used to compare two values and produce a boolean (`True` or `False`):
- `==` : Strictly equal to (Note: `=` assigns a value, `==` compares equality)
- `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

#### Chained Comparison Shorthand
Python supports mathematical chained comparisons:
```python
age = 50

# Standard logical syntax:
if age >= 45 and age <= 55:
    print("Eligible for midlife discount")

# Equivalent Pythonic chained comparison:
if 45 <= age <= 55:
    print("Eligible for midlife discount")
```

#### Common Pitfall: Chained Comparison Directionality
Python evaluates chained comparisons by joining each adjacent pair with an implicit `and`:
$$\text{operand}_1 \text{ op}_1 \text{ operand}_2 \text{ op}_2 \text{ operand}_3 \iff (\text{operand}_1 \text{ op}_1 \text{ operand}_2) \text{ and } (\text{operand}_2 \text{ op}_2 \text{ operand}_3)$$

A subtle bug occurs when reversing the comparison direction of the first operator:
```python
# Buggy attempt to check if user_choice is between 0 and 3:
if 0 >= user_choice <= 3:
    print(game_images[user_choice])
```

**Why this fails:**
1. Python evaluates `0 >= user_choice <= 3` as `(0 >= user_choice) and (user_choice <= 3)`.
2. The sub-expression `(0 >= user_choice)` asserts that `user_choice <= 0`.
3. If the user selects `1`, `2`, or `3`, `0 >= user_choice` evaluates to `False`, so the overall block is skipped and nothing prints.

**The Rule:**
Comparison operators in a chained condition must all face the same direction along the number line:
```python
# Correct ascending chain (lower_bound <= value <= upper_bound):
if 0 <= user_choice <= 3:
    print(game_images[user_choice])

# Correct descending chain (upper_bound >= value >= lower_bound):
if 3 >= user_choice >= 0:
    print(game_images[user_choice])
```

### The Modulo Operator (`%`)
The modulo operator returns the division remainder and is commonly used for even/odd parity checks:
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

### Logical Operators (`and`, `or`, `not`)
Combine or invert conditional statements:

- **`and`**: Returns `True` only if **both** operands evaluate to `True`.
- **`or`**: Returns `True` if **at least one** operand evaluates to `True`.
- **`not`**: Reverses the boolean state (`not True` $\rightarrow$ `False`, `not False` $\rightarrow$ `True`).

```python
a = 12

# AND: both conditions must be true
print(a > 10 and a < 15)  # True (both are True)
print(a > 10 and a < 12)  # False (12 < 12 is False)

# OR: only one condition needs to be true
print(a == 12 or a < 5)   # True

# NOT: inverts the result
print(not (a == 12))      # False
```

### Architectural Pattern: Mutually Exclusive vs. Additive Conditions
A common architectural pitfall is mixing mutually exclusive branches with independent feature add-ons. 
- Use `if-elif-else` for **mutually exclusive** tiers (only one applies).
- Use subsequent independent `if` statements for **cumulative** options.

#### Example: Theme Park Ticketing
```python
height = int(input("Please enter your height in cm: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Please enter your age: "))

    # Mutually exclusive base ticket tier
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        bill = 0
        print("Special pass: Free ride!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    # Independent conditional add-on (does not belong in the elif chain above)
    wants_photo = input("Do you want a photo taken? (Y/N): ").strip().upper()
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you must grow taller before riding.")
```

### Multi-Stage Decision Trees & Input Normalization
Interactive adventure flows use nested decision blocks where progression depends on valid choices at each step. Chaining `.lower()` directly onto `input()` ensures comparisons succeed regardless of user casing:

```python
print("Welcome to Treasure Island.")
choice1 = input('Crossroad: do you go "left" or "right"?\n').strip().lower()

if choice1 == "left":
    choice2 = input('Lake: type "wait" for a boat or "swim" to cross:\n').strip().lower()
    if choice2 == "wait":
        door = input('House with 3 doors: "red", "yellow", or "blue"?\n').strip().lower()
        if door == "yellow":
            print("You Win! You found the treasure!")
        elif door == "red":
            print("Room full of fire. Game Over.")
        elif door == "blue":
            print("Room full of beasts. Game Over.")
        else:
            print("Door does not exist. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fell into a hole. Game Over.")
```

---

## Day 4: Randomisation, Custom Modules, and Lists

### The `random` Module Functions
Python's standard `random` module provides pseudo-random number generation:

```python
import random

# 1. random.randint(a, b): Random integer in [a, b] inclusive of both endpoints
dice_roll = random.randint(1, 6)

# 2. random.uniform(a, b): Random float in range [a, b]
random_weight = random.uniform(2.5, 5.0)

# 3. random.random(): Random float in semi-open range [0.0, 1.0)
# Scale by 100 to obtain a float in [0.0, 100.0):
scaled_float = random.random() * 100

# 4. Binary event simulation (e.g. Coin Toss):
coin_toss = random.randint(0, 1)
print("Heads" if coin_toss == 0 else "Tails")
```

### Random Selection: Index vs. `random.choice()`
When selecting an element at random from a list or sequence, there are two distinct approaches:

```python
friends = ["Alice", "Bob", "Charlie", "Emma"]

# Approach A: Manual random index calculation
random_index = random.randint(0, len(friends) - 1)
selected_friend_1 = friends[random_index]

# Approach B: Pythonic one-liner using random.choice()
selected_friend_2 = random.choice(friends)
```

### Built-in `range()` Function
Generates a sequence of numbers from `start` to `stop` (exclusive) with an optional `step`:
```python
start = 0
stop = 100
step = 3

# Sequence from 0 up to 99 in steps of 3:
r = range(start, stop, step)
```

### Custom Modules & Imports
Any Python file (`.py`) can serve as an imported module.
For example, if `day4_my_module.py` contains:
```python
my_favourite_number = 3.1415
```

It can be imported and accessed in another file:
```python
import day4_my_module

print(day4_my_module.my_favourite_number)  # 3.1415
```

### Lists: Fundamentals & Modification
A list is an ordered, mutable sequence that can hold multiple values, including mixed data types:
```python
fruits = ["Pear", "Apple", "Grapes"]

# Access by zero-based index:
print(fruits[0])   # 'Pear' (1st element)
print(fruits[1])   # 'Apple' (2nd element)

# Negative index offsets from the end:
print(fruits[-1])  # 'Grapes' (last element)

# Modify item in-place:
fruits[2] = "Banana"
print(fruits)      # ['Pear', 'Apple', 'Banana']
```

### Common List Methods
```python
fruits = ["Pear", "Apple", "Banana"]

# .append(item): Adds single element to the end:
fruits.append("Pineapple")
# ['Pear', 'Apple', 'Banana', 'Pineapple']

# .extend(iterable): Appends elements from another list/iterable to the end:
fruits.extend(["Orange", "Apple", "Red Apple"])
# ['Pear', 'Apple', 'Banana', 'Pineapple', 'Orange', 'Apple', 'Red Apple']

# len(list): Returns total number of items
print(len(fruits))  # 7
```

Other available list methods include:
- `list.insert(index, item)`: Inserts an item at a given index.
- `list.remove(item)`: Removes the first matching item found.
- `list.clear()`: Empties the entire list.

### Preventing `IndexError` via Validation Guards
List indices run from `0` to `len(list) - 1`. Subscripting outside this range triggers an unhandled `IndexError`:

```python
items = ["a", "b", "c"]
total_items = len(items)  # 3

# Correct offset for the last element:
last_item = items[total_items - 1]  # items[2] -> 'c'
# Or using negative index:
last_item = items[-1]
```

#### Guarding User Selection
When mapping user input directly to list elements, validate the index boundary before accessing the list:

```python
options = ["Option A", "Option B", "Option C"]
user_choice = int(input("Choose an index (0-2): "))

# Validation guard to avert IndexError
if 0 <= user_choice < len(options):
    print(f"You selected: {options[user_choice]}")
else:
    print("Invalid choice! Out of bounds.")
```

### Nested Lists (2D Lists)
Lists can store other lists, creating multidimensional data structures:
```python
fruits = ["Pear", "Apple", "Grapes"]
vegetables = ["Kale", "Lettuce", "Carrot", "Broccoli"]

# Combine into a nested 2D list:
groceries = [fruits, vegetables]
print(groceries)
# Output: [['Pear', 'Apple', 'Grapes'], ['Kale', 'Lettuce', 'Carrot', 'Broccoli']]

print(len(groceries))  # 2 (contains two sublists)

# Access outer list:
print(groceries[1])    # ['Kale', 'Lettuce', 'Carrot', 'Broccoli']

# Access inner elements using chained brackets [outer_index][inner_index]:
print(groceries[0][0])  # 'Pear' (1st item of 1st list)
print(groceries[1][2])  # 'Carrot' (3rd item of 2nd list)
```

### Case Study: List-Driven Games & ASCII Visuals
Lists can store complex multi-line strings (such as ASCII graphics) indexed by numeric game choices. This pattern powers games like Rock-Paper-Scissors:

```python
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n"))

# 1. Guard against invalid input index
if user_choice < 0 or user_choice >= 3:
    print("You entered an invalid number. You lose!")
else:
    print(game_images[user_choice])

    # 2. Generate computer choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # 3. Evaluate game outcome logic
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win! Rock beats Scissors.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose! Rock beats Scissors.")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose!")
```

### Decision Matrix Architectures: Cyclic vs. Monotonic Hierarchies
When mapping game choices or decision rules to numerical list indices, conditional evaluation depends heavily on whether the hierarchy is **cyclic** or **monotonic**:

#### 1. Cyclic (Non-Transitive) Hierarchies (e.g., Rock-Paper-Scissors)
- **Rule Structure**: Rock (0) beats Scissors (2), Scissors (2) beats Paper (1), Paper (1) beats Rock (0).
- Because `0 > 2` is mathematically false, numeric order alone cannot resolve all matchups. You must include explicit edge-case overrides (`user == 0 and computer == 2`) or use modulo arithmetic `(user - computer) % 3 == 1`.

#### 2. Monotonic (Transitive) Hierarchies (e.g., Card High-Card Duel)
- **Rule Structure**: Ace (3) beats King (2), Queen (1), and Jack (0); King (2) beats Queen (1) and Jack (0); Queen (1) beats Jack (0); Jack (0) loses to all higher cards.
- **Exhaustive Matching vs. Collapsed Mathematical Ordering**:
  - In an *exhaustive* approach, each rank comparison is written as an explicit branch:
    ```python
    # Exhaustive Pairwise Matching (verbose and prone to missed combinations):
    if user_choice == 3 and computer_choice < 3:
        print("You win!")
    elif user_choice == 2 and computer_choice < 2:
        print("You win!")
    elif user_choice == 1 and computer_choice < 1:
        print("You win!")
    # ... repeats for all loss and draw permutations
    ```
  - In a *collapsed numerical* approach, because the list indices directly reflect rank order ($3 > 2 > 1 > 0$), once the draw and boundaries are handled, the entire decision tree collapses into single greater-than/less-than checks:

```python
import random

jack = r"""
.-----------.
| J         |
|   .---.   |
|  /     \  |
|  | ^ ^ |  |
|  \ 'V' /  |
|   `---'   |
|         J |
`-----------'
"""

queen = r"""
.-----------.
| Q         |
|   _ O _   |
|  ( / \ )  |
|   |v v|   |
|   \_O_/   |
|         Q |
`-----------'
"""

king = r"""
.-----------.
| K         |
|   _---_   |
|  [M_M_M]  |
|   |o_o|   |
|   \_-_/   |
|         K |
`-----------'
"""

ace = r"""
.-----------.
| A         |
|     _     |
|    ( )    |
|   (_._)   |
|     |     |
|         A |
`-----------'
"""

cards = [jack, queen, king, ace]

user_choice = int(input("Choose a card (0 for Jack, 1 for Queen, 2 for King, 3 for Ace):\n"))

# 1. Validation guard: bounds check
if user_choice < 0 or user_choice > 3:
    print("Wrong value, you lose!")
else:
    print(cards[user_choice])

    # 2. Computer turn
    computer_choice = random.randint(0, 3)
    print("Computer chose:")
    print(cards[computer_choice])

    # 3. Collapsed monotonic comparison
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose!")
```
