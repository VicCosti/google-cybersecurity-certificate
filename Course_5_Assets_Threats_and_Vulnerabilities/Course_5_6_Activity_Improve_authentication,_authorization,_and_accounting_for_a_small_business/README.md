# 🔑 Portfolio Activity: Access Controls Worksheet

> **Course:** Google Cybersecurity Professional Certificate — Course 5: Assets, Threats, and Vulnerabilities  
> **Type:** Access Control Analysis / Incident Investigation  
> **Framework:** Principle of Least Privilege / Separation of Duties  
> **Control:** AC-6 — Least Privilege | AC-2 — Account Management

---

## 📋 Scenario Overview

A business deposit was made to a fictional bank account — FAUX_BANK — without authorization. A payroll event was logged by the system under suspicious circumstances. The goal was to analyze the event log and the employee directory to identify who was responsible, what went wrong with the access controls, and recommend improvements.

---

## 🔍 Event Log Analysis

```
Event Type:    Information
Event Source:  AdsmEmployeeService
Event ID:      1227
Date:          10/03/2023
Time:          8:29:57 AM
User:          Legal\Administrator
Computer:      Up2-NoGud
IP:            152.207.255.255
Description:   Payroll event added. FAUX_BANK
```

---

## 👥 Employee Directory — Key Entry

| Name | Role | Email | IP Address | Authorization | Status | Last Access | Start Date | End Date |
|---|---|---|---|---|---|---|---|---|
| Robert Taylor Jr. | Legal attorney | rt.jr@erems.net | 152.207.255.255 | Contractor | Admin | 8:29:57 am (5 days ago) | 9/4/2019 | **12/27/2019** |

> The IP address `152.207.255.255` from the event log matches Robert Taylor Jr.'s IP in the employee directory — confirming he is the account responsible for the unauthorized payroll event.

---

## 📊 Access Controls Worksheet

### Authorization / Authentication

The incident was caused by someone who worked with the company, as the user role was administrator — indicating an admin level of authorization. The incident happened on **10/03/2023 at 8:29:57 AM**. The specific IP address is `152.207.255.255` and the device name used was `Up2-NoGud`.

### Issue(s)

By analyzing the employee directory, the access was made by a **contractor** with the role of **Legal attorney**, named **Robert Taylor Jr.** This was confirmed because:
- The IP address `152.207.255.255` matches exactly between the event log and the employee directory
- The last access time of `8:29:57 am (5 days ago)` matches the exact timestamp of the event log

The critical problem is that **this account should have been inactive and without admin authorization** — the contractor's end date was **12/27/2019**, over three years before the incident occurred on 10/03/2023. The account was never deactivated and retained full admin privileges.

### Recommendation(s)

1. **Revoke access for all inactive accounts** — Implement strong security controls to automatically deactivate accounts when their end date is reached. Any contractor or temporary employee whose contract has ended must have their access immediately revoked.

2. **Apply the Principle of Least Privilege** — Least privilege should be enforced at all times. No contractor should hold admin-level access. Contractors who work outside the company should only be granted limited, role-specific access — not administrative privileges.

3. **Implement account deactivation procedures** — Automated deactivation of user accounts after a certain period of inactivity or upon contract expiration should be a standard procedure.

4. **Improve Separation of Duties** — Admin access should not be granted to contractors. A better separation of duties would ensure that external parties only have access to what is strictly necessary for their work.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/1_support_Event_Log.pdf`](./assets/1_support_part_1_Event_Log_Accounting_exercise.pdf) | Event log from the payroll system |
| [`assets/1_support_Employee_directory.pdf`](./assets/1_support_part_2_Employee_directory_Accounting_exercise.pdf) | Employee directory with IP addresses and authorization levels |
| [`assets/2_my_answers_Access_control_worksheet.pdf`](./assets/2_my_answers_Access_control_worksheet.pdf) | My completed access controls worksheet |

---

## 🧠 Key Concepts Applied

- **Access control analysis** — Cross-referencing event logs with employee directories to identify the source of an incident
- **Principle of Least Privilege** — Contractors should only have the minimum access required for their role — never admin-level
- **Account lifecycle management** — Accounts must be deactivated when employment or contracts end
- **Separation of Duties** — Administrative privileges should not be granted to external contractors
- **IP address tracing** — Using IP addresses as forensic evidence to identify the user behind an event
- **AC-6 (Least Privilege) / AC-2 (Account Management)** — NIST SP 800-53 controls directly applicable to this incident

---

## 📚 What I Learned

- How to **cross-reference an event log with an employee directory** to identify the responsible party in a security incident
- That **expired accounts with retained admin privileges** are a critical vulnerability — accounts must be deactivated at contract end
- How the **Principle of Least Privilege** applies specifically to contractors — external parties should never hold admin access
- How **IP addresses serve as forensic evidence** in access control investigations
- The importance of **automated account management** — human error in deactivating accounts creates long-term security risks

---

## 🛠️ Frameworks & Concepts Referenced

![NIST SP 800-53](https://img.shields.io/badge/Standard-NIST_SP_800--53-blue?style=flat-square)
![Least Privilege](https://img.shields.io/badge/Control-Least_Privilege-red?style=flat-square)
![Account Management](https://img.shields.io/badge/Control-Account_Management-orange?style=flat-square)
![Separation of Duties](https://img.shields.io/badge/Control-Separation_of_Duties-purple?style=flat-square)
![Access Control](https://img.shields.io/badge/Concept-Access_Control-green?style=flat-square)
