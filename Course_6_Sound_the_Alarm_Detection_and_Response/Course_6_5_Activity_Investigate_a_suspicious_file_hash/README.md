# 🔺 Portfolio Activity: Pyramid of Pain

> **Course:** Google Cybersecurity Professional Certificate — Course 6: Sound the Alarm: Detection and Response  
> **Type:** Threat Intelligence / Indicator Analysis  
> **Framework:** Pyramid of Pain  
> **Tool:** VirusTotal

---

## 📋 Scenario Overview

A security analyst was alerted to a suspicious file found on an employee's computer. The goal was to use **VirusTotal** to investigate the file's hash value, determine whether it was malicious, and then map the associated indicators of compromise (IOCs) to the **Pyramid of Pain** framework — identifying the level of difficulty each indicator type imposes on an attacker when detected and blocked.

---

## 🔺 The Pyramid of Pain

The Pyramid of Pain is a framework developed by security researcher David Bianco that describes the relative difficulty attackers face when defenders detect and block different types of indicators.

```
            /\
           /  \  TTPs (Tactics, Techniques, Procedures) — Tough!
          /----\
         /      \  Tools — Challenging
        /--------\
       /          \  Network/Host Artifacts — Annoying
      /------------\
     /              \  Domain Names — Simple
    /----------------\
   /                  \  IP Addresses — Easy
  /--------------------\
 /                      \  Hash Values — Trivial
/------------------------\
```

The higher up the pyramid, the more painful it is for the attacker to adapt when that indicator is blocked.

---

## 🔍 VirusTotal Analysis

### Was the file identified as malicious?

**Yes — the file is malicious.**

| Indicator | Value |
|---|---|
| Vendor detection ratio | 50/69 vendors flagged as malicious |
| Community score | -295 (strongly negative) |
| Threat category | **Trojan** |

The combination of 50 out of 69 vendor detections and a community score of -295 provides strong evidence that this file is malicious. The threat category of **Trojan** indicates malware designed to appear legitimate while performing unauthorized actions in the background.

---

## 📊 Pyramid of Pain — IOC Mapping

| Level | Indicator Type | Value Found | Difficulty for Attacker |
|---|---|---|---|
| 🔴 **TTPs** | MITRE ATT&CK Technique | Credential Access — **Steal Web Session Cookie** + **Input Capture** | Tough — requires full retooling |
| 🟠 **Tools** | Malware tools used | *(identified via vendor analysis)* | Challenging |
| 🟡 **Network/Host Artifacts** | HTTP requests | Malicious HTTP request patterns observed | Annoying |
| 🟢 **Domain Names** | C2 domain contacted | `a.sinkhole.yourtrap.com` | Simple |
| 🔵 **IP Addresses** | IP contacted by malware | `104.86.229.106` | Easy |
| ⚪ **Hash Values** | Alternate file hash | `8f35a9e70dbec8f1904991773f394cd4f9a07f5e` | Trivial |

---

## 🎯 Key Findings

### TTPs — MITRE ATT&CK (Highest Level)
The MITRE ATT&CK framework identified two techniques:
- **Steal Web Session Cookie** — the malware captures browser session cookies to hijack authenticated sessions, allowing the attacker to impersonate the victim without needing their credentials
- **Input Capture** — the malware records user keystrokes or form inputs to steal credentials, passwords, or other sensitive data

These TTPs are the most valuable indicators because they describe **how** the attacker operates — even if they switch tools, domains, or IPs, the underlying behavior remains detectable.

### Domain Names
`a.sinkhole.yourtrap.com` — a domain contacted by the malware, likely used as a **Command and Control (C2)** channel. Domain names are relatively easy to block but also easy for attackers to replace with a new domain.

### IP Addresses
`104.86.229.106` — the IP address contacted by the malware. Easy to block with a firewall rule, but trivial for an attacker to change.

### Hash Values
`8f35a9e70dbec8f1904991773f394cd4f9a07f5e` — an alternate hash of the malicious file. Hash values are at the bottom of the pyramid — trivial to detect but also trivial for an attacker to change by modifying a single byte of the file.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/1_completed_work_Pyramid_of_Pain.pdf`](./assets/1_completed_work_Pyramid_of_Pain.pdf) | My completed Pyramid of Pain activity |

---

## 🧠 Key Concepts Applied

- **Pyramid of Pain** — Framework mapping IOC types to the difficulty they impose on attackers when detected
- **VirusTotal** — Online threat intelligence platform for analyzing files, URLs, IPs, and domains
- **Indicators of Compromise (IOCs)** — Evidence that a system has been compromised (hashes, IPs, domains, TTPs)
- **MITRE ATT&CK** — Framework cataloging attacker tactics and techniques; the highest level of the Pyramid of Pain
- **Trojan malware** — Malware disguised as legitimate software that executes malicious actions in the background
- **Session cookie theft** — Attack technique that bypasses authentication by stealing active session tokens
- **C2 (Command and Control)** — Infrastructure used by attackers to communicate with compromised systems

---

## 📚 What I Learned

- How to use **VirusTotal** to investigate a suspicious file hash and interpret vendor detection ratios and community scores
- How to apply the **Pyramid of Pain** to map indicators from a real malware investigation
- That **hash values** are at the bottom of the pyramid — easy to detect but trivially bypassed by modifying the file
- That **TTPs** are at the top — the most valuable indicators because they describe attacker behavior, which is hard to change
- How **Steal Web Session Cookie** bypasses authentication entirely — the attacker impersonates a legitimate user without needing their password
- The difference between indicators that are **easy to block but easy to replace** (IPs, hashes) vs those that **require full attacker retooling** (TTPs)

---

## 🛠️ Frameworks & Tools Referenced

![Pyramid of Pain](https://img.shields.io/badge/Framework-Pyramid_of_Pain-red?style=flat-square)
![MITRE ATT&CK](https://img.shields.io/badge/Framework-MITRE_ATT%26CK-blue?style=flat-square)
![VirusTotal](https://img.shields.io/badge/Tool-VirusTotal-orange?style=flat-square)
![Threat Intelligence](https://img.shields.io/badge/Skill-Threat_Intelligence-purple?style=flat-square)
![IOC](https://img.shields.io/badge/Concept-IOC_Analysis-darkgreen?style=flat-square)
