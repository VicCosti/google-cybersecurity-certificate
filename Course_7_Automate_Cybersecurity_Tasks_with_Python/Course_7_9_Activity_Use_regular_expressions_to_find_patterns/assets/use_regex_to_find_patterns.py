# ============================================================
# Lab: Use Regular Expressions to Find Patterns
# Course 7 — Automate Cybersecurity Tasks with Python
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: Import the re module ──────────────────────────────

import re

# The `re` module provides all regular expression functionality in Python.
# It must be imported before any re.findall(), re.search(), or re.match() calls.


# ── TASK 2: Display the device IDs log ───────────────────────
# Assign `devices` to a string containing device IDs

devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"

# Display the contents of `devices`

print(devices)

# Output:
# r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78
# ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q
# 081qc9t r159r1u

# The string contains 20 device IDs separated by spaces.
# Four of them begin with "r15": r151dm4, r15xk9h, r15u9q5, r159r1u.
# These are the targets for the extraction in the tasks that follow.


# ── TASK 3: Build the target pattern ─────────────────────────
# Assign `devices` to a string containing device IDs

devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"

# Assign `target_pattern` to a regular expression pattern for finding device IDs
# that start with "r15"

target_pattern = "r15\w+"

# No output — this cell only defines the pattern.

# Q1: The pattern "r15\w+" is composed of two parts:
#
#   r15   — a literal string that anchors the match; the pattern will only match
#             substrings that begin with exactly these three characters in this order.
#             If "r15" were removed, the pattern would collapse to "\w+", which would
#             match every device ID in the string regardless of its prefix — the filter
#             would be lost entirely.
#
#   \w+   — a combination of two regex symbols. \w matches any single alphanumeric
#             character (letters a-z, A-Z, and digits 0-9) or underscore. The + quantifier
#             means "one or more of the preceding element". Together, \w+ matches a
#             sequence of one or more alphanumeric characters of any length.
#             If \w were missing, the pattern would be "r15+", which would match "r15"
#             followed by one or more literal "5" characters — not a useful device ID pattern.
#             If + were missing, the pattern would be "r15\w", which would match "r15"
#             followed by exactly one alphanumeric character — this would only return
#             four-character matches like "r15x" instead of full device IDs like "r15xk9h".


# ── TASK 4: Extract matching device IDs ──────────────────────
# Assign `devices` to a string containing device IDs

devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"

# Assign `target_pattern` to a regular expression pattern for finding device IDs
# that start with "r15"

target_pattern = "r15\w+"

# Use `re.findall()` to find all device IDs that match `target_pattern` in `devices`

print(re.findall(target_pattern, devices))

# Output:
# ['r151dm4', 'r15xk9h', 'r15u9q5', 'r159r1u']

# re.findall() scans `devices` from left to right, finds every non-overlapping
# substring that matches the pattern, and returns them as a list of strings.
# Four device IDs starting with "r15" are identified: r151dm4, r15xk9h, r15u9q5,
# and r159r1u. These are the devices running the operating system that requires
# an update. Devices like "r262c36" are correctly excluded because they begin
# with "r2", not "r15".


# ── TASK 5: Display the login log file ───────────────────────
# Assign `log_file` to a string containing login attempt records

log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

# Display contents of `log_file`

print(log_file)

# Each line contains: username, date (YYYY-MM-DD), login time (H:MM:SS), IP address.
# The log has 15 entries. Most IP addresses follow the valid xxx.xxx.xxx.xxx format,
# but several are malformed due to data collection issues:
#   - 1923.1689.3.24   (arutley)   — segments with 4 digits
#   - 1924.1680.27.57  (aestrada)  — segment with 4 digits
#   - 1921.168.1283.75 (dkot)      — segments with 4 digits
#   - 19245.168.2345.49 (abernard) — segments with 5 digits
#   - 192.16874.1390.176 (alevitsk)— segments with 5 and 4 digits
#   - 192.168.103.10654 (yappiah)  — last segment with 5 digits


# ── TASK 6: Build the strict three-digit IP pattern ──────────
# Assign `log_file` to a string containing login attempt records

log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

# Assign `pattern` to a regular expression that matches IP addresses of the form xxx.xxx.xxx.xxx
# (exactly three digits per segment)

pattern = "\d{3}\.\d{3}\.\d{3}\.\d{3}"

