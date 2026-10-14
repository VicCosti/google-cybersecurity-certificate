# 🐍 Lab: Import and Parse a Text File

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** `open()`, `with` statement, file modes (`"r"`, `"a"`, `"w"`), `.read()`, `.write()`, `.split()`, file parsing, log analysis

---

## 📋 Scenario Overview

As a security analyst, the task is to automate two common file-handling workflows in Python. First, an existing security log file (`login.txt`) is imported, read into a string with `.read()`, and parsed into a list with `.split()`. A missing log entry is then appended to the file using `"a"` mode without disturbing the existing content. Second, a new allow-list text file (`allow_list.txt`) is created from scratch using `"w"` mode, a string of approved IP addresses is written to it with `.write()`, and the file is immediately read back to verify the content was persisted correctly.

---

## ✅ Tasks Completed

| Task | Description | Key Construct |
|---|---|---|
| 1 | Open a log file for reading using a `with` statement | `with open(file, "r") as file:` |
| 2 | Read the file content into a string variable | `.read()` |
| 3 | Split the string into a list and display it | `.split()` |
| 4 | Append a missing log entry to the file | `open(file, "a")`, `.write()` |
| 5 | Assign the allow-list filename and IP address string | Variable assignment |
| 6 | Create a new file and write IP addresses to it | `open(file, "w")`, `.write()` |
| 7 | Read the allow-list file back to verify its contents | `open(file, "r")`, `.read()` |

---

## 🔍 Questions & Answers

**Q1 — What do you notice about the output before and after using the `.split()` method?**  
Before calling `.split()`, `text` is a single continuous string containing the entire file content. Every log line is part of that one string, with newline characters (`\n`) embedded between entries — when printed, the string displays across multiple lines because `print()` interprets the `\n` characters, but it is still fundamentally one Python string object. After calling `.split()`, the output is a Python list. Each element of the list is one whitespace-separated token from the original string. Because the log file uses commas (not spaces) within each entry, and newlines between entries, the default `.split()` — which splits on any whitespace — treats each full log line as a single token, so each element in the resulting list is a complete comma-joined entry like `'tshah,192.168.92.147,15:26:08,2022-05-10'`. The transformation from a monolithic string to an indexed list is what makes the log data programmatically accessible: list elements can be iterated over, indexed, and filtered in ways that a raw string cannot.

**Q2 — What do you notice about the position of the entry that was added to the log file?**  
The new entry appears at the very end of the file — after all twenty original log lines. This is the defining behavior of `"a"` (append) mode: Python moves the write cursor to the end of the file before writing, so new content is always added after everything already there. No existing content is modified or overwritten. One detail worth noting is that the `missing_entry` string does not start with a newline character, so it is joined directly to the last character of the existing file with no line break between them. In the displayed output, the final original entry (`jsoto,192.168.25.60,5:09:21,2022-05-09`) and the appended entry (`jrafael,192.168.243.140,4:56:27,2022-05-09`) appear on the same line. In a real log-management workflow, the write call would typically use `"\n" + missing_entry` to ensure the new entry begins on its own line.

**Conclusion — What are your key takeaways from this lab?**  
Python's built-in file handling is centered on three components that work together: the `open()` function selects the file and the access mode, the `with` statement manages the file's lifecycle so it is automatically closed after the block, and the mode string (`"r"`, `"a"`, `"w"`) determines what operations are permitted and how the cursor is positioned. Reading a file with `.read()` produces a single string containing the entire content, which is then ready for string operations like `.split()` to convert it into a structured list. Writing is done with `.write()`, which takes a string argument — `"a"` mode appends without disturbing existing content, while `"w"` mode creates or overwrites. Together, these tools form a complete file I/O pipeline that applies directly to security tasks: importing logs for analysis, updating records when entries are missing, and writing allow or deny lists that can be read by other parts of an automated security workflow.

---

## 💡 Key Code

```python
# ── Read a file ───────────────────────────────────────────────
import_file = "login.txt"

with open(import_file, "r") as file:
    text = file.read()

print(text)           # entire file as one string
print(text.split())   # file content as a list of tokens

# ── Append a missing entry ────────────────────────────────────
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

with open(import_file, "a") as file:
    file.write(missing_entry)          # appended at end; no newline prefix

# To place it on its own line:
# file.write("\n" + missing_entry)

# ── Create a file and write to it ────────────────────────────
import_file = "allow_list.txt"
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 ..."

with open(import_file, "w") as file:
    file.write(ip_addresses)           # creates or overwrites the file

# ── Read it back to verify ────────────────────────────────────
with open(import_file, "r") as file:
    text = file.read()

print(text)
```

