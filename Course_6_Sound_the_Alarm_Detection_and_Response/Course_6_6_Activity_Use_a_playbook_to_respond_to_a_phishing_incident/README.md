# 📧 Portfolio Activity: Use a Playbook to Respond to a Phishing Incident

> **Course:** Google Cybersecurity Professional Certificate — Course 6: Sound the Alarm: Detection and Response  
> **Type:** Incident Response / Alert Triage  
> **Playbook:** Phishing Incident Response Playbook v1.0  
> **Tool:** VirusTotal  
> **Ticket ID:** A-2703 | **Final Status:** Escalated

---

## 📋 Scenario Overview

A SOC Level-1 analyst received an alert about a possible phishing attempt involving a malicious file download. Following the **Phishing Incident Response Playbook v1.0**, the analyst investigated the alert details, analyzed the email and its attachment, verified the file hash on VirusTotal, and escalated the ticket to a Level-2 analyst.

---

## 🎫 Alert Ticket — A-2703

| Field | Value |
|---|---|
| **Ticket ID** | A-2703 |
| **Alert Message** | SERVER-MAIL Phishing attempt possible download of malware |
| **Severity** | Medium |
| **Details** | The user may have opened a malicious email and opened attachments or clicked links |
| **Final Status** | **Escalated** |

---

## 📬 Phishing Email Analysis

| Field | Value |
|---|---|
| **From** | Def Communications `<76tguyhh6tgftrt7tg.su>` |
| **Sender IP** | `114.114.114.114` |
| **To** | `hr@inergy.com` |
| **Recipient IP** | `176.157.125.93` |
| **Date/Time** | Wednesday, July 20, 2022 09:30:14 AM |
| **Subject** | Re: Infrastructure Egnieer role |
| **Attachment** | `bfsvc.exe` (password protected) |
| **Password provided** | `paradise10789` |

### Email Body
> *"Dear HR at Ingergy, I am writing for to express my interest in the engineer role posted from the website. There is attached my resume and cover letter. For privacy, the file is password protected. Use the password paradise10789 to open. Thank you, Clyde West"*

---

## 🚩 Red Flags Identified

| # | Red Flag | Category |
|---|---|---|
| 1 | Sender name "Def Communications" does not match the signature "Clyde West" | Identity mismatch |
| 2 | Sender domain `.su` (Soviet Union ccTLD) — suspicious for a job application | Suspicious domain |
| 3 | Subject line contains misspelling: "Egnieer" instead of "Engineer" | Grammatical error |
| 4 | Email body contains grammatical errors: "I am writing for to express" | Poor language quality |
| 5 | Company name misspelled in body: "Ingergy" vs "Inergy" | Grammatical error |
| 6 | Attachment is `bfsvc.exe` — an executable file sent as a "resume" | Suspicious file extension |
| 7 | File is password protected — common tactic to bypass email security filters | Evasion technique |
| 8 | Hash value confirmed malicious by VirusTotal vendors — Trojan category | Confirmed malware |

---

## 🔍 VirusTotal Analysis

**Known malicious file hash:**
```
54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b
```

**Result:** Confirmed malicious by multiple vendors — classified as a **Trojan** threat.

---

## 📋 Playbook Steps Followed

| Step | Action | Result |
|---|---|---|
| Step 1 | Received phishing alert ticket A-2703 | ✅ Alert received |
| Step 2 | Evaluated alert details — severity, sender/receiver info, subject, body | ✅ Multiple red flags identified |
| Step 3.0 | Checked for links or attachments | ✅ Attachment found: `bfsvc.exe` |
| Step 3.1 | Verified hash on VirusTotal | ✅ Confirmed malicious — Trojan |
| Step 3.2 | Updated ticket and escalated to Level-2 analyst | ✅ Status → Escalated |

---

## 📓 Incident Handler's Journal — Entry 2

**Date:** 2026/09/24  
**Incident date:** July 20, 2022 at 9:30:14 AM

### The 5 W's

| Question | Answer |
|---|---|
| **Who** | Unknown external threat actor — "Def Communications `<76tguyhh6tgftrt7tg.su>`" IP `114.114.114.114` |
| **What** | A malicious executable attachment downloaded via a phishing email |
| **When** | July 20, 2022 at 9:30:14 AM |
| **Where** | On an employee's computer at Inergy (`hr@inergy.com`) |
| **Why** | Employee downloaded the malicious attachment without recognizing the phishing attempt. Attacker motivations appear unknown — no ransom or specific demand identified |

### Additional Notes
Security awareness training for employees should be implemented to prevent future incidents of this type — specifically training on how to recognize social engineering attacks, suspicious email patterns, and unsafe file handling.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/1_support_material_Phishing_playbook.pdf`](./assets/1_support_material_Phishing_incident_response_playbook.pdf) | Phishing Incident Response Playbook v1.0 |
| [`assets/2_completed_work_Incident_handlers_journal.pdf`](./assets/2_completed_work_Incident_handler_s_journal.pdf) | My completed incident handler's journal — Entry 2 |
| [`assets/3_completed_work_Alert_ticket.pdf`](./assets/3_my_completed_work_Alert_ticket.pdf) | My completed alert ticket A-2703 |

---

## 🧠 Key Concepts Applied

- **Phishing playbook** — Structured step-by-step procedure for responding to phishing alerts consistently and efficiently
- **Alert triage** — Evaluating alert severity, sender/receiver details, subject, body, and attachments to assess legitimacy
- **VirusTotal** — Threat intelligence platform used to verify file hash reputation across multiple vendor engines
- **Red flag identification** — Recognizing indicators of a phishing attempt: domain mismatch, grammatical errors, suspicious file extensions, password-protected executables
- **Ticket escalation** — Updating alert status to Escalated and notifying a Level-2 SOC analyst when malicious content is confirmed
- **Password-protected malware** — Attackers use file passwords to bypass email security filters that scan attachments
- **Executable as resume** — `.exe` files disguised as legitimate documents are a classic malware delivery technique

---

## 📚 What I Learned

- How to follow a **phishing incident response playbook** step by step to ensure consistent and complete triage
- How to identify **multiple red flags** in a phishing email — identity mismatches, grammatical errors, suspicious domains, and dangerous file extensions
- That **password-protected attachments** are a deliberate evasion technique — the password is provided in the email body to trick the victim while bypassing automated scanning
- How to use **VirusTotal** to confirm whether a file hash is malicious and identify the threat category
- The difference between **closing** (not malicious) and **escalating** (confirmed malicious) an alert ticket
- How a single employee action — opening an attachment — can trigger a full SOC incident response workflow

---

## 🛠️ Frameworks & Tools Referenced

![Phishing Playbook](https://img.shields.io/badge/Playbook-Phishing_Response-red?style=flat-square)
![VirusTotal](https://img.shields.io/badge/Tool-VirusTotal-orange?style=flat-square)
![SOC](https://img.shields.io/badge/Role-SOC_Analyst_L1-blue?style=flat-square)
![Incident Response](https://img.shields.io/badge/Skill-Incident_Response-purple?style=flat-square)
![Alert Triage](https://img.shields.io/badge/Skill-Alert_Triage-darkgreen?style=flat-square)
![Social Engineering](https://img.shields.io/badge/Attack-Social_Engineering-yellow?style=flat-square)
