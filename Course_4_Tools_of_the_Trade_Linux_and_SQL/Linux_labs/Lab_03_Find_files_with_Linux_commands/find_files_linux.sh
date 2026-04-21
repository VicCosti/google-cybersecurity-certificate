#!/bin/bash
# ============================================================
# Lab: Find Files with Linux Commands
# Course: Google Cybersecurity Professional Certificate
# Course 4: Tools of the Trade - Linux and SQL
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# ============================================================

# ------------------------------------------------------------
# TASK 1 - Get current directory information
# ------------------------------------------------------------

# Display current working directory
pwd
# Output: /home/analyst

# List contents of current directory
ls
# Output:
# logs  projects  reports  temp
# → 4 directories found: logs, projects, reports, temp

# ------------------------------------------------------------
# TASK 2 - Change directory and list subdirectories
# ------------------------------------------------------------

# Navigate to the reports directory
cd reports

# Confirm current location
pwd
# Output: /home/analyst/reports

# List contents of reports directory
ls
# Output: users
# → 1 subdirectory found: users

# ------------------------------------------------------------
# TASK 3 - Locate and read contents of a file
# ------------------------------------------------------------

# Navigate to the users subdirectory
cd users

# Confirm current location
pwd
# Output: /home/analyst/reports/users

# List files in current directory
ls
# Output: Q1_added_users.txt  Q1_deleted_users.txt

# Preview first lines of Q1_added_users.txt
head Q1_added_users.txt
# Output:
# employee_id  username  department
# 1001         bmoreno   Marketing
# 1026         apatel    Human Resources
# 1041         cgriffin  Sales
# 1104         mreed     Information Technology
# 1177         aezra     Human Resources
# 1188         noshiro   Finance

# Display full contents of Q1_added_users.txt
cat Q1_added_users.txt
# Output:
# employee_id  username  department
# 1001         bmoreno   Marketing
# 1026         apatel    Human Resources
# 1041         cgriffin  Sales
# 1104         mreed     Information Technology
# 1177         aezra     Human Resources
# 1188         noshiro   Finance

# Answers from file analysis:
# → aezra works in: Human Resources
# → mreed (Information Technology) employee_id: 1104

# ------------------------------------------------------------
# TASK 4 - Navigate to logs directory and read a file
# ------------------------------------------------------------

# Navigate back to home using absolute path
cd /home/analyst

# Confirm current location
pwd
# Output: /home/analyst

# Navigate to logs directory
cd logs

# List files in logs directory
ls
# Output: server_logs.txt

# Display first 10 lines of server_logs.txt
head server_logs.txt
# Output:
# 2022-09-28 13:55:55 info    User logged on successfully
# 2022-09-28 13:56:22 error   The password is incorrect
# 2022-09-28 13:56:48 warning The file storage is 75% full
# 2022-09-28 15:55:55 info    User logged on successfully
# 2022-09-28 15:56:22 error   The username is incorrect
# 2022-09-28 15:56:48 warning The file storage is 90% full
# 2022-09-28 16:55:55 info    User navigated to settings page
# 2022-09-28 16:56:22 error   The password is incorrect
# 2022-09-28 16:56:48 warning The current user's password expires in 15 days
# 2022-09-29 13:55:55 info    User logged on successfully

# Answer from log analysis:
# → Warning messages in first 10 lines: 3
# (lines 3, 6, 9 — "warning" entries)
