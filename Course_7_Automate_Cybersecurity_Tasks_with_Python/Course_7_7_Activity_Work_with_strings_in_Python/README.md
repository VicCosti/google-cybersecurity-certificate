# 🐍 Lab: Work with Strings in Python

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** String type conversion (`str()`), `len()`, string concatenation, zero-based indexing, string slicing, `.index()` method, URL parsing

---

## 📋 Scenario Overview

As a security analyst, string manipulation is a daily tool — employee IDs, device identifiers, and network URLs all arrive as string data that must be validated, reformatted, or parsed. In this lab, three real-world automation tasks were implemented: converting and standardizing a four-digit employee ID to a five-character format using `str()`, `len()`, and string concatenation; extracting specific characters from a device ID using zero-based indexing and slicing; and parsing the individual components of a URL (protocol, domain extension, and website name) using string slicing and the `.index()` method.

---

## ✅ Tasks Completed

| Task | Description | Key Construct |
|---|---|---|
| 1 | Convert `employee_id` from `int` to `str`; confirm type change | `str()`, `type()` |
| 2 | Display a message if the employee ID is shorter than 5 characters | `len()`, `if`, `<` |
| 3 | Prepend `"E"` to a short ID to bring it to 5 characters | String concatenation with `+` |
| 4 | Extract the fourth character of a device ID | Zero-based indexing `[3]` |
| 5 | Extract the first three characters of a device ID | String slice `[0:3]` |
| 6 | Extract the protocol and remaining URL components separately | String slicing |
| 7 | Find the starting index of `".com"` in a URL | `.index()` method |
| 8 | Store the `.index()` result in a variable `ind` | Variable assignment |
| 9 | Extract the domain extension using `ind` and `ind+4` | Relative slice `[ind:ind+4]` |
| 10 | Extract the website name using `ind` as the end boundary | Slice `[ind-11:ind]` |

---

## 🔍 Questions & Answers

**Q1 — What do you observe about the data type of `employee_id` the first time it's displayed? What about the second time?**  
The first `print(type(employee_id))` returns `<class 'int'>` because the initial assignment `employee_id = 4186` stores the value as an integer — a numeric type that supports arithmetic operations but cannot be sliced, measured with `len()`, or concatenated with other strings. After `employee_id = str(employee_id)`, the second `print(type(employee_id))` returns `<class 'str'>`, confirming the conversion. The numeric value is unchanged — `"4186"` looks identical to `4186` when printed — but the type is now a string. This matters because the remaining tasks require string operations: `len(employee_id)` to check character count, and `"E" + employee_id` to prepend a prefix. Neither of those operations is possible on an integer. Type conversion is a common first step when working with IDs or codes that are logically text even though they look like numbers.

**Q2 — What does `print(url[ind:ind+4])` output and why?**  
The output is `.com`. `url.index(".com")` returns `19` — the index where the substring `".com"` first appears in `"https://exampleURL1.com"`. The slice `url[ind:ind+4]` then starts at index 19 (inclusive) and ends at index 23 (exclusive), capturing exactly four characters: `.`, `c`, `o`, `m`. Expressing the end index as `ind + 4` rather than a hardcoded value is the correct approach here because it is relative: it relies only on knowing the fixed length of `".com"` (always 4) and the position where it starts, which `.index()` computes dynamically. This means the same slice expression works correctly regardless of where `".com"` appears in the URL, making it more generalizable than a hardcoded upper bound.

---

## 💡 Key Code

```python
# Task 1 — type conversion: int → str
employee_id = 4186
print(type(employee_id))   # <class 'int'>
employee_id = str(employee_id)
print(type(employee_id))   # <class 'str'>

# Task 3 — concatenation: prepend "E" to a short ID
if len(employee_id) < 5:
    employee_id = "E" + employee_id
print(employee_id)
# Output: E4186

# Task 4 — zero-based indexing: fourth character
device_id = "r262c36"
print(device_id[3])
# Output: 2

# Task 5 — slicing: first three characters
print(device_id[0:3])
# Output: r26

# Task 7 — .index(): find position of ".com"
url = "https://exampleURL1.com"
print(url.index(".com"))
# Output: 19

# Task 9 — relative slice: extract domain extension
ind = url.index(".com")
print(url[ind:ind + 4])
# Output: .com

# Task 10 — slice using ind as end boundary
print(url[8:ind])          # recommended: generalizable to any website name length
# or:
print(url[ind - 11:ind])   # works here but assumes website name is 11 chars
# Output (both): exampleURL1
```

