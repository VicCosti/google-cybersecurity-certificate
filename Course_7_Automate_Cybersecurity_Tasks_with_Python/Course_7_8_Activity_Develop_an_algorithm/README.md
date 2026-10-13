# 🐍 Lab: Develop an Algorithm

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** Synchronized lists, `.append()`, `.remove()`, `.index()`, `in` operator, `if/elif/else`, nested conditionals, user-defined functions

---

## 📋 Scenario Overview

As a security analyst, the task is to build a login authentication algorithm that verifies both a user's identity and their assigned device before granting access. Two synchronized lists — `approved_users` and `approved_devices` — store each approved username alongside its corresponding device ID at the same index. The algorithm was developed incrementally across nine tasks: from exploring index-based list correspondence and updating the lists with `.append()` and `.remove()`, to chaining username and device checks using the `in` operator and `.index()`, and finally encapsulating the full logic inside a `login(username, device_id)` function using nested conditionals.

---

## ✅ Tasks Completed

| Task | Description | Key Construct |
|---|---|---|
| 1 | Explore how synchronized lists share index positions | List indexing `[n]` |
| 2 | Add a new user/device pair to both lists | `.append()` |
| 3 | Remove a departed user/device pair from both lists | `.remove()` |
| 4 | Check if a username is in the approved list | `if username in approved_users` |
| 5 | Find the index of a username in the approved list | `.index()` |
| 6 | Use that index to retrieve the corresponding device ID | Cross-list lookup `approved_devices[ind]` |
| 7 | Check both username approval and device ID match | `if … and …` |
| 8 | Add an `elif` branch for approved user with wrong device | `elif`, `!=` |
| 9 | Encapsulate the full algorithm in `login(username, device_id)` | Nested conditionals, `def` |

---

## 🔍 Questions & Answers

**Q1 — What did you observe about the output when `approved_users[0]` is displayed and when `approved_devices[0]` is displayed? What happens when you replace each `0` with another index?**  
When `approved_users[0]` is displayed it returns `"elarson"` — the first element of that list. When `approved_devices[0]` is displayed it returns `"8rp2k75"` — the first element of the devices list. The key observation is that these two values correspond to each other: `"elarson"` is the user at index 0 and `"8rp2k75"` is her assigned device at that same index. This relationship holds at every position across both lists — the element at index `n` in `approved_users` is the owner of the device at index `n` in `approved_devices`. When the index is changed (e.g., to `2`), both prints shift to the third element of their respective lists: `"tshah"` and `"2ye3lzg"`. The two lists are synchronized by position, and this index-based correspondence is the structural foundation of the device-verification algorithm built across the remaining tasks.

**Q2 — After the new approved user is added, what did you observe about the output when `approved_users` is displayed and when `approved_devices` is displayed?**  
Both lists grow from 5 elements to 6. `"gesparza"` now appears as the last element of `approved_users` and `"3rcv4w6"` now appears as the last element of `approved_devices`. Critically, `.append()` adds each new element to the end of its respective list, so both were inserted at index 5. The synchronization between the two lists is preserved: gesparza's username and device ID now share the same index position. If only one list were updated, the index correspondence would break for all subsequent elements, causing every device lookup to return the wrong result. Both lists must always be updated together to maintain the pairing.

**Q3 — After the user who left the team is removed, what did you observe about the output when `approved_users` is displayed and when `approved_devices` is displayed?**  
Both lists shrink from 6 elements to 5. `"tshah"` no longer appears in `approved_users` and `"2ye3lzg"` no longer appears in `approved_devices`. Because both were removed, the synchronization is preserved — each remaining username still corresponds to the correct device at the same index position. If only the username were removed, the remaining device IDs would each shift to the wrong index, breaking every subsequent lookup. The user/device pairing must always be treated as a unit for both additions and removals.

**Q4 — What message do you observe in the output when `username` is `"sgilmore"`?**  
The output is `The user sgilmore is approved to access the system.` The `in` operator evaluates `username in approved_users` to `True` because `"sgilmore"` is an element of the list, so the `if` branch runs. If `username` were set to a value not present in the list — such as `"tshah"`, who was removed in Task 3 — the `in` operator would return `False` and the `else` branch would run instead, printing the not-approved message. The `in` operator is the most direct and readable way to test list membership in Python and forms the outer check of the full authentication algorithm.

**Q5 — What do you observe from the output when `username` is `"sgilmore"`?**  
The output is `2`. `approved_users.index("sgilmore")` searches the list left-to-right and returns the index of the first match — `"sgilmore"` is the third element of the list, at index 2 (zero-based). Storing this value in `ind` is the critical step that bridges the two synchronized lists: because `approved_users` and `approved_devices` share the same index structure, `ind` now points to the same position in both lists — the position that belongs to sgilmore and her assigned device. This allows the next task to retrieve the correct device ID through a direct index lookup rather than a second search.

