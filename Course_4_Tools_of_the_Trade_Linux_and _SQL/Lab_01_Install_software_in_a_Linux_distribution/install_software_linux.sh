#!/bin/bash
# ============================================================
# Lab: Install Software in a Linux Distribution
# Course: Google Cybersecurity Professional Certificate
# Course 4: Tools of the Trade - Linux and SQL
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# ============================================================

# ------------------------------------------------------------
# TASK 1 - Confirm APT is installed
# ------------------------------------------------------------

apt

# Expected output:
# apt 2.2.4 (amd64)
# Usage: apt [options] command
# ...

# ------------------------------------------------------------
# TASK 2 - Install Suricata
# ------------------------------------------------------------

sudo apt install suricata
# When prompted "Do you want to continue? [Y/n]" press ENTER

# Verify Suricata installation
suricata

# Expected output:
# Suricata 6.0.1
# USAGE: suricata [OPTIONS] [BPF FILTER]
# ...

# ------------------------------------------------------------
# TASK 2 (cont.) - Uninstall Suricata
# ------------------------------------------------------------

sudo apt remove suricata
# When prompted "Do you want to continue? [Y/n]" press ENTER

# Verify Suricata has been uninstalled
suricata

# Expected output:
# -bash: /usr/bin/suricata: No such file or directory

# ------------------------------------------------------------
# TASK 3 - Install tcpdump
# ------------------------------------------------------------

sudo apt install tcpdump

# Verify tcpdump installation
tcpdump

# Expected output (in sandbox environment without root):
# tcpdump: eth0: You don't have permission to capture on that device
# (socket: Operation not permitted)
# Note: This error is expected in the lab environment.
# It confirms tcpdump is installed — root privileges are required
# to capture live traffic.

# ------------------------------------------------------------
# TASK 4 - List all installed applications
# ------------------------------------------------------------

apt list --installed

# Search for tcpdump in the output:
# tcpdump/oldoldstable,now 4.99.0-2+deb11u1 amd64 [installed]

# Note: Suricata is not listed because it was uninstalled in Task 2

# ------------------------------------------------------------
# TASK 5 - Reinstall Suricata
# ------------------------------------------------------------

sudo apt install suricata
# When prompted "Do you want to continue? [Y/n]" press ENTER

# Verify both applications are now installed
apt list --installed

# Search for both entries in the output:
# suricata/oldoldstable-security,now 1:6.0.1-3+deb11u1 amd64 [installed]
# tcpdump/oldoldstable,now 4.99.0-2+deb11u1 amd64 [installed]
