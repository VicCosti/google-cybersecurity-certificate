# 🐍 Lab: Create a Conditional Statement

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** Conditional statements (`if`, `elif`, `else`), comparison operators (`==`, `in`), logical operators (`or`, `and`), Boolean logic

---

## 📋 Scenario Overview

As a security analyst, two automation tasks were required: first, checking whether a user's operating system is up-to-date and displaying an appropriate message; second, investigating login attempts to a specific device to determine whether the user is on the approved list and whether the attempt occurred during organization hours. Conditional statements in Python were used to build the decision logic for both scenarios, progressively refining the code from a simple `if` to a combined `if/and` statement.

---

## ✅ Tasks Completed

| Task | Description | Key Construct |
|---|---|---|
| 1 | Check if OS 2 is running; display "no update needed" | `if` + `==` |
| 2 | Observe behavior when OS 2 is not running (no output) | `if` only |
| 3 | Add an `else` branch to handle systems that need updates | `if/else` |
| 4 | Use `elif` to handle each OS explicitly; add fallback for unknown input | `if/elif/elif/else` |
| 5 | Combine the two `elif` branches into one using `or` | `if/elif` + `or` |
| 6 | Check login against two individual approved user variables | `if/else` + `or` |
| 7 | Scale the check to a list of five users using the `in` operator | `if/else` + `in` |
| 8 | Check login timing using a Boolean variable | `if/else` + `==` |
| 9 | Run both checks (username + timing) as independent conditionals | Two `if/else` blocks |
| 10 | Combine both checks into a single conditional using `and` | `if/else` + `and` |

---

## 🔍 Conditional Logic Progression

| Task | Structure | Handles unknown input? |
|---|---|---|
| 1–2 | `if` only | ❌ No output if condition is False |
| 3 | `if/else` | ⚠️ Catches everything — too broad |
| 4 | `if/elif/elif/else` | ✅ Each OS handled explicitly; fallback added |
| 5 | `if/elif` + `or` | ✅ Same logic, more concise |
| 6 | `if/else` + `or` (two variables) | ✅ Two named users |
| 7 | `if/else` + `in` (list) | ✅ Scales to any number of users |
| 10 | `if/else` + `and` (combined) | ✅ Both conditions must be met |

---

## 🔍 Questions & Answers

**Q1 — What happens when OS 2 is running? What happens when OS 1 is running?**  
When `system = "OS 2"`, the `==` comparison evaluates to `True` and the message `"no update needed"` is printed. When `system = "OS 1"`, the condition evaluates to `False` and nothing is displayed — because at this stage there is no `else` branch. The program runs without errors but produces no output, which highlights the limitation of a standalone `if` statement when only one outcome is handled.

**Q2 — What happens when OS 2 is running? What happens when OS 2 is not running?**  
With the `else` branch added, the conditional now handles both outcomes. When `system = "OS 2"`, the `if` branch executes and prints `"no update needed"`. For any other value — `"OS 1"`, `"OS 3"`, or anything else — the `else` branch executes and prints `"update needed"`. This is more complete than the previous step, but still too broad: any unknown string would also trigger `"update needed"`.

**Q3 — What happens for each OS? What happens for unknown input?**  
With explicit `elif` branches for each OS, the logic becomes precise. `"OS 2"` → `"no update needed"`; `"OS 1"` → `"update needed"`; `"OS 3"` → `"update needed"`. An `else` branch was added to handle unrecognized input — any string that doesn't match a known OS (such as `"OS 4"`) prints `"unknown input"` instead of silently falling through or incorrectly flagging an update. This is a deliberate improvement over the lab template, which did not require a fallback at this stage.

**Q4 — What do you observe about this conditional?**  
The two separate `elif` branches from Task 4 are merged into a single branch using the `or` logical operator: `elif (system == "OS 1" or system == "OS 3")`. The behavior is identical — both outdated operating systems trigger `"update needed"` — but the code is shorter and easier to read. This demonstrates a core principle in Python development: when multiple conditions lead to the same outcome, they can be combined with a logical operator rather than duplicated in separate branches.

**Q5 — What happens when an approved user tries to log in? What happens when an unapproved user tries to log in?**  
When the value of `username` is found in `approved_list`, the `in` operator returns `True` and the message `"This user has access to this device."` is printed. When the username is not in the list, `in` returns `False` and the `else` branch prints `"This user does not have access to this device."` Using a list with the `in` operator is significantly more scalable than comparing against individual variables — adding a new approved user only requires updating the list, not the conditional logic.

