#!/bin/bash
# ============================================================
# Lab: Examine Input/Output in the Linux Shell
# Course: Google Cybersecurity Professional Certificate
# Course 4: Tools of the Trade - Linux and SQL
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# ============================================================

# ------------------------------------------------------------
# TASK 1 - Generate output with the echo command
# ------------------------------------------------------------

# Basic echo output
echo hello
# Output: hello

# Echo with quotation marks (same output, quotes group characters)
echo "hello"
# Output: hello

# Note: Quotes are optional for simple strings but recommended
# when the string contains special characters or spaces

# Echo a custom string (name)
echo "vittorio"
# Output: vittorio

# ------------------------------------------------------------
# TASK 2 - Generate output with the expr command
# ------------------------------------------------------------

# ❌ WRONG - terms and operators must be separated by spaces
# expr 32-8
# Output: 32-8  ← returned as a string, not calculated!

# ✅ CORRECT - spaces between all terms and operators
expr 32 - 8
# Output: 24
# Use case: calculate false positives from 32 total alerts,
# 8 of which required action → 24 are false positives

expr 3500 \* 12
# Output: 42000
# Use case: calculate total expected yearly logins
# (3500/month average * 12 months)

# Note: the * operator must be escaped with \ when used in a
# non-interactive script to prevent Bash from interpreting it
# as a wildcard glob pattern. In the interactive shell, it
# works without escaping: expr 3500 * 12

# ------------------------------------------------------------
# TASK 3 - Clear the Bash shell
# ------------------------------------------------------------

clear
# Clears all previous input and output from the shell window
# Cursor returns to the top left of the terminal

# ------------------------------------------------------------
# OPTIONAL TASK - Further exploration of echo and expr
# ------------------------------------------------------------

# Echo with a longer custom string
echo "time is changing here, rain will fall and sun will rise"
# Output: time is changing here, rain will fall and sun will rise

# ❌ WRONG - parentheses are not supported by expr
# expr ( 26 * 6 ) + ( 46 / 2 )
# Error: -bash: syntax error near unexpected token `26'
# Reason: Bash interprets ( ) as subshell syntax, not math grouping

# ✅ CORRECT - expr evaluates left to right, no parentheses needed
expr 26 \* 6 + 15
# Output: 171
# Breakdown: 26 * 6 = 156, then 156 + 15 = 171

# Note: expr performs INTEGER arithmetic only
# - No decimal points supported
# - Results are always rounded down to the nearest integer
# - All terms and operators MUST be separated by spaces
