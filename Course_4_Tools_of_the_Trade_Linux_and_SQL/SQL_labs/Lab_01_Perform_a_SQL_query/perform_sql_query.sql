-- ============================================================
-- Lab: Perform a SQL Query
-- Course: Google Cybersecurity Professional Certificate
-- Course 4: Tools of the Trade - Linux and SQL
-- Platform: Google Skills / Qwiklabs (MariaDB)
-- Database: organization
-- ============================================================

-- Note: SQL keywords (SELECT, FROM, WHERE, ORDER BY) are
-- case-insensitive, but table names in MySQL/MariaDB ARE
-- case-sensitive. Always match table names exactly.

-- ------------------------------------------------------------
-- TASK 1 - Retrieve employee device data
-- ------------------------------------------------------------

-- Select ALL columns from the machines table
SELECT *
FROM machines;
-- Returns 200 rows with columns:
-- device_id | operating_system | email_client | OS_patch_date | employee_id

-- Note: SELECT* (without space) also works but SELECT * is best practice

-- Select only device_id and email_client columns
SELECT device_id, email_client
FROM machines;
-- Third row answer: Email Client 2 (device a305b818c708)

-- Select device_id, operating_system, and OS_patch_date columns
SELECT device_id, operating_system, OS_patch_date
FROM machines;
-- First entry patch date: 2021-09-01 (device a184b775c707, OS 1)

-- ------------------------------------------------------------
-- TASK 2 - Investigate login activity
-- ------------------------------------------------------------

-- Select event_id and country to check login locations
SELECT event_id, country
FROM log_in_attempts;
-- Answer: No login attempts from Australia
-- All countries are: USA, US, CAN, CANADA, MEX, MEXICO

-- Select username, login_date, login_time to check login schedule
SELECT username, login_date, login_time
FROM log_in_attempts;
-- Fifth row answer: jrafael (2022-05-11 at 03:05:59)

-- Select ALL columns from log_in_attempts
SELECT *
FROM log_in_attempts;
-- Returns 200 rows with columns:
-- event_id | username | login_date | login_time | country | ip_address | success
-- success: 1 = successful login, 0 = failed login

-- ------------------------------------------------------------
-- TASK 3 - Order login attempts data
-- ------------------------------------------------------------

-- Sort all login attempts by login_date (ascending by default)
SELECT *
FROM log_in_attempts
ORDER BY login_date;
-- First record: ivelasco on 2022-05-08
-- Note: within the same date, rows are NOT sorted by time yet

-- Sort login attempts by login_date AND login_time
SELECT *
FROM log_in_attempts
ORDER BY login_date, login_time;
-- First record: bsand on 2022-05-08 at 00:19:11
-- Adding login_time as secondary sort key gives precise chronological order

-- Note: ORDER BY can sort by multiple columns separated by commas
-- Each column sorts within the groups established by the previous column
-- Default sort direction is ASC (ascending) — add DESC for descending
