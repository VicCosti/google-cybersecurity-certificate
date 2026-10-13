# ============================================================
# Lab: Develop an Algorithm
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: Synchronized lists — explore index correspondence ─
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

# Display the element at the specified index in `approved_users`

print(approved_users[2])

# Display the element at the specified index in `approved_devices`

print(approved_devices[2])

# Output:
# tshah
# 2ye3lzg

# Q1: When approved_users[0] is displayed, it shows "elarson" — the first element
# in the list. When approved_devices[0] is displayed, it shows "8rp2k75" — the
# first element in the devices list. The key observation is that these two values
# correspond to each other: "elarson" is the user at index 0, and "8rp2k75" is
# that user's assigned device at the same index 0. This relationship holds at every
# position across both lists — the element at index n in approved_users is the
# owner of the device at index n in approved_devices. When the index is changed
# from 0 to 2, both prints shift to the third element of their respective lists:
# "tshah" and "2ye3lzg". The two lists are synchronized, meaning the pairing is
# preserved by position, and this index-based correspondence is the foundation of
# the device verification algorithm built in the tasks that follow.


# ── TASK 2: .append() — add a new user and device pair ───────
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

# Assign `new_user` to the username of a new approved user

new_user = "gesparza"

# Assign `new_device` to the device ID of the new approved user

new_device = "3rcv4w6"

# Add that user's username and device ID to `approved_users` and `approved_devices` respectively

approved_users.append(new_user)
approved_devices.append(new_device)

# Display the contents of `approved_users`

print(approved_users)

# Display the contents of `approved_devices`

print(approved_devices)

# Output:
# ['elarson', 'bmoreno', 'tshah', 'sgilmore', 'eraab', 'gesparza']
# ['8rp2k75', 'hl0s5o1', '2ye3lzg', '4n482ts', 'a307vir', '3rcv4w6']

# Q2: After calling .append() on each list, both approved_users and approved_devices
# each grow from 5 elements to 6. "gesparza" now appears as the last element of
# approved_users and "3rcv4w6" now appears as the last element of approved_devices.
# Critically, both were added at the same position — index 5 — so the synchronization
# between the two lists is preserved: gesparza's username and device ID are aligned
# at the same index. This is the correct way to onboard a new employee while
# maintaining the index-based pairing that the verification algorithm depends on.
# If only one list were updated, the correspondence between the two lists would
# break for all subsequent elements.


# ── TASK 3: .remove() — remove a departed user and device ────
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `removed_user` to the username of the employee who has left the team

removed_user = "tshah"

# Assign `removed_device` to the device ID of the employee who has left the team

removed_user = "2ye3lzg"   # NOTE: this line reassigns `removed_user` instead of assigning `removed_device`
                            # The variable `removed_device` is never created; the correct line should be:
                            # removed_device = "2ye3lzg"
                            # The .remove() calls below use hardcoded strings directly,
                            # so the output is still correct, but removed_device is unused.

# Remove that employee's username and device ID from `approved_users` and `approved_devices` respectively

approved_users.remove("tshah")
approved_devices.remove("2ye3lzg")

# Display `approved_users`

print(approved_users)

# Display `approved_devices`

print(approved_devices)

# Output:
# ['elarson', 'bmoreno', 'sgilmore', 'eraab', 'gesparza']
# ['8rp2k75', 'hl0s5o1', '4n482ts', 'a307vir', '3rcv4w6']

# Q3: After the .remove() calls, both lists shrink from 6 elements to 5. "tshah"
# no longer appears in approved_users and "2ye3lzg" no longer appears in
# approved_devices. Because both were removed, the synchronization between the
# two lists is preserved — each remaining username still corresponds to the
# correct device at the same index position. If only the username were removed
# and the device left in place, every remaining device ID would shift to the
# wrong index, breaking the algorithm. The pairing must be maintained as a unit.
#
# Note on variable assignment: the variable `removed_user` is overwritten with
# the device ID string "2ye3lzg" on the second assignment line. The intended
# variable name was `removed_device`. Since the .remove() calls use the correct
# hardcoded strings rather than the variable names, the functional result is
# correct — but the variable `removed_device` was never actually defined. In
# production code, the .remove() calls should reference the variables
# (approved_users.remove(removed_user) and approved_devices.remove(removed_device))
# to make the code reusable across different inputs.


# ── TASK 4: in — check if a username is approved ─────────────
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username

username = "sgilmore"

# Conditional statement
# If `username` belongs to `approved_users`, display approval message
# Otherwise display rejection message

if username in approved_users:
    print("The user", username, "is approved to access the system.")
else:
    print("The user", username, "is not approved to access the system.")

# Output:
# The user sgilmore is approved to access the system.

# Q4: The output is "The user sgilmore is approved to access the system." because
# "sgilmore" is an element of approved_users. The `in` operator evaluates
# `username in approved_users` to True, so the if branch runs and prints the
# approval message. If username were set to a value not in the list (e.g.,
# "tshah", who was removed in Task 3), the in operator would return False and
# the else branch would run instead, printing the not-approved message. The `in`
# operator is the most direct and readable way to test list membership in Python.


# ── TASK 5: .index() — find the position of a username ───────
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username

username = "sgilmore"

# Assign `ind` to the index of `username` in `approved_users`

ind = approved_users.index(username)

# Display the value of `ind`

print(ind)

# Output:
# 2

# Q5: The output is 2. approved_users.index("sgilmore") searches the list
# left-to-right and returns the index of the first match. "sgilmore" is the
# third element in the list (index 2, using zero-based indexing). Storing this
# value in `ind` is the critical step that bridges the two synchronized lists:
# because approved_users and approved_devices share the same index structure,
# `ind` now points to the same position in both lists — the position occupied
# by sgilmore and her assigned device. This allows the next task to look up the
# correct device ID without any explicit search of approved_devices.


