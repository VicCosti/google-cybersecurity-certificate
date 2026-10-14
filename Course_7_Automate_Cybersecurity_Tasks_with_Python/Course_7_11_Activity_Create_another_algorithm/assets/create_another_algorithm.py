# ============================================================
# Lab: Create Another Algorithm
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: explore the inputs — file name and remove list ───
# Assign `import_file` to the name of the file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed
# to access restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Display `import_file`

print(import_file)

# Display `remove_list`

print(remove_list)

# Output:
# allow_list.txt
# ['192.168.97.225', '192.168.158.170', '192.168.201.40', '192.168.58.57']

# Q1: The output shows two pieces of data. `import_file` is a string containing
# the name of the text file that holds the current allow list. `remove_list` is
# a Python list of four IP address strings — these are the addresses that have
# had their access revoked and need to be removed from the file. At this stage
# neither variable has been connected to the file on disk; the file-reading
# happens in the next task. The separation between the file name (a string)
# and the removal targets (a list) reflects the two inputs the algorithm will
# need: where to find the data, and what to remove from it.


# ── TASK 2: with statement — open the file for reading ───────
# Assign `import_file` to the name of the file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed
# to access restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# First line of `with` statement
# open(import_file, "r") opens the file in read-only mode
# The `with` keyword ensures the file is automatically closed when the block exits

with open(import_file, "r") as file:
    pass  # Body left empty intentionally — Task 2 only asks for the opening line

# Note: Running the incomplete `with` block in the original notebook raises a
# SyntaxError because the block has no body. The `pass` statement here is a
# valid placeholder that represents that intentionally incomplete state.


# ── TASK 3: .read() — read file content into a string ────────
# Assign `import_file` to the name of the file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed
# to access restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file

with open(import_file, "r") as file:

    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
    # `.read()` returns the entire file content as one string, with newlines between entries

    ip_addresses = file.read()

# Display `ip_addresses`
# At this point ip_addresses is a single string — all IP addresses joined by whitespace

print(ip_addresses)

# Output (example — actual content depends on allow_list.txt state):
# 192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153
# 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110
# 192.168.39.246

# Q2: Yes — `192.168.97.225` appears in both the allow list and the `remove_list`.
# It is the first element in `remove_list` and is also present in the file content
# displayed above. This confirms that the algorithm will need to find and remove it
# (along with any other `remove_list` entries that appear in the file) before
# writing the updated list back to disk.


# ── TASK 4: .split() — convert string to list ────────────────
# Assign `import_file` to the name of the file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed
# to access restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file

with open(import_file, "r") as file:

    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`

    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list
# `.split()` with no argument splits on any whitespace (spaces and newlines)
# Each IP address becomes its own element in the resulting list
# The result is reassigned back to `ip_addresses`, replacing the string with a list

ip_addresses = ip_addresses.split()

# Display `ip_addresses`

print(ip_addresses)

# Output:
# ['192.168.218.160', '192.168.97.225', '192.168.145.158', '192.168.108.13',
#  '192.168.60.153', '192.168.96.200', '192.168.247.153', '192.168.3.252',
#  '192.168.116.187', '192.168.15.110', '192.168.39.246']

# Note: reassignment (`ip_addresses = ip_addresses.split()`) is required here
# because `.split()` returns a new list — it does not modify the original string.
# After this line, `ip_addresses` is a list, not a string.


# ── TASK 5: for loop — iterate and display each element ──────
# Assign `import_file` to the name of the file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed
# to access restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file

with open(import_file, "r") as file:

    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`

    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list

ip_addresses = ip_addresses.split()

# Build iterative statement
# Name loop variable `element`
# Loop through `ip_addresses`

for element in ip_addresses:

    # Display `element` in every iteration

    print(element)

# Output:
# 192.168.218.160
# 192.168.97.225
# 192.168.145.158
# 192.168.108.13
# 192.168.60.153
# 192.168.96.200
# 192.168.247.153
# 192.168.3.252
# 192.168.116.187
# 192.168.15.110
# 192.168.39.246

# This task establishes the loop structure that will carry the conditional
# check in the next task — each `element` is one IP address string, ready
# to be compared against `remove_list`.


# ── TASK 6: conditional — remove flagged IPs from the list ───
# Assign `import_file` to the name of the file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed
# to access restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file

with open(import_file, "r") as file:

    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`

    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list

ip_addresses = ip_addresses.split()

# Build iterative statement
# Name loop variable `element`
# Loop through `ip_addresses`

for element in ip_addresses:

    # Build conditional statement
    # If current element is in `remove_list`,

    if element in remove_list:

        # then current element should be removed from `ip_addresses`

        ip_addresses.remove(element)

# Display `ip_addresses`

print(ip_addresses)

# Output:
# ['192.168.218.160', '192.168.145.158', '192.168.108.13', '192.168.60.153',
#  '192.168.96.200', '192.168.247.153', '192.168.3.252', '192.168.116.187',
#  '192.168.15.110', '192.168.39.246']

# IMPORTANT — known limitation of this pattern (mutating a list while iterating):
# Calling `.remove()` on `ip_addresses` inside a `for element in ip_addresses` loop
# modifies the list that the loop is currently iterating over. When an element is
# removed, the remaining elements shift left by one position, but the loop's
# internal index advances by one regardless. This means the element immediately
# after any removed element is silently skipped.
#
# In this specific lab the bug does not surface: `remove_list` contains only one
# address that is present in the allow list (`192.168.97.225`), and no two
# consecutive allow-list entries are both flagged. But if two back-to-back entries
# were both in `remove_list`, the second one would survive.
#
# The safer pattern is to iterate over a shallow copy of the list:
#   for element in ip_addresses[:]:   # ip_addresses[:] creates a copy
#       if element in remove_list:
#           ip_addresses.remove(element)
#
# Or use a list comprehension to build a clean filtered list:
#   ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]
#
# Both alternatives correctly remove every flagged address regardless of position.


# ── TASK 7: "w" mode — write the updated list back to file ───
# Assign `import_file` to the name of the file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addresses that are no longer allowed
# to access restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file

with open(import_file, "r") as file:

    # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`

    ip_addresses = file.read()

