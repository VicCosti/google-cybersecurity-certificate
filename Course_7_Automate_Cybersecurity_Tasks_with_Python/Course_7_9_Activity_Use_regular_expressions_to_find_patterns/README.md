# 🐍 Lab: Use Regular Expressions to Find Patterns

> **Course:** Google Cybersecurity Professional Certificate — Course 7: Automate Cybersecurity Tasks with Python  
> **Platform:** Google Skills / Jupyter Notebook environment  
> **Language:** Python 3  
> **Topics:** `re` module, `re.findall()`, regex symbols (`\w`, `\d`, `\.`, `+`, `{m,n}`), pattern refinement, log parsing, IP address validation

---

## 📋 Scenario Overview

As a security analyst, two extraction tasks were automated using Python regular expressions. First, device IDs that begin with `"r15"` — indicating devices running an operating system that requires an update — were isolated from a log string using `re.findall()` and a pattern built from literal characters and the `\w+` quantifier. Second, a network login log containing both valid and malformed IP addresses was parsed through three iterations of pattern refinement: a strict three-digit-per-segment pattern, an over-permissive pattern that captures all addresses including invalid ones, and a final `\d{1,3}` pattern that correctly matches only valid-format IP addresses. The extracted valid addresses were then compared against a flagged list using a `for` loop and conditional, completing a full log-analysis pipeline.

---

## ✅ Tasks Completed

| Task | Description | Key Construct |
|---|---|---|
| 1 | Import the `re` module | `import re` |
| 2 | Display the device ID log string | `print()` |
| 3 | Build a pattern to match device IDs starting with `"r15"` | `"r15\w+"` |
| 4 | Extract matching device IDs using `re.findall()` | `re.findall(pattern, string)` |
| 5 | Display the login log file | `print()` |
| 6 | Build a strict pattern for `xxx.xxx.xxx.xxx` IP addresses | `\d{3}\.\d{3}\.\d{3}\.\d{3}` |
| 7 | Extract IP addresses matching the strict pattern; compare both notations | `re.findall()`, equivalent patterns |
| 8 | Relax the pattern to capture addresses with variable-length segments | `\d{1,4}` (submitted) vs. `\d+` (lab) |
| 9 | Tighten the pattern to 1–3 digits per segment; store as `valid_ip_addresses` | `\d{1,3}` |
| 10 | Display the flagged addresses list | `print()` |
| 11 | Loop through valid IPs; flag any that appear in `flagged_addresses` | `for`, `if address in flagged_addresses` |

---

## 🔍 Questions & Answers

**Q1 — What regular expression pattern did you use? For each component of the pattern, what would happen if it were missing?**  
The pattern `"r15\w+"` consists of two parts. The literal prefix `r15` anchors every match to substrings that begin with exactly those three characters in that order. Without it, the pattern would reduce to `\w+`, which matches any alphanumeric sequence and would return every device ID in the string regardless of prefix — the filter would be lost entirely. The metacharacter sequence `\w+` is itself composed of two elements: `\w` matches any single alphanumeric character (letters, digits, or underscore), and `+` is a quantifier meaning "one or more occurrences of the preceding element." Without `\w`, the pattern would become `r15+`, which would match `"r15"` followed by one or more literal `"5"` characters — completely wrong for a device ID. Without `+`, the pattern would become `"r15\w"`, which matches `"r15"` followed by exactly one alphanumeric character, returning four-character fragments like `"r15x"` instead of complete device IDs like `"r15xk9h"`.

**Q2 — What are some examples of IP addresses that were extracted? What are some examples of IP addresses that were not extracted? Do any that were not extracted seem to be valid IP addresses?**  
The strict `\d\d\d\.` (or `\d{3}\.`) pattern extracted seven addresses, all with exactly three digits in every segment: `192.168.152.148`, `192.168.190.178`, `192.168.213.128`, `192.168.247.153`, `192.168.174.117`, `192.168.148.115`, and `192.168.168.144`. Addresses that were not extracted include `192.168.22.115` (iuduike), `192.168.96.200` (asundara), and all of the malformed entries. The first two — `192.168.22.115` and `192.168.96.200` — are genuine valid IP addresses. They were missed because they contain one or more segments with fewer than three digits (`"22"` and `"96"` are two-digit segments), and the strict pattern requires exactly three digits per segment. The pattern needs to be relaxed to accommodate the full range of valid segment lengths (1–3 digits).

