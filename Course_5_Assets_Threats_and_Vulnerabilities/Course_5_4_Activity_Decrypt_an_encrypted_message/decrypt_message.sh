#!/bin/bash
# ============================================================
# Lab: Decrypt an Encrypted Message
# Course: Google Cybersecurity Professional Certificate
# Course 5: Assets, Threats, and Vulnerabilities
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# ============================================================

# Concepts covered:
# - Caesar cipher decryption using tr command
# - AES-256-CBC symmetric encryption/decryption using openssl
# - Hidden files in Linux (files starting with .)

# ------------------------------------------------------------
# TASK 1 - Read the contents of a file
# ------------------------------------------------------------

# List contents of home directory
ls
# Output: Q1.encrypted  README.txt  caesar

# Read the README instructions
cat README.txt
# Output:
# Hello,
# All of your data has been encrypted. To recover your data,
# you will need to solve a cipher. To get started look for a
# hidden file in the caesar subdirectory.

# ------------------------------------------------------------
# TASK 2 - Find a hidden file and decrypt the Caesar cipher
# ------------------------------------------------------------

# Navigate to the caesar subdirectory
cd caesar

# List ALL files including hidden ones (starting with .)
ls -a
# Output: .  ..  .leftShift3
# → .leftShift3 is a hidden file (starts with .)

# Read the hidden file — contents appear scrambled (Caesar cipher)
cat .leftShift3
# Output (encrypted):
# Lq rughu wr uhfryhu brxu ilohv brx zloo qhhg wr hqwhu wkh iroorzlqj frppdqg:
# rshqvvo dhv-256-fef -sengi2 -d -g -lq T1.hqfubswhg -rxw T1.uhfryhuhg -n hwwxeuxwh

# Decrypt the Caesar cipher using tr (left shift of 3 positions)
cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"
# Output (decrypted):
# In order to recover your files you will need to enter the following command:
# openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute

# Note: The tr command maps each character from the first set to the second set
# "d-za-cD-ZA-C" → "a-zA-Z" shifts all letters 3 positions to the left
# 'd' becomes 'a', 'e' becomes 'b', 'f' becomes 'c', etc.

# Return to home directory
cd ~

# ------------------------------------------------------------
# TASK 3 - Decrypt the encrypted file using openssl
# ------------------------------------------------------------

# Decrypt Q1.encrypted using the key revealed by the Caesar cipher
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute

# Command breakdown:
# openssl          → cryptographic toolkit
# aes-256-cbc      → symmetric cipher (AES, 256-bit key, CBC mode)
# -pbkdf2          → key derivation function for extra security
# -a               → base64 encoding for the output
# -d               → decrypt mode (vs -e for encrypt)
# -in Q1.encrypted → input file to decrypt
# -out Q1.recovered → output file for decrypted content
# -k ettubrute     → password/key used for decryption

# Verify the new file was created
ls
# Output: Q1.encrypted  Q1.recovered  README.txt  caesar

# Read the decrypted message
cat Q1.recovered
# Output:
# If you are able to read this, then you have successfully decrypted
# the classic cipher text. You recovered the encryption key that was
# used to encrypt this file. Great work!
