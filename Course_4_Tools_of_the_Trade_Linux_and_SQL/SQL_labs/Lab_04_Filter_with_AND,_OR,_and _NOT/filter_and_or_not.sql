-- ============================================================
-- Lab: Filter with AND, OR, and NOT
-- Course: Google Cybersecurity Professional Certificate
-- Course 4: Tools of the Trade - Linux and SQL
-- Platform: Google Skills / Qwiklabs (MariaDB)
-- Database: organization
-- Tables: log_in_attempts, employees
-- ============================================================

-- Logical operators used in this lab:
-- AND  → both conditions must be true
-- OR   → at least one condition must be true
-- NOT  → negates a condition (returns rows where condition is false)

-- ------------------------------------------------------------
-- TASK 1 - Retrieve after hours failed login attempts
-- ------------------------------------------------------------

-- Find all FAILED login attempts made AFTER 18:00
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00:00' AND success = 0;
-- Returns 19 rows
-- Answer: 19 failed login attempts after business hours

-- Note: success is a Boolean column stored as integer
-- success = 1 → TRUE  (successful login)
-- success = 0 → FALSE (failed login)
-- Boolean values do NOT use single quotes (not string data)

-- ------------------------------------------------------------
-- TASK 2 - Retrieve login attempts on specific dates
-- ------------------------------------------------------------

-- Find all login attempts on 2022-05-09 OR 2022-05-08
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';
-- Returns 75 rows
-- Answer: 75 login attempts on these two days

-- Note: even though both conditions use the same column (login_date),
-- you must write the full condition each time:
-- ✅ WHERE login_date = '2022-05-09' OR login_date = '2022-05-08'
-- ❌ WHERE login_date = '2022-05-09' OR '2022-05-08'  (invalid syntax)

-- ------------------------------------------------------------
-- TASK 3 - Retrieve login attempts outside of Mexico
-- ------------------------------------------------------------

-- Find all login attempts NOT originating from Mexico
-- Country values include both 'MEX' and 'MEXICO'
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
-- Returns 144 rows
-- Answer: 144 login attempts made outside of Mexico

-- Note: NOT negates the LIKE condition
-- 'MEX%' matches both 'MEX' and 'MEXICO' with the % wildcard
-- NOT LIKE 'MEX%' excludes both variations in one filter

-- ------------------------------------------------------------
-- TASK 4 - Retrieve employees in Marketing (East building)
-- ------------------------------------------------------------

-- Find Marketing employees in East building offices
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East%';
-- Returns 7 rows
-- First employee: elarson (employee_id 1000, East-170)
-- Answer: first username = elarson

-- Note: AND requires BOTH conditions to be true simultaneously
-- department must be 'Marketing' AND office must start with 'East'

-- ------------------------------------------------------------
-- TASK 5 - Retrieve employees in Finance or Sales
-- ------------------------------------------------------------

-- Find employees in Finance OR Sales department
SELECT *
FROM employees
WHERE department = 'Finance' OR department = 'Sales';
-- Returns 71 rows
-- First Sales employee returned: lrodriqu (employee_id 1009)
-- Answer: first Sales username = lrodriqu

-- Note: both conditions must specify the column name explicitly
-- ✅ WHERE department = 'Finance' OR department = 'Sales'
-- ❌ WHERE department = 'Finance' OR 'Sales'  (invalid syntax)

-- ------------------------------------------------------------
-- TASK 6 - Retrieve all employees NOT in IT
-- ------------------------------------------------------------

-- Method 1: using NOT with = operator
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
-- Returns 161 rows

-- Method 2: using != operator (equivalent result)
SELECT *
FROM employees
WHERE department != 'Information Technology';
-- Returns 161 rows (identical result)

-- Answer: 161 employees are not in the Information Technology department

-- Note: NOT department = 'X' and department != 'X' are equivalent
-- Both produce the same result — choose whichever is clearer to read