# No output — this cell only defines the pattern.

# Note: the lab hint suggested writing this as \d\d\d\.\d\d\d\.\d\d\d\.\d\d\d
# (repeating \d three times per segment). The pattern used here, \d{3}\.\d{3}\.\d{3}\.\d{3},
# is functionally identical but uses curly-bracket quantifier syntax to express
# "exactly 3 digits" more concisely. This is the more compact and readable notation
# and demonstrates familiarity with regex quantifiers a task ahead of when the lab
# introduces them formally. \d matches any single digit (0–9). \. matches a literal
# period (the backslash escapes the dot, which would otherwise be a wildcard for any
# character). The pattern requires all four segments to be exactly three digits each,
# separated by literal periods.


# ── TASK 7: Extract strict three-digit IP addresses ──────────
# Assign `log_file` to a string containing login attempt records

log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

# Two equivalent patterns — one written with repeated \d, one with {3} quantifier

pattern  = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"   # lab scaffold version
pattern2 = "\d{3}\.\d{3}\.\d{3}\.\d{3}"        # submitted version (equivalent)

# Run both to confirm they produce identical output

print(re.findall(pattern,  log_file))
print(re.findall(pattern2, log_file))

# Output (both lines identical):
# ['192.168.152.148', '192.168.190.178', '192.168.213.128', '192.168.247.153',
#  '192.168.174.117', '192.168.148.115', '192.168.168.144']

# Q2: Examples of IP addresses that WERE extracted:
#   192.168.152.148 (eraab), 192.168.190.178 (smartell), 192.168.213.128 (rjensen)
#   These all have exactly three digits in every segment, so the pattern matches them.
#
# Examples of IP addresses that were NOT extracted:
#   192.168.22.115  (iuduike)   — second-to-last segment has only 2 digits ("22")
#   192.168.96.200  (asundara)  — third segment has only 2 digits ("96")
#   1923.1689.3.24  (arutley)   — all segments have wrong digit counts
#   192.168.103.10654 (yappiah) — last segment has 5 digits
#
# Among those not extracted, 192.168.22.115 and 192.168.96.200 ARE valid IP addresses.
# They were missed because the strict xxx.xxx.xxx.xxx pattern requires exactly three
# digits per segment, but valid IP addresses can have one, two, or three digits per
# segment (0–255). The pattern needs to be relaxed to capture these.

# Note: running both patterns side by side confirms they are functionally equivalent —
# the {3} quantifier is simply a more concise way to express "exactly three repetitions."


# ── TASK 8: Relax the pattern to allow 1–4 digits per segment ─
# Assign `log_file` to a string containing login attempt records

log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

# Update `pattern` to allow between 1 and 4 digits per segment

pattern = "\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}"

# Use `re.findall()` to extract all matching IP addresses

print(re.findall(pattern, log_file))

# Output:
# ['192.168.152.148', '192.168.22.115', '192.168.190.178', '1923.1689.3.24',
#  '192.168.213.128', '1924.1680.27.57', '192.168.96.200', '1921.168.1283.75',
#  '192.168.247.153', '192.168.174.117', '192.168.148.115', '192.168.103.1065',
#  '192.168.168.144']

# Q3: With {1,4}, the pattern now extracts all IP addresses that have between 1 and 4
# digits per segment, including previously missed valid addresses like 192.168.22.115
# and 192.168.96.200. Invalid addresses with oversized segments such as 1923.1689.3.24
# and 1924.1680.27.57 are also extracted because they contain segments of 4 digits,
# which the pattern now permits. Not all extracted addresses are valid: segments
# with 4 digits (e.g., "1923" in 1923.1689.3.24) exceed the maximum of 3 for a
# legitimate IP address. The pattern over-extracts because the upper bound of 4 is
# too permissive. The next task will tighten the upper bound to 3.
#
# Note: the lab asked for \d+ (no upper bound) to demonstrate over-extraction.
# The pattern used here, \d{1,4}, pre-emptively limits segments to at most 4 digits,
# which is stricter than \d+ but still over-extracts compared to the final {1,3} pattern.
# Both approaches serve the same pedagogical purpose: showing that the pattern
# captures some invalid addresses before the upper bound is correctly set to 3.


# ── TASK 9: Final pattern — exactly 1–3 digits per segment ───
# Assign `log_file` to a string containing login attempt records

