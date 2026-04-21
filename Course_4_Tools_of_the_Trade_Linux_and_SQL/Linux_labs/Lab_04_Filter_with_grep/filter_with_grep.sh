#!/bin/bash
# ============================================================
# Lab: Filter with grep
# Course: Google Cybersecurity Professional Certificate
# Course 4: Tools of the Trade - Linux and SQL
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# ============================================================

# ------------------------------------------------------------
# TASK 1 - Search for error messages in a log file
# ------------------------------------------------------------

# Navigate to the logs directory
cd /home/analyst/logs

# Confirm current location
pwd
# Output: /home/analyst/logs

# Search for all lines containing "error" in server_logs.txt
grep error server_logs.txt
# Output:
# 2022-09-28 13:56:22 error   The password is incorrect
# 2022-09-28 15:56:22 error   The username is incorrect
# 2022-09-28 16:56:22 error   The password is incorrect
# 2022-09-29 13:56:22 error   An unexpected error occurred
# 2022-09-29 15:56:22 error   Unauthorized access
# 2022-09-29 16:56:22 error   Unauthorized access

# Answer: 6 error lines found in server_logs.txt

# ------------------------------------------------------------
# TASK 2 - Find files containing specific strings in their names
# ------------------------------------------------------------

# Navigate to the users directory
cd /home/analyst/reports/users

# List all files in the directory
ls
# Output:
# Q1_access.txt       Q1_deleted_users.txt  Q2_added_users.txt    Q3_access.txt
# Q1_added_users.txt  Q2_access.txt         Q2_deleted_users.txt  Q3_added_users.txt
# Q3_deleted_users.txt  Q4_access.txt       Q4_added_users.txt    Q4_deleted_users.txt

# Pipe ls output to grep to filter files containing "Q1"
ls | grep Q1
# Output:
# Q1_access.txt
# Q1_added_users.txt
# Q1_deleted_users.txt

# Answer: 3 files contain "Q1" in their names

# Pipe ls output to grep to filter files containing "access"
ls | grep access
# Output:
# Q1_access.txt
# Q2_access.txt
# Q3_access.txt
# Q4_access.txt

# Answer: 4 files contain "access" in their names

# Note: the pipe operator | sends the output of the first command
# (ls) as input to the second command (grep), allowing us to filter
# file names without manually scanning the full directory listing

# ------------------------------------------------------------
# TASK 3 - Search more file contents
# ------------------------------------------------------------

# Search for username jhill in Q2_deleted_users.txt
grep jhill Q2_deleted_users.txt
# Output:
# 1025         jhill     Sales
# Answer: jhill WAS found in Q2_deleted_users.txt → Yes

# Search for users added to Human Resources in Q4
grep "Human Resources" Q4_added_users.txt
# Output:
# 1151         sshah     Human Resources
# 1145         msosa     Human Resources

# Answer: 2 users were added to Human Resources in Q4
# (sshah and msosa)

# Note: multi-word strings must be enclosed in quotes so grep
# treats them as a single search pattern and not two separate arguments
