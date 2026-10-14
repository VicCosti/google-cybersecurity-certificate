# 🐍 Lab: Debug Python Code

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** Syntax errors, exceptions (`NameError`, `IndexError`, `AttributeError`), logic errors, debugging strategy, `for` loop, list indexing, `.split()`, `with` statement

---

## 📋 Scenario Overview

As a security analyst, automated processes must run correctly and reliably. This lab develops debugging skills across all three categories of Python errors. Each task presents broken code that must be run, diagnosed by reading the error output, and fixed — using the strategy of correcting one error at a time and re-running after each fix. Tasks cover syntax errors (missing punctuation, wrong operators), runtime exceptions (mismatched variable names, out-of-range indices, incorrectly inverted method calls), and logic errors (wrong list indices that produce silent but incorrect output).

---

## ✅ Tasks Completed

| Task | Error Category | Bug | Fix |
|---|---|---|---|
| 1 | Syntax error | Missing `:` on `for` header | Added `:` after `range(10)` |
| 2 | Syntax error | Missing closing quote + comma in list literal | Closed `"zdutchma"` and added `,` before `"esmith"` |
| 3 | Syntax error | Missing closing `)` on `print()` call | Added `)` to close the outer `print()` |
| 4 | Syntax + NameError + IndentationError | `=` instead of `==`; variable name mismatch; `print` not indented | Changed to `==`; aligned variable names; indented `print` |
| 5 | Exception (`IndexError`) | `usernames_list[5]` on a 5-element list | Changed to `usernames_list[4]` |
| 6 | Syntax + AttributeError | Missing `:` on `with` header; `split.ip_addresses()` inverted | Added `:`; corrected to `ip_addresses.split()` |
| 7 | Logic errors | Wrong indices in all three `if/elif` branches | Mapped OS 1→`[0]`, OS 2→`[1]`, OS 3→`[2]` |

---

## 🔍 Questions & Answers

**Q1 — What happens when you run the code before modifying it? How can you fix this?**  
Running the original code raises a `SyntaxError` on the `for` line. Python's parser reports that it expected a `:` and found something else instead. The error fires before any code executes — Python cannot even begin running the loop because the statement is malformed. The fix is to add a colon at the end of the `for` header: `for i in range(10):`. Every compound statement header in Python — `for`, `while`, `if`, `def`, `with`, `class` — must end with a colon. Without it, Python cannot identify where the header ends and the body begins.

**Q2 — What happens when you run the code before modifying it? How can you fix it?**  
Running the original code raises a `SyntaxError`. The string `"zdutchma` is never closed — Python keeps reading characters looking for a closing quote and eventually encounters what it interprets as the opening of another string literal (`"esmith"`), producing a confusing error that may point to a different line than where the problem is. The fix is to add a closing `"` after `zdutchma` and a `,` to separate it from the next list element: `"zdutchma", "esmith"`. In Python string literals, every opening quote must have a matching closing quote of the same type, and list elements must be separated by commas.

**Q3 — What happens when you run the code before modifying it? What is causing the syntax error? How can you fix it?**  
Running the original code raises a `SyntaxError` reporting that the opening `(` of `print(` was never closed. The expression `print("update needed".upper()` has two opening parentheses — one for `print(` and one for `.upper(` — but only one closing `)` (which closes `.upper()`). The outer `print()` call is never closed. Fix: add a second `)` at the end of the line so both function calls are properly closed: `print("update needed".upper())`. The method call `.upper()` returns the string `"UPDATE NEEDED"`, which is then passed as the argument to `print()`.

**Q4 — What happens when you run the code before modifying it? What is causing the errors? How can you fix it?**  
The original code has three separate errors that fire in sequence. First, a `SyntaxError` on `if name = username:` — the assignment operator `=` is not valid in a conditional expression; Python requires `==` to compare two values. After fixing that, a `NameError` fires: the loop iterates over `username_list` but the variable was defined as `usernames_list` (with an `s`). Python cannot find `username_list` because it was never assigned. After fixing the name mismatch, an `IndentationError` fires because the `print` statement is not indented under the `if` block — Python cannot determine that it belongs to the `if` branch. Fixes: change `=` to `==`, align the variable names, and indent `print` four additional spaces inside the `if` block.

**Q5 — What happens when you run the code before modifying it? What type of error is this? How can you fix it?**  
Running the original code raises an `IndexError: list index out of range`. This is a runtime exception, not a syntax error — Python can parse the code correctly, but when it executes the `if` statement and tries to access `usernames_list[5]`, it finds that the index does not exist. `usernames_list` has five elements, and Python uses zero-based indexing, so valid indices are 0 through 4. Index 5 is one past the end of the list. Fix: change `[5]` to `[4]`, which accesses the last (fifth) element `"eraab"`. The general rule is: last valid index = `len(list) - 1`.

