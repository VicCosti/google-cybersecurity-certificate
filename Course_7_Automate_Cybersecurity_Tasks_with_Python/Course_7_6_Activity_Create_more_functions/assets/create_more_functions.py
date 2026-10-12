# ============================================================
# Lab: Create More Functions
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: sorted() — order a list of failed login attempts ─
# Assign `failed_login_list` to the list of failed login attempts per month
# (January through December, chronological order)

failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]

# Sort `failed_login_list` in ascending numerical order and display the result

print(sorted(failed_login_list))

# Output:
# [85, 88, 90, 91, 92, 99, 101, 105, 108, 119, 223, 264]

# Q1: When sorted in ascending order, the majority of monthly values cluster
# between 85 and 119. Two values — 223 and 264 — stand clearly apart from
# the rest, indicating a significant spike in failed login attempts during
# those two months (November and December). These outliers warrant further
# investigation as potential indicators of malicious activity.


# ── TASK 2: max() — isolate the highest failed login count ───
# Assign `failed_login_list` to the list of failed login attempts per month

failed_login_list = [119, 101, 99, 91, 92, 105, 108, 85, 88, 90, 264, 223]

# Determine the highest number of failed login attempts and display the result

print(max(failed_login_list))

# Output:
# 264

# Q2: The max() function returns 264, which corresponds to November — the month
# with the highest number of failed login attempts across the year. This value
# is more than twice the average of the remaining months, making November the
# primary month to investigate for potential unauthorized access attempts.


# ── TASK 3: Define analyze_logins() with two parameters ──────
# Define a function named `analyze_logins()` that takes in two parameters,
# `username` and `current_day_logins`

def analyze_logins(username, current_day_logins):

    # Display a message about how many login attempts the user has made that day

    print("Current day login total for", username, "is", current_day_logins)

# No output produced here — only the function definition is stored.
# The function must be called to produce output.


# ── TASK 4: Call analyze_logins() with two arguments ─────────
# Define a function named `analyze_logins()` that takes in two parameters,
# `username` and `current_day_logins`

def analyze_logins(username, current_day_logins):

    # Display a message about how many login attempts the user has made that day

    print("Current day login total for", username, "is", current_day_logins)

# Call `analyze_logins()` with "ejones" and 9

analyze_logins("ejones", 9)

# Output:
# Current day login total for ejones is 9

# Q3: The function displays one line substituting the argument values into the
# message template. Calling analyze_logins("ejones", 9) shows the login count
# for ejones specifically. The output would vary for different users: passing a
# different username and count (e.g., analyze_logins("tshah", 4)) would produce
# a different message reflecting that user's data. The function is reusable for
# any username/count pair without rewriting the print statement each time.


# ── TASK 5: Add a third parameter — average_day_logins ───────
# Define a function named `analyze_logins()` that takes in three parameters,
# `username`, `current_day_logins`, and `average_day_logins`

def analyze_logins(username, current_day_logins, average_day_logins):

    # Display a message about how many login attempts the user has made that day

    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made

    print("Average logins per day for", username, "is", average_day_logins)

# Call `analyze_logins()` with three arguments

analyze_logins("ejones", 9, 3)

# Output:
# Current day login total for ejones is 9
# Average logins per day for ejones is 3


# ── TASK 6: Calculate and display the login ratio ────────────
# Define a function named `analyze_logins()` that takes in three parameters,
# `username`, `current_day_logins`, and `average_day_logins`

def analyze_logins(username, current_day_logins, average_day_logins):

    # Display a message about how many login attempts the user has made that day

    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made

    print("Average logins per day for", username, "is", average_day_logins)

    # Calculate the ratio of current-day logins to average-day logins

    login_ratio = current_day_logins / average_day_logins

    # Display a message about the ratio

    print(username, "logged in", login_ratio, "times as much as they do on an average day.")

# Call `analyze_logins()`

analyze_logins("ejones", 9, 3)

# Output:
# Current day login total for ejones is 9
# Average logins per day for ejones is 3
# ejones logged in 3.0 times as much as they do on an average day.

# Q4: This version now displays three lines: the current-day login count, the
# average daily count, and the ratio between them. For ejones with 9 logins
# vs. an average of 3, the ratio is 3.0 — meaning they logged in three times
# more than usual. The output would vary for different users: a user with 6
# logins and an average of 2 would show a ratio of 3.0 as well, while a user
# with 4 logins and an average of 4 would show 1.0. Both the username and the
# computed values change with each function call.

# Note: if average_day_logins is 0, a ZeroDivisionError would occur.
# This scenario is excluded from the lab's scope (all users have logged in
# at least once), but in production code a guard clause would be added:
# if average_day_logins == 0: return None


# ── TASK 7: Add a return statement ───────────────────────────
# Define a function named `analyze_logins()` that takes in three parameters,
# `username`, `current_day_logins`, and `average_day_logins`

def analyze_logins(username, current_day_logins, average_day_logins):

    # Display a message about how many login attempts the user has made that day

    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made

    print("Average logins per day for", username, "is", average_day_logins)

    # Calculate the ratio of current-day logins to average-day logins

    login_ratio = current_day_logins / average_day_logins

    # Return the ratio so it can be used outside the function

    return login_ratio

# Call `analyze_logins()` and store the output in `login_analysis`

login_analysis = analyze_logins("ejones", 9, 3)

# Display a message about `login_analysis`

print("ejones", "logged in", login_analysis, "times as much as they do on an average day.")

# Output:
# Current day login total for ejones is 9
# Average logins per day for ejones is 3
# ejones logged in 3.0 times as much as they do on an average day.

# Q5: The key difference in this version is the return statement. In Task 6,
# login_ratio was computed and printed inside the function body but discarded
# when the function ended — it was inaccessible outside the function. Here,
# `return login_ratio` sends the value back to the caller, where it is stored
# in login_analysis. This makes the ratio available for further logic (such as
# a conditional check) anywhere in the program after the function call. The
# print statement inside the function still runs as before, so the output is
# identical — but the function is now significantly more composable and reusable.


# ── TASK 8: Use login_analysis in a conditional statement ────
# Define a function named `analyze_logins()` that takes in three parameters,
# `username`, `current_day_logins`, and `average_day_logins`

def analyze_logins(username, current_day_logins, average_day_logins):

    # Display a message about how many login attempts the user has made that day

    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made

    print("Average logins per day for", username, "is", average_day_logins)

    # Calculate the ratio of current-day logins to average-day logins

    login_ratio = current_day_logins / average_day_logins

    # Return the ratio

    return login_ratio

# Call `analyze_logins()` and store the output in `login_analysis`

login_analysis = analyze_logins("ejones", 9, 3)

# Conditional statement: alert if login activity is 3x or more than normal

if login_analysis >= 3:
    print("Alert! This account has more login activity than normal.")

# Output:
# Current day login total for ejones is 9
# Average logins per day for ejones is 3
# Alert! This account has more login activity than normal.

# ejones logged in 3.0 times their daily average, which satisfies the >= 3
# threshold, so the alert fires. This pattern — function returns a value,
# caller stores it, conditional acts on it — is the foundation of modular
# security automation: each piece (data collection, computation, decision)
# is separated into its own layer and can be updated independently.
