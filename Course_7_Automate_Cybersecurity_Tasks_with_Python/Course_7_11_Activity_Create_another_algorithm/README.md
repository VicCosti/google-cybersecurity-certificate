# 🐍 Lab: Create Another Algorithm

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** `open()`, `with` statement, `.read()`, `.split()`, `.remove()`, `.join()`, `for` loop, `if/in`, `def`, file update algorithm, list mutation hazard

---

## 📋 Scenario Overview

As a security analyst, the task is to develop a Python algorithm that keeps an IP address allow list up to date by automatically removing addresses that have had their access revoked. The algorithm reads `allow_list.txt` into a string, converts it to a list with `.split()`, iterates over the list and removes any address found in a `remove_list` using `.remove()`, converts the filtered list back to a string with `" ".join()`, and overwrites the original file with the updated content. The full pipeline is then encapsulated in a reusable `update_file(import_file, remove_list)` function and called with a new set of removal targets to verify it works for any input.

---

## ✅ Tasks Completed

| Task | Description | Key Construct |
|---|---|---|
| 1 | Display the file name and the remove list | `print()` |
| 2 | Open the allow-list file for reading | `with open(import_file, "r") as file:` |
| 3 | Read the file content into a string variable | `.read()` |
| 4 | Convert the string to a list | `ip_addresses.split()` |
| 5 | Loop through the list and print each element | `for element in ip_addresses:` |
| 6 | Remove flagged IPs from the list inside the loop | `if element in remove_list: ip_addresses.remove(element)` |
| 7 | Convert list back to string and overwrite the file | `" ".join(ip_addresses)`, `open(import_file, "w")`, `.write()` |
| 8 | Read the updated file to verify the result | `open(import_file, "r")`, `.read()`, `print(text)` |
| 9 | Encapsulate the full algorithm in a function | `def update_file(import_file, remove_list):` |
| 10 | Call the function with a new remove list and verify | `update_file(...)`, read-back verification |

---

## 🔍 Questions & Answers

**Q1 — What do you observe about the output above?**  
The output shows two values. `import_file` is a plain string, `"allow_list.txt"`, which is the name of the file that holds the current set of approved IP addresses — it is just a file-name label at this stage, not the file's content. `remove_list` is a Python list of four IP address strings: `"192.168.97.225"`, `"192.168.158.170"`, `"192.168.201.40"`, and `"192.168.58.57"`. These are the addresses whose access has been revoked and that the algorithm will need to locate and delete from the file. The two variables represent the two inputs the algorithm requires: where the data lives (the file name) and what needs to be removed from it (the revocation list). Neither variable contains the actual file contents yet — that happens in the next task when the file is opened and read.

**Q2 — Do you notice any IP addresses in the allow list that are also in the `remove_list`?**  
Yes — `192.168.97.225` appears in both the allow list and the `remove_list`. It is the first entry in `remove_list` and is also present in the file content displayed in Task 3. This is the address the algorithm must find and delete. The other three addresses in `remove_list` (`192.168.158.170`, `192.168.201.40`, `192.168.58.57`) do not appear in the allow list, which means the algorithm also needs to handle the case where a removal target is not present — `.remove()` would raise a `ValueError` if called with a value that is not in the list, but the `if element in remove_list` check prevents that by only calling `.remove()` when a match is confirmed.

**Q3 — What are the benefits of incorporating the algorithm into a single function?**  
Encapsulating the algorithm in `update_file()` provides four concrete benefits. First, it eliminates repetition: the full read → split → filter → join → write pipeline is written once and reused by calling the function with different arguments, rather than copy-pasting the same block every time a file needs updating. Second, it makes the code easier to maintain — if the logic needs to change (for example, switching to the safer iteration-over-copy pattern discussed in the Notable section), only the function body needs to be updated, and every call site benefits automatically. Third, the function makes intent visible at the call site: `update_file("allow_list.txt", remove_list)` reads as one clear action rather than a block of file-handling mechanics. Fourth, the function is general-purpose: because it accepts any file name and any remove list as parameters, it can manage multiple allow-list files or respond to different revocation events without any modification to its code.