**Q6 — What happens when you run the code before modifying it? What is causing the errors? How can you fix them?**  
Running the original code raises a `SyntaxError` on the `with open(...)` line — the header is missing its required colon. After adding the colon, an `AttributeError` (or `NameError`) fires on `ip_addresses = split.ip_addresses()`. Python tries to find a name called `split` in the current scope and fails — `split` is not a defined variable or module. The bug is an inverted method call: `.split()` is a string method that belongs to `ip_addresses`, not a standalone function. Fix: reverse the syntax to `ip_addresses.split()`, placing the string object before the dot and the method name after it.

**Q7 — What happens when you run the code before modifying it? What is causing the logic errors? How can you fix them?**  
Running the original code produces no error — it executes and prints output — but the output is wrong. With `system = "OS 2"`, it prints `"March 1st"` instead of `"April 1st"`. With `system = "OS 1"` it would print `"May 1st"`. These are logic errors: the code is syntactically valid and raises no exceptions, but the index values in each branch are mismatched to the operating systems. `patch_schedule = ["March 1st", "April 1st", "May 1st"]` stores the dates at indices 0, 1, and 2 in order. The correct mapping is OS 1 → index 0, OS 2 → index 1, OS 3 → index 2. Fix: update the three branches to use `patch_schedule[0]`, `patch_schedule[1]`, and `patch_schedule[2]` respectively. Logic errors are the hardest category to catch because nothing signals that something is wrong — only testing with known inputs and verifying expected outputs reveals them.

**Conclusion — What are your key takeaways from this lab?**  
This lab covers the complete Python error taxonomy and a concrete strategy for each category. Syntax errors are caught by the parser before execution and are identified by reading the error message, which points to the problem line — the fix is always a punctuation or operator correction. Runtime exceptions are raised during execution when a specific condition fails: a `NameError` fires when a variable name used in the code does not match any defined variable (commonly from a typo); an `IndexError` fires when an index exceeds the valid range of a list (always `0` to `len(list) - 1`); an `AttributeError` fires when a method is called on the wrong object or an object that doesn't exist. Logic errors are the most dangerous category because they are silent — the code runs, produces output, and raises no exception, but the output is incorrect. The only defense is systematic testing: run the code with known inputs and verify that the output matches the expected result. The key debugging strategy that applies to all three categories is to fix one error at a time and re-run after each fix, because Python usually stops at the first error it encounters — resolving it may reveal a different error underneath.

---

## 💡 Key Code

```python
# ── Task 1: syntax error — missing colon ─────────────────────
for i in range(10):                          # FIX: added ':'
    print("Connection cannot be established")

# ── Task 2: syntax error — missing quote + comma ─────────────
usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith",
                  "srobinso", "dcoleman", "fbautist"]
                  # FIX: "zdutchma" closed + comma before "esmith"

# ── Task 3: syntax error — missing closing parenthesis ───────
print("update needed".upper())               # FIX: added closing ')'

# ── Task 4: NameError + SyntaxError + IndentationError ───────
username_list = ["djames", "jpark", "tbailey", "zdutchma",
                 "esmith", "srobinso", "dcoleman", "fbautist"]
username = "esmith"
for name in username_list:
    if name == username:                     # FIX: '==' not '='
        print("The user is an approved user") # FIX: indented

# ── Task 5: IndexError — last element of 5-element list ──────
usernames_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "eraab"
if username == usernames_list[4]:            # FIX: [4] not [5]
    print("This username is the final one in the list.")

# ── Task 6: syntax + AttributeError ─────────────────────────
with open(import_file, "r") as file:        # FIX 1: added ':'
    ip_addresses = file.read()
ip_addresses = ip_addresses.split()         # FIX 2: not split.ip_addresses()
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# ── Task 7: logic errors — wrong indices ─────────────────────
patch_schedule = ["March 1st", "April 1st", "May 1st"]
# index:              0             1            2
if system == "OS 1":
    print("Patch date:", patch_schedule[0])  # FIX: was [2]
elif system == "OS 2":
    print("Patch date:", patch_schedule[1])  # FIX: was [0]
elif system == "OS 3":
    print("Patch date:", patch_schedule[2])  # correct
```

---

## 🔍 Python Error Taxonomy

```
Python Errors
├── Syntax Errors
│   ├── Detected: at parse time, before any code runs
│   ├── Signal: SyntaxError / IndentationError in terminal
│   └── Examples in this lab:
│       • Missing ':' on for/with header (Tasks 1, 6)
│       • Missing closing quote or comma in list (Task 2)
│       • Missing closing parenthesis (Task 3)
│       • '=' used instead of '==' in condition (Task 4)
│       • print() not indented under if block (Task 4)
│
├── Exceptions (Runtime Errors)
│   ├── Detected: during execution, when triggered
│   ├── Signal: error name + message + traceback
│   └── Examples in this lab:
│       • NameError — variable name typo (Task 4)
│       • IndexError — index out of range (Task 5)
│       • AttributeError — method called on wrong object (Task 6)
│
└── Logic Errors
    ├── Detected: only by testing with known inputs
    ├── Signal: none — code runs, output is silently wrong
    └── Examples in this lab:
        • Wrong list indices in if/elif branches (Task 7)
```

