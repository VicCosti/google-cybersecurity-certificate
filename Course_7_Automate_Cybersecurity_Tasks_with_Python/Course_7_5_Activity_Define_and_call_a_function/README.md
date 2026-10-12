# 🐍 Lab: Define and Call a Function

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** User-defined functions, `def` keyword, function headers, function bodies, calling functions, `for` loops inside functions, string concatenation, accumulator pattern

---

## 📋 Scenario Overview

As a security analyst, reusing the same block of code across multiple tasks is a daily reality. In this lab, two user-defined functions were built and called: `alert()`, which displays a security warning message — first as a single print statement, then with a `for` loop to repeat it three times — and `list_to_string()`, which progressively evolved from a simple loop that prints usernames to a string concatenation accumulator that merges the list into a single, comma-separated string.

---

## ✅ Tasks Completed

| Task | Description | Key Construct |
|---|---|---|
| 1 | Analyze an `alert()` function definition (no call) | `def`, function body, `print()` |
| 2 | Call `alert()` and observe single-line output | Function call syntax |
| 3 | Call a new `alert()` containing a `for` loop; observe 3-line output | `for` + `range()` inside a function |
| 4 | Write the function header for `list_to_string()` | `def list_to_string():` |
| 5 | Add a `for` loop body; print each username individually | `for` loop over a list |
| 6 | Use string concatenation to merge usernames into one string | Accumulator pattern with `+` |
| 7 | Append `", "` after each username for readability | String concatenation with separator |

---

## 🔍 Questions & Answers

**Q1 — Summarize what the `alert()` function does. What would the output be if it were called?**  
The function body contains a single call to the built-in `print()` function that displays a fixed security message. Defining the function with `def alert():` stores the instructions but does not execute them — no output is produced until the function is explicitly called. When `alert()` is called, Python enters the function body, executes `print("Potential security issue. Investigate further.")`, and displays that message to the console. Defining the function and calling it are two separate actions; the definition is the blueprint, and the call is what triggers execution.

