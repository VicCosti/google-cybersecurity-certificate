#!/bin/bash
# ============================================================
# Lab: Capture Your First Packet
# Course: Google Cybersecurity Professional Certificate
# Course 6: Sound the Alarm: Detection and Response
# Platform: Google Skills / Qwiklabs (Debian-based VM)
# ============================================================

# Key concepts:
# tcpdump -- command-line packet analyzer for capturing live traffic
# pcap   -- packet capture file format for storing network data
# -v     -- verbose mode (more packet detail)
# -nn    -- no DNS resolution (show raw IPs and port numbers)
# -X     -- show packet contents in hex AND ASCII
# -w     -- write captured packets to a file
# -r     -- read packets from a file
# &      -- run command in background (allows parallel execution)

# ------------------------------------------------------------
# TASK 1 - Identify network interfaces
# ------------------------------------------------------------

# List all network interfaces and their configuration
sudo ifconfig
# Output shows two interfaces:
#
# eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1460
#   inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255
#   ether 02:42:ac:11:00:02
#   RX packets 700  bytes 14783152 (14.0 MiB)
#   TX packets 348  bytes 33567 (32.7 KiB)
#
# lo: flags=73<UP,LOOPBACK,RUNNING> mtu 65536
#   inet 127.0.0.1  netmask 255.0.0.0
#   (loopback interface -- internal traffic only)
#
# Key info:
# eth0 IP: 172.17.0.2 (this is the machine we will capture on)
# MAC:     02:42:ac:11:00:02

# List all interfaces available for tcpdump capture
sudo tcpdump -D
# Output:
# 1.eth0          [Up, Running, Connected]
# 2.any           (Pseudo-device that captures on all interfaces)
# 3.lo            [Up, Running, Loopback]
# 4.bluetooth-monitor
# 5.nflog
# 6.nfqueue
# 7.dbus-system
# 8.dbus-session
#
# Answer: eth0 is the primary network interface for capture

# ------------------------------------------------------------
# TASK 2 - Inspect network traffic with tcpdump (live capture)
# ------------------------------------------------------------

# Capture 5 packets on eth0 with verbose output
sudo tcpdump -i eth0 -v -c5
# Options:
# -i eth0  -- capture on eth0 interface
# -v       -- verbose output (shows TTL, checksum, flags, etc.)
# -c5      -- capture exactly 5 packets then stop
#
# Sample output (first capture):
# TCP: ffe0baba1c1f.5000 > nginx-us-west1-b...42366 [P.] length 71
# TCP: nginx-us-west1-b...42366 > ffe0baba1c1f.5000 [.] length 0
# UDP: ffe0baba1c1f.41642 > metadata.google.internal.domain PTR? 196.0.19.172.in-addr.arpa.
# UDP: metadata.google.internal.domain > ffe0baba1c1f.41642 PTR nginx-us-west1-b...
# TCP: ffe0baba1c1f.5000 > nginx-us-west1-b...42366 [P.] length 325
# 5 packets captured -- 8 received by filter -- 0 dropped

# Note on checksum "incorrect" warnings:
# These are NOT real errors. This is "checksum offloading" --
# the virtual NIC calculates checksums at the hardware level.
# tcpdump captures packets BEFORE the checksum is computed,
# so they appear incorrect in the log. This is expected behavior
# in virtualized environments.

# Run a second live capture (5 packets)
sudo tcpdump -i eth0 -v -c5
# Similar traffic observed: TCP to nginx server + UDP DNS PTR query
# 5 packets captured -- 10 received by filter -- 0 dropped

# ------------------------------------------------------------
# TASK 3 - Capture network traffic with tcpdump to a file
# ------------------------------------------------------------

# Start tcpdump in BACKGROUND, capture 9 port 80 packets, save to file
sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &
# Options:
# -i eth0      -- capture on eth0
# -nn          -- no hostname/port resolution (show raw IPs and numbers)
# -c9          -- capture exactly 9 packets
# port 80      -- filter: only HTTP traffic on port 80
# -w capture.pcap -- write to file instead of printing to screen
# &            -- run in background (allows next command to run)
#
# Output: [1] 684 (background job PID)
# tcpdump: listening on eth0 ...

# Generate HTTP traffic to capture (while tcpdump runs in background)
curl opensource.google.com
# curl sends an HTTP GET request to opensource.google.com
# Response: HTTP 301 Moved Permanently (redirect to HTTPS)
#
# After 9 packets captured:
# 9 packets captured -- 10 received by filter -- 0 dropped

# Verify the capture file was created
ls -l capture.pcap
# Output: -rw-r--r-- 1 tcpdump tcpdump 1401 Sep 21 10:03 capture.pcap
# File size: 1401 bytes -- confirms packets were written successfully

# ------------------------------------------------------------
# TASK 4 - Filter captured packet data
# ------------------------------------------------------------

# Read and display capture.pcap with verbose output
sudo tcpdump -nn -r capture.pcap -v
# Options:
# -nn       -- no name resolution
# -r        -- read from file
# -v        -- verbose output
#
# 9 packets captured -- full TCP conversation:
# 1. [S]   172.17.0.2.37880  > 173.194.43.101.80  -- TCP SYN (connection request)
# 2. [S.]  173.194.43.101.80 > 172.17.0.2.37880   -- TCP SYN/ACK (connection accepted)
# 3. [.]   172.17.0.2.37880  > 173.194.43.101.80  -- TCP ACK (handshake complete)
# 4. [P.]  172.17.0.2.37880  > 173.194.43.101.80  -- HTTP GET / HTTP/1.1
# 5. [.]   173.194.43.101.80 > 172.17.0.2.37880   -- TCP ACK
# 6. [P.]  173.194.43.101.80 > 172.17.0.2.37880   -- HTTP/1.1 301 Moved Permanently
# 7. [.]   172.17.0.2.37880  > 173.194.43.101.80  -- TCP ACK
# 8. [F.]  172.17.0.2.37880  > 173.194.43.101.80  -- TCP FIN (connection close)
# 9. [F.]  173.194.43.101.80 > 172.17.0.2.37880   -- TCP FIN/ACK (close confirmed)
#
# Full HTTP exchange visible in verbose output:
# GET / HTTP/1.1
# Host: opensource.google.com
# User-Agent: curl/7.88.1
# Accept: */*
#
# HTTP/1.1 301 Moved Permanently
# Location: https://opensource.google/
# Server: sffe
# Date: Mon, 21 Sep 2026 10:03:38 GMT

# Read capture.pcap in hex AND ASCII format
sudo tcpdump -nn -r capture.pcap -X
# Options:
# -X   -- display packet contents in both hex and ASCII side by side
#
# This reveals the raw packet bytes alongside readable ASCII:
# Packet 4 (HTTP GET) hex shows:
# 0x0030: f644 305c 4745 5420 2f20 4854 5450 2f31  .D0\GET./.HTTP/1
# 0x0040: 2e31 0d0a 486f 7374 3a20 6f70 656e 736f  .1..Host:.openso
# 0x0050: 7572 6365 2e67 6f6f 676c 652e 636f 6d0d  urce.google.com.
# 0x0060: 0a55 7365 722d 4167 656e 743a 2063 7572  .User-Agent:.cur
# 0x0070: 6c2f 372e 3838 2e31                      l/7.88.1
#
# Packet 6 (HTTP 301) hex shows full response headers in readable ASCII:
# HTTP/1.1 301 Moved Permanently
# Location: https://opensource.google/
# This demonstrates that HTTP traffic is UNENCRYPTED --
# anyone capturing the traffic can read the full content.
