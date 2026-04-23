#!/bin/bash
# ============================================================
# Lab: Add and Manage Users with Linux Commands
# Course: Google Cybersecurity Professional Certificate
# Course 4: Tools of the Trade - Linux and SQL
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# User: analyst (with sudo privileges)
# ============================================================

# Note: All commands in this lab require sudo (superuser privileges)
# Adding, modifying, and deleting users are root-level operations

# ------------------------------------------------------------
# TASK 1 - Add a new user
# ------------------------------------------------------------

# Confirm starting location
pwd
# Output: /home/analyst

# Add new user researcher9 to the system
sudo useradd researcher9

# Add researcher9 to research_team as their primary group
sudo usermod -g research_team researcher9

# Note: -g (lowercase) sets the PRIMARY group
#       -G (uppercase) adds a SECONDARY group (used in Task 3)

# ------------------------------------------------------------
# TASK 2 - Assign file ownership
# ------------------------------------------------------------

# ❌ WRONG - typo in username (research9 instead of researcher9)
# sudo chown research9 /home/researcher2/projects/project_r.txt
# Error: chown: invalid user: 'research9'

# ✅ CORRECT - full username researcher9
sudo chown researcher9 /home/researcher2/projects/project_r.txt

# Note: chown changes the owner of a file or directory
# Syntax: sudo chown username /path/to/file

# ------------------------------------------------------------
# TASK 3 - Add user to a secondary group
# ------------------------------------------------------------

# Add researcher9 to sales_team as a secondary group
# Primary group (research_team) remains unchanged
sudo usermod -a -G sales_team researcher9

# Note: -a (append) must be used with -G to ADD a secondary group
# Without -a, -G would REPLACE all existing secondary groups
# Options are case-sensitive: -a is lowercase, -G is uppercase

# ------------------------------------------------------------
# TASK 4 - Delete a user
# ------------------------------------------------------------

# Delete researcher9 from the system
sudo userdel researcher9
# Expected message:
# userdel: group researcher9 not removed because it is not
# the primary group of user researcher9.
#
# This is expected behavior — when a user is created in Linux,
# a group with the same name is automatically created.
# userdel removes the user but not this auto-created group
# if it is not the primary group.

# Clean up the now-empty researcher9 group
sudo groupdel researcher9

# Note: always clean up orphaned groups after deleting users
# to keep the system tidy and avoid security risks