**Q3 — What gets extracted here? Do all extracted IP addresses have between one and three digits in every segment?**  
With the relaxed pattern (Task 8), all addresses that contain at least one digit per segment — separated by periods — are extracted, including several that are not valid IP addresses. For example, `1923.1689.3.24` (arutley) and `1924.1680.27.57` (aestrada) are now extracted because the pattern allows segments with up to 4 digits (in the submitted version) or unlimited digits (with `\d+`). Not all extracted addresses have between one and three digits in every segment: `1923.1689.3.24` has four-digit segments, and similarly for several other malformed entries. This over-extraction is expected at this stage and establishes why an upper bound of 3 is necessary in the final pattern.

**Q4 — What do you notice about the extracted IP addresses here compared to those extracted in the previous two tasks?**  
The final `\d{1,3}` pattern strikes the correct balance between the two earlier versions. Compared to Task 7 (strict three digits), it now correctly includes addresses with shorter segments: `192.168.22.115` and `192.168.96.200`, which were missed before, are now extracted. Compared to Task 8 (over-permissive), it no longer includes malformed addresses with oversized segments: `1923.1689.3.24`, `1924.1680.27.57`, `1921.168.1283.75`, `19245.168.2345.49`, and `192.16874.1390.176` are all correctly excluded because none of them can be matched as four consecutive segments of 1–3 digits. The result is a clean list of ten valid-format IP addresses — exactly the addresses that could plausibly appear in a legitimate login log and that are ready to be checked against the flagged list.

---

## 💡 Key Code

```python
import re

# ── Device ID extraction ──────────────────────────────────────
devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"

target_pattern = "r15\w+"
print(re.findall(target_pattern, devices))
# Output: ['r151dm4', 'r15xk9h', 'r15u9q5', 'r159r1u']

# ── IP address extraction — pattern progression ───────────────

# Task 7 — strict: exactly 3 digits per segment (misses 1–2 digit segments)
pattern = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"
# Equivalent with quantifier:
pattern = "\d{3}\.\d{3}\.\d{3}\.\d{3}"

# Task 8 — over-permissive: 1–4 digits per segment (extracts some invalid IPs)
pattern = "\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}"

# Task 9 — final: 1–3 digits per segment (correct)
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
valid_ip_addresses = re.findall(pattern, log_file)

# ── Flagged IP check ──────────────────────────────────────────
flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]

for address in valid_ip_addresses:
    if address in flagged_addresses:
        print("The IP address", address, "has been flagged for further analysis.")
    else:
        print("The IP address", address, "does not require further analysis.")
```

---

## 🔍 Pattern Progression Map

```
Task 7  \d\d\d\.\d\d\d\.\d\d\d\.\d\d\d   exactly 3 digits per segment
        = \d{3}\.\d{3}\.\d{3}\.\d{3}       ← submitted (equivalent, more concise)
        → extracts 7 addresses; misses valid ones with 1–2 digit segments

Task 8  \d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}  1 to 4 digits per segment
        (lab asked for \d+ — no upper bound)
        → extracts valid + some invalid (4-digit segments)

Task 9  \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}  1 to 3 digits per segment ✅
        → extracts only valid-format IP addresses
```

---

## 🔍 Flagged Addresses — Task 11 Results

| IP Address | In Log? | Flagged? | Action |
|---|---|---|---|
| `192.168.152.148` | ✅ | ❌ | Does not require further analysis |
| `192.168.22.115` | ✅ | ❌ | Does not require further analysis |
| `192.168.190.178` | ✅ | ✅ | **Flagged for further analysis** |
| `192.168.213.128` | ✅ | ❌ | Does not require further analysis |
| `192.168.96.200` | ✅ | ✅ | **Flagged for further analysis** |
| `192.168.247.153` | ✅ | ❌ | Does not require further analysis |
| `192.168.174.117` | ✅ | ✅ | **Flagged for further analysis** |
| `192.168.148.115` | ✅ | ❌ | Does not require further analysis |
| `192.168.103.106` | ✅ | ❌ | Does not require further analysis |
| `192.168.168.144` | ✅ | ✅ | **Flagged for further analysis** |

4 of 10 valid addresses flagged.

---

## 🔍 Notable Approaches & Deviations

**Task 6 — `\d{3}` used instead of `\d\d\d`:**  
The lab hint presented `\d\d\d\.` as the building block for a three-digit segment, implying the expected answer was `\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d`. The submitted pattern `\d{3}\.\d{3}\.\d{3}\.\d{3}` is functionally identical — `{3}` is simply the quantifier shorthand for "exactly 3 repetitions" — but more concise and readable. This demonstrates independent familiarity with curly-bracket quantifier syntax, which the lab only introduces formally in Task 9.

