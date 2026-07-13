-- ============================================================
-- Lab: Complete a SQL Join
-- Course: Google Cybersecurity Professional Certificate
-- Course 4: Tools of the Trade - Linux and SQL
-- Platform: Google Skills / Qwiklabs (MariaDB)
-- Database: organization
-- Tables: machines, employees, log_in_attempts
-- ============================================================

-- Join types used in this lab:
-- INNER JOIN → only rows with matching values in BOTH tables
-- LEFT JOIN  → all rows from LEFT table + matching rows from right
-- RIGHT JOIN → all rows from RIGHT table + matching rows from left

-- Shared columns used as join keys:
-- machines  ↔ employees     → device_id
-- employees ↔ log_in_attempts → username

-- ------------------------------------------------------------
-- TASK 1 - Match employees to their machines (INNER JOIN)
-- ------------------------------------------------------------

-- First, review the machines table alone
SELECT *
FROM machines;
-- Returns 200 rows — includes machines with employee_id = 0
-- (unassigned machines with no matching employee)

-- INNER JOIN machines and employees on device_id
SELECT *
FROM machines
INNER JOIN employees ON machines.device_id = employees.device_id;
-- Returns 185 rows
-- Answer: 185 rows returned by the inner join

-- Note: INNER JOIN excludes the 15 machines with employee_id = 0
-- because they have no matching record in the employees table
-- Only rows where device_id exists in BOTH tables are returned

-- ------------------------------------------------------------
-- TASK 2 - Return more data (LEFT JOIN and RIGHT JOIN)
-- ------------------------------------------------------------

-- LEFT JOIN: all machines + matching employees
-- Machines without an assigned employee will show NULL in employee columns
SELECT *
FROM machines
LEFT JOIN employees ON machines.device_id = employees.device_id;
-- Returns 200 rows (all machines, including unassigned ones)
-- Last record username: NULL (unassigned machine z821a946b264)
-- Answer: last username = NULL

-- Note: LEFT JOIN keeps ALL rows from the LEFT table (machines)
-- For unassigned machines (employee_id = 0), employee columns = NULL

-- RIGHT JOIN: all employees + matching machines
-- Employees without an assigned machine will show NULL in machine columns
SELECT *
FROM machines
RIGHT JOIN employees ON machines.device_id = employees.device_id;
-- Returns 200 rows (all employees, including those without machines)
-- Last record username: areyes (employee_id 1199)
-- Answer: last username = areyes

-- Note: RIGHT JOIN keeps ALL rows from the RIGHT table (employees)
-- Employees without a device_id in machines show NULL in machine columns
-- Example: lrodriqu (1009), asundara (1014), yappiah (1033) have no machine

-- ------------------------------------------------------------
-- TASK 3 - Retrieve login attempt data (INNER JOIN)
-- ------------------------------------------------------------

-- INNER JOIN employees and log_in_attempts on username
SELECT *
FROM employees
INNER JOIN log_in_attempts ON employees.username = log_in_attempts.username;
-- Returns 200 rows
-- Answer: 200 records returned by this inner join

-- Note: must specify table.column when both tables share the column name
-- employees.username = log_in_attempts.username
-- Without table prefix, SQL returns an ambiguity error

-- Note: the result has 200 rows because all 200 login attempts
-- match an employee username in the employees table
-- Some employees appear multiple times (one row per login attempt)
-- Example: tmitchel appears 11 times (11 login attempts)
