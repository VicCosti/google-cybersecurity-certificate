# ============================================================
# Lab: Create a Conditional Statement
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: if statement — check if OS is up to date ────────
# Assign a variable named `system` to a specific operating system, represented as a string
# This variable indicates which operating system is running

system = "OS 2"

# If OS 2 is running, then display a "no update needed" message

if (system == "OS 2"):
    print("no update needed")
else:
    print("update is needed")

# Output (system = "OS 2"): no update needed
# Output (system = "OS 1"): update is needed


# ── TASK 2: Observe if-only behavior with different OS values ─
# Assign `system` to a specific operating system

system = "OS 1"

# If OS 2 is running, then display a "no update needed" message

if system == "OS 2":
    print("no update needed")

# Output (system = "OS 2"): no update needed
# Output (system = "OS 1"): [no output — condition evaluates to False]

# Q1: When OS 2 is running, the condition evaluates to True and "no update needed" is printed.
# When OS 1 is running, the condition evaluates to False and nothing is displayed,
# because there is no else branch to handle the non-matching case.


# ── TASK 3: if/else — handle both OS 2 and all other systems ─
# Assign `system` to a specific operating system

system = "OS 3"

# If OS 2 is running, then display a "no update needed" message
# Otherwise, display a "update needed" message

if system == "OS 2":
    print("no update needed")
else:
    print("update needed")

# Output (system = "OS 2"): no update needed
# Output (system = "OS 3"): update needed

# Q2: When OS 2 is running, the if branch executes and prints "no update needed".
# When any other system is running, the else branch executes and prints "update needed".


# ── TASK 4: if/elif/elif — handle each OS explicitly ─────────
# Assign `system` to a specific operating system

system = "OS 3"

# If OS 2 is running, then display a "no update needed" message
# Otherwise if OS 1 is running, display a "update needed" message
# Otherwise if OS 3 is running, display a "update needed" message
# Note: an else branch was added to handle unrecognized input — a deliberate improvement

if system == "OS 2":
    print("no update needed")
elif system == "OS 1":
    print("update needed")
elif system == "OS 3":
    print("update needed")
else:
    print("unknown input")

# Output (system = "OS 2"): no update needed
# Output (system = "OS 1"): update needed
# Output (system = "OS 3"): update needed
# Output (system = "OS 4"): unknown input

# Q3: OS 2 → "no update needed"; OS 1 → "update needed"; OS 3 → "update needed";
# any other value → "unknown input" (no branch matches, else handles the fallback).


# ── TASK 5: Combine elif branches with or operator ───────────
# Assign `system` to a specific operating system

system = "OS 1"

# If OS 2 is running, then display a "no update needed" message
# Otherwise if either OS 1 or OS 3 is running, display a "update needed" message

if system == "OS 2":
    print("no update needed")
elif (system == "OS 1" or system == "OS 3"):
    print("update needed")

# Output (system = "OS 1"): update needed
# Output (system = "OS 2"): no update needed

# Q4: The two separate elif branches from Task 4 are merged into one using the `or` operator.
# This produces the same behavior with less code — more concise and easier to maintain.


# ── TASK 6: Check login against two approved users ───────────
# Assign `approved_user1` and `approved_user2` to usernames of approved users

approved_user1 = "elarson"
approved_user2 = "bmoreno"

# Assign `username` to the username of a specific user trying to log in

username = "bmoreno"

# If the user trying to log in is among the approved users, then display a message
# that they are approved to access this device
# Otherwise, display a message that they do not have access to this device

if (username == approved_user1 or username == approved_user2):
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")

# Output (username = "bmoreno"):  This user has access to this device.
# Output (username = "jsmith"):   This user does not have access to this device.


# ── TASK 7: Scale to a list of approved users with `in` ──────
# Assign `approved_list` to a list of approved usernames

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in

username = "bmoreno"

# If the user trying to log in is among the approved users, then display a message
# that they are approved to access this device
# Otherwise, display a message that they do not have access to this device

if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")

# Output (username = "bmoreno"):  This user has access to this device.
# Output (username = "jsmith"):   This user does not have access to this device.

# Q5: When an approved username is used, the `in` operator returns True and access is granted.
# When an unapproved username is used, it returns False and access is denied.


# ── TASK 8: Check login timing with a Boolean variable ───────
# Assign `organization_hours` to a Boolean value

organization_hours = True

# If the entered `organization_hours` has a value of True,
# then display "Login attempt made during organization hours."
# Otherwise, display "Login attempt made outside of organization hours."

if organization_hours == True:
    print("Login attempt made during organization hours.")
else:
    print("Login attempt made outside of organization hours.")

# Output (organization_hours = True):  Login attempt made during organization hours.
# Output (organization_hours = False): Login attempt made outside of organization hours.

# Q6: When organization_hours is True, the if branch executes and confirms the login timing.
# When False, the else branch executes and flags the attempt as outside business hours.


# ── TASK 9: Combine both checks independently ─────────────────
# Assign `approved_list` to a list of approved usernames

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in

username = "bmoreno"

# Check username against the approved list

if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")

# Assign `organization_hours` to a Boolean value

organization_hours = True

# Check whether the login attempt is within organization hours

if organization_hours == True:
    print("Login attempt made during organization hours.")
else:
    print("Login attempt made outside of organization hours.")

# Output (username = "bmoreno", organization_hours = True):
#   This user has access to this device.
#   Login attempt made during organization hours.

# Q7: An unapproved user triggers "This user does not have access to this device."
# An approved user triggers "This user has access to this device."
# Both checks run independently — a user can be approved but still log in outside hours.


# ── TASK 10: Combine both conditions with `and` ──────────────
# Assign `approved_list` to a list of approved usernames

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in

username = "bmoreno"

# Assign `organization_hours` to a Boolean value

organization_hours = True

# If the user is among the approved users AND logging in during organization hours,
# then confirm the login; otherwise, flag the attempt

if (username in approved_list) and (organization_hours == True):
    print("Login attempt made by an approved user during organization hours.")
else:
    print("Username not approved or login attempt made outside of organization hours.")

# Output (username = "bmoreno", organization_hours = True):
#   Login attempt made by an approved user during organization hours.
# Output (username = "jsmith", organization_hours = True):
#   Username not approved or login attempt made outside of organization hours.
# Output (username = "bmoreno", organization_hours = False):
#   Username not approved or login attempt made outside of organization hours.

# Q8: Both conditions must be True simultaneously for access to be confirmed.
# If either the username is not approved OR the login falls outside organization hours,
# the else branch executes — the `and` operator enforces both requirements at once.