---

## 🔍 File Mode Reference

```
Mode  Cursor starts at  File must exist?  Effect on existing content
────  ────────────────  ────────────────  ──────────────────────────
"r"   beginning         yes               read-only; no changes allowed
"a"   end of file       no (creates it)   new content added after existing
"w"   beginning         no (creates it)   existing content erased (truncated)
```

---

## 🔍 Notable Approaches & Observations

**Task 3 — `.split()` default separator behavior:**  
The lab instructs the use of `.split()` with no argument, which splits on any whitespace (spaces, tabs, and newlines). For this particular log file, each entry is a comma-separated string with no embedded spaces, so each full log line — e.g., `'tshah,192.168.92.147,15:26:08,2022-05-10'` — is treated as a single token and becomes one list element. The result is a clean list of complete entries. An alternative that makes the intent more explicit is `text.split("\n")`, which splits only on newlines; for this log format the outputs are identical. The key thing to understand is that `.split()` does not modify the original `text` variable — it returns a new list, so reassignment (`text = text.split()`) is required if the split result needs to be stored.

**Task 4 — missing newline before appended entry:**  
The `missing_entry` string does not include a leading `\n`, so the appended content runs directly onto the last line of the existing file. The lab does not ask for this to be fixed, but in production code the standard pattern is `file.write("\n" + missing_entry)` or ensuring that the file already ends with a newline (which log generators typically guarantee). This is a practical detail that comes up any time you use `"a"` mode to extend an existing text file.

---

## 🧠 Key Concepts Applied

- **`open(filename, mode)`** — Built-in function that opens a file and returns a file object; the mode string controls read/write access and cursor position
- **`with` statement** — Context manager that automatically calls `file.close()` when the block exits, even if an exception occurs; the idiomatic way to handle files in Python
- **`"r"` mode** — Read-only; file must already exist; cursor starts at the beginning; used for importing and analyzing existing log files
- **`"a"` mode** — Append; creates the file if it does not exist; cursor starts at the end of existing content; used for adding entries without overwriting existing data
- **`"w"` mode** — Write; creates the file if it does not exist, or truncates it to empty if it does; cursor starts at the beginning; used for creating new files or fully replacing content
- **`.read()`** — Method on a file object that reads the entire file content and returns it as a single string, including embedded newline characters
- **`.write(string)`** — Method on a file object that writes the given string to the file; does not add a newline automatically — the caller is responsible for including `\n` if a line break is needed
- **`.split()`** — String method that splits on any whitespace by default and returns a list of substrings; called on the result of `.read()` to convert the raw file string into a structured list
- **Write → read verification pattern** — Opening a file for writing and then immediately re-opening it for reading is a standard way to confirm that content was persisted correctly; used in Tasks 6–7

---

## 📚 What I Learned

- How to use Python's `with open()` pattern to safely open, read, and close files — the `with` statement handles cleanup automatically and is the preferred approach over manually calling `file.close()`
- The distinction between the three file modes: `"r"` for reading an existing file, `"a"` for appending to one without overwriting it, and `"w"` for creating a new file or replacing an existing one entirely — choosing the wrong mode is a common source of accidental data loss
- How `.read()` converts a text file into a single Python string, and how `.split()` then converts that string into a list — together these two methods form the core parsing pipeline for unstructured log files
- That `.split()` with no argument splits on any whitespace including newlines, and that the result is a new list that does not modify the original variable — reassignment is required if the list form needs to be stored
- The practical difference between `"a"` and `"w"` mode when updating a file: append mode preserves existing content and adds new entries at the end, while write mode erases everything first — both have legitimate uses in security workflows, and choosing between them depends on whether the existing content needs to be kept
- That `.write()` does not add a newline automatically — the caller must include `\n` explicitly if the new content should appear on its own line, which matters when appending entries to a log file
- The write → read verification pattern: writing to a file and immediately reading it back is a reliable way to confirm that the file on disk contains exactly what was intended before downstream code depends on it

---

## 📁 Project Files

| File | Description |
|---|---|
| [`import_and_parse_a_text_file.py`](./assets/import_and_parse_a_text_file.py) | Annotated Python script with all 7 tasks, code, expected outputs, and inline notes on file mode behavior |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
