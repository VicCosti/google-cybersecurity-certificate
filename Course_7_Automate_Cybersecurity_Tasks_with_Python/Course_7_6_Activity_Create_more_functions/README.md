# 🐍 Lab: Create More Functions

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** Built-in functions (`sorted()`, `max()`), user-defined functions with parameters, function arguments, `return` statements, composing functions with conditionals

---

## 📋 Scenario Overview

As a security analyst, two parallel workflows were automated in this lab. First, a list of monthly failed login attempts was analyzed using Python's built-in `sorted()` and `max()` functions to identify statistical outliers that could indicate malicious activity. Second, a user-defined function named `analyze_logins()` was built and progressively refined across six tasks — from a two-parameter display function to a fully composable function that computes and returns a login ratio, which is then used in a conditional alert.

---

## ✅ Tasks Completed

| Task | Description | Key Construct |
|---|---|---|
| 1 | Sort `failed_login_list` in ascending order and display it | `sorted()` built-in |
| 2 | Isolate the highest failed login count from the list | `max()` built-in |
| 3 | Define `analyze_logins()` with two parameters; no call | `def`, parameters |
| 4 | Call `analyze_logins("ejones", 9)` and observe output | Function call with arguments |
| 5 | Add a third parameter `average_day_logins`; call with three arguments | Three-parameter function |
| 6 | Calculate `login_ratio` inside the function and display it | Division, local variable |
| 7 | Add `return login_ratio`; store result in `login_analysis` | `return` statement |
| 8 | Use `login_analysis >= 3` in a conditional to trigger an alert | `return` value + `if` |

---

## 🔍 Questions & Answers

**Q1 — What do you observe from the sorted output? Do you notice any outliers indicating an increase in failed login attempts?**  
When the list is sorted in ascending order — `[85, 88, 90, 91, 92, 99, 101, 105, 108, 119, 223, 264]` — the majority of monthly values cluster tightly between 85 and 119. Two values, 223 and 264, stand clearly apart from the rest of the distribution. Sorting the list makes this pattern immediately visible: what was hidden in chronological order becomes obvious when values are ranked. These two outliers correspond to November and December and represent a roughly twofold increase over the typical monthly range, which warrants further investigation as a potential indicator of coordinated malicious activity or a sustained attack campaign during the end of the year.

**Q2 — What do you observe from the `max()` output?**  
`max(failed_login_list)` returns `264`, identifying November as the single month with the highest volume of failed login attempts across the year. This value is more than twice the median of the remaining months and confirms the direction of investigation suggested by the sorted output in Task 1. Isolating the maximum programmatically is more reliable than scanning the list by eye — especially as datasets grow — and provides a concrete starting point for pulling log details for that specific month.

**Q3 — What does `analyze_logins()` display? Would the output vary for different users?**  
Calling `analyze_logins("ejones", 9)` prints one line: `Current day login total for ejones is 9`. The function substitutes the two argument values into the message template each time it is called. The output would vary for every different pair of arguments: `analyze_logins("tshah", 4)` would produce `Current day login total for tshah is 4`. This is the core value of parameterized functions — the same logic is applied to different data simply by changing the arguments, without duplicating any code.

**Q4 — What does this version of `analyze_logins()` display? Would the output vary for different users?**  
This version now produces three lines of output for each call. For `analyze_logins("ejones", 9, 3)`:
```
Current day login total for ejones is 9
Average logins per day for ejones is 3
ejones logged in 3.0 times as much as they do on an average day.
```
All three values — username, current count, average, and the computed ratio — change with the arguments. A user with 2 logins against a daily average of 2 would show a ratio of 1.0; a user with 10 logins against an average of 2 would show 5.0. The ratio is calculated fresh on each call using the specific values passed in, making the function applicable to any user in the system. One edge case to be aware of is a `ZeroDivisionError` if `average_day_logins` is ever `0`; the lab assumes this cannot happen, but production code would include a guard clause.

**Q5 — How does this version of `analyze_logins()` compare to the previous versions?**  
The critical difference is the `return` statement. In Task 6, `login_ratio` was computed and displayed inside the function body, but it was discarded the moment the function finished — there was no way to use that value anywhere else in the program. Adding `return login_ratio` changes this: the computed ratio is now sent back to the caller and stored in `login_analysis`. This makes the function composable — its output can feed directly into a conditional, be passed to another function, be stored for later comparison, or be logged. The printed output in the function body is identical to Task 6, so from a display perspective nothing changes. But architecturally, the function has moved from a display-only utility to a proper computation unit that produces a reusable result.

