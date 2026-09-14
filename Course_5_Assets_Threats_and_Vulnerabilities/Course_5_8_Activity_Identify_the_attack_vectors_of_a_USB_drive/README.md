# 🔌 Portfolio Activity: Parking Lot USB Exercise

> **Course:** Google Cybersecurity Professional Certificate — Course 5: Assets, Threats, and Vulnerabilities  
> **Type:** Threat Analysis / Attacker Mindset / Social Engineering  
> **Concepts:** USB baiting, physical security, PII exposure, malware delivery

---

## 📋 Scenario Overview

A USB drive is found in a parking lot near the office of Rhetorical Hospital. As a security analyst, the task was to investigate the contents of the USB drive, think like an attacker to identify how the information could be exploited, and perform a risk analysis to recommend appropriate security controls.

This exercise simulates a real-world **USB baiting attack** — a social engineering technique where attackers intentionally leave infected USB drives in public areas hoping someone will plug them in.

---

## 🗂️ USB Contents

The USB drive belongs to **Jorge**, an HR manager at Rhetorical Hospital. It contains a mix of personal and work-related files:

| File / Folder | Type | Sensitivity |
|---|---|---|
| Family photos | Personal folder | PII — photos of Jorge and family |
| Our dog pics | Personal folder | Low sensitivity |
| New hire letter.gdoc | Work file | Confidential — internal HR document |
| Vacation ideas.gdoc | Personal file | Low sensitivity |
| Shift schedules.gsheet | Work file | **Sensitive** — employee work hours |
| Employee budget.gsheet | Work file | **Highly sensitive** — salary data |
| Wedding list.gslides | Personal file | PII — family and personal contacts |
| JB_Resume.gdoc | Personal file | PII — personal career information |

---

## 🔍 Analysis

### Contents Assessment

The USB drive contains both **personal and work-related files** belonging to HR manager Jorge. The most sensitive work files are the **shift schedule** and **employee budget** — which contain internal operational data and salary information. Personal files like the **JB_Resume** and **Family photos** folder contain PII that should be stored more securely.

Storing personal and work-related files on the same unprotected device is a significant security risk — it creates a single point of failure where a single lost device exposes both personal and corporate data.

---

### Attacker Mindset

**Employee budget → Salary exploitation attack**  
An attacker accessing the employee budget file could contact other employees and reveal salary differences — exploiting financial frustration to convince employees to share company PII or sensitive data in exchange for payment. This is a classic **insider threat facilitation** technique.

**Family photos + Wedding list → Family phishing attack**  
Personal files reveal the identities of Jorge's family members and personal contacts. An attacker could use this information to launch **targeted phishing attacks** against Jorge's relatives — impersonating trusted parties to extract information or credentials that could eventually be used to access company systems.

**Shift schedule → Impersonation attack**  
The shift schedule reveals exactly when each employee works. An attacker could use this to:
- Know when specific employees are online to impersonate their devices
- Time attacks to coincide with periods of high activity when anomalies are less likely to be noticed
- Exploit shift gaps where security monitoring may be reduced

---

### Risk Analysis

**Malicious code delivery (Critical risk)**  
A threat actor could hide malicious code inside the USB files — designed to execute automatically when a file is opened. This code could infect the device and propagate across the entire company network, giving the attacker internal access and a broad attack surface for data collection.

**Unintentional internal exposure**  
Another employee finding the USB and opening the files — even out of innocent curiosity — creates significant risk. They would immediately have access to sensitive salary data and shift schedules, creating both a data exposure and a potential insider threat scenario.

**Recommended controls:**

| Control Type | Recommendation |
|---|---|
| **Operational** | Security awareness training — employees should be trained never to plug in unknown USB devices |
| **Technical** | Encryption of sensitive files on portable devices |
| **Technical** | Authentication system required to access files |
| **Physical** | Policy prohibiting mixing personal and work files on the same device |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/1_Jorge_USB_content_screenshot.png`](./assets/1_Jorge's_USB_content_screenshot.png) | Screenshot of the USB drive contents |
| [`assets/2_completed_Parking_lot_USB_exercise.pdf`](./assets/2_completed_work_Parking_lot_USB_exercise.pdf) | My completed parking lot USB exercise |

---

## 🧠 Key Concepts Applied

- **USB baiting** — Social engineering attack where malicious USB drives are intentionally left in public areas
- **Attacker mindset** — Analyzing assets from the perspective of a threat actor to identify non-obvious attack vectors
- **PII exposure** — Personal files on work devices create unintended exposure of sensitive personal information
- **Malware delivery via USB** — Malicious code embedded in files executes when opened, potentially spreading across a network
- **Operational controls** — Security awareness training as a first line of defence against social engineering
- **Technical controls** — Encryption and authentication as layers of protection for portable devices

---

## 📚 What I Learned

- How **USB baiting** works as a social engineering attack and why it is so effective
- That **mixing personal and work files** on the same device creates a much larger attack surface than either alone
- How an attacker can use **non-sensitive-looking files** (shift schedules, family photos) to enable sophisticated attacks
- The value of thinking with an **attacker mindset** — identifying attack vectors that are not immediately obvious
- That **operational controls** (training) and **technical controls** (encryption, authentication) are both necessary — neither alone is sufficient
- Why **physical security awareness** is as important as digital security in a comprehensive security strategy

---

## 🛠️ Frameworks & Concepts Referenced

![Social Engineering](https://img.shields.io/badge/Attack-USB_Baiting-red?style=flat-square)
![Attacker Mindset](https://img.shields.io/badge/Skill-Attacker_Mindset-orange?style=flat-square)
![PII](https://img.shields.io/badge/Concept-PII_Exposure-blue?style=flat-square)
![Physical Security](https://img.shields.io/badge/Concept-Physical_Security-purple?style=flat-square)
![Security Training](https://img.shields.io/badge/Control-Security_Awareness_Training-green?style=flat-square)
![Encryption](https://img.shields.io/badge/Control-Encryption-darkgreen?style=flat-square)
