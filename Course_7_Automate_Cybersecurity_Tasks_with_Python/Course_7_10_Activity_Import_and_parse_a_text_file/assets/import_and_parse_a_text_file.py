# ============================================================
# Lab: Import and Parse a Text File
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: with statement — open a file for reading ─────────
# Assign `import_file` to the name of the text file that contains the security log file

import_file = "login.txt"

# First line of the `with` statement
# Use `open()` to import security log file and store it as a string
# `open(import_file, "r")` opens the file in read-only mode
# The `with` keyword ensures the file is automatically closed after the block exits,
# even if an error occurs — no need to call file.close() manually

with open(import_file, "r") as file:
    pass  # Body left empty intentionally — Task 1 only asks for the opening line

# Note: Running this cell as-is produces a syntax/indentation error in the original
# notebook because the `with` block has no body yet. The `pass` statement above
# is used here as a valid placeholder to represent that incomplete state.


# ── TASK 2: .read() — read the file into a string ────────────
# Assign `import_file` to the name of the text file that contains the security log file

import_file = "login.txt"

# The `with` statement
# Use `open()` to import security log file and store it as a string

with open(import_file, "r") as file:

    # Use `.read()` to read the imported file and store the result in a variable named `text`
    # `.read()` reads the entire file content as a single string, including newlines

    text = file.read()

# Display the contents of `text`
# At this point `text` is one continuous string with \n characters separating each log line

print(text)

# Output (first few lines shown):
# username,ip_address,time,date
# tshah,192.168.92.147,15:26:08,2022-05-10
# dtanaka,192.168.98.221,9:45:18,2022-05-09
# tmitchel,192.168.110.131,14:13:41,2022-05-11
# ... (20 entries total)

# Q1 answer: Before .split(), `text` is a single string containing the entire file
# content, with newlines (\n) embedded between each log line. After applying .split()
# in Task 3, the result becomes a Python list where each whitespace-separated token
# (field) is its own element. The raw string preserves the line structure visually
# when printed, while the list makes individual fields programmatically accessible.


# ── TASK 3: .split() — convert string to list ────────────────
# Assign `import_file` to the name of the text file that contains the security log file

import_file = "login.txt"

# The `with` statement
# Use `open()` to import security log file and store it as a string

with open(import_file, "r") as file:

    # Use `.read()` to read the imported file and store the result in a variable named `text`

    text = file.read()

# Display the contents of `text` split into separate lines
# `.split()` with no argument splits on any whitespace: spaces, tabs, and newlines
# This means each comma-separated field becomes a separate list element —
# e.g., "tshah", "192.168.92.147", "15:26:08", "2022-05-10" are four separate items
# rather than one complete log-line string

print(text.split())

# Output (partial):
# ['username,ip_address,time,date', 'tshah,192.168.92.147,15:26:08,2022-05-10',
#  'dtanaka,192.168.98.221,9:45:18,2022-05-09', ...]

# Note: Because each log entry is a single comma-separated string with no spaces,
# splitting on whitespace (the default) keeps each full log line together as one
# list element. If the fields were space-separated, the default split would break
# each entry into multiple elements. Using text.split("\n") would also work here
# and would more explicitly split only on newlines, producing the same result
# for this particular log format.

# Note on reassignment: `.split()` returns a new list but does NOT modify `text`.
# `text` still holds the original string. To persist the split result, you would
# need to reassign: text = text.split()


# ── TASK 4: "a" mode — append a missing log entry ────────────
# Assign `import_file` to the name of the text file that contains the security log file

import_file = "login.txt"

# Assign `missing_entry` to a log that was not recorded in the log file

missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

# Use `open()` to import security log file and store it as a string
# Pass in "a" as the second parameter to indicate that the file is being opened for appending purposes
# "a" mode: opens the file and positions the write cursor at the END of the file
# New content is added after all existing content; existing content is never overwritten
# Compare to "w" mode, which truncates the file and overwrites everything from the start

with open(import_file, "a") as file:

    # Use `.write()` to append `missing_entry` to the log file

    file.write(missing_entry)

# Use `open()` with the parameter "r" to open the security log file for reading purposes

with open(import_file, "r") as file:

    # Use `.read()` to read in the contents of the log file and store in a variable named `text`

    text = file.read()

# Display the contents of `text`

print(text)

# Output (last two lines shown):
# jsoto,192.168.25.60,5:09:21,2022-05-09
# jrafael,192.168.243.140,4:56:27,2022-05-09

# Q2 answer: The new entry is appended at the very end of the file — after all
# existing log lines. Because `missing_entry` does not begin with a newline
# character, it is joined directly to the last character of the existing file
# content with no line break. In practice this means the last original entry
# (jsoto) and the appended entry (jrafael) appear on the same line in the output.
# To avoid this, the write call could be changed to:
#   file.write("\n" + missing_entry)
# which would insert a newline before the new entry, placing it on its own line.


# ── TASK 5: variable assignment — define file name and IP list ─
# Assign `import_file` to the name of the text file that you want to create

import_file = "allow_list.txt"

# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
# Note: despite the variable name suggesting a list, ip_addresses is actually a string —
# the IP addresses are space-separated values stored as a single string

ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

# Display `import_file`

print(import_file)

# Display `ip_addresses`

print(ip_addresses)

# Output:
# allow_list.txt
# 192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153
# 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246


# ── TASK 6: "w" mode — create a file and write to it ─────────
# Assign `import_file` to the name of the text file that you want to create

import_file = "allow_list.txt"

# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information

ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

# Create a `with` statement to write to the text file
# "w" mode: creates the file if it does not exist, or truncates (empties) it if it does
# This is the correct mode here because we want a fresh file containing exactly the IP list

with open(import_file, "w") as file:

    # Write `ip_addresses` to the text file
    # `.write()` takes a string argument and writes it to the file
    # No output is produced to the screen by this block

    file.write(ip_addresses)

# Note: this cell produces no printed output — the only effect is creating/overwriting
# the file on disk. The next task reads it back to confirm the write worked correctly.


# ── TASK 7: "r" mode — read back the written file ────────────
# Assign `import_file` to the name of the text file that you want to create

import_file = "allow_list.txt"

# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information

ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

# Create a `with` statement to write to the text file

with open(import_file, "w") as file:

    # Write `ip_addresses` to the text file

    file.write(ip_addresses)

# Create a `with` statement to read in the text file
# Opening the same file immediately after writing confirms the content was persisted correctly

with open(import_file, "r") as file:

    # Read the file and store the result in a variable named `text`

    text = file.read()

# Display the contents of `text`

print(text)

# Output:
# 192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153
# 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246

# The write → read pattern (Tasks 6–7) is a standard verification workflow:
# write the data, then immediately read it back to confirm what was stored on disk
# matches what was intended. This pattern is useful any time file I/O is involved
# in a security workflow — for example, confirming that an updated allow list was
# saved correctly before using it to gate access decisions.