**Q6 — What happens when the user logs in during organization hours? What happens outside of organization hours?**  
When `organization_hours = True`, the condition `organization_hours == True` evaluates to `True` and prints `"Login attempt made during organization hours."` When `organization_hours = False`, the condition evaluates to `False` and the `else` branch prints `"Login attempt made outside of organization hours."` Boolean variables are well-suited to this kind of binary flag — they represent exactly two states, which maps directly to the `if/else` structure.

**Q7 — What happens when the user is not approved? When approved? When logging in outside of hours?**  
Because the two checks run as independent conditionals, each produces its own output. An unapproved user triggers `"This user does not have access to this device."` from the first block. An approved user triggers `"This user has access to this device."` A login outside of organization hours triggers `"Login attempt made outside of organization hours."` from the second block. Since the conditions are independent, both messages always print — a user can be approved but still receive the out-of-hours warning, which may be undesirable in a production system.

**Q8 — What happens when the user is approved and within hours? What happens otherwise?**  
The `and` operator requires both conditions to be `True` simultaneously. When `username in approved_list` is `True` and `organization_hours == True` is also `True`, the message `"Login attempt made by an approved user during organization hours."` is printed. If either condition is `False` — the user is not approved, or the login occurs outside business hours — the `else` branch fires: `"Username not approved or login attempt made outside of organization hours."` This is the most complete and concise version of the login check: a single conditional that enforces two security requirements at once.

---

## 💡 Key Code

```python
# if/elif/else — explicit OS check with unknown input fallback (Task 4)
if system == "OS 2":
    print("no update needed")
elif system == "OS 1":
    print("update needed")
elif system == "OS 3":
    print("update needed")
else:
    print("unknown input")

# Combine elif branches with or (Task 5)
if system == "OS 2":
    print("no update needed")
elif (system == "OS 1" or system == "OS 3"):
    print("update needed")

# Check username against a list with in (Task 7)
if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")

# Combine username and timing check with and (Task 10)
if (username in approved_list) and (organization_hours == True):
    print("Login attempt made by an approved user during organization hours.")
else:
    print("Username not approved or login attempt made outside of organization hours.")
```

---

## 🧠 Key Concepts Applied

- **`if` statement** — Executes a block of code only when the condition evaluates to `True`; produces no output and no error when the condition is `False` and no `else` is present
- **`else` statement** — Provides a fallback block that executes when all preceding conditions are `False`
- **`elif` statement** — Adds additional named conditions between `if` and `else`; only the first matching branch executes
- **`==` comparison operator** — Tests for equality between two values; returns a Boolean (`True` or `False`)
- **`or` logical operator** — Returns `True` if at least one of the combined conditions is `True`; used to merge equivalent branches
- **`and` logical operator** — Returns `True` only when both conditions are `True`; used to enforce multiple requirements simultaneously
- **`in` operator** — Tests whether a value is a member of a sequence (list, string, etc.); more scalable than chaining individual equality checks
- **Boolean variables** — Variables of type `bool` holding `True` or `False`; ideal for binary state flags such as login status or access windows
- **Graceful fallback** — An `else` at the end of an `if/elif` chain catches unrecognized input and prevents silent failures

---

## 📚 What I Learned

- How to build conditional logic in Python using `if`, `elif`, and `else`, and when each keyword is appropriate
- That a standalone `if` statement with no `else` produces no output when the condition is `False` — and why that can be a problem in security automation
- That `elif` chains evaluate top-to-bottom and stop at the first matching condition, making order and specificity important
- How to combine conditions with `or` (either condition can be True) and `and` (both must be True) to write more concise and expressive logic
- That the `in` operator is the clean, scalable way to check list membership — far preferable to chaining multiple `==` comparisons with `or` as the user count grows
- How Boolean variables map naturally to `if/else` structures, since they already hold a `True`/`False` state
- That adding an `else` fallback for unexpected input makes conditional logic more robust and easier to debug in a real security context

---

## 📁 Project Files

| File | Description |
|---|---|
| [`create_conditional_statement.py`](./assets/create_conditional_statement.py) | Annotated Python script with all 10 tasks, code, and expected outputs |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
