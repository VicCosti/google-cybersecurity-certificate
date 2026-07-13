# 🗄️ Lab: Complete a SQL Join

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** MariaDB — `organization` database  
> **Tables used:** `machines`, `employees`, `log_in_attempts`

---

## 📋 Scenario

During a security incident investigation, a security analyst needs to combine data from multiple tables to identify which employees are using which machines and which employees have made login attempts. This lab focuses on SQL JOIN operations to connect related tables through shared columns.

---

## 🔗 Table Relationships

```
machines ──────────── employees ──────────── log_in_attempts
         device_id               username
         (shared key)            (shared key)
```

---

## 🔀 Join Types Reference

| Join Type | Returns | Use case |
|---|---|---|
| `INNER JOIN` | Only rows with matches in BOTH tables | Find employees WITH machines |
| `LEFT JOIN` | ALL rows from left table + matches from right | Find ALL machines (assigned or not) |
| `RIGHT JOIN` | ALL rows from right table + matches from left | Find ALL employees (with or without machine) |

---

## ✅ Tasks Completed

| Task | Query | Result |
|---|---|---|
| 1 | `INNER JOIN machines + employees ON device_id` | 185 rows |
| 2 | `LEFT JOIN machines + employees ON device_id` | 200 rows, last username: NULL |
| 2 | `RIGHT JOIN machines + employees ON device_id` | 200 rows, last username: areyes |
| 3 | `INNER JOIN employees + log_in_attempts ON username` | 200 rows |

---

## 🔍 Key Findings

### Why INNER JOIN returns 185 rows (not 200)
The `machines` table has 200 entries, but 15 machines have `employee_id = 0` — meaning they are not assigned to any employee. These 15 unassigned machines have no match in the `employees` table, so INNER JOIN excludes them.

```
machines table:    200 rows
unassigned (id=0): 15 machines → excluded by INNER JOIN
INNER JOIN result: 185 rows
```

### LEFT JOIN — NULL values reveal unassigned machines
```sql
FROM machines LEFT JOIN employees ON machines.device_id = employees.device_id
-- 200 rows returned (ALL machines)
-- 15 rows have NULL in employee columns → unassigned machines
-- Last record: NULL username (machine z821a946b264)
```

### RIGHT JOIN — NULL values reveal employees without machines
```sql
FROM machines RIGHT JOIN employees ON machines.device_id = employees.device_id
-- 200 rows returned (ALL employees)
-- Some employees have NULL in machine columns → no assigned device
-- Examples: lrodriqu, asundara, yappiah, jreckley, ejones...
-- Last record: areyes (employee_id 1199)
```

### INNER JOIN on username — one row per login attempt
```sql
FROM employees INNER JOIN log_in_attempts ON employees.username = log_in_attempts.username
-- 200 rows (all 200 login attempts matched an employee)
-- Employees with multiple logins appear multiple times
-- tmitchel appears 11 times (11 login attempts in the dataset)
```

---

## 💡 SQL Syntax Reference

```sql
-- INNER JOIN
SELECT *
FROM table1
INNER JOIN table2 ON table1.shared_column = table2.shared_column;

-- LEFT JOIN
SELECT *
FROM table1
LEFT JOIN table2 ON table1.shared_column = table2.shared_column;

-- RIGHT JOIN
SELECT *
FROM table1
RIGHT JOIN table2 ON table1.shared_column = table2.shared_column;

-- Must use table.column when column name is shared between tables
FROM employees
INNER JOIN log_in_attempts ON employees.username = log_in_attempts.username;
```

---

## 📁 Project Files

| File | Description |
|---|---|
| [`complete_sql_join.sql`](./complete_sql_join.sql) | SQL script with all JOIN queries, comments, and findings |

---

## 🧠 Key Concepts Applied

- **INNER JOIN** — Returns only rows with matching values in both tables; excludes non-matching rows from either table
- **LEFT JOIN** — Returns all rows from the left table; fills with NULL where no match exists in the right table
- **RIGHT JOIN** — Returns all rows from the right table; fills with NULL where no match exists in the left table
- **Join key** — The shared column used to connect two tables (`device_id`, `username`)
- **table.column notation** — Required when the same column name exists in both joined tables
- **NULL in join results** — Indicates a record in one table has no matching record in the other

---

## 📚 What I Learned

- How **INNER JOIN** connects tables and why it may return fewer rows than either source table
- How **LEFT** and **RIGHT JOIN** preserve all records from one side of the join, filling unmatched fields with `NULL`
- Why `NULL` values in join results are meaningful — they reveal **unassigned machines** (LEFT JOIN) or **employees without devices** (RIGHT JOIN)
- The importance of **table.column notation** when joining tables that share a column name
- How the same employee can appear **multiple times** in join results when they have multiple matching records (e.g. multiple login attempts)

---

## 🛠️ Tools & Concepts Referenced

![MariaDB](https://img.shields.io/badge/Database-MariaDB-blue?style=flat-square&logo=mariadb&logoColor=white)
![SQL](https://img.shields.io/badge/Language-SQL-orange?style=flat-square)
![INNER JOIN](https://img.shields.io/badge/Join-INNER_JOIN-green?style=flat-square)
![LEFT JOIN](https://img.shields.io/badge/Join-LEFT_JOIN-purple?style=flat-square)
![RIGHT JOIN](https://img.shields.io/badge/Join-RIGHT_JOIN-red?style=flat-square)
