# 🐧 Lab: Filter with grep

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **Shell:** Bash  

---

## 📋 Scenario

As a security analyst, being able to quickly search through logs and user data files is essential. In this lab, the goal was to use `grep` and the pipe operator `|` to filter specific information from server logs and user report files — simulating real tasks like identifying error events and tracking user access changes.

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | Navigate to logs directory | `cd /home/analyst/logs` |
| 1 | Search for error entries in log file | `grep error server_logs.txt` |
| 2 | Navigate to users directory | `cd /home/analyst/reports/users` |
| 2 | Filter files containing "Q1" in name | `ls \| grep Q1` |
| 2 | Filter files containing "access" in name | `ls \| grep access` |
| 3 | Search for username in deleted users file | `grep jhill Q2_deleted_users.txt` |
| 3 | Search for department in added users file | `grep "Human Resources" Q4_added_users.txt` |

---

## 🔍 Key Findings

### Task 1 — Error messages in server_logs.txt

```
2022-09-28 13:56:22 error   The password is incorrect
2022-09-28 15:56:22 error   The username is incorrect
2022-09-28 16:56:22 error   The password is incorrect
2022-09-29 13:56:22 error   An unexpected error occurred
2022-09-29 15:56:22 error   Unauthorized access
2022-09-29 16:56:22 error   Unauthorized access
```
**Total error entries: 6**

### Task 2 — Files in /home/analyst/reports/users/

| Filter | Matching files | Count |
|---|---|---|
| `Q1` | Q1_access.txt, Q1_added_users.txt, Q1_deleted_users.txt | 3 |
| `access` | Q1_access.txt, Q2_access.txt, Q3_access.txt, Q4_access.txt | 4 |

### Task 3 — User data search

| Search | File | Result |
|---|---|---|
| `jhill` | Q2_deleted_users.txt | ✅ Found — employee_id 1025, Sales dept |
| `Human Resources` | Q4_added_users.txt | 2 users: sshah (1151), msosa (1145) |

---

## 💡 Key Concepts

### grep — basic usage
```bash
grep pattern filename
```
Returns all lines in the file that contain the specified pattern.

### Pipe operator `|`
```bash
command1 | command2
```
Sends the output of `command1` as input to `command2`. In this lab used to filter `ls` output by filename pattern.

### grep with multi-word strings
```bash
grep "Human Resources" filename
```
Quotes are **required** for strings containing spaces — without them, grep treats each word as a separate argument and returns an error.

### ⚠️ Platform note
When using `ls | grep` the lab platform requires you to be **inside the target directory** before running the command. Running `ls /path/to/dir | grep pattern` from a different directory produces the same output but may not be recognized by the progress checker.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`filter_with_grep.sh`](./filter_with_grep.sh) | Bash script with all grep and pipe commands, outputs, and findings |

---

## 🧠 Key Concepts Applied

- **grep** — Search for specific patterns within file contents
- **Pipe `|`** — Chain commands by passing output of one as input to another
- **ls | grep** — Filter directory listings by filename pattern
- **Quoted strings** — Required for multi-word search patterns in grep
- **Log analysis** — Filtering server logs by severity level (`error`)
- **User access tracking** — Searching added/deleted user files by username or department

---

## 📚 What I Learned

- How to use `grep` to search file **contents** for specific patterns
- How to combine `ls` and `grep` with a **pipe** to filter file **names**
- Why **quotes are required** for multi-word grep patterns
- How `grep` is used in real security workflows — filtering error logs, tracking user changes, investigating access events
- The importance of being in the **correct directory** when running piped commands in guided lab environments

---

## 🛠️ Commands Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![grep](https://img.shields.io/badge/Command-grep-blue?style=flat-square)
![pipe](https://img.shields.io/badge/Operator-pipe_%7C-orange?style=flat-square)
![ls](https://img.shields.io/badge/Command-ls-green?style=flat-square)
![cd](https://img.shields.io/badge/Command-cd-purple?style=flat-square)