**Conclusion — What are your key takeaways from this lab?**  
This lab demonstrates a complete file-update algorithm that connects three core skills: file I/O (reading and overwriting a text file), list manipulation (converting a string to a list, removing elements, converting back), and function design (encapsulating a multi-step workflow into a reusable, parameterized function). The pipeline follows a clear read → process → write structure that applies directly to security operations: any time an access control list needs to be updated in response to a revocation event, the same pattern of reading the list, filtering it programmatically, and writing back the clean version can automate what would otherwise be a manual, error-prone task. One important edge case emerged during this lab: modifying a list while iterating over it with a `for` loop can silently skip elements. Understanding this hazard — and knowing the safer alternatives — is essential before applying this pattern in a production environment where missing a flagged address could be a security failure.

---

## 💡 Key Code

```python
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# ── Step 1: read file into string ────────────────────────────
with open(import_file, "r") as file:
    ip_addresses = file.read()

# ── Step 2: convert string to list ───────────────────────────
ip_addresses = ip_addresses.split()

# ── Step 3: remove flagged addresses ─────────────────────────
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)   # ⚠ see note below

# ── Step 4: convert list back to string ──────────────────────
ip_addresses = " ".join(ip_addresses)

# ── Step 5: overwrite the file ───────────────────────────────
with open(import_file, "w") as file:
    file.write(ip_addresses)

# ── Step 6: verify ───────────────────────────────────────────
with open(import_file, "r") as file:
    text = file.read()
print(text)

# ── Encapsulated as a function ───────────────────────────────
def update_file(import_file, remove_list):
    with open(import_file, "r") as file:
        ip_addresses = file.read()
    ip_addresses = ip_addresses.split()
    for element in ip_addresses:
        if element in remove_list:
            ip_addresses.remove(element)
    ip_addresses = " ".join(ip_addresses)
    with open(import_file, "w") as file:
        file.write(ip_addresses)

update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])
```

---

## 🔍 Algorithm Pipeline

```
allow_list.txt (on disk)
        │
        ▼
open(import_file, "r")  ──►  file.read()  ──►  ip_addresses  [string]
                                                      │
                                                      ▼
                                              ip_addresses.split()
                                                      │
                                                      ▼
                                              ip_addresses  [list]
                                                      │
                                          for element in ip_addresses:
                                            if element in remove_list:
                                              ip_addresses.remove(element)
                                                      │
                                                      ▼
                                          " ".join(ip_addresses)
                                                      │
                                                      ▼
                                              ip_addresses  [string]
                                                      │
                                                      ▼
                                         open(import_file, "w")  ──►  file.write(ip_addresses)
                                                      │
                                                      ▼
                                           allow_list.txt (updated)
```

---

## 🔍 Notable Approaches & Observations

**Task 6 — Mutating a list while iterating over it (hidden bug):**  
The lab's Task 6 pattern — `for element in ip_addresses: ... ip_addresses.remove(element)` — modifies the list that the `for` loop is currently iterating over. When `.remove()` deletes an element, the remaining elements shift left by one index position. At the same time, Python's loop counter advances by one. The net effect is that the element immediately after any removed entry is silently skipped. In this lab the bug does not surface because only `192.168.97.225` is present in the allow list from `remove_list`, and no two consecutive entries are both flagged. But in a real allow list where two adjacent entries both appear in `remove_list`, the second would survive — a security failure.

Two safe alternatives:

```python
# Option 1 — iterate over a shallow copy
for element in ip_addresses[:]:
    if element in remove_list:
        ip_addresses.remove(element)

# Option 2 — list comprehension (cleaner and more idiomatic)
ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]
```

Both correctly remove every flagged address regardless of position or adjacency.

