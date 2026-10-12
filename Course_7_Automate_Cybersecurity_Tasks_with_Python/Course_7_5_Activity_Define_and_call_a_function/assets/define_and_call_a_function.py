# ============================================================
# Lab: Define and Call a Function
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: Analyze a function definition ────────────────────
# The function below is defined but not called.
# Running this cell produces no output — only the definition is stored.

def alert():
    print("Potential security issue. Investigate further.")

# The `def` keyword introduces a function definition.
# `alert` is the function name; the empty parentheses indicate no parameters.
# The body contains a single built-in `print()` call.
# When `alert()` is called, Python executes the body and displays the message.

# Q1: The function body contains a call to the built-in print() function that
# displays a fixed alert message. Defining the function does not execute it —
# calling alert() is what triggers the print statement and produces output.


# ── TASK 2: Call alert() and observe output ───────────────────

def alert():
    print("Potential security issue. Investigate further.")

# Call the `alert()` function

alert()

# Output:
# Potential security issue. Investigate further.

# Q2: Placing this code inside a function allows it to be reused anywhere in a
# program by simply writing alert() — a single function call replaces repeating
# the entire print statement wherever it is needed. This follows the DRY
# (Don't Repeat Yourself) principle: if the message ever changes, only the
# function body needs to be updated rather than every place the code appears.
# It also makes the code self-documenting: alert() immediately signals intent.


# ── TASK 3: alert() with a for loop inside the body ──────────

def alert():
    for i in range(3):
        print("Potential security issue. Investigate further.")

# Call the `alert()` function

alert()

# Output:
# Potential security issue. Investigate further.
# Potential security issue. Investigate further.
# Potential security issue. Investigate further.

# Q3: The new version adds a for loop inside the function body that iterates
# range(3), printing the alert message once per iteration — three times total.
# The previous version printed the message exactly once. Both functions are
# called with the identical syntax alert(), but the internal logic differs:
# the first body is a single statement; the second wraps it in a loop.
# From the caller's perspective nothing changes — the added repetition is
# entirely encapsulated inside the function.


# ── TASK 4: Write the function header for list_to_string() ───
# Only the header is written here; the body will be added in Task 5.
# Running this cell alone would raise an IndentationError / SyntaxError
# because the body is missing — this is expected at this stage.

def list_to_string():
    pass  # placeholder — body defined in Tasks 5–7


# ── TASK 5: Add a for loop body to list_to_string() ──────────

def list_to_string():

    # Store the list of approved usernames
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore",
                     "eraab", "gesparza", "alevitsk", "wjaffrey"]

    # Iterate through the list and print each username
    for i in username_list:
        print(i)

# Call the function
list_to_string()

# Output:
# elarson
# bmoreno
# tshah
# sgilmore
# eraab
# gesparza
# alevitsk
# wjaffrey

# Q4: Calling list_to_string() executes the entire function body in one step —
# the loop iterates over all eight usernames and displays each on its own line.
# Without a function, the same loop would have to be written out every time
# the list needs to be printed; with the function, a single call handles it.


# ── TASK 6: String concatenation accumulator ─────────────────

def list_to_string():

    username_list = ["elarson", "bmoreno", "tshah", "sgilmore",
                     "eraab", "gesparza", "alevitsk", "wjaffrey"]

    # Initialize an empty string to accumulate usernames
    sum_variable = ""

    # Concatenate each username onto sum_variable
    for i in username_list:
        sum_variable = sum_variable + i

    # Display the final concatenated string
    print(sum_variable)

list_to_string()

# Output:
# elarsonbmorenotshahsgilmoreeraabgesparzaalevitskwjaffrey

# Q5: The output is a single unbroken string containing all eight usernames
# merged together with no spaces or separators between them. Each iteration of
# the loop appends the current username directly to sum_variable, so the
# boundaries between names are invisible in the final result. While the data
# is now in string form — which makes it easy to write to a file or pass to
# another function — it is not human-readable in this state.


# ── TASK 7: Add ", " separator for readability ───────────────

def list_to_string():

    username_list = ["elarson", "bmoreno", "tshah", "sgilmore",
                     "eraab", "gesparza", "alevitsk", "wjaffrey"]

    sum_variable = ""

    # Concatenate each username followed by a comma and space
    for i in username_list:
        sum_variable = sum_variable + i + ", "

    print(sum_variable)

list_to_string()

# Output:
# elarson, bmoreno, tshah, sgilmore, eraab, gesparza, alevitsk, wjaffrey,

# Q6: Each username is now clearly separated by ", ", making the output easy
# to read and distinguish at a glance. One side effect is a trailing ", " at
# the very end of the string — after the last username "wjaffrey" — because
# the separator is appended unconditionally on every iteration, including the
# last one. In a production script this trailing separator would typically be
# removed with Python's str.rstrip(", ") or by using ", ".join(username_list),
# but the current implementation correctly demonstrates the concatenation
# pattern the lab is teaching.
