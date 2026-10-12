# 🐍 Lab: Create Loops

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** `for` loops, `while` loops, `range()`, `break`, loop variables, iterating over lists, nested conditionals

---

## 📋 Scenario Overview

As a security analyst, many tasks involve repetition: checking multiple IP addresses, retrying failed connections, or generating batches of employee IDs. In this lab, iterative statements were used to automate three distinct security-related workflows — displaying repeated network connection messages, checking IP addresses against an allow list with early termination on violation, and generating a range of unique employee IDs with an embedded milestone alert.

---

## ✅ Tasks Completed

| Task | Description | Construct |
|---|---|---|
| 1 | Display a connection failure message exactly 3 times | `for` + `range()` |
| 2 | Repeat the message a variable number of times using `connection_attempts` | `for` + `range(variable)` |
| 3 | Achieve the same result using a condition-based loop | `while` |
| 4 | Iterate over a list of IP addresses and display each one | `for` over a list |
| 5 | Check each IP against an allow list and display access status | `for` + `if/else` + `in` |
| 6 | Halt the loop immediately when an unauthorized IP is detected | `for` + `if/else` + `break` |
| 7 | Generate all employee IDs divisible by 5 between 5000 and 5150 | `while` + increment |
| 8 | Add a milestone alert when the loop variable reaches 5100 | `while` + nested `if` |

---

## 🔍 for vs. while — Key Differences

| | `for` loop | `while` loop |
|---|---|---|
| **Use when** | Number of iterations is known | Condition determines when to stop |
| **Counter management** | Handled automatically by `range()` or the iterable | Must be updated manually inside the loop |
| **Risk of infinite loop** | No — sequence has a fixed end | Yes — if the condition never becomes `False` |
| **Used in this lab for** | Fixed repetitions, iterating over lists | Condition-based repetition, ID generation |

---

## 🔍 Questions & Answers

**Q1 — What do you observe about the differences between the `for` loop and the `while` loop?**  
Both loops produce the same output — the connection message printed three times — but they operate on different underlying logic. The `for` loop uses `range(3)` to define a fixed sequence of iterations upfront; Python automatically tracks the counter and stops when the sequence is exhausted. No manual counter management is needed. The `while` loop, by contrast, evaluates the condition `connection_attempts < 3` before each iteration and continues as long as it is `True`. The counter must be explicitly incremented inside the loop body (`connection_attempts = connection_attempts + 1`), otherwise the loop would run forever. In security automation, `while` loops are better suited to scenarios where the stopping condition depends on a runtime state — for example, retrying a connection until it succeeds or polling a log file until a threat is detected — rather than iterating a predetermined number of times.

**Q2 — Why is `print(i)` written before the `if` statement rather than inside it?**  
`print(i)` is placed before the `if` statement so that every employee ID is displayed on every iteration, unconditionally. The `if` block only fires once — when `i == 5100` — and its purpose is to print a supplementary alert message alongside that specific ID. If `print(i)` were placed inside the `if` block, only the value `5100` would ever be printed; all other IDs (5000 through 5095, and 5105 through 5150) would be silently skipped. The intended behavior is: display the ID first, then check whether the milestone condition applies and print the alert if so. Placing `print(i)` before the conditional achieves this separation — every ID is always shown, and the alert appears only once as an extra line when the threshold is reached.

---

## 💡 Key Code

```python
# Task 1 — for loop, fixed iterations
for i in range(0, 3):
    print("Connection could not be established.")

# Task 3 — while loop, condition-based
connection_attempts = 0
while connection_attempts < 3:
    print("Connection could not be established.")
    connection_attempts = connection_attempts + 1

# Task 5 — for loop over list, allow list check
for i in ip_addresses:
    if i in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed")

# Task 6 — break on first unauthorized IP
for i in ip_addresses:
    if i in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed. Further investigation of login activity required")
        break

# Task 8 — while loop with milestone alert
i = 5000
while i <= 5150:
    print(i)
    if i == 5100:
        print("Only 10 valid employee ids remaining")
    i = i + 5
```

---

## 🔍 Task 6 — IP Allow List Check Results

| IP Address | In allow_list? | Action |
|---|---|---|
| `192.168.142.245` | ❌ No | Alert printed → loop terminates |
| `192.168.109.50` | ❌ No | Never reached |
| `192.168.86.232` | ✅ Yes | Never reached |
| `192.168.131.147` | ❌ No | Never reached |
| `192.168.205.12` | ✅ Yes | Never reached |
| `192.168.200.48` | ❌ No | Never reached |

The first IP in the list is unauthorized, so `break` fires immediately and the remaining IPs are never evaluated.

---

## 🧠 Key Concepts Applied

- **`for` loop** — Iterates over a sequence (a `range()` or a list) a fixed number of times; the counter is managed automatically
- **`while` loop** — Repeats as long as a condition evaluates to `True`; requires manual counter updates to avoid infinite loops
- **`range()`** — Generates a sequence of integers; accepts a single argument (`range(n)`) or start/stop arguments (`range(start, stop)`)
- **Loop variable** — A temporary variable (here `i`) that holds the current element or index on each iteration
- **Iterating over a list** — `for i in list_name` assigns each element of the list to `i` in turn, without needing `range()` or an index
- **`in` operator (in a loop condition)** — Tests membership: `i in allow_list` returns `True` if `i` is an element of `allow_list`
- **`break` statement** — Immediately terminates the enclosing loop; useful for halting iteration when a critical condition is met
- **Nested conditionals in loops** — An `if` statement inside a loop body runs on every iteration, allowing per-element decisions
- **Increment pattern** — `i = i + 5` (or equivalently `i += 5`) advances the loop variable by a fixed step; essential in `while` loops

---

## 📚 What I Learned

- How to write `for` loops using `range()` with a fixed number or a variable, and when to prefer one over the other
- How `while` loops differ from `for` loops: they check a condition each iteration rather than counting through a sequence, and require a manual counter update
- How to iterate directly over a Python list with a `for` loop, without needing an index or `range()`
- How to combine loops with `if/else` statements to make per-element decisions — such as checking each IP address against an allow list
- How the `break` keyword works: it exits the loop immediately at the point it's called, leaving remaining iterations unexecuted
- That the order of statements inside a loop body matters: placing `print(i)` before a conditional ensures it runs on every iteration, not just when the condition fires
- That `while` loops are the right tool when the stopping condition depends on runtime state, such as a counter reaching a threshold or an event occurring

---

## 📁 Project Files

| File | Description |
|---|---|
| [`create_loops.py`](./assets/create_loops.py) | Annotated Python script with all 8 tasks, code, and expected outputs |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
