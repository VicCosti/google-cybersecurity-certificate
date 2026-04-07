# 🛡️ Portfolio Activity: Analyze Network Attacks

> **Course:** Google Cybersecurity Professional Certificate — Course 3: Connect and Protect: Networks and Network Security  
> **Type:** Network Attack Analysis / Cybersecurity Incident Report  
> **Tools used:** Wireshark (TCP/HTTP log analysis)  
> **Attack identified:** DoS SYN Flood Attack  

---

## 📋 Scenario Overview

A travel agency's web server became unreachable during working hours. Employees trying to access the company's internal sales webpage (`/sales.html`) received **connection timeout errors**.

As a cybersecurity analyst, the task was to:
- Capture and analyze network traffic using a packet sniffer
- Identify the type of attack from the Wireshark TCP/HTTP log
- Explain how the attack caused the service interruption
- Report findings to management and suggest remediation steps

---

## 🔍 Wireshark Log Analysis

### Network participants

| Color in log | IP Address | Role |
|---|---|---|
| 🟢 Green | `198.51.100.x` | Legitimate employee visitors |
| 🔴 Red | `203.0.113.0` | Attacker (malicious actor) |
| ⚪ White | `192.0.2.1` | Company web server |
| 🟡 Yellow | `192.0.2.1` → employees | Failed/timed-out responses |

### Attack progression

| Log entries | Event |
|---|---|
| 47–51 | Normal TCP three-way handshake and HTTP traffic between employees and server |
| 52–54 | Attacker (`203.0.113.0`) initiates first SYN request — server responds normally |
| 55–62 | Server still handles both attacker SYN requests and legitimate employee traffic |
| 63–83 | Server begins struggling — first timeout errors (`RST, ACK`) appear for employees |
| 119–125 | Server nearly overwhelmed — employee requests consistently failing |
| 125–152 | Server completely unresponsive to legitimate traffic — only attacker SYN requests logged |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`Original_cybersecurity_report.pdf`](./original_Cybersecurity_incident_report.pdf) | Original Blank report (PDF) |
| [`Wireshark_TCP_HTTP_log.pdf`](./Wireshark_TCP_log.pdf) | Wireshark TCP/HTTP log (no color coded) |
| [`Wireshark_Color_Coded_TCP_HTTP_log.pdf`](./Wireshark_Color_coded_TCP_log.pdf) | Wireshark Color Coded TCP/HTTP log |
| [`My_cybersecurity_incident_report.pdf`](./myanswers_Cybersecurity_incident_report.pdf) | My incident report — attack identification, log analysis, and remediation |



<!--

-->
---

## 🧠 Key Concepts Applied

- **TCP Three-Way Handshake** — SYN → SYN/ACK → ACK connection process
- **DoS vs DDoS** — Single-source vs multi-source denial of service attacks
- **SYN Flood Attack** — Exploiting TCP to exhaust server resources
- **Wireshark log analysis** — Identifying attack patterns from packet data
- **Incident Reporting** — Documenting attack type, impact, and response

---

## 📚 What I Learned

- How to read and interpret **Wireshark TCP/HTTP packet logs**
- How a **SYN flood attack** exploits the TCP handshake to overwhelm a server
- The difference between a **DoS** (single source) and **DDoS** (multiple sources) attack
- How to identify **attack patterns** in network traffic (abnormal SYN volume, RST/ACK errors, gateway timeouts)
- How to write a structured **cybersecurity incident report** for management

---

## 🛠️ Tools & Protocols Referenced

![Wireshark](https://img.shields.io/badge/Tool-Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white)
![TCP](https://img.shields.io/badge/Protocol-TCP-blue?style=flat-square)
![HTTP](https://img.shields.io/badge/Protocol-HTTP-orange?style=flat-square)
![DoS](https://img.shields.io/badge/Attack-DoS_SYN_Flood-red?style=flat-square)
![TCP/IP](https://img.shields.io/badge/Model-TCP%2FIP-lightblue?style=flat-square)
