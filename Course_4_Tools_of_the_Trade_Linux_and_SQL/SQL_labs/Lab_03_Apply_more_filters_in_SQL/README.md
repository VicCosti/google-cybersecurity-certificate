# 🗄️ Lab: Apply More Filters in SQL

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** MariaDB — `organization` database  
> **Table used:** `log_in_attempts`

---

## 📋 Scenario

During a security incident investigation, a security analyst needs to query login attempt data by date, time, and event ID. This lab focuses on applying comparison operators and the `BETWEEN` keyword to filter numeric and date/time data precisely.

---

## 🔢 Comparison Operators Reference

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to | `WHERE login_date = '2022-05-09'` |
| `>` | Greater than | `WHERE login_date > '2022-05-09'` |
| `<` | Less than | `WHERE login_time < '07:00:00'` |
| `<>` | Not equal to | `WHERE success <> 1` |
| `>=` | Greater than or equal to | `WHERE login_date >= '2022-05-09'` |
| `<=` | Less than or equal to | `WHERE event_id <= 150` |

---

## ✅ Tasks Completed

| Task | Query | Result |
|---|---|---|
| 1 | `WHERE login_date > '2022-05-09'` | 125 login attempts |
| 1 | `WHERE login_date >= '2022-05-09'` | 165 login attempts |
| 2 | `WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11'` | 123 login attempts |
| 3 | `WHERE login_time < '07:00:00'` | 5th user: eraab |
| 3 | `WHERE login_time BETWEEN '06:00:00' AND '07:00:00'` | Earliest: 06:01:31 |
| 4 | `WHERE event_id >= 100` | 101 rows, 3rd date: 2022-05-09 |
| 4 | `WHERE event_id BETWEEN 100 AND 150` | 51 rows, 7th user: tmitchel |

---

## 🔍 Key Findings

### > vs >= — the boundary matters
```sql
WHERE login_date >  '2022-05-09'  -- 125 rows (excludes May 9)
WHERE login_date >= '2022-05-09'  -- 165 rows (includes May 9)
-- Difference: 40 logins occurred exactly on 2022-05-09
```

### BETWEEN is inclusive on both ends
```sql
WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11'
-- Equivalent to: WHERE login_date >= '2022-05-09' AND login_date <= '2022-05-11'
-- Returns: 123 rows covering May 9, 10, and 11
```

### String quotes vs no quotes
```sql
-- Dates and times → single quotes required
WHERE login_date = '2022-05-09'
WHERE login_time < '07:00:00'

-- Numbers → no quotes
WHERE event_id >= 100       -- ✅ correct
WHERE event_id >= '100'     -- ❌ incorrect
```

---

## 💡 SQL Syntax Reference

```sql
-- Greater than / less than
SELECT * FROM log_in_attempts WHERE login_date > '2022-05-09';
SELECT * FROM log_in_attempts WHERE login_date >= '2022-05-09';

-- Date range with BETWEEN
SELECT * FROM log_in_attempts
WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11';

-- Time filter
SELECT * FROM log_in_attempts WHERE login_time < '07:00:00';
SELECT * FROM log_in_attempts
WHERE login_time BETWEEN '06:00:00' AND '07:00:00';

-- Numeric filter with specific columns
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id >= 100;

SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id BETWEEN 100 AND 150;
```

---

## 📁 Project Files

| File | Description |
|---|---|
| [`apply_more_filters_sql.sql`](./apply_more_filters_sql.sql) | SQL script with all comparison and range filter queries |

---

## 🧠 Key Concepts Applied

- **Comparison operators** — `>`, `<`, `>=`, `<=`, `=`, `<>` for numeric and date filtering
- **BETWEEN...AND** — Inclusive range filter for dates, times, and numbers
- **Date filtering** — Format `'YYYY-MM-DD'` in single quotes
- **Time filtering** — Format `'HH:MM:SS'` in single quotes
- **Numeric filtering** — No quotes around numeric values
- **Security investigation** — Using date/time filters to narrow down suspicious login events

---

## 📚 What I Learned

- How to use **comparison operators** to filter dates, times, and numbers in SQL
- The critical difference between `>` (excludes boundary) and `>=` (includes boundary)
- How `BETWEEN...AND` creates an **inclusive range** — equivalent to `>= X AND <= Y`
- That **date and time values require single quotes**, but **numeric values do not**
- How time-based filtering helps identify logins outside of normal working hours — a key security investigation technique

---

## 🛠️ Tools & Concepts Referenced

![MariaDB](https://img.shields.io/badge/Database-MariaDB-blue?style=flat-square&logo=mariadb&logoColor=white)
![SQL](https://img.shields.io/badge/Language-SQL-orange?style=flat-square)
![BETWEEN](https://img.shields.io/badge/Keyword-BETWEEN-green?style=flat-square)
![Operators](https://img.shields.io/badge/Operators->%20<%20>%3D%20<%3D-purple?style=flat-square)
![Date Filter](https://img.shields.io/badge/Filter-Date_%26_Time-red?style=flat-square)
