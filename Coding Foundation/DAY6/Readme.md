# Python Loops — Study Notes

These notes explain Python loops in beginner-friendly language, with syntax, examples, tracing, common mistakes, and practice questions.

## Contents

1. [Introduction to Loops](01_introduction_to_loops.md)
2. [The `while` Loop](02_while_loop.md)
3. [The `for` Loop and `range()`](03_for_loop_and_range.md)
4. [Loop Control: `break`, `continue`, and `pass`](04_loop_control.md)
5. [Nested Loops and Loop Patterns](05_nested_loops_and_patterns.md)
6. [Common Mistakes and Practice Questions](06_practice_and_common_mistakes.md)

## Quick revision

- A **loop** repeats a block of code.
- Use `while` when repetition depends on a condition.
- Use `for` to iterate over a sequence or iterable.
- `range(start, stop, step)` generates a sequence of integers; `stop` is excluded.
- `break` exits the nearest loop.
- `continue` skips the rest of the current iteration.
- `pass` is a placeholder that does nothing.
- An **infinite loop** keeps running until stopped or its condition becomes false.
""",
"01_introduction_to_loops.md": r"""# 1. Introduction to Python Loops

## What is a loop?

A **loop** is a programming structure that executes a block of code repeatedly. Loops help us avoid writing the same instructions many times.

### Without a loop

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

### With a loop

```python
for i in range(5):
    print("Hello")
```

Both examples print `Hello` five times, but the loop version is shorter and easier to maintain.

## Why do we use loops?

Loops are useful when we need to:
- Print a sequence of numbers.
- Process items in a list.
- Calculate a total or average.
- Repeat a program menu until the user exits.
- Validate input until the user enters a valid value.
- Create patterns such as triangles of stars.

## Types of loops in Python

Python commonly uses two looping statements:

1. **`for` loop** — iterates over items in an iterable, such as a string, list, tuple, or range.
2. **`while` loop** — repeats while a condition evaluates to `True`.

Python also supports **nested loops**, where one loop is placed inside another.

## General syntax

```python
for item in iterable:
    # code to repeat
    print(item)
```

```python
while condition:
    # code to repeat
    print("Running")
```

The indented statements belong to the loop body. Python uses indentation to identify the block.

## Important terms

- **Iteration:** one execution of the loop body.
- **Condition:** an expression that evaluates to `True` or `False`.
- **Iterable:** an object whose items can be visited one by one, such as a list or string.
- **Loop body:** the indented code that runs during each iteration.

## Example: count from 1 to 5

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

`range(1, 6)` includes 1 but excludes 6, so the loop prints 1 through 5.
""",
"02_while_loop.md": r"""# 2. The `while` Loop

## Definition

A **`while` loop** repeatedly executes a block of code as long as its condition is `True`. The condition is checked before each iteration.

## Syntax

```python
while condition:
    # statements to repeat
```

## Example 1: print numbers from 1 to 5

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Output:

```text
1
2
3
4
5
```

### How it works

1. `number = 1` initializes the counter.
2. `number <= 5` checks whether the loop should continue.
3. `print(number)` displays the current number.
4. `number += 1` increases the number by one.
5. When `number` becomes 6, the condition is false and the loop stops.

## Example 2: countdown

```python
count = 5

while count >= 1:
    print(count)
    count -= 1

print("Go!")
```

Output:

```text
5
4
3
2
1
Go!
```

## Example 3: repeat until the user enters `quit`

```python
while True:
    command = input("Enter a command (or quit): ")

    if command.lower() == "quit":
        break

    print("You entered:", command)
```

This uses `while True` to keep running. `break` exits the loop when the user types `quit`.

## Infinite loops

An **infinite loop** continues indefinitely because its stopping condition is never reached.

Example of an accidental infinite loop:

```python
number = 1

while number <= 5:
    print(number)
    # Missing number += 1
```

The value remains 1, so `number <= 5` remains true.

To avoid this, make sure the loop changes the relevant variable or has a clear exit condition.

## When should you use `while`?

Use a `while` loop when the number of repetitions is not known in advance, such as:
- Asking for a password until it is correct.
- Repeating a menu until the user chooses Exit.
- Reading input until a special value is entered.

