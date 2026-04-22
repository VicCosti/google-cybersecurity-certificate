#!/bin/bash
# ============================================================
# Lab: Manage Files with Linux Commands
# Course: Google Cybersecurity Professional Certificate
# Course 4: Tools of the Trade - Linux and SQL
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# ============================================================

# Initial directory structure:
# /home/analyst/
# ├── notes/
# │   ├── Q3patches.txt
# │   └── tempnotes.txt
# ├── reports/
# │   ├── Q1patches.txt
# │   └── Q2patches.txt
# └── temp/

# Target directory structure:
# /home/analyst/
# ├── logs/
# ├── notes/
# │   └── tasks.txt
# └── reports/
#     ├── Q1patches.txt
#     ├── Q2patches.txt
#     └── Q3patches.txt

# ------------------------------------------------------------
# TASK 1 - Create a new directory
# ------------------------------------------------------------

# Confirm current location
pwd
# Output: /home/analyst

# Create the logs subdirectory
mkdir logs

# Verify the new directory was created
ls
# Output: logs  notes  reports  temp

# ------------------------------------------------------------
# TASK 2 - Remove a directory
# ------------------------------------------------------------

# Verify temp directory is empty before removing
cd /home/analyst/temp/
ls
# Output: (empty — no files)

# Return to home directory
cd /home/analyst

# Remove the temp directory
rmdir temp

# Verify temp has been removed
ls
# Output: logs  notes  reports

# Note: rmdir only works on EMPTY directories
# Use "rm -r dirname" to remove directories that contain files

# ------------------------------------------------------------
# TASK 3 - Move a file
# ------------------------------------------------------------

# Navigate to notes directory
cd /home/analyst/notes/

# List current contents
ls
# Output: Q3patches.txt  tempnotes.txt

# Move Q3patches.txt to the reports directory
mv Q3patches.txt /home/analyst/reports/

# Verify Q3patches.txt has been moved from notes
ls
# Output: tempnotes.txt

# Navigate to reports and verify Q3patches.txt is there
cd /home/analyst/reports/
ls
# Output: Q1patches.txt  Q2patches.txt  Q3patches.txt

# ------------------------------------------------------------
# TASK 4 - Remove a file
# ------------------------------------------------------------

# Navigate back to notes directory
cd /home/analyst/notes/

# Remove the unused tempnotes.txt file
rm tempnotes.txt

ls
# Output: (empty — notes directory is now empty)

# Confirm current location
pwd
# Output: /home/analyst/notes

# ------------------------------------------------------------
# TASK 5 - Create a new file
# ------------------------------------------------------------

# Create an empty tasks.txt file using touch
touch tasks.txt

# Verify the file was created
ls
# Output: tasks.txt

# ------------------------------------------------------------
# TASK 6 - Edit a file with nano
# ------------------------------------------------------------

# Open tasks.txt in the nano text editor
nano tasks.txt

# Inside nano, the following text was added:
# -------------------------------------------
# Completed tasks
# 1. Managed file structure in /home/analyst
# -------------------------------------------
# Save sequence: CTRL+X → Y → ENTER

# Clear the shell after exiting nano
clear

# Verify the file contents were saved correctly
head tasks.txt
# Output:
# Completed tasks
# 1. Managed file structure in /home/analyst
