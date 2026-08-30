#!/bin/bash
# ============================================================
# Lab: Create Hash Values
# Course: Google Cybersecurity Professional Certificate
# Course 5: Assets, Threats, and Vulnerabilities
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# ============================================================

# Key concept: hash functions produce a unique fixed-length digest
# for any input. Even a single character difference produces a
# completely different hash -- this is called the avalanche effect.
# Hash values cannot be decrypted -- they are one-way functions.

# ------------------------------------------------------------
# TASK 1 - Generate hashes for files
# ------------------------------------------------------------

# List home directory contents
ls
# Output: file1.txt  file2.txt

# Display contents of file1.txt
cat file1.txt
# Output: X5O!P%@AP[4\PZX54(P^)7CC)7}EICAR-STANDARD-ANTIVIRUS-TEST-FILE!

# Display contents of file2.txt
cat file2.txt
# Output: X5O!P%@AP[4\PZX54(P^)7CC)7}EICAR-STANDARD-ANTIVIRUS-TEST-FILE!

# Note: the two files APPEAR identical when read with cat
# but they are NOT -- file2.txt contains hidden extra characters
# This is exactly how malicious files can disguise themselves
# as legitimate ones

# Generate SHA-256 hash of file1.txt
sha256sum file1.txt
# Output: 131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267  file1.txt

# Generate SHA-256 hash of file2.txt
sha256sum file2.txt
# Output: 2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b  file2.txt

# Answer: the two files produce DIFFERENT hash values -- they are NOT identical
# Even though cat showed the same visible content, the hashes reveal the difference

# ------------------------------------------------------------
# TASK 2 - Compare hashes
# ------------------------------------------------------------

# Write hash of file1.txt to file1hash
sha256sum file1.txt >> file1hash

# Write hash of file2.txt to file2hash
sha256sum file2.txt >> file2hash

# Verify both hash files were created
ls
# Output: file1.txt  file1hash  file2.txt  file2hash

# Display hash stored in file1hash
cat file1hash
# Output: 131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267  file1.txt

# Display hash stored in file2hash
cat file2hash
# Output: 2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b  file2.txt

# Compare the two hash files byte by byte
cmp file1hash file2hash
# Output: file1hash file2hash differ: char 1, line 1
# The hashes differ from the very first character
# Conclusion: file1.txt and file2.txt are NOT identical

# Note: >> operator appends output to a file (creates it if it does not exist)
# Note: cmp reports the first byte and line where files differ
#       char 1, line 1 means the difference starts at the very beginning
