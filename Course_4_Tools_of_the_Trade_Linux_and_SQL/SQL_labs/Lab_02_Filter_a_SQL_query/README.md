# 🗄️ Lab: Filter a SQL Query

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** MariaDB — `organization` database  
> **Tables used:** `machines`, `employees`

---

## 📋 Scenario

As a security analyst, filtering SQL queries allows you to find specific data quickly instead of scanning through entire tables. In this lab, the goal was to retrieve targeted information about employee devices and departments using `WHERE` filters and the `LIKE` operator — simulating real tasks like identifying machines that need updates and locating employees in specific offices.

---

## 🗂️ Database Structure

### employees table
| Column | Description |
|---|---|
| `employee_id` | Unique employee identifier |
| `device_id` | Device assigned to the employee |
| `username` | Employee username |
| `department` | Department name |
| `office` | Office location (building-number format) |

---

## ✅ Tasks Completed

| Task | Query | Finding |
|---|---|---|
| 1 | `SELECT device_id, operating_system FROM machines` | 200 rows returned |
| 2 | `WHERE operating_system = 'OS 2'` | 80 machines need update |
| 3 | `WHERE department = 'Finance'` | 38 employees, first id: 1003 |
| 3 | `WHERE department = 'Sales'` | 33 employees |
| 4 | `WHERE office = 'South-109'` | jlansky (Finance, employee 1010) |
| 4 | `WHERE office LIKE 'South%'` | 41 employees in South building |

---

## 🔍 Key Findings

### Machines requiring OS 2 update
```
80 out of 200 machines run OS 2 and need to be updated
```

### Employee in South-109 (machine with issue)
```
employee_id: 1010
username:    jlansky
department:  Finance
office:      South-109
```

### South building — department breakdown (41 employees)
| Department | Count |
|---|---|
| Finance | 8 |
| Sales | 7 |
| Marketing | 9 |
| Human Resources | 8 |
| Information Technology | 9 |

---

## 💡 SQL Syntax Reference

### WHERE clause — exact match
```sql
SELECT *
FROM employees
WHERE department = 'Finance';
-- String values must be enclosed in single quotes
-- Comparison is case-sensitive in MariaDB
```

### WHERE clause — pattern matching with LIKE
```sql
SELECT *
FROM employees
WHERE office LIKE 'South%';
-- % matches any sequence of characters of any length
```

### LIKE wildcard patterns
```sql
WHERE office LIKE 'South%'   -- starts with 'South'
WHERE office LIKE '%109'     -- ends with '109'
WHERE office LIKE '%South%'  -- contains 'South' anywhere
WHERE office LIKE 'South-1__' -- exactly 3 chars after 'South-1'
```

---

## 📁 Project Files

| File | Description |
|---|---|
| [`filter_sql_query.sql`](./filter_sql_query.sql) | SQL script with all filtered queries, comments, and findings |

---

## 🧠 Key Concepts Applied

- **WHERE** — Filter rows returned by a query based on a condition
- **Exact match** (`=`) — Return only rows where the column equals the specified value
- **LIKE operator** — Pattern matching for partial string searches
- **`%` wildcard** — Matches any sequence of characters of any length
- **String quoting** — String values in SQL must be enclosed in single quotes

---

## 📚 What I Learned

- How to use `WHERE` to filter query results to only the rows that meet a specific condition
- The difference between **exact match** (`= 'OS 2'`) and **pattern matching** (`LIKE 'South%'`)
- How the `%` wildcard works in `LIKE` — it can be placed before, after, or on both sides of a pattern
- How SQL filtering applies directly to security tasks — identifying devices needing updates, locating employees in specific offices
- That `NULL` values in `device_id` indicate employees without an assigned device — a potential security concern worth investigating

---

## 🛠️ Tools & Concepts Referenced

![MariaDB](https://img.shields.io/badge/Database-MariaDB-blue?style=flat-square&logo=mariadb&logoColor=white)
![SQL](https://img.shields.io/badge/Language-SQL-orange?style=flat-square)
![WHERE](https://img.shields.io/badge/Keyword-WHERE-green?style=flat-square)
![LIKE](https://img.shields.io/badge/Keyword-LIKE-purple?style=flat-square)
![Wildcard](https://img.shields.io/badge/Operator-Wildcard_%25-red?style=flat-square)
