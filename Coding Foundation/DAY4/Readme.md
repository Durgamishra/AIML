
# Python Notes: Numbers, Comparisons, and Booleans

Beginner-friendly notes with examples and practice questions.

## 1. Numbers in Python

Python commonly uses these numeric types:

- `int`: Whole numbers, such as `10`, `-4`, and `0`.
- `float`: Numbers with a decimal point, such as `3.14`, `-2.5`, and `10.0`.

### Example

```python
age = 19
price = 99.50
temperature = -3

print(age)
print(price)
print(type(age))
print(type(price))
```

### Arithmetic Operators

| Operator | Meaning | Example | Result |
|---|---|---|---:|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Modulus (remainder) | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

### Example Program

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

**Remember:**
- `/` gives a division result as a float.
- `//` gives the floor of the division result.
- `%` gives the remainder.
- `**` calculates a power.

### Operator Precedence

Python generally evaluates arithmetic in this order:

1. Parentheses: `()`
2. Powers: `**`
3. Multiplication, division, floor division, modulus: `*`, `/`, `//`, `%`
4. Addition and subtraction: `+`, `-`

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

Use parentheses when they make your intention clearer.

---

## 2. Comparison Operators

Comparison operators compare two values. Their result is always a Boolean: `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `8 > 4` | `True` |
| `<` | Less than | `2 < 1` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `3 <= 2` | `False` |

### Example Program

```python
x = 10
y = 7

print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
```

### Important: `=` vs `==`

- `=` assigns a value to a variable.
- `==` checks whether two values are equal.

```python
score = 80
print(score == 80)  # True
```

---

## 3. Boolean Values

The Boolean type, `bool`, has only two values:

- `True`
- `False`

Capitalization matters. Write `True` and `False`, not `true` or `false`.

### Example

```python
is_student = True
is_logged_in = False

print(is_student)
print(is_logged_in)
print(type(is_student))
```

Output:

```text
True
False
<class 'bool'>
```

Booleans represent conditions, such as whether a user is logged in or whether a number passes a test.

---

## 4. Logical Operators

Logical operators combine or reverse Boolean conditions.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | True when both conditions are true | `5 > 2 and 8 > 3` | `True` |
| `or` | True when at least one condition is true | `5 < 2 or 8 > 3` | `True` |
| `not` | Reverses a Boolean value | `not True` | `False` |

### Example Program

```python
age = 19
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)            # False
```

### Truth Table

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

For the `not` operator:

| A | `not A` |
|---|---|
| `True` | `False` |
| `False` | `True` |

**Easy way to remember:**
- `and`: Both conditions must be true.
- `or`: At least one condition must be true.
- `not`: Reverses the result.

---

## 5. Using Comparisons and Booleans with `if`

Comparisons are often used to make decisions.

### Example 1: Pass or Fail

```python
marks = 72

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Output:

```text
Pass
```

### Example 2: Checking Eligibility

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")
else:
    print("Entry not allowed")
```

Output:

```text
Entry allowed
```

---

## 6. Taking Numeric Input

The `input()` function returns text, also called a string. Convert it when you need a number.

### Example

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))

print(age)
print(height)
```

Without conversion, `"10"` is text, not the number `10`.

```python
print("10" + "5")  # 105: joins text
print(10 + 5)      # 15: adds numbers
```

Use:
- `int()` for whole numbers.
- `float()` for decimal numbers.

---

## 7. Common Mistakes

1. Using `=` instead of `==` for a comparison.
2. Writing `true` or `false` instead of `True` or `False`.
3. Forgetting that `input()` returns a string.
4. Trying to compare incompatible values, such as `10 > "5"`, which raises a `TypeError` in Python 3.
5. Forgetting that `and` requires both conditions to be true, while `or` requires at least one.
6. Forgetting to convert numeric input using `int()` or `float()`.

---

## 8. Practice Questions

Try these without running the code first.

### A. Predict the Output

```python
print(8 + 2 * 3)
print(17 // 5)
print(17 % 5)
print(6 == 6)
print(9 < 4)
print(not (5 > 2))
print(10 > 3 and 2 > 8)
print(10 > 3 or 2 > 8)
```

### B. Write Small Programs

1. Ask the user for two numbers and print their sum.
2. Ask for a number and print whether it is greater than zero.
3. Ask for marks and print `Pass` if marks are at least 40; otherwise print `Fail`.
4. Ask for age and whether the user has an ID. Print whether entry is allowed if age is at least 18 and the user has an ID.
5. Ask for a number and print whether it is even.

**Hint for question 5:** An even number has a remainder of `0` when divided by `2`. Use the modulus operator `%`.

Example:

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

## Quick Revision

- `int` = whole number.
- `float` = decimal number.
- Arithmetic operators calculate values.
- Comparison operators produce `True` or `False`.
- `bool` contains `True` and `False`.
- `and`, `or`, and `not` combine or reverse conditions.
- `=` assigns a value; `==` compares values.
- Convert numeric input with `int()` or `float()` when needed.

**Learning goal:** Understand how Python performs calculations, compares values, and makes decisions using Boolean logic.
