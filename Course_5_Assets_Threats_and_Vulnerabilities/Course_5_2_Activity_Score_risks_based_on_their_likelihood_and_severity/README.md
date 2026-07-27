# ⚠️ Portfolio Activity: Score Risks Based on Their Likelihood and Severity

> **Course:** Google Cybersecurity Professional Certificate — Course 5: Assets, Threats, and Vulnerabilities  
> **Type:** Risk Assessment / Risk Register  
> **Framework:** NIST CSF — Risk Assessment  
> **Formula:** Likelihood × Severity = Priority Score

---

## 📋 Scenario Overview

A commercial bank is conducting a risk assessment of its operational environment. The cybersecurity team has identified five primary risks to the bank's funds. The goal was to evaluate each risk by scoring its likelihood and severity, then calculate a priority score to help the team focus resources on the most critical threats.

**Formula:** `Likelihood × Severity = Priority`

---

## 🏦 Operational Environment

The bank operates in a coastal area with low crime rates. It has 100 on-premise and 20 remote employees handling sensitive data. The customer base includes 2,000 individual accounts and 200 commercial accounts. The bank's services are marketed by a professional sports team and ten local businesses. Strict financial regulations — including Federal Reserve cash requirements — apply.

---

## 📊 Risk Register

| Risk | Description | Likelihood | Severity | Priority |
|---|---|---|---|---|
| Business email compromise | An employee is tricked into sharing confidential information | 2 | 2 | **4** |
| Compromised user database | Customer data is poorly encrypted | 2 | 3 | **6** |
| Financial records leak | A database server of backed up data is publicly accessible | 3 | 3 | **9** |
| Theft | The bank's safe is left unlocked | 1 | 3 | **3** |
| Supply chain disruption | Delivery delays due to natural disasters | 1 | 2 | **2** |

---

## 🎯 Risk Priority Summary

| Priority | Risk | Action |
|---|---|---|
| 🔴 9 — Critical | Financial records leak | Immediate action required |
| 🟠 6 — High | Compromised user database | High priority remediation |
| 🟡 4 — Moderate | Business email compromise | Address with training and controls |
| 🟢 3 — Low | Theft | Monitor and maintain physical controls |
| 🟢 2 — Low | Supply chain disruption | Contingency planning |

---

## 🗒️ Notes — Risk Context

The sharing of sensitive information due to collaborations and exchanges with businesses in the area can impact the security of internal data and information, leading to possible malicious attacks. Even a physical theft attempt is a security concern, but due to the low crime rate in the area it remains a rare and difficult possibility.

---

## 📊 Risk Matrix Reference

| | Low Severity (1) | Moderate Severity (2) | Catastrophic Severity (3) |
|---|---|---|---|
| **Certain (3)** | 3 | 6 | 9 |
| **Likely (2)** | 2 | 4 | 6 |
| **Rare (1)** | 1 | 2 | 3 |

---

## 🔍 Scoring Rationale

**Financial records leak → Priority 9 (Critical)**  
A publicly accessible backup server has a high likelihood of being discovered and exploited. The impact would be catastrophic — regulatory fines, reputational damage, loss of customer trust, and potential business closure.

**Compromised user database → Priority 6 (High)**  
Poor encryption of customer data is a significant vulnerability. With 2,000+ accounts, a breach would expose a large number of customers to identity theft and financial fraud, triggering heavy regulatory penalties.

**Business email compromise → Priority 4 (Moderate)**  
With 120 employees (100 on-premise + 20 remote), phishing attacks are a realistic threat. Remote workers are particularly vulnerable. The impact is moderate — sensitive information could be leaked but financial damage is more contained.

**Theft → Priority 3 (Low)**  
The area has low crime rates, making physical theft rare. However, if the safe were left unlocked the impact would be severe — direct financial loss. The low likelihood keeps the priority score low.

**Supply chain disruption → Priority 2 (Low)**  
Located in a coastal area, hurricanes could disrupt cash delivery and violate Federal Reserve requirements. However, such events are rare and contingency plans can mitigate their impact significantly.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/completed_Risk_register.pdf`](./assets/completed_Risk_register.pdf) | Completed risk register with all scores and notes |

---

## 🧠 Key Concepts Applied

- **Risk register** — Central record of potential risks used during risk assessments
- **Risk formula** — Likelihood × Severity = Priority Score
- **Risk matrix** — Visual tool for mapping likelihood vs severity to determine priority
- **NIST CSF Identify function** — Risk assessment as the foundation of a security plan
- **Risk prioritization** — Focusing security resources on the highest-priority threats first

---

## 📚 What I Learned

- How to conduct a structured **risk assessment** using a risk register
- How to estimate **likelihood** based on operating environment factors (location, crime rate, workforce size)
- How to estimate **severity** based on potential financial, regulatory, and reputational impact
- How to apply the **risk formula** to calculate priority scores and rank risks
- That **publicly accessible data** (financial records leak, score 9) is typically the highest priority risk — combining high likelihood and catastrophic impact

---

## 🛠️ Frameworks & Concepts Referenced

![NIST CSF](https://img.shields.io/badge/Framework-NIST_CSF-blue?style=flat-square)
![Risk Assessment](https://img.shields.io/badge/Skill-Risk_Assessment-orange?style=flat-square)
![Risk Register](https://img.shields.io/badge/Tool-Risk_Register-red?style=flat-square)
![Risk Matrix](https://img.shields.io/badge/Tool-Risk_Matrix-purple?style=flat-square)
