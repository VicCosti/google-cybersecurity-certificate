# 🔒 Portfolio Activity: Apply OS Hardening Techniques

> **Course:** Google Cybersecurity Professional Certificate — Course 3: Connect and Protect: Networks and Network Security  
> **Type:** Security Incident Report / OS Hardening  
> **Tools used:** tcpdump  
> **Attack identified:** Brute Force Attack + Malware Injection  
> **Protocols analyzed:** DNS, HTTP  

---

## 📋 Scenario Overview

The cooking website `yummyrecipesforme.com` was compromised by a former employee who executed a **brute force attack** to gain access to the admin panel. After guessing the default admin password, the attacker:

1. Injected a **JavaScript function** into the website's source code
2. The script prompted visitors to download a malicious executable file
3. Running the file **redirected users to a fake malicious website** — `greatrecipesforme.com`
4. Changed the admin password, locking out the legitimate owner

Multiple customers reported that after downloading the file their browsers were redirected and their computers began running slowly. The website owner was unable to log back into the admin panel.

As a cybersecurity analyst, the task was to:
- Analyze the tcpdump traffic log from a sandbox environment
- Identify the network protocols involved in the attack
- Document the incident in detail
- Recommend security measures to prevent future brute force attacks

---

## 🔍 tcpdump Log Summary

| Time | Event |
|---|---|
| `14:18:32` | Browser sends DNS request for `yummyrecipesforme.com` → DNS replies with IP `203.0.113.22` |
| `14:18:36` | Browser establishes HTTP connection to `yummyrecipesforme.com` (TCP three-way handshake) |
| `14:18:36` | `HTTP GET / HTTP/1.1` — webpage loads, malware download is triggered |
| `14:18:36–14:20:32` | Large volume of HTTP traffic on port 80 — malware file download in progress |
| `14:20:32` | Browser sends DNS request for `greatrecipesforme.com` → DNS replies with IP `192.0.2.17` |
| `14:25:29` | Browser establishes HTTP connection to `greatrecipesforme.com` — malicious site loaded |

### Protocols involved

| Layer (TCP/IP Model) | Protocol | Role |
|---|---|---|
| Application | DNS | Domain name resolution for both websites |
| Application | HTTP | Website requests and malware download (port 80) |
| Transport | TCP | Connection establishment (three-way handshake) |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`tcpdump_traffic_log.pdf`](./tcpdump_traffic_log.pdf) | Original tcpdump traffic log |
| [`My_Completed_security_incident_report.pdf`](./myanswers_Security_incident_report.pdf) | My completed report (PDF) |

---

## 🧠 Key Concepts Applied

- **Brute Force Attacks** — How attackers exploit weak/default passwords to gain unauthorized access
- **DNS & HTTP protocols** — How they are used and abused at the application layer
- **Malware injection via source code** — How a compromised admin panel can affect all website visitors
- **tcpdump log analysis** — Tracing the full attack chain from DNS request to malicious redirect
- **OS Hardening** — Security measures to reduce attack surface and prevent future incidents

---

## 📚 What I Learned

- How to trace a **multi-step attack** through a tcpdump log (DNS → HTTP → malware → redirect)
- How a **brute force attack** on weak/default credentials can lead to full website compromise
- The importance of **application layer protocol security** (HTTP vs HTTPS)
- How to write a structured **security incident report** with protocol identification, documentation, and remediation
- Practical **OS and web hardening techniques** — MFA, password policies, login attempt limits, network segmentation

---

## 🛠️ Tools, Protocols & Concepts Referenced

![tcpdump](https://img.shields.io/badge/Tool-tcpdump-darkgreen?style=flat-square)
![DNS](https://img.shields.io/badge/Protocol-DNS-orange?style=flat-square)
![HTTP](https://img.shields.io/badge/Protocol-HTTP-blue?style=flat-square)
![Brute Force](https://img.shields.io/badge/Attack-Brute_Force-red?style=flat-square)
![MFA](https://img.shields.io/badge/Defense-MFA%2F2FA-green?style=flat-square)
![OS Hardening](https://img.shields.io/badge/Technique-OS_Hardening-lightblue?style=flat-square)