## Exam-ready answer

A `while` loop is a control structure that repeatedly executes a block of statements as long as a specified condition is true. The condition is tested before each iteration. If it becomes false, the loop terminates. Care must be taken to update the condition-related variable; otherwise, an infinite loop may occur.
""",
"03_for_loop_and_range.md": r"""# 3. The `for` Loop and `range()`

## Definition

A **`for` loop** executes a block of code once for each item in an iterable, such as a list, string, tuple, or range.

## Syntax

```python
for item in iterable:
    # statements
```

## Example 1: loop through a string

```python
for letter in "Python":
    print(letter)
```

Output:

```text
P
y
t
h
o
n
```

Each iteration assigns the next character to `letter`.

## The `range()` function

`range()` produces a sequence of integers. It is commonly used when you want to repeat something a certain number of times.

### Forms of `range()`

| Form | Meaning |
|---|---|
| `range(stop)` | Starts at 0 and stops before `stop` |
| `range(start, stop)` | Starts at `start` and stops before `stop` |
| `range(start, stop, step)` | Moves by `step` each time |

### Example 2: `range(stop)`

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

The stop value 5 is excluded.

### Example 3: `range(start, stop)`

```python
for i in range(2, 6):
    print(i)
```

Output:

```text
2
3
4
5
```

### Example 4: use a step

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```text
2
4
6
8
10
```

The step is 2, so the sequence increases by two.

### Example 5: count backwards

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

A negative step counts down. The stop value 0 is still excluded.

## Example: calculate the sum from 1 to 5

```python
total = 0

for number in range(1, 6):
    total += number

print("Total:", total)
```

Output:

```text
Total: 15
```

The loop adds 1 + 2 + 3 + 4 + 5.

## Example: multiplication table

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
```

## `for` vs `while`

| `for` loop | `while` loop |
|---|---|
| Iterates over an iterable | Repeats while a condition is true |
| Often useful when items or repetition range are known | Often useful when the stopping point depends on a condition |
| Can manage iteration automatically | Programmer often updates a counter or state |

Both loops can solve many of the same problems. Choose the one that makes the logic clearest.

## Exam-ready answer

A `for` loop is used to iterate over the items of an iterable and execute a block of statements for each item. The `range()` function is frequently used with `for` loops to generate integer sequences. Its stop value is excluded, and an optional step controls the increment or decrement.
""",
"04_loop_control.md": r"""# 4. Loop Control: `break`, `continue`, and `pass`

These statements change how a loop behaves.

## 1. `break`

`break` immediately terminates the **nearest enclosing loop**.

```python
for number in range(1, 6):
    if number == 3:
        break
    print(number)
```

Output:

```text
1
2
```

When `number` becomes 3, `break` exits the loop. The number 3 is not printed.

## 2. `continue`

`continue` skips the remaining statements in the current iteration and moves to the next iteration.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

```text
1
2
4
5
```

Only the iteration for 3 is skipped; the loop continues afterward.

### Example: print only odd numbers

```python
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)
```

Output:

```text
1
3
5
7
9
```

The `%` operator returns the remainder. Even numbers have remainder 0 when divided by 2.

## 3. `pass`

`pass` does nothing. It is a placeholder used where Python requires a statement but you have not written the implementation yet.

```python
for number in range(3):
    pass

print("Loop finished")
```

Output:

```text
Loop finished
```

## Difference between `break`, `continue`, and `pass`

| Statement | Action |
|---|---|
| `break` | Exits the nearest loop |
| `continue` | Skips to the next iteration |
| `pass` | Does nothing; execution continues normally |

## Example: search for a number

```python
numbers = [4, 7, 10, 13, 16]
target = 10

for number in numbers:
    if number == target:
        print("Found!")
        break
else:
    print("Not found")
```

Output:

```text
Found!
```

The optional `else` attached to a loop runs only if the loop finishes without being stopped by `break`. It does not mean the same thing as an `if` statement's `else`.

## Exam-ready answer

`break`, `continue`, and `pass` are control statements used with loops. `break` terminates the nearest loop, `continue` skips the remaining part of the current iteration, and `pass` performs no operation and serves as a placeholder.
""",
"05_nested_loops_and_patterns.md": r"""# 5. Nested Loops and Loop Patterns

## What is a nested loop?

A **nested loop** is a loop placed inside another loop. The inner loop runs through its iterations for each iteration of the outer loop.

## Example 1: print a grid

```python
for row in range(3):
    for column in range(4):
        print("*", end=" ")
    print()
