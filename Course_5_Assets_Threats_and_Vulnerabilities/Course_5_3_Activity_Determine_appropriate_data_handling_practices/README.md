# 🔒 Portfolio Activity: Determine Appropriate Data Handling Practices

> **Course:** Google Cybersecurity Professional Certificate — Course 5: Assets, Threats, and Vulnerabilities  
> **Type:** Data Privacy / Least Privilege Analysis  
> **Framework:** NIST SP 800-53: AC-6 — Least Privilege  
> **Control:** PR.DS-5 — Protections against data leaks

---

## 📋 Scenario Overview

An educational technology company experienced a data leak when an employee accidentally shared a link to an internal folder — instead of just the promotional materials — with an external business partner during a sales call. The business partner then posted the link on social media.

The goal was to analyze the incident, review NIST SP 800-53: AC-6, and recommend control enhancements to prevent similar leaks in the future.

---

## 📊 Data Leak Worksheet

### Incident Summary

A sales manager shared access to a folder of internal-only documents with their team during a meeting. The folder contained files related to a new unannounced product, customer analytics, and promotional materials. After the meeting, the manager did not revoke access to the folder.

During a video call, a sales representative accidentally shared a link to the entire internal folder instead of just the promotional materials. The business partner posted the link on their company's social media page, causing a data leak.

---

### Control: Least Privilege

| Section | Content |
|---|---|
| **Issue(s)** | The factors that contributed to the information leak were: the sharing of the internal-only folder with the team without proper access restrictions; the failure to revoke access after the meeting; and the absence of security measures protecting the folder — such as access controls that would prevent unauthorized sharing with external parties. |
| **Review** | NIST SP 800-53: AC-6 addresses protections against data leaks through the principle of least privilege — granting users only the minimal access and authorization required to complete a task or function. It provides control enhancements to improve the effectiveness of this principle within an organization. |
| **Recommendation(s)** | **1.** Implement user roles to restrict access to sensitive resources only to users with the appropriate privilege level. **2.** Implement automatic revocation of access after a set period of time, especially for users who do not have the required privilege level to retain access. |
| **Justification** | These improvements would protect data from unauthorized access — both intentional and unintentional — inside and outside the company. If role-based access controls had been in place, the sales representative would not have had permission to share the internal folder link with an external party. Automatic access revocation would have closed the window of exposure after the meeting. |

---

## 📋 NIST SP 800-53: AC-6 Reference

### Control
Only the minimal access and authorization required to complete a task or function should be provided to users.

### Discussion
Processes, user accounts, and roles should be enforced as necessary to achieve least privilege. The intention is to prevent a user from operating at privilege levels higher than what is necessary to accomplish business objectives.

### Control Enhancements
- Restrict access to sensitive resources based on user role
- Automatically revoke access to information after a period of time
- Keep activity logs of provisioned user accounts
- Regularly audit user privileges

---

## 🗺️ NIST CSF Security Plan Snapshot

| Function | Category | Subcategory | Reference |
|---|---|---|---|
| Protect | PR.DS: Data security | PR.DS-5: Protections against data leaks | NIST SP 800-53: AC-6 |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/completed_Data_leak_worksheet.pdf`](./assets/completed_Activity_Template_Data_leak_worksheet.pdf) | My completed data leak worksheet |

---

## 🧠 Key Concepts Applied

- **Principle of Least Privilege** — Users should only have access to the minimum data necessary to perform their job
- **NIST SP 800-53: AC-6** — Federal security control standard for implementing least privilege
- **Data leak root cause analysis** — Identifying the chain of events and control failures that led to the incident
- **Role-based access control (RBAC)** — Restricting data access based on a user's role within the organization
- **Automatic access revocation** — Time-limited access to reduce the window of exposure after a task is complete
- **NIST CSF PR.DS-5** — Protection category specifically addressing data leak prevention

---

## 📚 What I Learned

- How the **principle of least privilege** reduces the risk of both accidental and malicious data leaks
- How **NIST SP 800-53: AC-6** provides specific, actionable control enhancements for implementing least privilege
- That **data leaks often result from a chain of small failures** — oversharing access, not revoking it, and lacking safeguards against external sharing
- How to map a security incident to a **NIST CSF control** and recommend concrete improvements
- The importance of **role-based access controls** and **automatic revocation** as technical controls that reduce human error impact

---

## 🛠️ Frameworks & Concepts Referenced

![NIST CSF](https://img.shields.io/badge/Framework-NIST_CSF-blue?style=flat-square)
![NIST SP 800-53](https://img.shields.io/badge/Standard-NIST_SP_800--53-orange?style=flat-square)
![Least Privilege](https://img.shields.io/badge/Control-Least_Privilege-red?style=flat-square)
![Data Privacy](https://img.shields.io/badge/Concept-Data_Privacy-green?style=flat-square)
![RBAC](https://img.shields.io/badge/Control-RBAC-purple?style=flat-square)
