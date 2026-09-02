# 🛡️ Portfolio Activity: Vulnerability Assessment Report

> **Course:** Google Cybersecurity Professional Certificate — Course 5: Assets, Threats, and Vulnerabilities  
> **Type:** Vulnerability Assessment / Risk Analysis  
> **Framework:** NIST SP 800-30 Rev. 1 — Guide to Assessing Risk  
> **Period:** June 20XX – August 20XX

---

## 📋 Scenario Overview

A small business operates a publicly accessible database server that stores sensitive customer data and is used daily by employees to identify potential customers. The server has no access restrictions — anyone on the internet can connect to it. The goal was to conduct a vulnerability assessment using NIST SP 800-30 Rev. 1 to analyze threats, score risks, and recommend a remediation strategy.

---

## 🖥️ System Description

| Component | Details |
|---|---|
| Hardware | Powerful CPU, 128GB RAM |
| Operating System | Latest Linux version |
| Database | MySQL DBMS |
| Network | IPv4, connected to other servers |
| Security (current) | SSL/TLS encrypted connections |
| Exposure | **Publicly accessible** — no access restrictions |

---

## 🎯 Scope & Purpose

**Scope:** Current access controls of the system — June 20XX to August 20XX  
**Framework:** NIST SP 800-30 Rev. 1

**Purpose:** The database is critical to daily business operations — employees use it to query data and identify potential customers. It stores sensitive information including PII, competitive intelligence, and internal company data. Unauthorized access, data manipulation, or server disruption could freeze core business operations entirely. With no backup server in place, any data loss would be permanent.

---

## 📊 Risk Assessment

| Threat Source | Threat Event | Likelihood | Severity | Risk Score |
|---|---|---|---|---|
| Competitor | Obtain sensitive information via exfiltration | 1 | 3 | **3** |
| Hacker | Install persistent network sniffers on organizational systems | 2 | 2 | **4** |
| Hacktivist | Alter/Delete critical information + DoS attack | 3 | 3 | **9** |

> **Formula:** Likelihood × Severity = Risk Score

---

## 🔍 Risk Analysis — Approach

**Competitor (Risk: 3 — Low)**  
Competitors could access the database and obtain information about potential customers in advance. This could lead to significant sales failures — competitors contacting leads before the company's own employees. Despite the low risk score, the business impact is substantial.

**Hacker (Risk: 4 — Moderate)**  
Without proper access controls, hackers could install persistent network sniffers to intercept data. This could result in sensitive data being sold to external actors, leading to both financial and security consequences — including exposure of PII.

**Hacktivist (Risk: 9 — Critical)**  
The most critical threat. A hacktivist could alter or permanently delete critical data. With no backup server in place, data loss would be irreversible. A DoS attack would take the entire company offline — employees would lose access to the database entirely, halting all business operations.

---

## 💊 Remediation Strategy

1. **Authentication, Authorization & Auditing (AAA)**  
   Implement strong passwords, role-based access controls (RBAC), and multi-factor authentication (MFA). Apply the Principle of Least Privilege and Separation of Duties to limit user privileges.

2. **Encryption upgrade — TLS + PKI**  
   Replace SSL with TLS for encrypted data in motion. Implement a PKI framework to prevent external actors from intercepting data.

3. **IP allow-listing**  
   Restrict database access to corporate office IP addresses only — preventing random internet users from connecting.

4. **Backup server**  
   Create a backup server to prevent permanent data loss in the event of a destructive attack or accidental deletion.

5. **Defence in depth**  
   Implement layered security at both the network layer (firewall) and the perimeter layer (authentication systems). A multi-layer approach reduces the risk of any single point of failure.

6. **IPv4 → IPv6 migration**  
   Migrating to IPv6 would improve the overall security posture of the network environment.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/1_NIST_SP_800-30_Rev1_reference.pdf`](./assets/1_supporting_material_NIST_SP_800-30_Rev__1.pdf) | NIST SP 800-30 Rev. 1 reference guide used for the assessment |
| [`assets/2_mycompletedwork_Vulnerability_assessment_report.pdf`](./assets/2_mycompletedwork_Vulnerability_assessment_report.pdf) | My completed vulnerability assessment report |

---

## 🧠 Key Concepts Applied

- **NIST SP 800-30 Rev. 1** — Framework for conducting risk assessments, identifying threat sources and threat events
- **Risk scoring** — Likelihood × Severity = Risk Score (1–9 scale)
- **Threat sources** — Outsiders (hacker, hacktivist), groups (competitor)
- **Threat events** — Data exfiltration, network sniffing, data destruction, DoS attack
- **Remediation strategy** — AAA controls, TLS/PKI, IP allow-listing, backup, defence in depth
- **Principle of Least Privilege** — Limiting user access to only what is required
- **Defence in depth** — Layered security approach across network and perimeter

---

## 📚 What I Learned

- How to apply **NIST SP 800-30 Rev. 1** to conduct a structured vulnerability assessment
- How to identify and categorize **threat sources** (standard user, privileged user, outsider, group) and **threat events**
- How to calculate **risk scores** and use them to prioritize remediation efforts
- That a **publicly accessible database with no access controls** represents a critical vulnerability regardless of encryption
- The importance of **backup servers** — without one, a destructive attack causes irreversible damage
- How **defence in depth** layers multiple security controls to reduce overall risk

---

## 🛠️ Frameworks & Concepts Referenced

![NIST SP 800-30](https://img.shields.io/badge/Framework-NIST_SP_800--30-blue?style=flat-square)
![Risk Assessment](https://img.shields.io/badge/Skill-Risk_Assessment-orange?style=flat-square)
![Least Privilege](https://img.shields.io/badge/Control-Least_Privilege-red?style=flat-square)
![Defence in Depth](https://img.shields.io/badge/Strategy-Defence_in_Depth-purple?style=flat-square)
![TLS/PKI](https://img.shields.io/badge/Security-TLS%2FPKI-green?style=flat-square)
![MFA](https://img.shields.io/badge/Control-MFA-darkgreen?style=flat-square)