**Q6 — What do you observe from the output when `username` is `"sgilmore"`?**  
The output is `4n482ts`. `approved_users.index("sgilmore")` returns `2`, which is stored in `ind`. Then `approved_devices[2]` retrieves the element at that same index in `approved_devices` — which is `"4n482ts"`, sgilmore's assigned device. The cross-list lookup works because the two lists are synchronized: the user at position `n` always corresponds to the device at position `n`. By using the index from one list as the subscript for the other, the algorithm retrieves the correct device without needing to iterate over or search `approved_devices` at all. This pattern — find index in list A, use it to access list B — is the core mechanism that the full `login()` function is built on.

**Q7 — What do you observe from the output when `username` is `"sgilmore"` and `device_id` is `"4n482ts"`?**  
Both messages are displayed: `The username sgilmore is approved to access the system.` and `4n482ts is the assigned device for sgilmore`. Both conditions joined by `and` evaluate to `True` — `"sgilmore"` is in `approved_users` (first condition: `True`), and `approved_devices[2]` is `"4n482ts"`, which equals the `device_id` variable (second condition: `True`). Since both are `True`, the entire `and` expression is `True` and the `if` block runs. This task introduces the two-factor check that is the heart of the algorithm: identity (is the user approved?) and possession (do they have the right device?). If either condition were `False`, the `and` expression would evaluate to `False` and neither message would print.

**Q8 — What do you observe from the output when `username` is `"sgilmore"` and `device_id` is `"4n482ts"`?**  
In the submitted code, `device_id` is actually set to `"4n582ts"` (one character transposed from the correct `"4n482ts"`), so the output is: `The user sgilmore is approved to access the system, but 4n582ts is not their assigned device.` The `if` condition fails because the device IDs do not match. Python then evaluates the `elif`, which confirms that the username is still approved (`True`) and that the device does not match (`True`), so the `elif` block runs. This is an important distinction from an unknown user: the system can confirm identity while flagging the device mismatch separately, giving the security team more actionable information than a generic rejection would.

**Q9 — After Python enters the inner conditional, what happens when the `device_id` is correct, and what happens when the `device_id` is incorrect?**  
When `device_id` matches the element at `ind` in `approved_devices` (the correct device), the inner `if` branch runs and displays a confirmation that the device is assigned to that user — as seen with `login("eraab", "a307vir")`. When `device_id` does not match (the wrong device), the inner `else` branch runs and displays a mismatch message — as seen with `login("bmoreno", "3rcv4w6")`, where bmoreno's assigned device is `"hl0s5o1"`, not `"3rcv4w6"`. The inner conditional is only ever reached after the outer `if` has already confirmed that the username is approved; this nested structure separates the two verification layers cleanly: identity first, device second. A third test call, `login("notknowuser", "unknowndevice")`, exercises the outer `else` branch, showing what happens when a username is not recognized at all.

---

## 💡 Key Code

```python
# Synchronized lists — user at index n owns device at index n
approved_users  = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts",  "a307vir", "3rcv4w6"]

# .append() — add a new user/device pair (both lists updated together)
approved_users.append("gesparza")
approved_devices.append("3rcv4w6")

# .remove() — remove a departed user/device pair
approved_users.remove("tshah")
approved_devices.remove("2ye3lzg")

# Cross-list lookup via .index()
ind = approved_users.index("sgilmore")   # returns 2
print(approved_devices[ind])             # prints "4n482ts"

# Full login() function with nested conditionals
def login(username, device_id):
    if username in approved_users:
        print("The user", username, "is approved to access the system.")
        ind = approved_users.index(username)
        if device_id == approved_devices[ind]:
            print(device_id, "is the assigned device for", username)
        else:
            print(device_id, "is not their assigned device.")
    else:
        print("The username", username, "is not approved to access the system.")

login("eraab", "a307vir")          # correct device → both approval messages
login("bmoreno", "3rcv4w6")        # wrong device  → approved + mismatch message
login("notknowuser", "unknowndevice")  # unknown user → not approved message
```

---

## 🔍 Algorithm Logic Map

```
login(username, device_id)
│
├── username in approved_users?
│   │
│   ├── YES → "User is approved."
│   │         ind = approved_users.index(username)
│   │         │
│   │         ├── device_id == approved_devices[ind]?
│   │         │   ├── YES → "device_id is the assigned device for username"
│   │         │   └── NO  → "device_id is not their assigned device."
│   │
│   └── NO  → "Username is not approved."
```

---

## 🔍 Notable Approaches & Deviations

