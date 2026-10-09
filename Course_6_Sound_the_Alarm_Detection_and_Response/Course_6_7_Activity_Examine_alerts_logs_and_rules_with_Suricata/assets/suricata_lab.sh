#!/bin/bash
# ============================================================
# Lab: Examine Alerts, Logs, and Rules with Suricata
# Course 6 — Sound the Alarm: Detection and Response
# Google Cybersecurity Professional Certificate
# ============================================================

# ── TASK 1: Examine the custom rule ─────────────────────────
# Display the Suricata rule defined in custom.rules
cat custom.rules
# Output:
# alert http $HOME_NET any -> $EXTERNAL_NET any \
#   (msg:"GET on wire"; flow:established,to_server; \
#    content:"GET"; http_method; sid:12345; rev:3;)
#
# Rule breakdown:
#   Action  : alert
#   Protocol: http
#   Source  : $HOME_NET (172.21.224.0/20), any port
#   Direction: -> (to external network)
#   Dest    : $EXTERNAL_NET, any port
#   msg     : "GET on wire"  — alert label
#   flow    : established,to_server — match client→server traffic
#   content : "GET" in http_method — detect HTTP GET requests
#   sid     : 12345 — unique signature ID
#   rev     : 3 — rule revision

# ── TASK 2: Trigger the custom rule ─────────────────────────
# Check log directory before running (should be empty)
ls -l /var/log/suricata
# total 0

# Run Suricata against the sample pcap using our custom rule
sudo suricata -r sample.pcap -S custom.rules -k none
# -r sample.pcap  : read from packet capture file (simulate network traffic)
# -S custom.rules : use only our custom rules file
# -k none         : disable checksum validation (not needed for pcap files)
#
# Output:
# i: suricata: This is Suricata version 7.0.10 RELEASE running in USER mode
# i: pcap: read 1 file, 200 packets, 54238 bytes

# Check log directory after running (4 new files created)
ls -l /var/log/suricata
# -rw-r--r-- 1 root root 1673 Oct  9 09:13 eve.json
# -rw-r--r-- 1 root root  292 Oct  9 09:13 fast.log
# -rw-r--r-- 1 root root 4029 Oct  9 09:13 stats.log
# -rw-r--r-- 1 root root 2008 Oct  9 09:13 suricata.log

# Read the fast.log — quick-check alert format (deprecated but useful for QA)
cat /var/log/suricata/fast.log
# 11/23/2022-12:38:34.624866  [**] [1:12345:3] GET on wire [**] \
#   [Classification: (null)] [Priority: 3] {TCP} 172.21.224.2:49652 -> 142.250.1.139:80
# 11/23/2022-12:38:58.958203  [**] [1:12345:3] GET on wire [**] \
#   [Classification: (null)] [Priority: 3] {TCP} 172.21.224.2:58494 -> 142.250.1.102:80
#
# 2 alerts triggered: both from internal host 172.21.224.2 to Google IPs on port 80
# Format: [gid:sid:rev]  message  {proto}  src -> dst

# ── TASK 3: Examine eve.json output ─────────────────────────
# Display raw eve.json (verbose, hard to read)
cat /var/log/suricata/eve.json

# Pretty-print with jq (pipe to less for pagination)
jq . /var/log/suricata/eve.json | less
# First alert severity value: 3
# Key fields per alert:
#   event_type  : "alert"
#   src_ip      : 172.21.224.2 (internal host)
#   dest_ip     : 142.250.1.139 (first alert) / 142.250.1.102 (second alert)
#   dest_port   : 80
#   proto       : TCP
#   alert.signature : "GET on wire"
#   alert.severity  : 3
#   http.hostname   : opensource.google.com
#   http.method     : GET
#   http.status     : 301 (redirect to HTTPS)
#   http.redirect   : https://opensource.google/
#   http_user_agent : curl/7.74.0

# Extract specific fields from both events (compact output)
jq -c "[.timestamp,.flow_id,.alert.signature,.proto,.dest_ip]" /var/log/suricata/eve.json
# ["2022-11-23T12:38:34.624866+0000",695533784871914,"GET on wire","TCP","142.250.1.139"]
# ["2022-11-23T12:38:58.958203+0000",726728852993465,"GET on wire","TCP","142.250.1.102"]
# Last event destination IP: 142.250.1.102

# Filter all events by flow_id (correlate packets within a single network flow)
jq "select(.flow_id==695533784871914)" /var/log/suricata/eve.json
# Returns full event details for flow 695533784871914:
#   4 packets sent to server, 3 received from server
#   Total bytes: 357 toserver / 788 toclient
