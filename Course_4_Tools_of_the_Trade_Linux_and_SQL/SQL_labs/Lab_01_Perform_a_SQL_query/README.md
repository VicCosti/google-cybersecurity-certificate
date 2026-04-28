# 🗄️ Lab: Perform a SQL Query

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** MariaDB — `organization` database  
> **Tables used:** `machines`, `log_in_attempts`

---

## 📋 Scenario

As a security analyst, being able to query a database is essential for investigating security events. In this lab, the goal was to retrieve device information to identify machines needing updates, analyze login attempt data to detect unusual activity, and use `ORDER BY` to sort query results chronologically.

---

## 🗂️ Database Structure

### machines table
| Column | Description |
|---|---|
| `device_id` | Unique device identifier |
| `operating_system` | OS version (OS 1, OS 2, OS 3) |
| `email_client` | Email client installed |
| `OS_patch_date` | Last OS patch date |
| `employee_id` | Associated employee ID |

### log_in_attempts table
| Column | Description |
|---|---|
| `event_id` | Unique event identifier |
| `username` | Username attempting login |
| `login_date` | Date of login attempt |
| `login_time` | Time of login attempt |
| `country` | Country of login attempt |
| `ip_address` | Source IP address |
| `success` | 1 = successful, 0 = failed |

---

## ✅ Tasks Completed

| Task | Query | Finding |
|---|---|---|
| 1 | `SELECT * FROM machines` | 200 devices returned |
| 1 | `SELECT device_id, email_client FROM machines` | 3rd row: Email Client 2 |
| 1 | `SELECT device_id, operating_system, OS_patch_date FROM machines` | 1st entry patch date: 2021-09-01 |
| 2 | `SELECT event_id, country FROM log_in_attempts` | No logins from Australia |
| 2 | `SELECT username, login_date, login_time FROM log_in_attempts` | 5th row: jrafael |
| 2 | `SELECT * FROM log_in_attempts` | All 200 login events with full details |
| 3 | `ORDER BY login_date` | First record: ivelasco on 2022-05-08 |
| 3 | `ORDER BY login_date, login_time` | First record: bsand on 2022-05-08 at 00:19:11 |

---

## 🔍 Key Findings

### Login attempt countries
All 200 login attempts originated from: USA, US, CAN, CANADA, MEX, MEXICO — no unexpected countries detected.

> **Note:** The same country appears with different formats (e.g. `USA` vs `US`, `CANADA` vs `CAN`, `MEXICO` vs `MEX`). In a real investigation, this inconsistency would be addressed with data normalization or `WHERE` filters.

### Chronological order — ORDER BY result
```sql
-- Sorted by date only → rows within same date unordered by time
ORDER BY login_date

-- Sorted by date AND time → precise chronological order
ORDER BY login_date, login_time
-- First event: bsand | 2022-05-08 | 00:19:11
```

---

## 💡 SQL Syntax Reference

```sql
-- Select all columns
SELECT * FROM table_name;

-- Select specific columns
SELECT col1, col2, col3 FROM table_name;

-- Sort by one column (ascending by default)
SELECT * FROM table_name ORDER BY column_name;

-- Sort by multiple columns
SELECT * FROM table_name ORDER BY col1, col2;

-- Sort descending
SELECT * FROM table_name ORDER BY column_name DESC;
```

---

## 📁 Project Files

| File | Description |
|---|---|
| [`perform_sql_query.sql`](./perform_sql_query.sql) | SQL script with all queries, comments, and findings |

---

## 🧠 Key Concepts Applied

- **SELECT** — Specify which columns to retrieve
- **FROM** — Specify which table to query
- **\*** — Wildcard to select all columns
- **ORDER BY** — Sort results by one or more columns
- **Multi-column sorting** — Secondary sort applied within groups of the primary sort
- **MariaDB table name case sensitivity** — Table names are case-sensitive in MySQL/MariaDB

---

## 📚 What I Learned

- How to use `SELECT` and `FROM` to retrieve specific columns from a database table
- The difference between `SELECT *` (all columns) and selecting specific columns
- How `ORDER BY` sorts results — ascending by default, `DESC` for descending
- How to apply **multi-column sorting** with `ORDER BY col1, col2` for precise ordering
- How login attempt data can be used in security investigations — checking countries, timestamps, and success status
- That inconsistent data formats (`USA` vs `US`) in real databases require normalization or careful filtering

---

## 🛠️ Tools & Concepts Referenced

![MariaDB](https://img.shields.io/badge/Database-MariaDB-blue?style=flat-square&logo=mariadb&logoColor=white)
![SQL](https://img.shields.io/badge/Language-SQL-orange?style=flat-square)
![SELECT](https://img.shields.io/badge/Keyword-SELECT-green?style=flat-square)
![ORDER BY](https://img.shields.io/badge/Keyword-ORDER_BY-purple?style=flat-square)
