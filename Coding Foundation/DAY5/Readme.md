# Python Conditional Statements — Study Notes

These notes cover Python decision-making statements with simple explanations, syntax, examples, common mistakes, and practice questions.

## Contents

1. [Introduction and `if`](01_if_statement.md)
2. [`if-else` and `if-elif-else`](02_if_else_elif.md)
3. [Nested conditions and logical operators](03_nested_conditions_and_logic.md)
4. [`match-case`](04_match_case.md)
5. [Common mistakes and practice](05_practice_and_common_mistakes.md)

## Quick learning order

Study one file at a time. Type each example yourself, predict the output, and then run the code.

**Core idea:** Python checks a condition. If it evaluates to `True`, the associated indented block runs.
""",
    "01_if_statement.md": r"""# 1. Python `if` Statement

## What is a conditional statement?

A conditional statement allows a program to make a decision. For example, a program can check whether a number is positive, whether a person is old enough to vote, or whether a password matches.

## Syntax

```python
if condition:
    # code runs when condition is True
```

The colon (`:`) marks the beginning of the block. The indented lines underneath belong to the `if` statement.

## Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

Output:

```text
You are eligible to vote.
```

The condition `age >= 18` is `True`, so Python runs the `print()` statement.

## Example when the condition is false

```python
temperature = 15

if temperature > 30:
    print("It is hot.")

print("Program finished.")
```

Output:

```text
Program finished.
```

The `if` block is skipped because `15 > 30` is false. The final `print()` is not indented, so it runs regardless of the condition.

## Comparison operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `8 > 4` | `True` |
| `<` | Less than | `2 < 1` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `3 <= 7` | `True` |

**Important:** `=` assigns a value; `==` compares two values.

```python
score = 80       # assignment
print(score == 80)  # comparison: True
```

## Indentation

Python uses indentation to define code blocks. Four spaces is the usual convention.

Correct:

```python
if True:
    print("Inside the if block")
```

Incorrect:

```python
if True:
print("This causes an indentation error")
```

## Exam-ready definition

A conditional statement in Python controls the flow of a program by executing a block of code when a specified condition evaluates to `True`.

## Quick practice

1. Write a program that prints `"Positive"` if a number is greater than zero.
2. Write a program that prints `"Adult"` if `age >= 18`.
3. Predict the output:

```python
x = 4
if x == 5:
    print("Five")
print("Done")
```
""",
    "02_if_else_elif.md": r"""# 2. `if-else` and `if-elif-else`

## The `if-else` statement

Use `else` to provide an alternative block when the `if` condition is false.

### Syntax

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

### Example: even or odd

```python
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

Output:

```text
Odd number
```

The `%` operator returns the remainder. An even integer has remainder `0` when divided by `2`.

## The `if-elif-else` statement

Use `elif` (meaning “else if”) to test several conditions. Python checks them from top to bottom and runs the first matching branch.

### Syntax

```python
if condition1:
    # first case
elif condition2:
    # second case
elif condition3:
    # third case
else:
    # runs if no earlier condition is True
```

The final `else` is optional.

### Example: grade calculator

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade D")
```

Output:

```text
Grade B
```

The first condition is false. The second condition is true, so Python prints `Grade B` and skips the remaining branches.

**Tip:** Order threshold conditions carefully. Check higher marks before lower marks.

## Example: positive, negative, or zero

```python
number = -3

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Output: `Negative`

## When to use each form

- `if`: make a decision with one condition.
- `if-else`: choose between two alternatives.
- `if-elif-else`: choose between several alternatives.

## Exam-ready difference

| Statement | Purpose |
|---|---|
| `if` | Executes a block when its condition is true. |
| `if-else` | Selects between two paths. |
| `if-elif-else` | Selects the first matching path from multiple conditions. |

## Practice

1. Check whether a number is even or odd.
2. Print `"Pass"` if marks are at least 40; otherwise print `"Fail"`.
3. Print `"Small"`, `"Medium"`, or `"Large"` for a number based on thresholds you choose.
""",
    "03_nested_conditions_and_logic.md": r"""# 3. Nested Conditions and Logical Operators

## Nested `if`

A nested `if` means an `if` statement inside another `if` statement. It is useful when a second check should happen only after the first condition succeeds.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Please show your ID.")
else:
    print("You must be at least 18.")
```

Output: `Entry allowed.`

The inner `if` checks `has_id` only when `age >= 18` is true.

## Logical operators

Logical operators combine or reverse conditions.

| Operator | Meaning | Example |
|---|---|---|
| `and` | True only when both conditions are true | `age >= 18 and has_id` |
| `or` | True when at least one condition is true | `day == "Sat" or day == "Sun"` |
| `not` | Reverses a Boolean result | `not is_raining` |

### `and` example

```python
age = 21
has_ticket = True

if age >= 18 and has_ticket:
    print("You may enter.")
else:
    print("Entry denied.")
```

Both conditions must be true.

### `or` example

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")
```

Either condition can be true.

### `not` example

```python
is_raining = False

if not is_raining:
    print("You can go outside.")
```

`not False` evaluates to `True`.

## Combining comparisons

Python supports chained comparisons:

```python
marks = 65

if 0 <= marks <= 100:
    print("Valid marks")
else:
    print("Invalid marks")
```

This checks that `marks` is between 0 and 100, including both limits.

## Truth values

Conditions often evaluate to `True` or `False`. Values such as `0`, `""`, `None`, and empty collections are treated as false in a condition; non-empty strings and non-zero numbers are generally treated as true.

```python
name = ""