---

## 🔍 Notable Approaches & Observations

**Task 4 — Fix the usage, not the definition:**  
The original scaffold defined `usernames_list` (with an `s`) but used `username_list` (without) in the loop. The correct fix is to update the loop line to match the definition: `for name in usernames_list:`. The submitted fix renamed the definition to `username_list` instead, which also works. However, keeping `usernames_list` is more consistent with the name used in every other task in this lab and throughout the course. When a variable name mismatch causes a `NameError`, the right question is: which spelling best describes the variable? Fix the one that is wrong.

**Task 6 — Loop over `remove_list`, not `ip_addresses`:**  
The filter loop in Task 6 iterates over `remove_list` and calls `ip_addresses.remove(element)` only after confirming the element is present. Because the loop variable and the list being modified are *different objects*, the mutation-during-iteration bug from Lab 11 does not apply. This design is inherently safer: the loop can never skip an element in `remove_list`, and the `if element in ip_addresses` guard prevents a `ValueError` when a removal target is not in the list.

**Task 7 — Logic errors require testing, not reading:**  
Logic errors are the hardest category because nothing signals that something is wrong. The code runs, Python shows no error, but the output is incorrect. The only way to catch them is to test with multiple known inputs and compare each output to the expected result. In Task 7, testing with `system = "OS 1"` reveals `"May 1st"` instead of `"March 1st"`, immediately showing the index mismatch. For any conditional that maps inputs to outputs, testing every branch is essential before trusting the code.

---

## 🧠 Key Concepts Applied

- **Syntax error** — An error Python's parser detects before execution; the code cannot run at all. Every compound statement header (`for`, `if`, `with`, `def`) requires a `:`. Every open parenthesis, bracket, or string quote requires a matching close. Equality comparisons require `==`, not `=`
- **Exception (runtime error)** — An error raised during execution when a specific condition fails. Code that is syntactically correct can still fail at runtime
- **`NameError`** — Raised when a name used in the code does not match any defined variable in the current scope; most commonly caused by a typo in the variable name
- **`IndexError`** — Raised when a list index is out of range. Python uses zero-based indexing: a list with `n` elements has valid indices `0` through `n-1`. Accessing index `n` or beyond raises `IndexError`
- **`AttributeError`** — Raised when a method or attribute is called on an object that doesn't have it, or when the object itself doesn't exist. The `split.ip_addresses()` call tried to use `split` as an object name — the fix is `ip_addresses.split()`, placing the string object before the dot
- **Logic error** — An error that produces incorrect output without raising any exception. The code runs successfully but does not do what was intended. Only detectable through testing with known inputs
- **Debugging strategy** — Fix one error at a time; re-run after each fix; read the full error message (it names the error type and points to the line); test all branches of conditional logic with known inputs
- **Zero-based indexing** — Python lists start at index 0. Last element index = `len(list) - 1`. Accessing index `len(list)` or beyond raises `IndexError`

---

## 📚 What I Learned

- Python errors fall into three distinct categories that require different debugging approaches: syntax errors are caught by the parser and fixed by correcting punctuation or operators; exceptions are caught at runtime and fixed by understanding what the specific error type means; logic errors are silent and only caught by testing
- The `=` vs `==` distinction is one of the most common syntax bugs in Python — `=` assigns a value to a variable, while `==` compares two values. Using `=` inside a condition is a `SyntaxError` in Python (unlike some other languages that allow it silently)
- Zero-based indexing means the last valid index for a list of `n` elements is always `n-1`, not `n`. Accessing index `n` raises an `IndexError` — the error message "list index out of range" combined with checking the list length immediately points to this pattern
- Method call syntax in Python always follows the pattern `object.method()` — the object the method belongs to comes first, then a dot, then the method name. Inverting this (`method.object()`) produces a `NameError` or `AttributeError` because `method` is not a defined object in scope
- Logic errors are the hardest bug category because Python provides no signal that something went wrong. The only defense is systematic testing: for every conditional branch, test with an input that triggers that branch and verify the output matches what is expected
- Fixing one error at a time is essential because Python stops at the first error it encounters. Resolving a syntax error may reveal an exception underneath; resolving that exception may reveal a logic error. Fixing multiple things simultaneously makes it impossible to know which change resolved which issue

---

## 📁 Project Files

| File | Description |
|---|---|
| [`debug_python_code.py`](./assets/debug_python_code.py) | Annotated Python script with all 7 tasks: original bugs documented, fixes applied and explained, error category noted for each |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
