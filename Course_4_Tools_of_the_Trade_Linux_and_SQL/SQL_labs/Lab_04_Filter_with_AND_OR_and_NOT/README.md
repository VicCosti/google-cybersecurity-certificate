# 🗄️ Lab: Filter with AND, OR, and NOT

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** MariaDB — `organization` database  
> **Tables used:** `log_in_attempts`, `employees`

---

## 📋 Scenario

A security team needs to investigate potential security issues and update employee computers. This lab focuses on using logical operators (`AND`, `OR`, `NOT`) to build complex multi-condition SQL filters — retrieving specific subsets of login attempt and employee data.

---

## 🔗 Logical Operators Reference

| Operator | Behavior | Example |
|---|---|---|
| `AND` | Both conditions must be true | `login_time > '18:00:00' AND success = 0` |
| `OR` | At least one condition must be true | `department = 'Finance' OR department = 'Sales'` |
| `NOT` | Negates the condition | `NOT country LIKE 'MEX%'` |

---

## ✅ Tasks Completed

| Task | Query | Result |
|---|---|---|
| 1 | `login_time > '18:00:00' AND success = 0` | 19 failed after-hours logins |
| 2 | `login_date = '2022-05-09' OR login_date = '2022-05-08'` | 75 login attempts |
| 3 | `NOT country LIKE 'MEX%'` | 144 non-Mexico logins |
| 4 | `department = 'Marketing' AND office LIKE 'East%'` | 7 employees, first: elarson |
| 5 | `department = 'Finance' OR department = 'Sales'` | 71 employees, first Sales: lrodriqu |
| 6 | `NOT department = 'Information Technology'` | 161 employees |

---

## 🔍 Key Findings

### Task 1 — After-hours failed logins
```sql
WHERE login_time > '18:00:00' AND success = 0
-- 19 suspicious failed login attempts outside business hours
-- success = 0 (Boolean FALSE) → no quotes around numeric value
```

### Task 3 — NOT + LIKE combination
```sql
WHERE NOT country LIKE 'MEX%'
-- Excludes both 'MEX' and 'MEXICO' in one filter
-- 144 out of 200 logins originated outside Mexico
```

### Task 6 — Two equivalent ways to write NOT
```sql
WHERE NOT department = 'Information Technology'  -- using NOT keyword
WHERE department != 'Information Technology'      -- using != operator
-- Both return identical results: 161 rows
```

---

## 💡 SQL Syntax Rules

### Always repeat the column name with OR
```sql
-- ✅ Correct
WHERE department = 'Finance' OR department = 'Sales'

-- ❌ Invalid syntax
WHERE department = 'Finance' OR 'Sales'
```

### Boolean values — no quotes
```sql
-- ✅ Correct (success is numeric: 1=TRUE, 0=FALSE)
WHERE success = 0
WHERE success = 1

-- ❌ Incorrect
WHERE success = 'FALSE'
WHERE success = 'TRUE'
```

### Combining AND with LIKE
```sql
-- Both conditions must be satisfied simultaneously
WHERE department = 'Marketing' AND office LIKE 'East%'
-- Returns only Marketing employees in East building offices
```

---

## 📁 Project Files

| File | Description |
|---|---|
| [`filter_and_or_not.sql`](./filter_and_or_not.sql) | SQL script with all AND, OR, NOT queries and findings |

---

## 🧠 Key Concepts Applied

- **AND** — Combine two conditions that must both be true (narrows results)
- **OR** — Return rows matching either condition (broadens results)
- **NOT** — Exclude rows matching a condition
- **NOT + LIKE** — Exclude pattern matches (e.g. exclude all Mexico variants)
- **Boolean values** — Stored as `1` (TRUE) and `0` (FALSE), no quotes needed
- **Repeating column names** — Each condition in an OR clause needs its own column reference

---

## 📚 What I Learned

- How `AND` narrows results by requiring multiple conditions to be simultaneously true
- How `OR` broadens results by returning rows matching any one of the conditions
- How `NOT` negates a condition — useful for exclusion filters
- That `NOT LIKE 'MEX%'` elegantly handles multiple country format variants (`MEX`, `MEXICO`) in a single filter
- That Boolean values (`success = 0`) never use quotes — they are numeric, not strings
- That `NOT col = 'X'` and `col != 'X'` produce identical results — both are valid

---

## 🛠️ Tools & Concepts Referenced

![MariaDB](https://img.shields.io/badge/Database-MariaDB-blue?style=flat-square&logo=mariadb&logoColor=white)
![SQL](https://img.shields.io/badge/Language-SQL-orange?style=flat-square)
![AND](https://img.shields.io/badge/Operator-AND-green?style=flat-square)
![OR](https://img.shields.io/badge/Operator-OR-purple?style=flat-square)
![NOT](https://img.shields.io/badge/Operator-NOT-red?style=flat-square)
![Boolean](https://img.shields.io/badge/Type-Boolean-lightblue?style=flat-square)
