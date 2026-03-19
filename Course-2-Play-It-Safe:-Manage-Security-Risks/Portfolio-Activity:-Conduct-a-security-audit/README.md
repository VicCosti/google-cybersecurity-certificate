# 🔐 Portfolio Activity: Conduct a Security Audit

> **Course:** Google Cybersecurity Professional Certificate — Course 2: Play It Safe: Manage Security Risks  
> **Framework used:** NIST Cybersecurity Framework (CSF)  
> **Type:** Internal IT Security Audit  
> **Company:** Botium Toys *(fictional scenario)*

---

## 📋 Scenario Overview

Botium Toys is a small U.S. toy company with a growing online presence serving customers in the U.S. and the E.U. The IT department, under increasing pressure to support international operations, commissioned an internal security audit to:

- Identify and mitigate risks, threats, and vulnerabilities
- Ensure compliance with PCI DSS (online payments) and GDPR (E.U. customers)
- Improve the overall security posture of the organization

The IT manager established the audit scope and goals, listed current assets, and completed a risk assessment with a **risk score of 8/10** — indicating a high-risk environment due to missing controls and compliance gaps.

---

## 🎯 Audit Objectives

1. Review the existing scope, goals, and risk assessment report
2. Evaluate current assets managed by the IT department
3. Complete a **Controls Assessment Checklist** based on the NIST CSF
4. Complete a **Compliance Checklist** covering PCI DSS, GDPR, and SOC standards
5. Provide recommendations to improve security posture

---

## 📁 Project Files

| File | Description |
|---|---|
| [`scope-goals-risk-assessment.md`](./scope-goals-risk-assessment.md) | Original audit scope, goals, asset list, and risk assessment |
| [`controls-compliance-checklist.md`](./controls-compliance-checklist.md) | Completed controls and compliance checklist with findings |

---

## 🔍 Key Findings Summary

### Controls Assessment

| Status | Count | Controls |
|---|---|---|
| ✅ In place | 4 | Firewall, Antivirus software, CCTV, Locks, Fire detection |
| ❌ Missing | 9 | Least Privilege, Disaster Recovery, IDS, Backups, Encryption, Password Management, Separation of Duties, Password Policy, Manual monitoring |

### Compliance Gaps

| Standard | Status |
|---|---|
| PCI DSS | ❌ Partially non-compliant — no encryption, no access controls on card data |
| GDPR | ⚠️ Partially compliant — 72h breach notification plan exists, but data not classified |
| SOC type 1/2 | ⚠️ Partially compliant — data integrity maintained, but access policies missing |

---

## 💡 Recommendations

Based on the audit findings, the following controls should be prioritized:

1. **Least Privilege & Separation of Duties** — Immediately restrict access to PII/SPII and cardholder data
2. **Encryption** — Implement encryption for all credit card data at rest and in transit
3. **Disaster Recovery Plan** — Establish backup and recovery procedures to ensure business continuity
4. **Centralized Password Management** — Deploy a password manager and enforce stronger password policies
5. **Intrusion Detection System (IDS)** — Add detective controls to identify anomalous network activity
6. **Asset Classification** — Categorize assets by criticality to prioritize protection efforts

---

## 📚 What I Learned

- How to apply the **NIST CSF Identify function** to assess an organization's security posture
- The difference between **administrative, technical, and physical controls**
- How to evaluate compliance with **PCI DSS**, **GDPR**, and **SOC** frameworks
- How to communicate risk findings and prioritize remediation recommendations

---

## 🛠️ Frameworks & Standards Referenced

![NIST](https://img.shields.io/badge/NIST_CSF-1.1-blue?style=flat-square)
![PCI DSS](https://img.shields.io/badge/PCI_DSS-Compliance-red?style=flat-square)
![GDPR](https://img.shields.io/badge/GDPR-EU_Regulation-003399?style=flat-square)
![SOC](https://img.shields.io/badge/SOC-Type_1_%26_2-green?style=flat-square)