---

## 🔍 Notable Approaches & Deviations

**Task 6 — Protocol extraction split into two prints:**  
The lab expected a single slice `url[0:8]` to extract `"https://"` as one unit. The submitted solution splits this into two separate prints: `url[0:5]` for the protocol (`"https"`) and `url[8:23]` for the domain and path (`"exampleURL1.com"`). This demonstrates a clear understanding of URL structure — knowing exactly where each component starts and ends — but goes beyond the task scope. The hardcoded upper bound `23` also makes this version brittle: it would break for URLs of different lengths, whereas `url[0:8]` extracts the protocol prefix reliably regardless of what follows.

**Task 10 — Website name extracted via `ind - 11` instead of `8`:**  
The lab hint recommended `url[8:ind]` as the generalizable solution: start at index 8 (the fixed position after `"https://"`) and end at `ind` (the dynamically computed position of `".com"`). The submitted solution uses `url[ind-11:ind]`, subtracting the known length of `"exampleURL1"` from `ind` to compute the start. This produces the correct result for this specific URL but would break for any URL where the website name is not exactly 11 characters. In production automation, `url[8:ind]` is the preferred pattern because it does not assume anything about the website name's length.

---

## 🔍 URL Component Map

```
https://exampleURL1.com
0123456789...
│        │          │  │
│        8          19 23
│
0

url[0:5]    → "https"          (protocol)
url[0:8]    → "https://"       (protocol + separator — lab expected answer for Task 6)
url[8:19]   → "exampleURL1"    (website name — generalizable)
url[19:23]  → ".com"           (domain extension)
```

---

## 🧠 Key Concepts Applied

- **`str()` conversion** — Converts an integer to its string representation; required before applying string operations like `len()`, slicing, or concatenation
- **`type()` function** — Returns the data type of a variable; used here to confirm the conversion from `<class 'int'>` to `<class 'str'>`
- **`len()` function** — Returns the number of characters in a string; used to check whether an employee ID meets the five-digit requirement
- **String concatenation with `+`** — Joins two strings into one; `"E" + "4186"` → `"E4186"`; operands must both be strings (integers must be converted first)
- **Zero-based indexing** — Characters in a string are numbered from 0; the fourth character is at index 3; `device_id[3]` extracts it
- **String slicing `[start:stop]`** — Extracts a substring from `start` (inclusive) to `stop` (exclusive); `device_id[0:3]` → first three characters
- **`.index()` method** — Searches a string for a substring and returns the index of its first occurrence; `url.index(".com")` returns `19`
- **Relative slice indexing** — Expressing slice bounds relative to a computed index (`ind`, `ind+4`) makes the extraction portable across different URLs, unlike hardcoded values
- **URL structure** — A standard `https://` URL consists of a protocol (`https`), separator (`://`), website name, and domain extension (`.com`); each occupies a predictable position that can be targeted with slicing

---

## 📚 What I Learned

- That integers and strings are fundamentally different types in Python even when they represent the same value — `4186` (int) and `"4186"` (str) cannot be used interchangeably, and conversion with `str()` is necessary before applying string operations
- How `len()` enables length-based validation: checking `len(employee_id) < 5` catches IDs that need to be updated without inspecting each one manually
- That string concatenation with `+` requires both operands to be strings — a type mismatch between a string and an integer would raise a `TypeError`
- How zero-based indexing works: the nth character is at index n−1, so the fourth character is at index 3
- How slicing with `[start:stop]` extracts a substring, with the stop index always excluded — `[0:3]` returns three characters at indices 0, 1, and 2
- How `.index()` dynamically locates a substring within a string, returning its starting position without requiring any knowledge of the URL's length
- That combining `.index()` with relative offsets (`ind`, `ind+4`, `ind-11`) allows targeted extraction of URL components, and that the more generalizable approach anchors the start at a known fixed position (`8` for the start of the website name) rather than computing it from the end
- The importance of writing portable slices: hardcoded index values work for a single known string but break as soon as the data changes; relative and dynamic indices are the foundation of reusable string-parsing code

---

## 📁 Project Files

| File | Description |
|---|---|
| [`work_with_strings.py`](./assets/work_with_strings.py) | Annotated Python script with all 10 tasks, code, expected outputs, and notes on approach |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
