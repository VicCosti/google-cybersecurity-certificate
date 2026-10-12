# ============================================================
# Lab: Create Loops
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: for loop with range() — fixed iterations ─────────
# Iterative statement using `for`, `range()`, and a loop variable of `i`
# Display "Connection could not be established." three times

for i in range(0, 3):
    print("Connection could not be established.")

# Output:
# Connection could not be established.
# Connection could not be established.
# Connection could not be established.


# ── TASK 2: for loop with range() — variable iterations ──────
# Create a variable called `connection_attempts` that stores the number of times
# the user has tried to connect to the network

connection_attempts = 9

# Iterative statement using `for`, `range()`, a loop variable of `i`, and `connection_attempts`
# Display "Connection could not be established." as many times as specified by `connection_attempts`

for i in range(0, connection_attempts):
    print("Connection could not be established")

# Output: "Connection could not be established" printed 9 times
# Changing connection_attempts changes how many times the message prints


# ── TASK 3: while loop — condition-based iteration ────────────
# Assign `connection_attempts` to an initial value of 0

connection_attempts = 0

# Iterative statement using `while` and `connection_attempts`
# Display "Connection could not be established." until connection_attempts reaches 3

while connection_attempts < 3:
    print("Connection could not be established.")
    # Update `connection_attempts` (increment it by 1 at the end of each iteration)
    connection_attempts = connection_attempts + 1

# Output:
# Connection could not be established.
# Connection could not be established.
# Connection could not be established.

# Q1: The for loop uses range() to define upfront how many iterations to run — it counts
# through a fixed sequence and stops automatically. The while loop evaluates a condition
# before each iteration and stops when that condition becomes False. The while loop requires
# a manually incremented counter to avoid running forever, whereas the for loop manages
# the counter implicitly. Both produce the same output here, but while loops are better
# suited to situations where the number of iterations is not known in advance.


# ── TASK 4: for loop — iterate over a list ───────────────────
# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For loop that displays the elements of `ip_addresses` one at a time

for i in ip_addresses:
    print(i)

# Output:
# 192.168.142.245
# 192.168.109.50
# 192.168.86.232
# 192.168.131.147
# 192.168.205.12
# 192.168.200.48


# ── TASK 5: for loop + if/else — allow list check ────────────
# Assign `allow_list` to a list of IP addresses that are allowed to log in

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71",
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have tried to log in,
# If it is among the allowed addresses, then display "IP address is allowed"
# Otherwise, display "IP address is not allowed"

for i in ip_addresses:
    if i in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed")

# Output:
# IP address is not allowed   (192.168.142.245 — not in allow_list)
# IP address is not allowed   (192.168.109.50  — not in allow_list)
# IP address is allowed       (192.168.86.232  — in allow_list)
# IP address is not allowed   (192.168.131.147 — not in allow_list)
# IP address is allowed       (192.168.205.12  — in allow_list)
# IP address is not allowed   (192.168.200.48  — not in allow_list)


# ── TASK 6: for loop + if/else + break — halt on violation ───
# Assign `allow_list` to a list of IP addresses that are allowed to log in

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71",
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have tried to log in,
# If it is among the allowed addresses, then display "IP address is allowed"
# Otherwise, display the extended alert message and terminate the loop

for i in ip_addresses:
    if i in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed. Further investigation of login activity required")
        break

# Output:
# IP address is not allowed. Further investigation of login activity required
# (loop terminates immediately — 192.168.142.245 is not in allow_list)

# Note: break exits the loop at the first unauthorized IP encountered.
# Any remaining IPs in the list are not checked after the loop is terminated.


# ── TASK 7: while loop — generate employee IDs ───────────────
# Assign the loop variable `i` to an initial value of 5000

i = 5000

# While loop that generates unique employee IDs for the Sales department
# by iterating through numbers and displays each ID created
# IDs are divisible by 5 and fall between 5000 and 5150 (inclusive)

while i <= 5150:
    print(i)
    i = i + 5

# Output: 5000, 5005, 5010, 5015, ..., 5145, 5150
# Total: 31 unique employee IDs generated


# ── TASK 8: while loop + if — milestone alert ────────────────
# Assign the loop variable `i` to an initial value of 5000

i = 5000

# While loop that generates unique employee IDs for the Sales department
# This loop displays "Only 10 valid employee ids remaining" once `i` reaches 5100

while i <= 5150:
    print(i)
    if i == 5100:
        print("Only 10 valid employee ids remaining")
    i = i + 5

# Output (excerpt):
# ...
# 5095
# 5100
# Only 10 valid employee ids remaining
# 5105
# ...
# 5150

# Q2: print(i) is written before the if statement so that every employee ID is displayed
# regardless of whether the milestone condition is met. If print(i) were inside the
# if block, only the value 5100 would be printed — all other IDs would be silently skipped.
# Placing it before the conditional ensures the ID is always shown first, and the alert
# message only appears as a supplementary line when the specific threshold is reached.
