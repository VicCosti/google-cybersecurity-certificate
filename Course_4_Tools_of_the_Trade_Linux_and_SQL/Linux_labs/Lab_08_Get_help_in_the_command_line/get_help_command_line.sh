#!/bin/bash
# ============================================================
# Lab: Get Help in the Command Line
# Course: Google Cybersecurity Professional Certificate
# Course 4: Tools of the Trade - Linux and SQL
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# ============================================================

# Three main commands for getting help in Linux:
# whatis  → one-line description of a command
# man     → full manual page with all options
# apropos → search manual pages by keyword

# ------------------------------------------------------------
# TASK 1 - Learn more about commands
# ------------------------------------------------------------

# Get a short description of the cat command
whatis cat
# Output: cat (1) - concatenate files and print on the standard output
# → First two words of description: "concatenate files"

# Get the full manual page for cat
man cat
# Output: full man page showing all options including:
# -n, --number       → number all output lines
# -b, --number-nonblank → number nonempty output lines only
#
# Answer: use -n to number all output lines

# Note: inside man pages navigation works as follows:
# ENTER     → scroll one line at a time
# SPACE     → scroll one page at a time
# Q         → quit and return to the shell
#
# ❌ Common mistake: typing Q or q directly in the shell
# (outside of man) returns "command not found"
# Q and q only work as navigation keys INSIDE the man pager

# Search for a command that returns the first part of a file
apropos -a first part file
# Output: head (1) - output the first part of files
# Answer: head

# Note: -a flag means ALL keywords must match
# Without -a, results include commands matching ANY keyword

# ------------------------------------------------------------
# TASK 2 - Explore the useradd command
# ------------------------------------------------------------

# Get the full manual page for useradd
man useradd
# Key option found in the manual:
# -e, --expiredate EXPIRE_DATE
#     The date on which the user account will be disabled.
#     Format: YYYY-MM-DD
#
# Answer: use -e to set an expiration date for a temporary account
# Example: sudo useradd -e 2024-12-31 tempuser

# ------------------------------------------------------------
# TASK 3 - Explore the rm and rmdir commands
# ------------------------------------------------------------

# Get quick descriptions of both commands
whatis rm
# Output: rm (1) - remove files or directories

whatis rmdir
# Output: rmdir (1) - remove empty directories
#         rmdir (2) - delete a directory

# Answer: rmdir removes ONLY empty directories
# rm removes files or directories (use rm -r for directories with content)

# ------------------------------------------------------------
# TASK 4 - Determine which command to use
# ------------------------------------------------------------

# Search for the command to create a new group
apropos -a create new group
# Output: groupadd (8) - create a new group
# Answer: groupadd
