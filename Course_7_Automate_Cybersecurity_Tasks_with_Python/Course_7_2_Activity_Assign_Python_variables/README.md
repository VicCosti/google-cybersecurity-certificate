# 🐍 Lab: Assign Python Variables

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** Variables, data types (`str`, `int`, `list`, `bool`), `type()`, comparison operators, Boolean values

---

## 📋 Scenario Overview

As a security analyst responsible for automating analysis of login attempts, the first step is creating variables to track key information: the device ID, the list of approved usernames, the maximum number of login attempts allowed, the current number of attempts made, and the user's login status. In this lab, variables were assigned across all four core Python data types, and the `type()` function was used to inspect and confirm each one.

---

## ✅ Tasks Completed

| Task | Description | Variable(s) |
|---|---|---|
| 1 | Assign the device ID string and display it | `device_id` |
| 2 | Retrieve and display the data type of `device_id` | `device_id_type` |
| 3 | Assign a list of approved usernames and display it | `username_list` |
| 4 | Retrieve and display the data type of `username_list` | `username_list_type` |
| 5 | Update the username list with a new employee (`"lpope"`) | `updated_username_list` |
| 6 | Assign the maximum login attempts and check its type | `max_logins`, `max_logins_type` |
| 7 | Assign the current login attempts and check its type | `login_attempts`, `login_attempts_type` |
| 8 | Evaluate whether login attempts are within the allowed limit | `login_attempts <= max_logins` |
| 9 | Reassign `login_attempts` to exceed the limit and observe the result | `login_attempts = 5` |
| 10 | Assign a Boolean login status and check its type | `login_status`, `login_status_type` |

---

## 🔍 Variable Summary

| Variable | Value | Type |
|---|---|---|
| `device_id` | `"72e08x0"` | `str` |
| `username_list` | `["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]` | `list` |
| `updated_username_list` | `[..., "lpope"]` | `list` |
| `max_logins` | `3` | `int` |
| `login_attempts` | `2` (then reassigned to `5`) | `int` |
| `login_status` | `False` | `bool` |

---

## 🔍 Questions & Answers

**Q1 — What do you observe about the data type of `device_id`?**  
`device_id` is of type `str` (string). In Python, any value enclosed in quotation marks is treated as a string — a sequence of characters. Even though `"72e08x0"` looks partially numeric, the quotes make it a string, not an integer. The `type()` function confirms this by returning `<class 'str'>`.

**Q2 — What do you observe about the data type of `username_list`?**  
`username_list` is of type `list`. A Python list is an ordered, mutable collection of values enclosed in square brackets, with elements separated by commas. In this case, each element is a string (a username). The `type()` function returns `<class 'list'>`.

**Q3 — What do you observe about the contents of `username_list` after the update?**  
The updated list contains all five original usernames plus the newly authorized employee `"lpope"`, bringing the total to six entries. In this implementation, the updated list was stored in a new variable `updated_username_list` to preserve the original for comparison — both lists were then displayed to make the addition visible. Functionally, the result is the same as reassigning `username_list` directly.

**Q4 — What do you observe about the data type of `max_logins`?**  
`max_logins` is of type `int` (integer). Integers represent whole numbers with no decimal component. Since login attempt counts are always whole numbers, `int` is the appropriate type here. The `type()` function returns `<class 'int'>`.

**Q5 — What do you observe about the data type of `login_attempts`?**  
`login_attempts` is also of type `int`, same as `max_logins`. Both variables track discrete counts, so `int` is correct for both. This consistency is important for the comparison in Task 8 — comparing two values of the same type is reliable and avoids type-related errors.

**Q6 — What is the output of `login_attempts <= max_logins`? What does this mean?**  
The output is `True`. With `login_attempts = 2` and `max_logins = 3`, the expression `2 <= 3` evaluates to `True` — the user is still within the permitted threshold. In a real login system, this Boolean result would determine whether to allow the next attempt or block the user.

**Q7 — What do you observe when `login_attempts` is reassigned to a higher value?**  
With `login_attempts = 5`, the expression `5 <= 3` evaluates to `False`. The output changes from `True` to `False`, confirming that the user has exceeded the maximum number of allowed login attempts. This demonstrates how the same comparison expression can drive different security decisions depending on the current state of the variable.

**Q8 — What do you observe about the data type of `login_status`?**  
`login_status` is of type `bool` (Boolean). A Boolean variable holds one of two values: `True` or `False`. It is the appropriate type for representing binary states such as whether a user is currently logged in. Note that Boolean literals in Python are capitalized (`True`, `False`) and written without quotation marks — wrapping them in quotes would make them strings instead.

---

## 💡 Key Code

```python
# String variable
device_id = "72e08x0"
print(type(device_id))      # <class 'str'>

# List variable
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
print(type(username_list))  # <class 'list'>

# Integer variables
max_logins = 3
login_attempts = 2
print(type(max_logins))     # <class 'int'>

# Boolean comparison
print(login_attempts <= max_logins)   # True
login_attempts = 5
print(login_attempts <= max_logins)   # False

# Boolean variable
login_status = False
print(type(login_status))   # <class 'bool'>
```

---

## 🧠 Key Concepts Applied

- **Variables** — Named containers that store values in memory; assigned using the `=` operator
- **`str` (string)** — Text data enclosed in single or double quotation marks; `"72e08x0"` is a string even though it contains digits
- **`list`** — An ordered, mutable collection of values in square brackets; supports mixed data types
- **`int` (integer)** — A whole number with no decimal component; used for counts and numeric comparisons
- **`bool` (Boolean)** — A binary value (`True` or `False`); the result type of comparison expressions
- **`type()` function** — Returns the data type of any Python value or variable as a class object
- **Comparison operators** — `<=` (less than or equal to) evaluates to a Boolean; used here to check whether login attempts are within the allowed limit
- **Variable reassignment** — Assigning a new value to an existing variable name replaces the old value; Python is dynamically typed, so the type can change too

---

## 📚 What I Learned

- How to assign values to Python variables using the `=` operator and how to display them with `print()`
- That Python has four fundamental data types used in security contexts: `str`, `list`, `int`, and `bool`
- How to use the `type()` function to inspect the data type of any variable at runtime
- That string values must be enclosed in quotation marks — even values that look numeric, like a device ID
- That Boolean values (`True`/`False`) are the direct output of comparison expressions like `<=`
- How reassigning a variable changes what a comparison expression returns — critical for building dynamic logic like login attempt enforcement
- That variables act as reusable, updateable containers: changing the value of `login_attempts` immediately changes the result of any expression that uses it

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assign_python_variables.py`](./assets/assign_python_variables.py) | Annotated Python script with all 10 tasks, code, and expected outputs |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