log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

# Assign `pattern` to a regular expression that matches valid IP addresses only
# (1 to 3 digits per segment)

pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# NOTE: The submitted pattern for this task was \w{2,4}\.\w{2,4}\.\w{2,4}\.\w{2,4}.
# That pattern has two issues:
#   1. \w matches alphanumeric characters (letters + digits), not digits alone.
#      It would incorrectly match segments containing letters.
#   2. The lower bound of 2 would skip single-digit segments like the "3" in 1923.1689.3.24.
# The correct pattern, \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}, is used here and in Task 11.
# \d restricts matches to digit characters only; {1,3} allows 1, 2, or 3 digits per segment.

# Use `re.findall()` on `pattern` and `log_file` and assign `valid_ip_addresses` to the output

valid_ip_addresses = re.findall(pattern, log_file)

# Display the contents of `valid_ip_addresses`

print(valid_ip_addresses)

# Output:
# ['192.168.152.148', '192.168.22.115', '192.168.190.178', '192.168.213.128',
#  '192.168.96.200', '192.168.247.153', '192.168.174.117', '192.168.148.115',
#  '192.168.103.106', '192.168.168.144']

# Q4: Compared to Task 7 (strict three digits): the {1,3} pattern now correctly
# includes addresses with shorter segments, such as 192.168.22.115 (segment "22")
# and 192.168.96.200 (segment "96"), which the Task 7 pattern missed entirely.
#
# Compared to Task 8 (1–4 digits): the {1,3} upper bound now correctly excludes
# malformed addresses with oversized segments. For example, 1923.1689.3.24 is no
# longer extracted as a whole — the engine matches only a valid three-digit prefix
# within it. Invalid addresses like 19245.168.2345.49 and 192.16874.1390.176 are
# filtered out entirely because no substring within them forms four consecutive
# segments of 1–3 digits separated by periods.
#
# The result is a clean list of valid-format IP addresses extracted from the log,
# ready to be compared against the flagged address list in Task 11.


# ── TASK 10: Display the flagged addresses list ───────────────
# Assign `flagged_addresses` to a list of previously flagged IP addresses

flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]

# Display the contents of `flagged_addresses`

print(flagged_addresses)

# Output:
# ['192.168.190.178', '192.168.96.200', '192.168.174.117', '192.168.168.144']

# These four IP addresses have been previously flagged for unusual activity.
# All four are private IP addresses in the 192.168.x.x range, which confirms they
# originated inside the internal network. They will be compared against the extracted
# valid IP addresses in Task 11 to identify which log entries require further investigation.


# ── TASK 11: Loop and flag matching addresses ─────────────────
# Assign `log_file` to a string containing login attempt records

log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

# Assign `pattern` to a regular expression that matches valid IP addresses only

pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Use `re.findall()` to extract valid IP addresses from `log_file`

valid_ip_addresses = re.findall(pattern, log_file)

# Assign `flagged_addresses` to a list of previously flagged IP addresses

flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]

# Loop through `valid_ip_addresses`; check each against `flagged_addresses`

for address in valid_ip_addresses:
    if address in flagged_addresses:
        print("The IP address", address, "has been flagged for further analysis.")
    else:
        print("The IP address", address, "does not require further analysis.")

# Output:
# The IP address 192.168.152.148 does not require further analysis.
# The IP address 192.168.22.115 does not require further analysis.
# The IP address 192.168.190.178 has been flagged for further analysis.
# The IP address 192.168.213.128 does not require further analysis.
# The IP address 192.168.96.200 has been flagged for further analysis.
# The IP address 192.168.247.153 does not require further analysis.
# The IP address 192.168.174.117 has been flagged for further analysis.
# The IP address 192.168.148.115 does not require further analysis.
# The IP address 192.168.103.106 does not require further analysis.
# The IP address 192.168.168.144 has been flagged for further analysis.

# The for loop iterates over each valid IP address extracted from the log.
# For each address, the `in` operator checks list membership against `flagged_addresses`.
# Four addresses match — 192.168.190.178, 192.168.96.200, 192.168.174.117, and
# 192.168.168.144 — and are flagged for further investigation.
# The remaining six are cleared. This completes the full pipeline:
# import re → build pattern → extract valid IPs → compare against flagged list → alert.