if name:
    print("Name entered")
else:
    print("Name is empty")
```

Output: `Name is empty`

For beginner programs, explicit comparisons can make your intention clearer.

## Practice

1. Allow login only when both username and password are correct.
2. Check whether a number is in the range 1 through 10.
3. Print `"Closed"` when `is_open` is false using `not`.
""",
    "04_match_case.md": r"""# 4. Python `match-case` Statement

## What is `match-case`?

`match-case` is Python's pattern-matching statement, introduced in Python 3.10. It is useful for choosing an action based on a value, such as a menu selection.

## Basic syntax

```python
match value:
    case pattern1:
        # code for pattern1
    case pattern2:
        # code for pattern2
    case _:
        # fallback case
```

The underscore (`_`) is a wildcard pattern. It works as a default case when no earlier case matches.

## Example: simple menu

```python
choice = int(input("Choose 1, 2, or 3: "))

match choice:
    case 1:
        print("Addition selected")
    case 2:
        print("Subtraction selected")
    case 3:
        print("Multiplication selected")
    case _:
        print("Invalid choice")
```

If the user enters `2`, the output is `Subtraction selected`.

## Using `match-case` in a calculator

```python
a = 10
b = 5
choice = 4

match choice:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case 4:
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(a / b)
    case _:
        print("Invalid operation")
```

The `if` statement inside `case 4` is an example of combining `match-case` with a conditional statement.

## `match-case` versus `if-elif-else`

| `match-case` | `if-elif-else` |
|---|---|
| Convenient for matching a value against patterns or fixed cases. | Flexible for ranges and complex Boolean conditions. |
| Requires Python 3.10 or later. | Available in older Python versions too. |
| Uses `case _` as a wildcard fallback. | Uses `else` as the fallback. |

For checking ranges such as `marks >= 75`, `if-elif-else` is usually clearer. For fixed menu choices such as `1`, `2`, and `3`, either approach can work.

## Common mistake

This is a valid `match-case` structure:

```python
match choice:
    case 1:
        print("One")
    case _:
        print("Something else")
```

Do not forget the colon after each `case` and indent its body.

## Practice

1. Make a menu with options for greeting, showing the date, and exiting.
2. Use `case _` to handle an invalid choice.
3. Add a division case that checks for division by zero.
""",
    "05_practice_and_common_mistakes.md": r"""# 5. Common Mistakes and Practice Questions

## Common mistakes

### Mistake 1: Using `=` instead of `==`

Incorrect:

```python
if number = 10:
    print("Ten")
```

Correct:

```python
if number == 10:
    print("Ten")
```

`=` assigns a value. `==` compares values.

### Mistake 2: Forgetting the colon

Incorrect:

```python
if age >= 18
    print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

### Mistake 3: Incorrect indentation

Correct:

```python
if score >= 40:
    print("Pass")
else:
    print("Fail")
```

The bodies of `if` and `else` must be indented consistently.

### Mistake 4: Checking conditions in the wrong order

Problematic:

```python
marks = 95

if marks >= 50:
    print("Grade C")
elif marks >= 90:
    print("Grade A")
```

The first condition is already true, so `Grade A` is never reached.

Better:

```python
if marks >= 90:
    print("Grade A")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

### Mistake 5: Incorrect membership validation

Problematic:

```python
if unit_from or unit_to not in units:
    print("Invalid")
```

This does not check both units as intended. Use:

```python
if unit_from not in units or unit_to not in units:
    print("Invalid unit")
```

### Mistake 6: Forgetting that `input()` returns text

```python
choice = input("Enter 1 or 2: ")

if choice == "1":
    print("Option one")
```

Here, compare with `"1"` because `input()` returns a string. Alternatively, convert the input with `int()` and handle invalid input appropriately.

---

## Practice questions

Try writing each program before checking the solutions.

1. **Positive or negative:** Ask the user for a number and print whether it is positive, negative, or zero.
2. **Even or odd:** Ask for an integer and use `%` to identify even or odd.
3. **Voting eligibility:** Ask for age and print whether the person is at least 18.
4. **Largest of two:** Ask for two numbers and print the larger one, or say they are equal.
5. **Grade calculator:** Use marks to print grades with your chosen thresholds.
6. **Login check:** Check a username and password using `and`.
7. **Calculator menu:** Use `match-case` for addition, subtraction, multiplication, division, and remainder.
8. **Unit validation:** Given a dictionary called `units`, reject input if either the source or destination unit is not in the dictionary.

## Solutions for selected questions

### 1. Positive, negative, or zero

```python
number = float(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### 2. Even or odd

```python
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 3. Voting eligibility

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

### 4. Largest of two numbers

```python
a = float(input("First number: "))
b = float(input("Second number: "))

if a > b:
    print(a, "is larger")
elif b > a:
    print(b, "is larger")
else:
    print("Both numbers are equal")
```

---

## Final revision summary

- `if`: checks one condition.
- `else`: provides an alternative when the preceding `if` condition is false.
- `elif`: checks another condition when earlier conditions were false.
- Nested `if`: puts a condition inside another condition.
- `and`: requires both conditions to be true.
- `or`: requires at least one condition to be true.
- `not`: reverses a Boolean value.
- `match-case`: matches a value against patterns; `case _` is the wildcard fallback.
- Use `==` for comparison and `=` for assignment.
- Use a colon (`:`) and correct indentation for conditional blocks.