---

## 💡 Key Code

```python
# Task 1 — sorted() to reveal distribution and outliers
failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]
print(sorted(failed_login_list))
# Output: [85, 88, 90, 91, 92, 99, 101, 105, 108, 119, 223, 264]

# Task 2 — max() to isolate the peak month
print(max(failed_login_list))
# Output: 264

# Task 6 — analyze_logins() with ratio calculation
def analyze_logins(username, current_day_logins, average_day_logins):
    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)
    login_ratio = current_day_logins / average_day_logins
    print(username, "logged in", login_ratio, "times as much as they do on an average day.")

analyze_logins("ejones", 9, 3)

# Task 7 — return statement makes the ratio available outside the function
def analyze_logins(username, current_day_logins, average_day_logins):
    print("Current day login total for", username, "is", current_day_logins)
    print("Average logins per day for", username, "is", average_day_logins)
    login_ratio = current_day_logins / average_day_logins
    return login_ratio

login_analysis = analyze_logins("ejones", 9, 3)
print("ejones", "logged in", login_analysis, "times as much as they do on an average day.")

# Task 8 — use the returned value in a conditional alert
if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")
```

---

## 🔍 Login Analysis — Task 8 Result

| Parameter | Value |
|---|---|
| Username | `ejones` |
| Current day logins | `9` |
| Average day logins | `3` |
| Login ratio (`login_analysis`) | `3.0` |
| Threshold | `>= 3` |
| Alert triggered? | ✅ Yes |

The ratio of 3.0 meets the `>= 3` threshold exactly, so the alert fires. A user with 8 logins vs. an average of 3 (ratio ≈ 2.67) would not trigger it.

---

## 🧠 Key Concepts Applied

- **`sorted()` built-in** — Returns a new sorted list in ascending order without modifying the original; makes outliers immediately visible when passed into `print()`
- **`max()` built-in** — Returns the largest element from a sequence; used here to pinpoint the month with the highest failed login count
- **Parameters vs. arguments** — Parameters are the placeholder names in the function definition (`username`, `current_day_logins`); arguments are the actual values passed at the call site (`"ejones"`, `9`)
- **Progressive function refinement** — A function can be expanded across iterations by adding parameters and logic; each version replaces the previous one while maintaining backward compatibility of the interface
- **Local variable** — `login_ratio` is defined inside the function body and exists only for the duration of that call; without `return`, its value cannot escape the function
- **`return` statement** — Sends a value from inside the function back to the caller; the returned value can be stored in a variable, passed to another function, or used directly in an expression
- **Composing functions with conditionals** — Storing a function's return value in `login_analysis` and then evaluating it in an `if` statement is a core pattern in security automation: compute once, decide anywhere
- **`>=` comparison operator** — Returns `True` when the left operand is greater than or equal to the right; used here to define the threshold at which login activity is flagged as anomalous
- **ZeroDivisionError awareness** — Dividing by `average_day_logins` raises an error if that value is `0`; the lab excludes this case, but production code would guard against it

---

## 📚 What I Learned

- How `sorted()` and `max()` work as built-in functions: they take a sequence as input and return a result without modifying the original list
- That sorting a dataset before analyzing it is a simple but powerful technique for surfacing outliers — the two anomalous months (264, 223) were not obvious in the original chronological order but became immediately visible after sorting
- How to define functions with multiple parameters and how each parameter is filled by the corresponding argument in the function call
- That functions can be refined incrementally: start with a minimal definition and expand it one parameter or one computation at a time, testing at each step
- The critical difference between printing inside a function and returning a value: `print()` displays something on screen but discards it; `return` passes the value back to the caller where it can be stored and reused
- That combining `return` with variable assignment (`login_analysis = analyze_logins(...)`) is what makes functions genuinely composable — the result of one operation feeds directly into the next
- How to close a security automation loop: collect data (function with parameters), compute a risk metric (ratio), return it, and act on it (conditional alert) — all in a clean, readable sequence

---

## 📁 Project Files

| File | Description |
|---|---|
| [`create_more_functions.py`](./assets/create_more_functions.py) | Annotated Python script with all 8 tasks, code, and expected outputs |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
