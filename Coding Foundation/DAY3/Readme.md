from pathlib import Path

content = r"""# Python Text Formatter 🐍

A beginner-friendly Python project that transforms text using a simple menu-driven program. This project practises Python strings, string methods, functions, arguments, return values, user input, and f-string formatting.

## 📌 Project Overview

The **Text Formatter** asks the user to enter text and choose an operation. It then formats the text or reports its character and word counts.

## ✨ Features

- Convert text to **UPPERCASE**
- Convert text to **lowercase**
- Convert text to **Title Case**
- Remove surrounding whitespace
- Count characters and words
- Handle invalid menu choices gracefully
- Display results in a neat, readable format

## 🧠 Python Concepts Practised

- Variables and data types
- `input()` and `print()`
- Strings and string methods: `.upper()`, `.lower()`, `.title()`, `.strip()`, `.split()`
- Functions, parameters, arguments, and `return`
- Conditional statements: `if`, `elif`, and `else`
- f-strings for formatted output
- Basic input validation

## 🛠️ Requirements

- Python 3.10 or newer
- Visual Studio Code (recommended)

No external Python packages are required.

## 🚀 How to Run

1. Install Python if it is not already installed.
2. Open the project folder in Visual Studio Code.
3. Create a file named `text_formatter.py`.
4. Add your completed program and save the file.
5. Open the VS Code terminal.
6. Run:

   ```bash
   python text_formatter.py
   ```

   On Windows, you can also try:

   ```bash
   py text_formatter.py
   ```

## 📋 Menu Options

| Choice | Operation | Example |
|---|---|---|
| 1 | Uppercase | `hello` → `HELLO` |
| 2 | Lowercase | `HELLO` → `hello` |
| 3 | Title Case | `hello python` → `Hello Python` |
| 4 | Remove surrounding spaces | `  hello  ` → `hello` |
| 5 | Count characters and words | `Hello Python` → 12 characters, 2 words |

For option 5, count characters after removing surrounding whitespace. Spaces between words are included in the character count.

## 💻 Example Run

```text
========== TEXT FORMATTER ==========
Enter your text:   hello python

Choose an operation:
1. Uppercase
2. Lowercase
3. Title Case
4. Remove surrounding spaces
5. Count characters and words

Enter your choice: 3

========== RESULT ==========
Original text: hello python
Formatted text: Hello Python
================================
```

## 📁 Suggested Project Structure

```text
python-text-formatter/
├── text_formatter.py
└── README.md
```

## 🧪 Testing Checklist

- [ ] Uppercase conversion works
- [ ] Lowercase conversion works
- [ ] Title Case conversion works
- [ ] Surrounding whitespace is removed
- [ ] Character and word counts are correct
- [ ] Invalid choices are handled clearly
- [ ] Empty input is handled appropriately

## 🎯 Learning Goal

The goal is to build the program independently and understand how functions, string methods, conditions, and formatted output work together.

## 📜 License

This project is intended for learning and practice. You may adapt it for your own educational use.
"""
path = Path("/mnt/data/README.md")
path.write_text(content, encoding="utf-8")
print(f"Created: {path}\nSize: {path.stat().st_size} bytes")