**Task 7 — Why `.join()` is necessary before `.write()`:**  
After the loop, `ip_addresses` is a Python list. The `.write()` method only accepts a string argument — passing a list directly raises a `TypeError`. The line `ip_addresses = " ".join(ip_addresses)` converts the list back to a space-separated string. The `" "` (space) is the separator placed between each element; `"\n".join(ip_addresses)` would produce a newline-separated version instead, which would restore the original one-address-per-line format of the file.

**Task 10 — Reusability demonstrated with a different remove list:**  
The function call in Task 10 uses `["192.168.25.60", "192.168.140.81", "192.168.203.198"]` — a completely different set from the `remove_list` used in Tasks 6–8. None of these addresses appear in the allow list at that point, so the file content is unchanged after the call. This is still a meaningful test: it confirms the function runs without error when none of the removal targets are present, which is a valid real-world scenario (a revocation list may contain addresses that have already been removed in a previous run).

---

## 🧠 Key Concepts Applied

- **`open(filename, mode)`** — Opens a file and returns a file object; mode controls access type and cursor position
- **`with` statement** — Context manager that automatically closes the file when the block exits, even if an error occurs
- **`.read()`** — Reads the entire file content as a single string; the string includes embedded newlines between lines
- **`.split()`** — Converts a string to a list by splitting on whitespace; used here to separate each IP address into its own list element; reassignment is required because `.split()` returns a new list
- **`for element in list:`** — Iterates over each element in sequence; the loop variable `element` holds the current value on each iteration
- **`if element in remove_list:`** — Tests list membership using the `in` operator; evaluates to `True` if `element` is found anywhere in `remove_list`
- **`.remove(element)`** — Removes the first occurrence of `element` from the list in place; raises `ValueError` if the element is not present — the `if in` check above prevents that
- **Mutating a list while iterating** — A known Python hazard: calling `.remove()` inside a `for` loop over the same list can cause elements to be skipped; safer patterns are iterating over a copy (`list[:]`) or using a list comprehension
- **`" ".join(list)`** — Concatenates all list elements into a single string, separated by the specified string (here a space); the inverse of `.split()`; required before `.write()` because `.write()` accepts only strings
- **`open(filename, "w")`** — Opens the file for writing; creates it if it does not exist and truncates (empties) it if it does — the entire previous content is replaced
- **`def update_file(import_file, remove_list):`** — Encapsulates the full pipeline in a reusable function; the two parameters make it applicable to any file and any removal set without changing the function body

---

## 📚 What I Learned

- How to build a complete file-update algorithm from scratch in Python: read the file, convert its content to a manipulable list, filter the list, convert back to a string, and overwrite the original file — a pattern that applies directly to maintaining access control lists in a security environment
- Why `.split()` and `.join()` are inverse operations in this workflow: `.split()` converts the flat file string into a list of individual addresses for programmatic processing, and `" ".join()` reverses that conversion so the result can be written back to disk
- That `.write()` requires a string argument — passing a list raises a `TypeError` — which is why the `.join()` conversion step is mandatory before opening the file for writing
- A critical Python pitfall: modifying a list while iterating over it with a `for` loop can silently skip elements, because removing an item shifts the remaining elements left while the loop index continues to advance. The safer patterns are iterating over a copy of the list (`list[:]`) or using a list comprehension to build a clean filtered list
- How encapsulating an algorithm in a function (`def update_file(import_file, remove_list):`) separates the logic from the data: the function body stays constant while the arguments change, making the same workflow reusable across different files and different revocation events without duplicating any code
- The write → read verification pattern: after overwriting a file, immediately reading it back and displaying the result is a reliable way to confirm that the file on disk matches what the algorithm computed in memory — an essential check in any automated security workflow

---

## 📁 Project Files

| File | Description |
|---|---|
| [`create_another_algorithm.py`](./assets/create_another_algorithm.py) | Annotated Python script with all 10 tasks, code, expected outputs, and notes on the list mutation hazard and safer alternatives |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