# ── TASK 6: Cross-list lookup — find device from username index
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username

username = "sgilmore"

# Assign `ind` to the index of `username` in `approved_users`

ind = approved_users.index(username)

# Display the device ID at the index that matches the value of `ind` in `approved_devices`

print(approved_devices[ind])

# Output:
# 4n482ts

# Q6: The output is "4n482ts". approved_users.index("sgilmore") returns 2,
# which is stored in `ind`. Then approved_devices[2] retrieves the element at
# that same index in approved_devices — which is "4n482ts", sgilmore's assigned
# device. The cross-list lookup works because the two lists are synchronized:
# the user at position n always corresponds to the device at position n. By using
# the index from one list as the subscript for the other, the algorithm retrieves
# the correct device without needing to search approved_devices at all. This
# pattern — find index in list A, use it to access list B — is the core
# mechanism that the full login() function is built on.


# ── TASK 7: Combined condition — username and device match ────
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username

username = "sgilmore"

# Assign `device_id` to a device ID

device_id = "4n482ts"

# Assign `ind` to the index of `username` in `approved_users`

ind = approved_users.index(username)

# Conditional statement
# If `username` belongs to `approved_users` AND the device at `ind` matches `device_id`,
# display approval messages

if username in approved_users and approved_devices[ind] == device_id:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

# Output:
# The username sgilmore is approved to access the system.
# 4n482ts is the assigned device for sgilmore

# Q7: Both messages are displayed because both conditions joined by `and` evaluate
# to True. "sgilmore" is in approved_users (first condition: True), and
# approved_devices[2] is "4n482ts", which equals the device_id variable
# (second condition: True). Since both are True, the entire `and` expression is
# True and the if block runs. If either condition were False — the username not
# recognized or the device ID not matching — the `and` expression would short-circuit
# to False and neither message would print. This task introduces the two-factor
# check that is the heart of the algorithm: identity (is the user approved?) and
# possession (do they have the right device?).


# ── TASK 8: elif — handle wrong device for approved user ──────
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username

username = "sgilmore"

# Assign `device_id` to a device ID (deliberately incorrect to test the elif branch)

device_id = "4n582ts"

# Assign `ind` to the index of `username` in `approved_users`

ind = approved_users.index(username)

# If statement: approved user with correct device
if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

# Elif statement: approved user but wrong device
elif username in approved_users and device_id != approved_devices[ind]:
    print("The user", username, "is approved to access the system, but", device_id, "is not their assigned device.")

# Output (with device_id = "4n582ts"):
# The user sgilmore is approved to access the system, but 4n582ts is not their assigned device.

# Q8: With device_id set to "4n582ts" (one character different from the correct
# "4n482ts"), the if condition fails because device_id != approved_devices[ind].
# Python then evaluates the elif, which checks that the username is approved
# (True) and that the device does not match (True), so the elif block runs.
# The output correctly reports that sgilmore is an approved user but has presented
# the wrong device. This is an important distinction from an unknown user: the
# system can confirm identity while flagging the device mismatch separately,
# which gives the security team more useful information than a generic rejection.
#
# Style note: the elif condition `username in approved_users and device_id != approved_devices[ind]`
# is technically redundant. Python reaches the elif only if the if condition was False.
# Since the if requires both `username in approved_users` (True) and device match (True),
# the only way the if fails when the username is valid is if the device doesn't match.
# The elif could be written simply as `elif username in approved_users:`, which is
# slightly cleaner. The version above is not wrong — it is just more explicit than necessary.


# ── TASK 9: login() — full algorithm as a function ───────────
# Assign `approved_users` to a list of approved usernames

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`

approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Define a function named `login` that takes in two parameters, `username` and `device_id`

def login(username, device_id):

    # Outer conditional: check if `username` belongs to `approved_users`

    if username in approved_users:

        # Display approval message

        print("The user", username, "is approved to access the system.")

        # Find the index of `username` in `approved_users`

        ind = approved_users.index(username)

        # Inner conditional: check if `device_id` matches the assigned device at `ind`

        if device_id == approved_devices[ind]:

            # Correct device: display assignment confirmation

            print(device_id, "is the assigned device for", username)

        else:

            # Wrong device: display mismatch message

            print(device_id, "is not their assigned device.")

    else:

        # Outer else: username not in approved_users

        print("The username", username, "is not approved to access the system.")

# Call the function with three different combinations to exercise all branches

login("eraab", "a307vir")
login("bmoreno", "3rcv4w6")
login("notknowuser", "unknowndevice")

# Output:
# The user eraab is approved to access the system.
# a307vir is the assigned device for eraab
#
# The user bmoreno is approved to access the system.
# 3rcv4w6 is not their assigned device.
#
# The username notknowuser is not approved to access the system.

# Q9: When Python enters the inner conditional, two outcomes are possible.
# If device_id matches the element at ind in approved_devices (the correct device),
# the inner if branch runs and displays a confirmation that the device is assigned
# to the user — as seen with login("eraab", "a307vir"). If device_id does not
# match (the wrong device), the inner else branch runs and displays a mismatch
# message — as seen with login("bmoreno", "3rcv4w6"), where bmoreno's assigned
# device is "hl0s5o1", not "3rcv4w6". The inner conditional is only ever reached
# when the outer if has already confirmed that the username is approved; this nested
# structure cleanly separates the two verification layers: identity first, device second.
