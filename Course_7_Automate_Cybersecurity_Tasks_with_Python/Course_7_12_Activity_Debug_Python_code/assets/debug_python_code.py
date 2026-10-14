# ============================================================
# Lab: Debug Python Code
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================
#
# This lab covers all three Python error categories:
#   • Syntax errors  — code that Python cannot parse at all
#   • Exceptions     — code that parses but fails at runtime
#   • Logic errors   — code that runs but produces wrong output
#
# Debugging strategy used throughout: run the cell, read the
# error message, identify the category, fix one error at a
# time, re-run to confirm before moving to the next.


# ── TASK 1: syntax error — missing colon on for-loop header ──
#
# BUG (original):
#   for i in range(10)          ← SyntaxError: expected ':'
#       print("Connection cannot be established")
#
# FIX: add the required colon `:` at the end of the for header.
# Every compound statement header in Python (for, while, if,
# def, with, …) must end with a colon.

# For loop that iterates over a range of numbers
# and displays a message each iteration

for i in range(10):
    print("Connection cannot be established")

# Output (10 lines):
# Connection cannot be established
# Connection cannot be established
# ... (repeated 10 times)

# Q1: Before the fix, running the cell raises a SyntaxError —
# Python cannot parse the loop at all because the header is
# missing the required colon. The error message points to the
# `for` line. Fix: add `:` after `range(10)`.


# ── TASK 2: syntax error — missing closing quote + comma ─────
#
# BUG (original):
#   usernames_list = ["djames", "jpark", "tbailey", "zdutchma "esmith", ...]
#                                                              ^
#                           missing closing quote on "zdutchma"
#                           and missing comma before "esmith"
#
# FIX: close the string "zdutchma" with a quote and add a comma
# before "esmith" so each list element is properly separated.

# Assign `usernames_list` to a list of usernames

usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith", "srobinso", "dcoleman", "fbautist"]

# Display `usernames_list`

print(usernames_list)

# Output:
# ['djames', 'jpark', 'tbailey', 'zdutchma', 'esmith', 'srobinso', 'dcoleman', 'fbautist']

# Q2: Before the fix, Python raises a SyntaxError because the
# string literal "zdutchma is never closed — Python keeps
# reading characters looking for the closing quote and then
# encounters another quote as part of "esmith", which produces
# a confusing error. Fix: add a closing quote after zdutchma
# and a comma to separate it from the next element.


# ── TASK 3: syntax error — missing closing parenthesis ───────
#
# BUG (original):
#   print("update needed".upper()       ← SyntaxError: '(' was never closed
#
# FIX: add the missing closing parenthesis `)` to close the
# outer print() call.
#
# Note on the expression structure:
#   print(  "update needed".upper()  )
#   │                               │
#   └── outer print() call ─────────┘
#
# "update needed".upper() is a method call on the string literal,
# which returns "UPDATE NEEDED". That result is then passed as
# the argument to print(). Both sets of parentheses are required.

# Display a message in upper case

print("update needed".upper())

# Output:
# UPDATE NEEDED

# Q3: Before the fix, Python raises a SyntaxError reporting
# that the opening parenthesis of print() was never closed.
# Fix: add the missing `)` at the end of the line.


# ── TASK 4: NameError + syntax error + indentation error ─────
#
# BUGS (original):
#   1. `username_list` used in the for loop, but the variable
#      was defined as `usernames_list` — NameError at runtime
#      (Python can't find `username_list`)
#   2. `if name = username:` — SyntaxError: assignment `=`
#      used where comparison `==` is required
#   3. `print(...)` not indented under the `if` block —
#      SyntaxError / IndentationError
#
# FIX APPROACH (one error at a time):
#   Step 1 — fix `if name = username:` → `if name == username:`
#             (run → NameError fires now)
#   Step 2 — fix `username_list` → `usernames_list` in for line
#             (or rename the definition; keeping `usernames_list`
#             is more consistent with the rest of the course)
#   Step 3 — indent the print() statement under the if block
#
# Note on what Vittorio submitted:
#   The definition was renamed to `username_list` (no 's') to
#   match the loop line. This makes the code run correctly and
#   is a valid fix. The cleaner approach is the reverse:
#   keep `usernames_list` in the definition and fix the loop
#   line to match, since `usernames_list` is the name used in
#   every other task and better describes the variable.
#
# SUBMITTED FIX (runs correctly):

# Assign `usernames_list` to a list of usernames that represent approved users

username_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith", "srobinso", "dcoleman", "fbautist"]

# Assign `username` to a specific username

username = "esmith"

# For loop that iterates over the elements of `username_list`

for name in username_list:

    # Check if `name` matches `username`

    if name == username:
        print("The user is an approved user")

# Output:
# The user is an approved user

# Q4: Before the fix, Python raises a SyntaxError on the `if`
# line because `=` (assignment) is not valid in a condition —
# Python requires `==` (comparison) to test equality. After
# fixing that, a NameError fires because `username_list` (used
# in the loop) didn't match the defined variable name
# `usernames_list`. After fixing the name mismatch, an
# IndentationError fires because the `print` was not indented
# inside the `if` block. Fixing all three: use `==`, align the
# variable names, and indent `print` four additional spaces.


# ── TASK 5: IndexError — index out of range ───────────────────
#
# BUG (original):
#   if username == usernames_list[5]:   ← IndexError at runtime
#
# `usernames_list` has 5 elements. In Python, zero-based
# indexing means valid indices are 0–4. Index 5 does not exist
# and raises an IndexError at runtime (the code is syntactically
# correct but fails when executed).
#
# FIX: use index 4 to access the last (fifth) element.
# General rule: last index = len(list) - 1