# Use `.split()` to convert `ip_addresses` from a string to a list

ip_addresses = ip_addresses.split()

# Build iterative statement
# Name loop variable `element`
# Loop through `ip_addresses`

for element in ip_addresses:

    # Build conditional statement
    # If current element is in `remove_list`,

    if element in remove_list:

        # then current element should be removed from `ip_addresses`

        ip_addresses.remove(element)

# Convert `ip_addresses` back to a string so that it can be written into the text file
# `.write()` requires a string argument — a list cannot be written directly
# `" ".join(ip_addresses)` concatenates all list elements separated by a single space

ip_addresses = " ".join(ip_addresses)

# Build `with` statement to rewrite the original file
# "w" mode truncates the existing file and replaces its entire content

with open(import_file, "w") as file:

    # Rewrite the file, replacing its contents with `ip_addresses`

    file.write(ip_addresses)

# Note: this cell produces no printed output — the only effect is overwriting
# the file on disk with the filtered IP address string.


# ── TASK 8: verify — read the updated file ───────────────────
# (full pipeline repeated so this cell is self-contained)

import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
    ip_addresses = file.read()

ip_addresses = ip_addresses.split()

for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)

ip_addresses = " ".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)

# Build `with` statement to read in the updated file
# Opening the same file immediately after writing confirms the content on disk
# matches what was computed in memory

with open(import_file, "r") as file:

    # Read in the updated file and store the contents in `text`

    text = file.read()

# Display the contents of `text`

print(text)

# Output (space-separated, all on one line after .join()):
# 192.168.218.160 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200
# 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246


# ── TASK 9: encapsulate — define update_file() function ──────
# Define a function named `update_file` that takes in two parameters:
# `import_file` and `remove_list`
# and combines the steps written in this lab leading up to this

def update_file(import_file, remove_list):

    # Build `with` statement to read in the initial contents of the file

    with open(import_file, "r") as file:

        # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`

        ip_addresses = file.read()

    # Use `.split()` to convert `ip_addresses` from a string to a list

    ip_addresses = ip_addresses.split()

    # Build iterative statement
    # Name loop variable `element`
    # Loop through `ip_addresses`

    for element in ip_addresses:

        # Build conditional statement
        # If current element is in `remove_list`,

        if element in remove_list:

            # then current element should be removed from `ip_addresses`

            ip_addresses.remove(element)

    # Convert `ip_addresses` back to a string so that it can be written into the text file

    ip_addresses = " ".join(ip_addresses)

    # Build `with` statement to rewrite the original file

    with open(import_file, "w") as file:

        # Rewrite the file, replacing its contents with `ip_addresses`

        file.write(ip_addresses)

# Note: defining a function produces no output — the body is stored but not executed
# until the function is called. The function is called in the next task.

# Q3: Encapsulating the algorithm in a single function provides several benefits.
# First, it eliminates repetition: instead of rewriting the same sequence of
# open → read → split → loop → join → write steps every time a file needs to be
# updated, the logic is written once and reused by calling the function with
# different arguments. Second, it makes the code easier to maintain — if the
# removal logic needs to change (for example, to use the safer iteration-over-copy
# pattern), only one place needs to be updated rather than every copy of the code.
# Third, it makes the intent clear at the call site: `update_file("allow_list.txt",
# remove_list)` reads as a single, self-describing action rather than a block of
# file-handling mechanics. Fourth, the function accepts any file name and any
# remove list as arguments, so it can be applied to different allow-list files
# or different sets of revoked addresses without modification.


# ── TASK 10: call update_file() with a new remove list ───────
# Define `update_file` (repeated so this cell is self-contained)

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

# Call `update_file()` and pass in "allow_list.txt" and a new list of IP addresses
# to be removed — different from the remove_list used in Tasks 6–8
# This demonstrates that the function is reusable with any set of arguments

update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

# Build `with` statement to read in the updated file

with open("allow_list.txt", "r") as file:

    # Read in the updated file and store the contents in `text`

    text = file.read()

# Display the contents of `text`

print(text)

# Output: the allow list after removing 192.168.25.60, 192.168.140.81,
# and 192.168.203.198. Since none of those three addresses appear in the
# allow_list.txt content from previous tasks, the list is unchanged from
# Task 8's output — confirming the function ran without error and that
# those addresses were not present to begin with.

# Conclusion:
# This lab demonstrates a complete file-update pipeline built from first principles.
# The full algorithm reads a text file into a string, converts the string to a list
# for iteration, removes flagged entries using a for loop and .remove(), converts the
# filtered list back to a string with .join(), and overwrites the original file with
# the updated content. Encapsulating this pipeline in update_file() shows how
# reusable functions make security automation cleaner and easier to maintain.
# One important edge case to be aware of: modifying a list while iterating over it
# can cause elements to be skipped. The lab's data avoids triggering this bug, but
# production code should iterate over a copy (ip_addresses[:]) or use a list
# comprehension to filter safely.
