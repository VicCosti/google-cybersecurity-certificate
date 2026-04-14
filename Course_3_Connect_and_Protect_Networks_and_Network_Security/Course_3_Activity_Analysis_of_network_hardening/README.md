# 🔐 Portfolio Activity: Analysis of Network Hardening

> **Course:** Google Cybersecurity Professional Certificate — Course 3: Connect and Protect: Networks and Network Security  
> **Type:** Security Risk Assessment Report / Network Hardening  
> **Focus:** Network Hardening Tools & Methods  

---

## 📋 Scenario Overview

A social media organization experienced a **major data breach** that compromised customers' personal information (names and addresses). After inspecting the network, four critical vulnerabilities were identified:

| # | Vulnerability |
|---|---|
| 1 | Employees share passwords |
| 2 | Admin database password is set to default |
| 3 | Firewalls have no rules to filter incoming/outgoing traffic |
| 4 | Multifactor Authentication (MFA) is not in use |

As a security analyst, the task was to:
- Select the most effective network hardening tools to address the vulnerabilities
- Explain why each method is effective and how frequently it should be implemented
- Write a security risk assessment report with prioritized recommendations

---

## 🛡️ Hardening Tools Selected

### Priority 1 — Immediate Implementation

| Tool / Method | Vulnerability addressed |
|---|---|
| **Multifactor Authentication (MFA)** | Password sharing, brute force attacks, unauthorized access |
| **Password Policies** | Default admin password, shared passwords, brute force attacks |
| **Network Access Privileges** | Unauthorized internal access to sensitive data and database |

### Priority 2 — Follow-up Implementation

| Tool / Method | Vulnerability addressed |
|---|---|
| **Encryption (latest standards)** | Data confidentiality in transit and at rest |
| **Firewall Maintenance** | No traffic filtering rules on the network perimeter |
| **Port Filtering** | Unused open ports as potential entry points |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`Network_hardening_tools.pdf`](./Network_hardening_tools.pdf) | Reference guide for network hardening tools |
| [`my_selection_hardening_tools.pdf`](./myselection_Network_hardening_tools.pdf) | Selected hardening tools (my worksheet selection) |
| [`my_completed_security_risk_assessment.pdf`](./myanswers_Security_risk_assessment_report.pdf) | My completed report (PDF) |

---

## 🧠 Key Concepts Applied

- **Network Hardening** — Identifying and reducing the attack surface of an organization's network
- **MFA / 2FA** — Adding authentication layers to prevent unauthorized access
- **Password Policies (NIST)** — Salting, hashing, and complexity requirements
- **Network Access Privileges** — Least privilege principle applied at the network level
- **Firewall Maintenance & Port Filtering** — Perimeter defence and traffic control
- **Encryption** — Protecting data confidentiality in transit and at rest
- **Risk Prioritization** — Ranking hardening measures by urgency and impact

---

## 📚 What I Learned

- How to evaluate **network vulnerabilities** and map them to appropriate hardening tools
- The difference between **one-time** hardening tasks (MFA, access privileges) and **recurring** ones (firewall maintenance, patch updates, password rotation)
- How to write a structured **security risk assessment report** with prioritized recommendations
- How **layered defences** (defence in depth) work together to reduce overall risk

---

## 🛠️ Tools & Methods Referenced

![MFA](https://img.shields.io/badge/Defense-MFA%2F2FA-green?style=flat-square)
![Password Policy](https://img.shields.io/badge/Defense-Password_Policies-blue?style=flat-square)
![Firewall](https://img.shields.io/badge/Defense-Firewall_Maintenance-orange?style=flat-square)
![Encryption](https://img.shields.io/badge/Defense-Encryption-purple?style=flat-square)
![Port Filtering](https://img.shields.io/badge/Defense-Port_Filtering-red?style=flat-square)
![Network Access](https://img.shields.io/badge/Defense-Network_Access_Privileges-lightblue?style=flat-square)