**Q2 — What are the advantages of placing this code in a function rather than running it directly?**  
Wrapping the print statement in a function follows the DRY (Don't Repeat Yourself) principle: instead of copying the same line of code everywhere a security alert is needed, a single call to `alert()` can be placed anywhere in the program. This has three concrete benefits. First, it reduces the amount of code that needs to be written. Second, it makes maintenance simpler — if the message text ever changes, only the function body needs to be updated rather than every location where the message appears. Third, it makes the code self-documenting: reading `alert()` in a script immediately communicates the intent, whereas an inline `print("Potential security issue...")` requires the reader to interpret the message manually each time.

**Q3 — How does the output from the new `alert()` compare to the previous version? How are the two definitions different?**  
The previous `alert()` printed the message exactly once. The new version wraps the `print()` call in a `for` loop — `for i in range(3)` — so the message is printed three times in sequence. Both functions are called with identical syntax (`alert()`), but their internal implementations differ: the first body is a single statement, while the second adds a loop that controls how many times that statement runs. The key takeaway is that the function's internal complexity is hidden from the caller — the interface stays the same while the behavior changes.

**Q4 — What do you observe from the output of `list_to_string()`?**  
Calling `list_to_string()` executes the entire function body in one step: the `for` loop iterates over all eight usernames in `username_list` and prints each one on its own line. Without the function, the same loop would need to be written out in full every time the list needs to be printed. With the function, a single call handles all eight iterations — demonstrating how functions reduce repetition and keep the main program flow clean and readable.

**Q5 — What do you observe from the string concatenation output?**  
The output is a single unbroken string containing all eight usernames merged together with no spaces or separators: `elarsonbmorenotshahsgilmoreeraabgesparzaalevitskwjaffrey`. Each iteration of the `for` loop appends the current username directly to `sum_variable` using the `+` operator, and because no separator is added, the boundaries between names are invisible in the final result. While the data is now in a string format — which makes it easier to write to a file or pass to another function — the absence of delimiters makes the output difficult to interpret by eye.

**Q6 — What do you notice about the output from the function call this time?**  
The output is now clearly readable: `elarson, bmoreno, tshah, sgilmore, eraab, gesparza, alevitsk, wjaffrey,`. Appending `", "` after each username inside the loop separates every name with a comma and a space, making it straightforward to distinguish one username from the next. One side effect worth noting is the trailing `", "` at the very end of the string — after `"wjaffrey"` — because the separator is appended on every loop iteration, including the last one. In production code, this would typically be removed with `str.rstrip(", ")` or avoided entirely by using Python's `", ".join(username_list)`, but the current implementation correctly demonstrates the concatenation and separator pattern the lab is teaching.

---

## 💡 Key Code

```python
# Task 2 — define and call alert()
def alert():
    print("Potential security issue. Investigate further.")

alert()

# Task 3 — alert() with a for loop inside the body
def alert():
    for i in range(3):
        print("Potential security issue. Investigate further.")

alert()

# Task 5 — list_to_string() with individual prints
def list_to_string():
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore",
                     "eraab", "gesparza", "alevitsk", "wjaffrey"]
    for i in username_list:
        print(i)

list_to_string()

# Task 6 — accumulator: concatenate without separator
def list_to_string():
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore",
                     "eraab", "gesparza", "alevitsk", "wjaffrey"]
    sum_variable = ""
    for i in username_list:
        sum_variable = sum_variable + i
    print(sum_variable)

list_to_string()
# Output: elarsonbmorenotshahsgilmoreeraabgesparzaalevitskwjaffrey

# Task 7 — accumulator with ", " separator
def list_to_string():
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore",
                     "eraab", "gesparza", "alevitsk", "wjaffrey"]
    sum_variable = ""
    for i in username_list:
        sum_variable = sum_variable + i + ", "
    print(sum_variable)

list_to_string()
# Output: elarson, bmoreno, tshah, sgilmore, eraab, gesparza, alevitsk, wjaffrey,
```

---

## 🧠 Key Concepts Applied

- **`def` keyword** — Introduces a function definition; the function name, parentheses, and colon follow on the same line
- **Function header** — The `def function_name():` line that names the function and defines its parameter list (empty here)
- **Function body** — The indented block below the header; contains the statements that execute when the function is called
- **Calling a function** — Writing `function_name()` triggers execution of the function body; the function must be defined before it is called
- **Reusability (DRY principle)** — A function defined once can be called anywhere; updating the body updates every call site simultaneously
- **`for` loop inside a function** — The loop runs each time the function is called; the loop variable and its logic are fully encapsulated in the body
- **Accumulator pattern** — Initializing a variable to an empty string (`sum_variable = ""`) and repeatedly appending to it inside a loop to build up a result
- **String concatenation with `+`** — Joins two strings into one; used here to merge usernames and separator strings step by step
- **Separator string** — Adding `", "` after each element makes the concatenated output human-readable; a trailing separator on the last element is a known side effect of this pattern
- **`print()` as a built-in** — Used both directly (Task 2) and inside a `for` loop (Task 3) within user-defined functions; calling `alert()` triggers the `print()` call inside it

---

## 📚 What I Learned

- How to define a function in Python using `def`, and that defining a function does not execute it — calling it does
- That functions make code reusable: one `alert()` call replaces repeating the same print statement everywhere it is needed
- How to embed a `for` loop inside a function body to control repeated behavior, and that the caller's syntax stays the same regardless of what the body contains
- That `range(3)` inside a loop runs the body exactly three times — useful for fixed repetition tasks like displaying a repeated alert
- How to build the `list_to_string()` function step by step: first just printing each element, then using the accumulator pattern to build a single string
- That the accumulator pattern (`sum_variable = sum_variable + i`) merges strings but produces no separator between elements unless one is explicitly added
- That appending `", "` after each element separates the output cleanly but leaves a trailing separator at the end — and how `", ".join()` or `str.rstrip()` would eliminate it in production code
- That encapsulating logic inside a function hides its complexity: from the outside, `list_to_string()` looks the same in Tasks 5, 6, and 7, even though the implementation changes significantly between them

---

## 🔍 Conclusion — Key Takeaways

Functions are one of the most important tools in Python for writing clean, maintainable, and scalable automation scripts. This lab demonstrated three core principles:

1. **Define once, call anywhere.** Wrapping repeated logic in a function means the code only needs to be written — and maintained — in one place.
2. **Functions can contain any Python construct.** Loops, conditionals, and other functions can all live inside a function body, and none of that complexity is visible to the caller.
3. **Data structures and strings serve different purposes.** A list is easy to add to or remove from; converting it to a string (with the accumulator pattern and a separator) makes it easy to export or embed in text output. Knowing when to use each form — and how to convert between them — is a practical skill for security automation.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`define_and_call_a_function.py`](./assets/define_and_call_a_function.py) | Annotated Python script with all 7 tasks, code, and expected outputs |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
