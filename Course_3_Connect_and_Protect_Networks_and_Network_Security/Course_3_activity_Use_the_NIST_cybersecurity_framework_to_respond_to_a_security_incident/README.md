# 📊 Portfolio Activity: Use the NIST Cybersecurity Framework to Respond to a Security Incident

> **Course:** Google Cybersecurity Professional Certificate — Course 3: Connect and Protect: Networks and Network Security  
> **Type:** Incident Report Analysis  
> **Framework:** NIST Cybersecurity Framework (CSF)  
> **Attack identified:** DDoS ICMP Flood Attack  

---

## 📋 Scenario Overview

A multimedia company offering web design, graphic design, and social media marketing services experienced a **DoS attack** that compromised its internal network for **two hours**.

The attack was carried out by flooding the network with **ICMP packets** through an **unconfigured firewall**, causing all internal network services to stop responding. Normal internal traffic was unable to access any network resources during the attack.

As a cybersecurity analyst, the task was to apply the **NIST Cybersecurity Framework (CSF)** to analyze the incident and build a comprehensive security improvement plan across all five CSF functions: **Identify, Protect, Detect, Respond, Recover**.

---

## 🛡️ NIST CSF Analysis Summary

| CSF Function | Key Actions |
|---|---|
| **Identify** | Unconfigured firewall identified as entry point — ICMP flood DoS attack confirmed |
| **Protect** | Firewall rules, IP verification, IDS/IPS, network monitoring implemented |
| **Detect** | Network monitoring software + SIEM tools deployed for abnormal traffic detection |
| **Respond** | ICMP traffic blocked, non-critical services taken offline, critical services restored |
| **Recover** | Gradual service restoration after network classified as safe, data integrity verified |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`incident-report-analysis.md`](./incident-report-analysis.md) | Full NIST CSF incident report — all five framework functions |
| [`assets/my_answers_incident_report_analysis.pdf`](./assets/3_firstanswers_Incident_report_analysis.pdf) | Original completed report (PDF) |

---

## 🧠 Key Concepts Applied

- **NIST Cybersecurity Framework (CSF)** — Applying all five functions to a real incident
- **DoS ICMP Flood Attack** — How ICMP packets can overwhelm a network
- **Firewall Configuration** — Rate limiting, IP spoofing verification, port filtering
- **IDS/IPS** — Filtering suspicious ICMP traffic based on characteristics
- **SIEM Tools** — Detecting abnormal network traffic patterns
- **Network Segmentation** — Isolating network environments to limit blast radius
- **Incident Response** — Containment, neutralization, and recovery procedures

---

## 📚 What I Learned

- How to apply the **NIST CSF** systematically to analyze and respond to a cybersecurity incident
- How an **ICMP flood DoS attack** exploits unconfigured firewalls to overwhelm a network
- The importance of **firewall configuration and maintenance** as a first line of defence
- How **network monitoring software and SIEM tools** improve detection speed
- How to structure a **recovery plan** that prioritizes critical services and data integrity
- The value of **network segmentation** in limiting the impact of future attacks

---

## 🛠️ Tools, Frameworks & Concepts Referenced

![NIST CSF](https://img.shields.io/badge/Framework-NIST_CSF-blue?style=flat-square)
![ICMP](https://img.shields.io/badge/Attack-DDoS_ICMP_Flood-red?style=flat-square)
![Firewall](https://img.shields.io/badge/Defense-Firewall_Rules-orange?style=flat-square)
![IDS/IPS](https://img.shields.io/badge/Defense-IDS%2FIPS-purple?style=flat-square)
![SIEM](https://img.shields.io/badge/Tool-SIEM-darkgreen?style=flat-square)
![Network Segmentation](https://img.shields.io/badge/Defense-Network_Segmentation-lightblue?style=flat-square)
