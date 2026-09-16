# 🏥 Entry 01 — Ransomware Attack on a Healthcare Clinic

> **Course:** Google Cybersecurity Professional Certificate — Course 6: Sound the Alarm: Detection and Response  
> **Journal Entry:** 01  
> **Date:** 2026/09/16  
> **Incident Type:** Ransomware / Phishing / Social Engineering

---

## 📋 Incident Description

A small U.S. health care clinic experienced a security incident on Tuesday at 9:00 AM. The incident involved all employees of the company and interrupted all business operations.

A group of unethical hackers used a **phishing email** as an attack vector to install **ransomware** and encrypt all data stored by the company. After encryption, they left a ransom note demanding money in exchange for the decryption key.

---

## 🔍 The 5 W's

| Question | Answer |
|---|---|
| **Who** caused the incident? | A group of unethical hackers (organized threat actors) |
| **What** happened? | A malicious attachment downloaded via a phishing email installed ransomware, encrypting all company data |
| **When** did the incident occur? | Tuesday at 9:00 AM |
| **Where** did the incident happen? | On the servers and devices of a small U.S. health care clinic |
| **Why** did the incident happen? | An employee opened a malicious email attachment without recognizing it as a phishing attempt. The organization lacked adequate security awareness training and email filtering controls to prevent the attack. Motivations appear to be financial. |

---

## ⚔️ Attack Chain

```
Phishing email sent to employee
        ↓
Employee opens malicious attachment
        ↓
Ransomware installed on device
        ↓
Ransomware spreads across company network
        ↓
All data encrypted on servers and devices
        ↓
Ransom note left — decryption key demanded in exchange for payment
        ↓
All business operations interrupted
```

---

## 🛠️ Tools Used

None — this entry is based on incident scenario analysis without active investigation tools.

---

## 💡 Additional Notes

Security awareness training for employees should be implemented immediately to prevent future incidents of this type. Employees need to be able to recognize phishing emails and understand how to handle social engineering attacks safely — including:

- Never opening attachments from unknown senders
- Verifying sender identity before clicking links
- Reporting suspicious emails to the security team immediately

**Additional technical controls recommended:**
- Email filtering to block malicious attachments
- Endpoint Detection and Response (EDR) tools to detect ransomware behavior
- Regular backups stored offline or in an air-gapped environment — so encrypted data can be restored without paying the ransom
- Network segmentation to prevent ransomware from spreading across all devices

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/journal_entry_01.pdf`](./assets/0_completed_work_Incident_handler's_journal.pdf) | Original completed journal entry (PDF) |

---

## 🧠 Key Concepts Applied

- **Ransomware** — Malware that encrypts victim data and demands payment for the decryption key
- **Phishing** — Social engineering attack delivered via email using deceptive messages to trick users
- **Attack vector** — The method used to gain initial access (in this case: malicious email attachment)
- **5 W's framework** — Structured approach to document the key facts of a security incident
- **Incident response** — Identifying, containing, and recovering from a security incident
- **Business impact** — All operations interrupted; healthcare data unavailable, potentially affecting patient care

---

## 📚 What I Learned

- How to apply the **5 W's framework** to document a security incident clearly and concisely
- How **phishing emails** serve as the initial attack vector for ransomware campaigns
- That **healthcare organizations** are high-value targets for ransomware — encrypted patient data creates urgent pressure to pay
- The importance of **employee security awareness training** as the first line of defence against social engineering
- That **offline backups** are the most effective technical control against ransomware — they eliminate the attacker's leverage entirely
- How a single employee action can cause a **company-wide disruption** when proper controls are not in place

---

## 🛠️ Concepts Referenced

![Ransomware](https://img.shields.io/badge/Attack-Ransomware-red?style=flat-square)
![Phishing](https://img.shields.io/badge/Attack-Phishing-orange?style=flat-square)
![Social Engineering](https://img.shields.io/badge/Attack-Social_Engineering-yellow?style=flat-square)
![Incident Response](https://img.shields.io/badge/Skill-Incident_Response-blue?style=flat-square)
![5 W's](https://img.shields.io/badge/Framework-5_W's-green?style=flat-square)
![Security Training](https://img.shields.io/badge/Control-Security_Awareness_Training-darkgreen?style=flat-square)
