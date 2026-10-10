# ============================================================
# Lab: Assign Python Variables
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: Assign device_id and display it ─────────────────
# Assign the `device_id` variable to the device ID that only specified users can access
device_id = "72e08x0"

# Display `device_id`
print(device_id)
# Output: 72e08x0


# ── TASK 2: Find the data type of device_id ─────────────────
# Assign the `device_id` variable to the device ID that only specified users can access
device_id = "72e08x0"

# Assign `device_id_type` to the data type of `device_id`
device_id_type = type(device_id)

# Display `device_id_type`
print(device_id_type)
# Output: <class 'str'>

# Q1: device_id is of type str (string) — text data enclosed in quotation marks.


# ── TASK 3: Create a list of approved usernames ──────────────
# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Display `username_list`
print(username_list)
# Output: ['madebowa', 'jnguyen', 'tbecker', 'nhersh', 'redwards']


# ── TASK 4: Find the data type of username_list ──────────────
# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Assign `username_list_type` to the data type of `username_list`
username_list_type = type(username_list)

# Display `username_list_type`
print(username_list_type)
# Output: <class 'list'>

# Q2: username_list is of type list — an ordered, mutable collection of values.


# ── TASK 5: Update the username list with a new employee ─────
# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Display `username_list`
print(username_list)
# Output: ['madebowa', 'jnguyen', 'tbecker', 'nhersh', 'redwards']

# Assign `username_list` to the updated list of usernames who are allowed to access the device
# Note: a new variable was used here to preserve the original list for comparison
updated_username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards", "lpope"]

# Display updated list
print(updated_username_list)
# Output: ['madebowa', 'jnguyen', 'tbecker', 'nhersh', 'redwards', 'lpope']

# Q3: The updated list contains all original usernames plus the new entry "lpope".


# ── TASK 6: Assign max_logins and find its data type ─────────
# Assign `max_logins` to the value 3
max_logins = 3

# Assign `max_logins_type` to the data type of `max_logins`
max_logins_type = type(max_logins)

# Display `max_logins_type`
print(max_logins_type)
# Output: <class 'int'>

# Q4: max_logins is of type int (integer) — a whole number with no decimal point.


# ── TASK 7: Assign login_attempts and find its data type ─────
# Assign `login_attempts` to the value 2
login_attempts = 2

# Assign `login_attempts_type` to the data type of `login_attempts`
login_attempts_type = type(login_attempts)

# Display `login_attempts_type`
print(login_attempts_type)
# Output: <class 'int'>

# Q5: login_attempts is of type int — same as max_logins, both represent whole number counts.


# ── TASK 8: Boolean comparison — is login within limit? ──────
# Assign `max_logins` to the value 3
max_logins = 3

# Assign `login_attempts` to the value 2
login_attempts = 2

# Determine whether the current number of login attempts a user has made is less than
# or equal to the maximum number of login attempts allowed
print(login_attempts <= max_logins)
# Output: True

# Q6: The expression evaluates to True — 2 is less than or equal to 3,
# meaning the user is still within the permitted login threshold.


# ── TASK 9: Reassign login_attempts to exceed the maximum ────
# Assign `max_logins` to the value 3
max_logins = 3

# Assign `login_attempts` to a value that exceeds the allowed maximum
login_attempts = 5

# Determine whether the current number of login attempts a user has made is less than
# or equal to the maximum number of login attempts allowed
print(login_attempts <= max_logins)
# Output: False

# Q7: The expression evaluates to False — 5 is not less than or equal to 3,
# indicating the user has exceeded the maximum allowed login attempts.


# ── TASK 10: Assign a Boolean value to login_status ──────────
# Assign `login_status` to the Boolean value False
login_status = False

# Assign `login_status_type` to the data type of `login_status`
login_status_type = type(login_status)

# Display `login_status_type`
print(login_status_type)
# Output: <class 'bool'>

# Q8: login_status is of type bool (Boolean) — a binary value that is either True or False.
# Boolean variables are often used to represent on/off states, such as whether a user is logged in.
