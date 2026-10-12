# ============================================================
# Lab: Work with Strings in Python
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: str() — convert an integer employee ID to a string ─
# Assign `employee_id` to a four-digit number as an initial value

employee_id = 4186

# Display the data type of `employee_id` before conversion

print(type(employee_id))

# Reassign `employee_id` to the same value but in the form of a string

employee_id = str(employee_id)

# Display the data type of `employee_id` after conversion

print(type(employee_id))

# Output:
# <class 'int'>
# <class 'str'>

# Q1: The first print(type(employee_id)) returns <class 'int'> because the
# initial assignment stores 4186 as an integer — a numeric type that supports
# arithmetic but has no concept of length or character positions. After
# employee_id = str(employee_id), the second print returns <class 'str'>,
# confirming that the value is now a string. The numeric value 4186 and the
# string "4186" look the same when printed, but their types differ: the integer
# supports math operations while the string supports len(), slicing, and
# concatenation — all of which are needed in the tasks that follow.


# ── TASK 2: len() + if — check ID length requirement ─────────
# Assign `employee_id` to a four-digit number as an initial value

employee_id = 4186

# Reassign `employee_id` to the same value in string form

employee_id = str(employee_id)

# Conditional statement: display a message if length is less than 5

if len(employee_id) < 5:
    print("This employee ID has less than five digits. It does not meet length requirements.")

# Output:
# This employee ID has less than five digits. It does not meet length requirements.

# "4186" has 4 characters, so len(employee_id) == 4, which is less than 5,
# and the message is displayed.


# ── TASK 3: Concatenation — prepend "E" to a short ID ────────
# Assign `employee_id` to a four-digit number as an initial value

employee_id = 4186

# Reassign `employee_id` to the same value in string form

employee_id = str(employee_id)

# Display the employee ID as it currently stands

print(employee_id)

# Conditional statement: if length < 5, prepend "E" to standardize the ID

if len(employee_id) < 5:
    employee_id = ("E" + employee_id)

# Display the updated employee ID

print(employee_id)

# Output:
# 4186
# E4186

# Note: the parentheses around ("E" + employee_id) are not required —
# Python evaluates the concatenation correctly without them — but they are
# harmless and do not affect the result.


# ── TASK 4: Indexing — extract the fourth character ──────────
# Assign `device_id` to a string containing alphanumeric characters

device_id = "r262c36"

# Extract the fourth character in `device_id` and display it
# Python uses zero-based indexing: index 0 → 'r', 1 → '2', 2 → '6', 3 → '2'

print(device_id[3])

# Output:
# 2

# device_id[3] accesses the character at index 3, which is the fourth character
# (counting from 1). Because indexing starts at 0, the fourth position maps to
# index 3.


# ── TASK 5: Slicing — extract the first three characters ─────
# Assign `device_id` to a string containing alphanumeric characters

device_id = "r262c36"

# Extract the first through the third characters in `device_id` and display it

print(device_id[0:3])

# Output:
# r26

# device_id[0:3] slices from index 0 (inclusive) up to index 3 (exclusive),
# returning the characters at positions 0, 1, and 2: 'r', '2', '6'.
# The upper bound is always excluded in Python slice notation.


# ── TASK 6: URL slicing — extract protocol and domain ────────
# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Extract the protocol and the syntax following it, and display the result
# The lab asked for a single slice url[0:8] to extract "https://" as one unit.
# Here, the components are separated for clarity:

print("Protocol is:", url[0:5])          # extracts "https" (indices 0–4)
print("the syntax following it is:", url[8:23])  # extracts "exampleURL1.com" (indices 8–22)

# Output:
# Protocol is: https
# the syntax following it is: exampleURL1.com

# Note: the expected answer was print(url[0:8]), which outputs "https://" as a
# single slice. The approach above goes beyond the task by splitting the URL
# into its two constituent parts separately, which demonstrates a clear
# understanding of the URL structure — but url[0:8] would have been the
# minimal correct answer. The hardcoded upper bound (23) also makes this
# version brittle: it would break for URLs of different lengths, whereas
# url[0:8] extracts a fixed-length prefix regardless of what follows.


# ── TASK 7: .index() — find the position of ".com" ───────────
# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Display the index where the domain extension ".com" is located in `url`

print(url.index(".com"))

# Output:
# 19

# url.index(".com") searches the string left-to-right and returns the index
# of the first character of the first match. ".com" starts at index 19 in
# "https://exampleURL1.com" (h=0, t=1, t=2, p=3, s=4, :=5, /=6, /=7,
# e=8 ... 1=18, .=19).


# ── TASK 8: Store .index() result in a variable ───────────────
# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Assign `ind` to the starting index of ".com" in `url`

ind = url.index(".com")

# No output — this cell only stores the result for use in later tasks.
# ind == 19


# ── TASK 9: Slice the domain extension using ind ─────────────
# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Assign `ind` to the starting index of ".com" in `url`

ind = url.index(".com")

# Extract the domain extension and display it

print(url[ind:ind + 4])

# Output:
# .com

# Q2: The output is ".com". url.index(".com") returns 19, the index where
# ".com" begins. The slice url[ind:ind+4] starts at index 19 (inclusive) and
# ends at index 23 (exclusive), capturing exactly four characters: '.', 'c',
# 'o', 'm'. Expressing the end index as ind+4 rather than a hardcoded 23 is
# the preferred approach because it stays correct regardless of where ".com"
# appears in the URL — only the length of ".com" (always 4) needs to be known.


# ── TASK 10: Slice the website name using ind ────────────────
# Assign `url` to a specific URL

url = "https://exampleURL1.com"

# Assign `ind` to the starting index of ".com" in `url`

ind = url.index(".com")

# Extract the website name and display it

print(url[ind - 11:ind])

# Output:
# exampleURL1

# url[ind-11:ind] slices from index 8 (19 - 11) up to index 19 (exclusive),
# extracting the 11-character website name "exampleURL1".
#
# Note: the lab hint recommended url[8:ind] as the standard solution. That
# approach is more robust because it uses a fixed start index (8, the known
# position after "https://") and does not depend on knowing the website name's
# length. url[ind-11:ind] produces the correct result here but would break for
# any URL where the website name is not exactly 11 characters long. In
# production code, url[8:ind] is the preferred pattern.
