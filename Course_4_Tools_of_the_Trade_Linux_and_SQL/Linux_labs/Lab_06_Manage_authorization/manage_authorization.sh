#!/bin/bash
# ============================================================
# Lab: Manage Authorization
# Course: Google Cybersecurity Professional Certificate
# Course 4: Tools of the Trade - Linux and SQL
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# User: researcher2 | Group: research_team
# ============================================================

# Permission string reference:
# d r w x | r w x | r w x
# │ └─┬─┘   └─┬─┘   └─┬─┘
# │  user    group   other
# └── file type: d=directory, -=file

# ------------------------------------------------------------
# TASK 1 - Check file and directory details
# ------------------------------------------------------------

# Confirm starting location
pwd
# Output: /home/researcher2

# List contents of home directory
ls
# Output: projects

# Navigate to projects directory
cd projects/

# List all files including hidden files with permissions
ls -la
# Output:
# total 32
# drwxr-xr-x 3 researcher2 research_team 4096 Apr 22 14:58 .
# drwxr-xr-x 3 researcher2 research_team 4096 Apr 22 15:52 ..
# -rw--w---- 1 researcher2 research_team   46 Apr 22 14:58 .project_x.txt
# drwx--x--- 2 researcher2 research_team 4096 Apr 22 14:58 drafts
# -rw-rw-rw- 1 researcher2 research_team   46 Apr 22 14:58 project_k.txt
# -rw-r----- 1 researcher2 research_team   46 Apr 22 14:58 project_m.txt
# -rw-rw-r-- 1 researcher2 research_team   46 Apr 22 14:58 project_r.txt
# -rw-rw-r-- 1 researcher2 research_team   46 Apr 22 14:58 project_t.txt

# List hidden files only
ls -a
# Output: .  ..  .project_x.txt  drafts  project_k.txt  project_m.txt  project_r.txt  project_t.txt

# Answers:
# → Group owner of all files: research_team
# → Hidden file found: .project_x.txt (starts with .)

# ------------------------------------------------------------
# TASK 2 - Change file permissions
# ------------------------------------------------------------

# ISSUE 1: project_k.txt has write permission for other (-rw-rw-rw-)
# Fix: remove write permission from other, set to read only
chmod o=r project_k.txt

# Verify change
ls -la
# project_k.txt is now: -rw-rw-r--

# ISSUE 2: project_m.txt has read permission for group (-rw-r-----)
# Fix: project_m.txt should be user-only, remove group read permission
chmod g-r project_m.txt

# Verify change
ls -la
# project_m.txt is now: -rw-------

# ------------------------------------------------------------
# TASK 3 - Change file permissions on a hidden file
# ------------------------------------------------------------

# ISSUE: .project_x.txt has write permission for both user and group
# Current: -rw--w----
# Required: read only for user and group, no write for anyone

# Fix: set user=read only, group=read only
chmod u=r,g=r .project_x.txt

# Verify change
ls -la
# .project_x.txt is now: -r--r-----

# Note: hidden files in Linux start with a period (.)
# They are visible with ls -a or ls -la but not with plain ls

# ------------------------------------------------------------
# TASK 4 - Change directory permissions
# ------------------------------------------------------------

# Confirm location
pwd
# Output: /home/researcher2/projects

# Check drafts directory permissions
ls -la
# drafts: drwx--x---
# → group has execute (x) permission — should be removed
# Only researcher2 (user) should have access to drafts

# Remove execute permission from group on drafts directory
chmod g-x drafts/

# Verify final state of all permissions
ls -la
# Output:
# drwxr-xr-x 3 researcher2 research_team 4096 Apr 22 14:58 .
# drwxr-xr-x 3 researcher2 research_team 4096 Apr 22 15:52 ..
# -r--r----- 1 researcher2 research_team   46 Apr 22 14:58 .project_x.txt
# drwx------ 2 researcher2 research_team 4096 Apr 22 14:58 drafts
# -rw-rw-r-- 1 researcher2 research_team   46 Apr 22 14:58 project_k.txt
# -rw------- 1 researcher2 research_team   46 Apr 22 14:58 project_m.txt
# -rw-rw-r-- 1 researcher2 research_team   46 Apr 22 14:58 project_r.txt
# -rw-rw-r-- 1 researcher2 research_team   46 Apr 22 14:58 project_t.txt
