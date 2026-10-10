# 🐍 Lab: Practice Writing Python Code

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** Notebook environment, code comments, `print()` function, strings

---

## 📋 Scenario Overview

As a security analyst, notebook environments are a common tool for writing, testing, and documenting code. In this introductory lab, the goal was to get familiar with the Jupyter notebook interface, understand the difference between markdown cells and code cells, write Python code comments, and use the `print()` function to display strings to the screen.

---

## ✅ Tasks Completed

| Task | Description | Type |
|---|---|---|
| 1 | Write text in a markdown cell | Markdown |
| 2 | Run a pre-written `print("Hello world!")` statement | Code |
| 3 | Observe that comment-only cells produce no output | Code |
| 4 | Add a descriptive comment to a code cell | Code |
| 5 | Use `print()` to display `"I am a security analyst."` | Code |
| 6 | Write a `print()` statement from scratch | Code |
| 7 | Combine all `print()` statements into a single cell | Code |

---

## 🔍 Questions & Answers

**Q1 — What do you observe about the output after running `print("Hello world!")`?**  
The `print()` function outputs the string argument directly to the screen. The text `Hello world!` appears below the code cell as standard output. This confirms that `print()` is used in Python to display information during program execution.

**Q2 — What do you observe about a cell containing only comments?**  
No output is produced. In Python, lines beginning with `#` are comments — they are ignored by the interpreter at runtime and exist solely to document the code for the reader. They have no effect on program behavior.

**Q3 — What do you observe after running a cell with only a comment line?**  
Again, no output is displayed. A comment is not an executable statement; it is documentation. The cell runs without errors, but produces no visible result — confirming that `#` lines are entirely skipped by the Python interpreter.

**Q4 — What do you observe after running `print("I am a security analyst.")`?**  
The string `I am a security analyst.` is printed to the screen. This demonstrates the basic use of `print()` with a string literal passed as an argument inside the parentheses.

**Q5 — What do you observe after running `print("Python is useful for security!")`?**  
The string `Python is useful for security!` is displayed as output. Writing this statement independently reinforced that `print()` always requires the string to be enclosed in quotes inside the parentheses.

**Q6 — What do you observe after running all three `print()` statements in a single cell?**  
All three strings are printed in sequence, each on its own line, in the exact order they appear in the code. This shows that Python executes statements top to bottom and that multiple `print()` calls in one cell produce multiple lines of output.

---

## 💡 Key Code

```python
# Task 2 — Pre-written example
print("Hello world!")

# Task 5 — Display a string
print("I am a security analyst.")

# Task 6 — Write from scratch
print("Python is useful for security!")

# Task 7 — Combine all statements
# here we will display all the messages printed before
print("Hello world!")
print("I am a security analyst.")
print("Python is useful for security!")
```

**Output (Task 7):**
```
Hello world!
I am a security analyst.
Python is useful for security!
```

---

## 🧠 Key Concepts Applied

- **Markdown cells** — Used for formatted plain text, documentation, and notes within a notebook
- **Code cells** — Used to write and execute Python code
- **Code comments (`#`)** — Document the intent of code; ignored by the Python interpreter at runtime
- **`print()` function** — Outputs a value or string to standard output (the screen)
- **String literals** — Text values enclosed in quotes passed as arguments to `print()`
- **Sequential execution** — Python executes statements in a code cell from top to bottom

---

## 📚 What I Learned

- How to navigate and use a Jupyter notebook environment (markdown vs. code cells)
- That Python comments begin with `#` and produce no output when executed
- How to use `print()` to display strings on the screen
- That multiple `print()` statements in one cell execute in order, each on a new line
- The importance of writing clear comments to document code intent — a standard practice in security analyst workflows

---

## 📁 Project Files

| File | Description |
|---|---|
| [`practice_writing_python.py`](./assets/practice_writing_python.py) | Python script with all tasks, comments, and expected outputs |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
