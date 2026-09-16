# 🍝 Portfolio Activity: Apply the PASTA Threat Model Framework

> **Course:** Google Cybersecurity Professional Certificate — Course 5: Assets, Threats, and Vulnerabilities  
> **Type:** Threat Modeling / Risk Analysis  
> **Framework:** PASTA (Process for Attack Simulation and Threat Analysis)  
> **Application:** Sneaker company mobile app

---

## 📋 Scenario Overview

A sneaker company is developing a new mobile app that connects buyers and sellers. The app handles sensitive data including user accounts, payment information, and inventory. The goal was to apply the **PASTA threat modeling framework** across all 7 stages to identify business objectives, technical components, threats, vulnerabilities, and recommend security controls.

---

## 🍝 PASTA Framework — 7 Stages

### Stage I — Define Business and Security Objectives

| Objective |
|---|
| Account and security logins stored securely |
| Safe back-end processing |
| Safe PII storing |
| Secure payment request and stored payment data |
| Secure inventory processing |

---

### Stage II — Define the Technical Scope

| Technology | Role | Security Notes |
|---|---|---|
| API | Application Programming Interface — connects front-end to back-end | Entry point for external requests |
| PKI | Public Key Infrastructure — manages encryption certificates | Provides strong encryption layer |
| SHA-256 | Hashing algorithm for credentials and sensitive data | Good security baseline |
| SQL | Database query language | **High priority — unclear if prepared statements are in use** |

> **Priority focus:** SQL — the absence of prepared statements represents a high risk for SQL injection attacks. PKI and SHA-256 provide a good level of security through encryption and hashing.

---

### Stage III — Decompose Application

**Data flow (from the diagram):**

```
User → searches for sneakers
     → Product search process triggered
     → SQL query sent to database
     → Listings of current inventory returned
     → Results displayed to user
```

---

### Stage IV — Threat Analysis

**Internal threat:**  
An internal employee with access to the SQL database could steal sensitive information — especially if targeted by social engineering tactics. A security implementation of **least privilege** and **role-based access control** should be in place to limit who can query sensitive data.

**External threat:**  
Without prepared statements for SQL queries, an external threat actor could exploit this vulnerability to launch a **SQL injection attack**, gaining unauthorized access to sensitive information and potentially taking control of the database.

---

### Stage V — Vulnerability Analysis

| Vulnerability | Risk |
|---|---|
| Unsecure payment information processes | High — payment data could be intercepted or stolen |
| No prepared statements for SQL queries | Critical — direct path to SQL injection |
| No MFA or more secure login processes | High — session hijacking and credential theft |

---

### Stage VI — Attack Modeling

**From the attack tree:**

**Path 1 — SQL Injection**
```
User data
  └── SQL injection
        └── Lack of prepared statements
              → Attacker gains access to sensitive data and high-privilege roles
              → Potential full database takeover
```

**Path 2 — Session Hijacking**
```
User data
  └── Session hijacking
        └── Weak login credentials / No MFA
              → Attacker steals session ID
              → Accesses sensitive data by impersonating legitimate user
```

---

### Stage VII — Risk Analysis and Impact

| # | Security Control | Addresses |
|---|---|---|
| 1 | Backup database | Data loss from destructive attacks |
| 2 | Prepared statements for SQL queries | SQL injection attacks |
| 3 | MFA for login access | Session hijacking, credential theft |
| 4 | Role-based access controls for database queries | Insider threats, privilege escalation |
| 5 | Encryption and hashing of sensitive data (payments + credentials) | Data exposure in transit and at rest |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/1_PASTA_data_flow_diagram.pdf`](./assets/1789488180573_1_support_material_1_PASTA_data_flow_diagram.pdf) | Data flow diagram — product search process |
| [`assets/2_PASTA_attack_tree.pdf`](./assets/1789488180573_2_support_material_2_PASTA_attack_tree.pdf) | Sample attack tree — SQL injection and session hijacking |
| [`assets/3_completed_PASTA_worksheet.pdf`](./assets/1789488261807_3_completed_work_PASTA_worksheet.pdf) | My completed PASTA worksheet |

---

## 🧠 Key Concepts Applied

- **PASTA framework** — 7-stage threat modeling process: objectives → scope → decomposition → threats → vulnerabilities → attack modeling → risk analysis
- **SQL injection** — Exploiting unsanitized SQL queries to manipulate or extract database data
- **Prepared statements** — Parameterized queries that prevent SQL injection by separating code from data
- **Session hijacking** — Stealing a session ID to impersonate a legitimate authenticated user
- **Reflected XSS** — Cross-site scripting attack that injects malicious scripts into application responses
- **Attack tree** — Visual diagram mapping attack paths from goal to exploitation method
- **Data flow diagram** — Visual representation of how data moves through an application

---

## 📚 What I Learned

- How to apply the **PASTA framework** systematically across all 7 stages to model threats for a real application
- That **SQL without prepared statements** is one of the most critical and exploitable vulnerabilities in web applications
- How **attack trees** map the relationship between an attacker's goal and the technical paths to achieve it
- The connection between **missing MFA** and session hijacking attacks — authentication gaps directly enable this attack vector
- How **threat modeling** bridges the gap between business objectives and technical security controls
- The importance of **defence in depth** — multiple controls (MFA, prepared statements, RBAC, encryption, backup) working together

---

## 🛠️ Frameworks & Concepts Referenced

![PASTA](https://img.shields.io/badge/Framework-PASTA-orange?style=flat-square)
![SQL Injection](https://img.shields.io/badge/Attack-SQL_Injection-red?style=flat-square)
![Session Hijacking](https://img.shields.io/badge/Attack-Session_Hijacking-red?style=flat-square)
![MFA](https://img.shields.io/badge/Control-MFA-green?style=flat-square)
![Prepared Statements](https://img.shields.io/badge/Control-Prepared_Statements-blue?style=flat-square)
![RBAC](https://img.shields.io/badge/Control-RBAC-purple?style=flat-square)