```

Output:

```text
* * * *
* * * *
* * * *
```

How it works:
- The outer loop runs 3 times, once for each row.
- For every row, the inner loop prints 4 stars.
- `end=" "` keeps the stars on the same line.
- The final `print()` moves to a new line.

## Example 2: right-angled triangle

```python
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")
    print()
```

Output:

```text
*
* *
* * *
* * * *
* * * * *
```

The number of stars depends on the current row.

## Example 3: number pattern

```python
for row in range(1, 5):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()
```

Output:

```text
1
1 2
1 2 3
1 2 3 4
```

## Example 4: multiplication grid

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(row * column, end=" ")
    print()
```

Output:

```text
1 2 3
2 4 6
3 6 9
```

## How many times does the inner loop run?

If the outer loop runs 3 times and the inner loop runs 4 times for each outer iteration, the inner body executes:

`3 × 4 = 12` times.

This is a useful way to understand nested-loop tracing.

## Common pattern tips

- Use `print(value, end=" ")` to stay on the same line.
- Use `print()` to start a new line.
- Trace the outer loop first, then the inner loop.
- Indentation determines which loop contains each statement.

## Exam-ready answer

A nested loop is a loop written inside another loop. The inner loop executes completely for every iteration of the outer loop. Nested loops are useful for processing tables, grids, matrices, and printing patterns. The total number of inner-loop executions depends on how many times both loops run.
""",
"06_practice_and_common_mistakes.md": r"""# 6. Common Mistakes and Practice Questions

## Common mistakes

### Mistake 1: forgetting the colon

Incorrect:

```python
for i in range(5)
    print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

### Mistake 2: incorrect indentation

Incorrect:

```python
while count < 3:
print(count)
```

Correct:

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

### Mistake 3: forgetting to update a `while` loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

If `count += 1` is omitted, the condition may never become false.

### Mistake 4: misunderstanding `range()`

```python
for i in range(1, 5):
    print(i)
```

This prints 1, 2, 3, 4 — not 5. The stop value is excluded.

### Mistake 5: confusing `break` and `continue`

- `break`: stop the loop.
- `continue`: skip this iteration and continue looping.

### Mistake 6: changing the wrong variable

In nested loops, make sure you understand which variable belongs to the inner loop and which belongs to the outer loop.

## Practice questions

Try these before checking the answers.

### Beginner

1. Print numbers from 1 to 10 using a `for` loop.
2. Print even numbers from 2 to 20.
3. Print numbers from 10 down to 1.
4. Calculate the sum of numbers from 1 to 100.
5. Print each character of a word entered by the user.

### Intermediate

6. Ask the user for a number and print its multiplication table up to 10.
7. Use a `while` loop to keep asking for a password until the correct password is entered.
8. Print numbers from 1 to 10 but skip 5 using `continue`.
9. Search for a target number in a list using `break`.
10. Print a triangle of stars with five rows.

## Sample solutions

### Solution 1: numbers from 1 to 10

```python
for number in range(1, 11):
    print(number)
```

### Solution 2: even numbers from 2 to 20

```python
for number in range(2, 21, 2):
    print(number)
```

### Solution 3: countdown

```python
for number in range(10, 0, -1):
    print(number)
```

### Solution 4: sum from 1 to 100

```python
total = 0

for number in range(1, 101):
    total += number

print("Sum:", total)
```

### Solution 5: print each character

```python
word = input("Enter a word: ")

for character in word:
    print(character)
```

### Solution 6: multiplication table

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

### Solution 7: password loop

```python
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted")
```

For real applications, do not store plain-text passwords like this; this is only a beginner exercise.

### Solution 8: skip 5

```python
for number in range(1, 11):
    if number == 5:
        continue
    print(number)
```

### Solution 9: search a list

```python
numbers = [3, 8, 12, 17, 21]
target = 17

for number in numbers:
    if number == target:
        print("Found")
        break
else:
    print("Not found")
```