**Task 7 — both `pattern` and `pattern2` printed:**  
Rather than printing only the lab-scaffold pattern, both the repeated-symbol version (`\d\d\d\.`) and the quantifier version (`\d{3}\.`) were run side by side. Both produce identical output, which confirms the two notations are equivalent. This is a useful verification step and goes beyond the task scope.

**Task 8 — `\d{1,4}` used instead of `\d+`:**  
The lab asked for `\d+` (one or more digits, no upper bound) to demonstrate that the pattern now captures invalid addresses with oversized segments. The submitted pattern `\d{1,4}` (one to four digits) is stricter: it starts limiting segments at 4 digits rather than allowing arbitrarily long ones. The pedagogical result is similar — some invalid addresses are still extracted — but the `\d+` version would extract more of them. Both approaches lead naturally to the conclusion that `{1,3}` is the correct bound. Worth noting: `\d{1,4}` is arguably a more thoughtful intermediate step, since the analyst is already reasoning about segment-length boundaries.

**Task 9 — `\w{2,4}` submitted instead of `\d{1,3}`:**  
The submitted pattern for this task was `\w{2,4}\.\w{2,4}\.\w{2,4}\.\w{2,4}`. This has two issues: `\w` matches alphanumeric characters (letters and digits), not digits alone — it would incorrectly match letter-containing strings — and the lower bound of 2 would skip single-digit segments entirely. The correct pattern `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}` was used correctly in Task 11, so the final output of the notebook is right. The correct pattern is used throughout `use_regex_to_find_patterns.py`.

---

## 🧠 Key Concepts Applied

- **`import re`** — Loads Python's built-in regular expression module; required before any `re.*` function calls
- **`re.findall(pattern, string)`** — Returns a list of all non-overlapping matches of `pattern` in `string`; scans left to right and never returns overlapping matches
- **`\w`** — Matches any alphanumeric character (letters a–z, A–Z, digits 0–9) or underscore; used for device IDs which can contain any alphanumeric character
- **`\d`** — Matches any single digit (0–9); more precise than `\w` when the target is known to be numeric, as in IP address segments
- **`\.`** — Matches a literal period; the backslash escapes the dot, which without it would be a wildcard matching any character
- **`+` quantifier** — Matches one or more occurrences of the preceding element; `\w+` matches an alphanumeric string of any length ≥ 1
- **`{m,n}` quantifier** — Matches between `m` and `n` occurrences of the preceding element; `\d{1,3}` matches 1, 2, or 3 digits — the exact range of valid IP segment lengths
- **Pattern refinement** — Building a regex incrementally (too strict → too loose → correct) is a standard workflow; each iteration reveals what the current pattern misses or over-matches
- **`for` loop + `in` operator** — Iterating over a list of extracted values and checking each for membership in a second list combines the results of regex extraction with a pre-defined threat intelligence list

---

## 📚 What I Learned

- How to import and use Python's `re` module, and why `import re` is a prerequisite for all regex operations in the notebook
- How `re.findall()` works: it applies a pattern to a string and returns a list of all matches, making it the right tool for extracting multiple values from an unstructured log
- The difference between `\w` (alphanumeric) and `\d` (digits only): choosing the right character class is important — `\w` would incorrectly match letter-containing substrings when extracting IP addresses
- How `\.` differs from `.` in a regex: without the backslash, `.` is a wildcard that matches any character; with it, it matches only a literal period — an essential distinction when parsing dot-separated formats like IP addresses
- How quantifiers control match length: `+` is open-ended (one or more), while `{1,3}` is bounded (between one and three). The bounded quantifier is the precise tool for enforcing IP address segment constraints
- The value of iterative pattern refinement: starting with a strict pattern (Task 7) reveals what gets missed; loosening it (Task 8) shows what gets over-captured; tightening to the correct bounds (Task 9) produces the right result. This three-step process applies to any regex problem
- How to connect regex extraction to a threat intelligence workflow: `re.findall()` extracts candidate values, and a `for`/`if`/`in` loop compares each against a flagged list — the output is an automated triage of every log entry, separating entries that need investigation from those that don't

---

## 📁 Project Files

| File | Description |
|---|---|
| [`use_regex_to_find_patterns.py`](./assets/use_regex_to_find_patterns.py) | Annotated Python script with all 11 tasks, code, expected outputs, and notes on pattern deviations |

---

## 🛠️ Tools & Concepts Referenced

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Google Skills](https://img.shields.io/badge/Platform-Google_Skills-4285F4?style=flat-square&logo=google&logoColor=white)