# Assign `usernames_list` to a list of usernames

usernames_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to a specific username

username = "eraab"

# Determine whether `username` is the final username in `usernames_list`

if username == usernames_list[4]:
    print("This username is the final one in the list.")

# Output:
# This username is the final one in the list.

# Q5: Before the fix, an IndexError is raised because index 5
# is out of range for a 5-element list (valid indices: 0–4).
# This is a runtime exception, not a syntax error — Python can
# parse the code fine, but it fails when it tries to look up
# index 5. Fix: change [5] to [4].


# ── TASK 6: syntax error + AttributeError (wrong method call) ─
#
# BUGS (original):
#   1. `with open(import_file, "r") as file`  ← missing `:`
#      → SyntaxError before the code even runs
#   2. `ip_addresses = split.ip_addresses()`
#      → AttributeError / NameError: `split` is not a defined
#        object; the method `.split()` belongs to the string
#        `ip_addresses`, not to a standalone name `split`
#
# FIX:
#   1. Add `:` at the end of the `with` header
#   2. Reverse the call: `ip_addresses.split()` not `split.ip_addresses()`
#
# Additional note on the filter loop design:
#   This loop iterates over `remove_list` (not over `ip_addresses`)
#   and calls `ip_addresses.remove(element)` only when the element
#   is found. Because the loop variable and the list being modified
#   are different objects, the mutation-during-iteration bug from
#   Lab 11 does not apply here. This is a safer pattern than
#   iterating directly over the list being modified.

# Assign `import_file` to the name of the text file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses no longer allowed

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# With statement that reads in the text file

with open(import_file, "r") as file:       # FIX 1: added ':'
    ip_addresses = file.read()

# Convert `ip_addresses` from a string to a list

ip_addresses = ip_addresses.split()        # FIX 2: ip_addresses.split() not split.ip_addresses()

# For loop that iterates over remove_list and removes matches

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Display `ip_addresses` after the removal process

print(ip_addresses)

# Output (example — depends on allow_list.txt content):
# ['192.168.218.160', '192.168.145.158', '192.168.108.13', '192.168.60.153',
#  '192.168.96.200', '192.168.247.153', '192.168.3.252', '192.168.116.187',
#  '192.168.15.110', '192.168.39.246']

# Q6: Before any fix, a SyntaxError fires on the `with` line
# (missing colon). After adding the colon, an AttributeError
# fires on the `split.ip_addresses()` line — Python tries to
# look up a name called `split` and finds nothing. Fix: swap
# to `ip_addresses.split()`, calling the method on the string.


# ── TASK 7: logic errors — wrong list indices ─────────────────
#
# BUGS (original):
#   if   system == "OS 1": print(...patch_schedule[2])  ← wrong: gives May 1st
#   elif system == "OS 2": print(...patch_schedule[0])  ← wrong: gives March 1st
#   elif system == "OS 3": print(...patch_schedule[2])  ← accidentally correct for OS 3
#
# patch_schedule = ["March 1st", "April 1st", "May 1st"]
#                               ↑ index 0      ↑ index 1   ↑ index 2
#
# The correct mapping is:
#   OS 1 → patch_schedule[0]  ("March 1st")
#   OS 2 → patch_schedule[1]  ("April 1st")
#   OS 3 → patch_schedule[2]  ("May 1st")
#
# Logic errors do not raise exceptions — the code runs and
# produces output, but the output is wrong. The only way to
# detect them is to test with known inputs and verify outputs.
# Testing with system = "OS 1" and system = "OS 2" reveals the
# mismatch immediately.

# Assign `system` to a specific operating system as a string

system = "OS 2"

# Assign `patch_schedule` to a list of patch dates in order of OS

patch_schedule = ["March 1st", "April 1st", "May 1st"]

# Conditional statement — corrected indices

if system == "OS 1":
    print("Patch date:", patch_schedule[0])    # FIX: was [2], should be [0]

elif system == "OS 2":
    print("Patch date:", patch_schedule[1])    # FIX: was [0], should be [1]

elif system == "OS 3":
    print("Patch date:", patch_schedule[2])    # correct — [2] maps to May 1st

# Output (with system = "OS 2"):
# Patch date: April 1st

# Q7: Before the fix, the code runs without errors but displays
# wrong patch dates. With system = "OS 2" the original code
# prints "March 1st" (index 0) instead of "April 1st" (index 1).
# These are logic errors — the code is syntactically valid and
# raises no exceptions, but the index values are mismatched to
# the operating systems. Fix: align each branch's index to the
# OS number minus 1 (OS 1 → 0, OS 2 → 1, OS 3 → 2).

# Conclusion:
# This lab demonstrates the three distinct categories of Python
# errors and how to approach each one:
#   • Syntax errors  — caught by the Python parser before the
#     code runs; error messages point to the problem line.
#     Fixes: add missing punctuation (colon, parenthesis, quote,
#     comma) or use the correct operator (== vs =).
#   • Exceptions     — the code is syntactically valid but fails
#     at runtime when a specific condition is met. NameError
#     fires when a variable name doesn't match its definition;
#     IndexError fires when an index exceeds the list's length.
#   • Logic errors   — the code runs without exception but
#     produces incorrect output. Only detectable by testing with
#     known inputs and verifying results. Fix by tracing the
#     index-to-value mapping and correcting the values.
# Debugging one error at a time and re-running after each fix
# is the key strategy — fixing multiple errors simultaneously
# makes it harder to identify which change resolved which issue.
