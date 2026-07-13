# 🏠 Portfolio Activity: Home Asset Inventory

> **Course:** Google Cybersecurity Professional Certificate — Course 5: Assets, Threats, and Vulnerabilities  
> **Type:** Asset Management / Asset Classification  
> **Framework:** Asset Inventory & Sensitivity Classification

---

## 📋 Scenario Overview

Effective security starts with knowing what you have. In this activity, the goal was to create an asset inventory for a home office network — identifying connected devices, documenting their characteristics, and classifying their sensitivity level based on the type of information they store and their exposure to risk.

This mirrors a real-world security task: before you can protect assets, you must first identify and classify them.

---

## 🗂️ Asset Inventory

| # | Asset | Network Access | Owner | Location | Notes | Sensitivity |
|---|---|---|---|---|---|---|
| 1 | Network router | Continuous | ISP | On-premises | Has a 2.4 GHz and 5 GHz connection. All devices on the home network connect to the 5 GHz frequency. | Confidential |
| 2 | Desktop | Occasional | Homeowner | On-premises | Contains private information, like photos. | Restricted |
| 3 | Guest smartphone | Occasional | Friend | On and Off-premises | Connects to the home network. | Internal-only |
| 4 | Smart TV | Occasional | Homeowner | On-premises | Contains private information, like Google account connected to streaming platforms. | Confidential |
| 5 | Smart Fridge | Occasional | Homeowner | On-premises | No private information stored, only access to the home network for internal updates. | Internal-only |
| 6 | Laptop (friend's) | Occasional | Friend | On and Off-premises | Contains all private information of the owner and connects to the home network. Used frequently outside the home. | Internal-only |

---

## 🔐 Sensitivity Classification Reference

| Category | Access Designation |
|---|---|
| **Restricted** | Need-to-know only |
| **Confidential** | Limited to specific users |
| **Internal-only** | Users on-premises |
| **Public** | Anyone |

---

## 🔍 Classification Reasoning

**Network router → Confidential**  
The router controls access to the entire home network. Access is limited to the homeowner and ISP. A compromised router could expose all devices on the network.

**Desktop → Restricted**  
Contains the homeowner's private files and photos. Access should be strictly need-to-know — only the owner should be able to use this device.

**Guest smartphone → Internal-only**  
Belongs to a friend and connects to the home network only while on-premises. Limited trust level as it is an external device.

**Smart TV → Confidential**  
Connected to a Google account and multiple streaming platforms — contains credentials and personal preferences. Access should be limited to the homeowner.

**Smart Fridge → Internal-only**  
No sensitive personal information stored on the device. Connects to the network only for firmware updates. Low risk but still part of the network attack surface.

**Laptop (friend's) → Internal-only**  
An external device that connects to the home network and is frequently used outside the home — increasing the risk of exposure to external threats. Contains the friend's private data but not the homeowner's.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/1_empty_Home_asset_inventory.pdf`](./assets/1_empty_Home_asset_inventory.pdf) | Original blank template provided by the course |
| [`assets/2_completed_Home_asset_inventory.pdf`](./assets/2_completed_Home_asset_inventory.pdf) | Completed asset inventory with all 6 devices classified |

---

## 🧠 Key Concepts Applied

- **Asset inventory** — Cataloging all devices connected to a network as the first step in asset management
- **Asset classification** — Assigning sensitivity levels based on the type of information stored and potential business impact
- **CIA Triad considerations** — Evaluating each asset in terms of Confidentiality, Integrity, and Availability
- **Network exposure** — Considering whether devices are on-premises only or also used off-premises
- **Attack surface awareness** — Recognizing that every connected device is a potential entry point

---

## 📚 What I Learned

- How to build a structured **asset inventory** for a network environment
- How to apply **sensitivity classifications** based on the data stored and the risk of compromise
- That **IoT devices** (like smart TVs and fridges) expand the network attack surface even when they store no personal data
- That **external devices** (guest phones, friend's laptop) introduce additional risk because they connect to unknown networks outside the home
- The importance of **asset management as the foundation of security** — you can't protect what you don't know you have

---

## 🛠️ Frameworks & Concepts Referenced

![Asset Management](https://img.shields.io/badge/Concept-Asset_Management-blue?style=flat-square)
![CIA Triad](https://img.shields.io/badge/Framework-CIA_Triad-orange?style=flat-square)
![Classification](https://img.shields.io/badge/Skill-Data_Classification-green?style=flat-square)
![NIST](https://img.shields.io/badge/Framework-NIST-lightblue?style=flat-square)