**Task 3 — variable name collision (`removed_user` overwritten):**  
The lab provided two variable assignments: `removed_user = "tshah"` and then `removed_device = "2ye3lzg"`. In the submitted code, the second line reads `removed_user = "2ye3lzg"` — reassigning `removed_user` instead of creating a new variable `removed_device`. The `.remove()` calls that follow use the correct hardcoded strings (`"tshah"` and `"2ye3lzg"`) rather than the variable names, so the output is functionally correct. However, `removed_device` was never defined. In production code the `.remove()` calls should reference the variables directly (`approved_users.remove(removed_user)`, `approved_devices.remove(removed_device)`) to make the logic reusable; using hardcoded strings means a different removal would require editing both the variable assignments and the `.remove()` calls separately.

**Task 8 — `elif` condition is over-specified:**  
The submitted `elif` uses `username in approved_users and device_id != approved_devices[ind]`. This is logically correct but the first condition (`username in approved_users`) is redundant: Python only evaluates the `elif` when the preceding `if` was `False`. Since the `if` requires `username in approved_users` to be `True`, any execution that reaches the `elif` with a valid username already implies the username is approved. The `elif` could be written as `elif username in approved_users:` (or even just `else:` in a two-branch structure) without changing behavior. The explicit redundancy is not a bug, but in larger conditional chains it can obscure the logic.

---

## 🔍 Login Test Cases

| Call | Username approved? | Device correct? | Branch reached | Output |
|---|---|---|---|---|
| `login("eraab", "a307vir")` | ✅ Yes | ✅ Yes | Outer `if` → Inner `if` | Approved + correct device |
| `login("bmoreno", "3rcv4w6")` | ✅ Yes | ❌ No (`hl0s5o1`) | Outer `if` → Inner `else` | Approved + wrong device |
| `login("notknowuser", "unknowndevice")` | ❌ No | — | Outer `else` | Not approved |

---

## 🧠 Key Concepts Applied

- **Synchronized lists** — Two lists where element at index `n` in one list always corresponds to element at index `n` in the other; the pairing is maintained by updating both lists together on every add or remove
- **`.append()` method** — Adds an element to the end of a list in place; both lists must be appended to together to preserve synchronization
- **`.remove()` method** — Removes the first occurrence of a specified value from a list in place; both lists must be updated together to preserve synchronization
- **`in` operator** — Tests whether a value is an element of a sequence; returns `True` or `False` and is the idiomatic way to check list membership in Python
- **`.index()` method (on lists)** — Returns the index of the first occurrence of a specified value; used here to find a username's position so the same position can be used to look up the corresponding device
- **Cross-list lookup** — Using an index returned from one list as the subscript for another; the pattern `ind = listA.index(x); listB[ind]` retrieves the paired element without any additional search
- **`and` logical operator** — Evaluates to `True` only when both conditions are `True`; used to check username approval and device match in a single `if` expression
- **`elif` statement** — Evaluated only when all preceding `if`/`elif` conditions were `False`; used here to distinguish the wrong-device case from the unknown-user case
- **Nested conditionals** — A conditional statement placed inside the body of another; the outer conditional handles username verification and the inner conditional handles device verification, separating the two checks into their own logical layers
- **Encapsulation with `def`** — Wrapping the full algorithm in a named function means the logic is written once and can be called with any username/device combination; the function accesses `approved_users` and `approved_devices` from the enclosing scope

---

## 📚 What I Learned

- How synchronized lists work as a data structure for paired records: the index is the implicit link between corresponding elements, and maintaining the pairing is a discipline — every add and every remove must touch both lists at the same time
- How `.append()` and `.remove()` modify lists in place, and why both lists must always be updated together when using a synchronized-list design
- How `.index()` on a list returns a position, and how that position serves as a bridge to a second synchronized list — the pattern of finding index in list A and using it to access list B is fundamental to working with parallel data structures
- That the `in` operator is the cleanest way to test list membership: it reads naturally and evaluates to a boolean that drops directly into a conditional
- How nested conditionals structure multi-stage logic: the outer layer handles the first check (identity), and the inner layer handles the second check (device), so each decision point is separate and readable
- The practical difference between `elif` and `else`: `elif` requires its own condition to be evaluated, while `else` catches everything the preceding branches did not — choosing the simpler branch type where possible makes conditional chains easier to follow
- That encapsulating an algorithm in a function separates the logic from the data: the function body stays constant while the arguments change, making it reusable across every user in the system without duplicating any code

---

## 📁 Project Files

| File | Description |
|---|---|
| [`develop_an_algorithm.py`](./assets/develop_an_algorithm.py) | Annotated Python script with all 9 tasks, code, expected outputs, and notes on notable approaches |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
