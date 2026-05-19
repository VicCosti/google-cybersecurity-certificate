-- ============================================================
-- Lab: Filter a SQL Query
-- Course: Google Cybersecurity Professional Certificate
-- Course 4: Tools of the Trade - Linux and SQL
-- Platform: Google Skills / Qwiklabs (MariaDB)
-- Database: organization
-- Tables: machines, employees
-- ============================================================

-- ------------------------------------------------------------
-- TASK 1 - List all organization machines
-- ------------------------------------------------------------

-- Select ALL columns from machines (for reference)
SELECT *
FROM machines;
-- Returns 200 rows

-- Select only device_id and operating_system columns
SELECT device_id, operating_system
FROM machines;
-- Returns 200 rows — same number, fewer columns
-- Answer: 200 rows returned

-- ------------------------------------------------------------
-- TASK 2 - Retrieve machines with OS 2
-- ------------------------------------------------------------

-- Filter machines table to return only OS 2 devices
SELECT device_id, operating_system
FROM machines
WHERE operating_system = 'OS 2';
-- Returns 80 rows
-- Answer: 80 machines use OS 2 and need an update

-- Note: WHERE clause filters rows based on a condition
-- String values in WHERE must be enclosed in single quotes: 'OS 2'
-- The comparison is case-sensitive in MariaDB

-- ------------------------------------------------------------
-- TASK 3 - List employees in specific departments
-- ------------------------------------------------------------

-- Filter employees table for Finance department
SELECT *
FROM employees
WHERE department = 'Finance';
-- Returns 38 rows
-- First row: employee_id 1003 (sgilmore, South-153)
-- Answer: first employee_id = 1003

-- Filter employees table for Sales department
SELECT *
FROM employees
WHERE department = 'Sales';
-- Returns 33 rows
-- Answer: 33 employees work in the Sales department

-- ------------------------------------------------------------
-- TASK 4 - Identify employee machines
-- ------------------------------------------------------------

-- Find the employee using office South-109
SELECT *
FROM employees
WHERE office = 'South-109';
-- Returns 1 row:
-- employee_id: 1010 | username: jlansky | department: Finance
-- Answer: jlansky uses the computer with the issue

-- Find ALL employees in the South building using LIKE with wildcard
SELECT *
FROM employees
WHERE office LIKE 'South%';
-- Returns 41 rows
-- First row: employee_id 1003, sgilmore, Finance, South-153
-- Answer: first employee listed belongs to Finance department

-- Note: LIKE operator is used for pattern matching
-- % wildcard matches any sequence of characters of any length
-- 'South%' matches any office starting with 'South':
--   South-109, South-153, South-366, etc.
-- To match offices ENDING with a pattern: '%109'
-- To match offices CONTAINING a pattern: '%South%'
