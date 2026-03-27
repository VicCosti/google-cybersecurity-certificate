# 🌐 Portfolio Activity: Analyze Network Layer Communication

> **Course:** Google Cybersecurity Professional Certificate — Course 3: Connect and Protect: Networks and Network Security  
> **Type:** Network Traffic Analysis / Cybersecurity Incident Report  
> **Tools used:** tcpdump  
> **Protocols analyzed:** UDP, DNS, ICMP

---

## 📋 Scenario Overview

Several customers reported being unable to access the website `www.yummyrecipesforme.com`, receiving the error **"destination port unreachable"** after waiting for the page to load.

As a cybersecurity analyst, the task was to:
- Reproduce the issue and capture network traffic using **tcpdump**
- Analyze the DNS and ICMP packets in the log
- Identify which network protocol and service were affected
- Write a cybersecurity incident report with findings and next steps

---

## 🔍 tcpdump Log Overview

```
13:24:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)
13:24:36.098564 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 udp port 53 unreachable length 254

13:26:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)
13:27:15.934126 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 udp port 53 unreachable length 320

13:28:32.192571 IP 192.51.100.15.52444 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com. (24)
13:28:50.022967 IP 203.0.113.2 > 192.51.100.15: ICMP 203.0.113.2 udp port 53 unreachable length 150
```

| Field | Value |
|---|---|
| Source IP (client) | `192.51.100.15` |
| Destination IP (DNS server) | `203.0.113.2` |
| Protocol (outgoing) | UDP |
| Port (targeted) | 53 — DNS |
| Error response protocol | ICMP |
| Error message | `udp port 53 unreachable` |
| Attempts logged | 3 |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`tcpdump_log_udp_error.jpg`](./tcpdump_log_udp_error.jpg) | Screenshot of the tcpdump log |
| [`original_Cybersecurity_incident_report_network_traffic_analysis.pdf`](./original_Cybersecurity_incident_report_network_traffic_analysis.pdf) | Original empty incident report (PDF) |
| [`my_answers_Cybersecurity_incident_report_network_traffic_analysis.pdf`](./my_answers_Cybersecurity_incident_report_network_traffic_analysis.pdf) | My completed incident report answers (PDF) |

<!--
| [`cybersecurity-incident-report.md`](./cybersecurity-incident-report.md) | Full incident report — tcpdump analysis, findings, and next steps |
| [`cybersecurity-incident-report.md`](./cybersecurity-incident-report.md) | Full incident report — tcpdump analysis, findings, and next steps |
-->
---

## 🧠 Key Concepts Applied

- **TCP/IP Model** — Internet layer analysis using IP datagrams
- **UDP vs ICMP** — Understanding request/response protocols at the network layer
- **DNS (Port 53)** — How domain name resolution works and what happens when it fails
- **tcpdump** — Reading and interpreting packet capture logs
- **Incident Reporting** — Documenting findings, timeline, and remediation steps

---

## 📚 What I Learned

- How to read and interpret **tcpdump packet logs**
- The role of **UDP** in DNS queries and why **ICMP** returns error messages when a port is unreachable
- How to identify the **affected protocol and service** from raw network data
- How to structure a professional **cybersecurity incident report**

---

## 🛠️ Tools & Protocols Referenced

![tcpdump](https://img.shields.io/badge/Tool-tcpdump-darkgreen?style=flat-square)
![UDP](https://img.shields.io/badge/Protocol-UDP-blue?style=flat-square)
![DNS](https://img.shields.io/badge/Protocol-DNS_Port_53-orange?style=flat-square)
![ICMP](https://img.shields.io/badge/Protocol-ICMP-red?style=flat-square)
![TCP/IP](https://img.shields.io/badge/Model-TCP%2FIP-lightblue?style=flat-square)
