-- ============================================================
-- Lab: Apply More Filters in SQL
-- Course: Google Cybersecurity Professional Certificate
-- Course 4: Tools of the Trade - Linux and SQL
-- Platform: Google Skills / Qwiklabs (MariaDB)
-- Database: organization
-- Table: log_in_attempts
-- ============================================================

-- Comparison operators used in this lab:
-- =    equal to
-- >    greater than
-- <    less than
-- <>   not equal to
-- >=   greater than or equal to
-- <=   less than or equal to

-- ------------------------------------------------------------
-- TASK 1 - Retrieve login attempts after a certain date
-- ------------------------------------------------------------

-- Filter login attempts AFTER 2022-05-09 (not including that date)
SELECT *
FROM log_in_attempts
WHERE login_date > '2022-05-09';
-- Returns 125 rows (dates: 2022-05-10, 2022-05-11, 2022-05-12)
-- Answer: 125 login attempts made after 2022-05-09

-- Filter login attempts ON OR AFTER 2022-05-09 (including that date)
SELECT *
FROM log_in_attempts
WHERE login_date >= '2022-05-09';
-- Returns 165 rows (dates: 2022-05-09, 2022-05-10, 2022-05-11, 2022-05-12)
-- Answer: 165 login attempts made on or after 2022-05-09

-- Note: the difference between > and >= is whether the boundary
-- date is included in the results:
-- >  '2022-05-09' → excludes May 9 → 125 rows
-- >= '2022-05-09' → includes May 9 → 165 rows
-- Difference: 40 login attempts were made on exactly 2022-05-09

-- ------------------------------------------------------------
-- TASK 2 - Retrieve logins in a date range
-- ------------------------------------------------------------

-- Filter login attempts BETWEEN 2022-05-09 and 2022-05-11 (inclusive)
SELECT *
FROM log_in_attempts
WHERE login_date BETWEEN '2022-05-09' AND '2022-05-11';
-- Returns 123 rows
-- Answer: 123 login attempts between May 9 and May 11

-- Note: BETWEEN is inclusive on both ends
-- BETWEEN 'X' AND 'Y' is equivalent to: >= 'X' AND <= 'Y'
-- Date values must be enclosed in single quotes
-- Format: 'YYYY-MM-DD'

-- ------------------------------------------------------------
-- TASK 3 - Investigate logins at certain times
-- ------------------------------------------------------------

-- Filter login attempts made BEFORE 07:00:00 (outside work hours)
SELECT *
FROM log_in_attempts
WHERE login_time < '07:00:00';
-- Fifth row username: eraab
-- Answer: eraab is the fifth user returned

-- Narrow the range: logins BETWEEN 06:00:00 and 07:00:00
SELECT *
FROM log_in_attempts
WHERE login_time BETWEEN '06:00:00' AND '07:00:00';
-- Earliest login time in this range: 06:01:31 (lyamamot)
-- Answer: earliest login was at 06:01:31

-- Note: time values also use single quotes and follow HH:MM:SS format
-- BETWEEN works the same for time as for dates (inclusive on both ends)

-- ------------------------------------------------------------
-- TASK 4 - Investigate logins by event ID
-- ------------------------------------------------------------

-- Filter login attempts with event_id GREATER THAN OR EQUAL TO 100
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id >= 100;
-- Returns 101 rows
-- Third row login date: 2022-05-09 (event_id 102, jreckley)
-- Answer: login date of third result = 2022-05-09

-- Narrow the range: event_id BETWEEN 100 AND 150
SELECT event_id, username, login_date
FROM log_in_attempts
WHERE event_id BETWEEN 100 AND 150;
-- Returns 51 rows
-- Seventh result: event_id 106, tmitchel, 2022-05-12
-- Answer: seventh username = tmitchel

-- Note: numeric values do NOT use single quotes in SQL
-- WHERE event_id >= 100   ✅ correct (no quotes for numbers)
-- WHERE event_id >= '100' ❌ incorrect (quotes are for strings/dates)
