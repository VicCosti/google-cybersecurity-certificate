# 🐧 Lab: Find Files with Linux Commands

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **Shell:** Bash  

---

## 📋 Scenario

As a security analyst, navigating the Linux file system without a graphical interface is a core skill. In this lab, the goal was to locate and read files within the `/home/analyst` directory structure — simulating a real scenario where an analyst investigates user access reports and server logs.

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | Display current working directory | `pwd` |
| 1 | List contents of current directory | `ls` |
| 2 | Navigate to reports directory | `cd reports` |
| 2 | List subdirectories in reports | `ls` |
| 3 | Navigate to users subdirectory | `cd users` |
| 3 | List files in users directory | `ls` |
| 3 | Preview file contents | `head Q1_added_users.txt` |
| 3 | Display full file contents | `cat Q1_added_users.txt` |
| 4 | Navigate back using absolute path | `cd /home/analyst` |
| 4 | Navigate to logs directory | `cd logs` |
| 4 | List files in logs directory | `ls` |
| 4 | Display first 10 lines of log file | `head server_logs.txt` |

---

## 🗂️ Directory Structure Explored

```
/home/analyst/
├── logs/
│   └── server_logs.txt
├── projects/
├── reports/
│   └── users/
│       ├── Q1_added_users.txt
│       └── Q1_deleted_users.txt
└── temp/
```

---

## 🔍 Key Findings

### Q1_added_users.txt

| employee_id | username | department |
|---|---|---|
| 1001 | bmoreno | Marketing |
| 1026 | apatel | Human Resources |
| 1041 | cgriffin | Sales |
| 1104 | mreed | Information Technology |
| 1177 | aezra | Human Resources |
| 1188 | noshiro | Finance |

**Quiz answers:**
- `aezra` works in → **Human Resources**
- `mreed` (Information Technology) employee_id → **1104**

### server_logs.txt — First 10 lines

```
2022-09-28 13:55:55 info    User logged on successfully
2022-09-28 13:56:22 error   The password is incorrect
2022-09-28 13:56:48 warning The file storage is 75% full
2022-09-28 15:55:55 info    User logged on successfully
2022-09-28 15:56:22 error   The username is incorrect
2022-09-28 15:56:48 warning The file storage is 90% full
2022-09-28 16:55:55 info    User navigated to settings page
2022-09-28 16:56:22 error   The password is incorrect
2022-09-28 16:56:48 warning The current user's password expires in 15 days
2022-09-29 13:55:55 info    User logged on successfully
```

**Log analysis:**
- `info` entries → 4
- `error` entries → 3
- `warning` entries → **3** (lines 3, 6, 9)

---

## 📁 Project Files

| File | Description |
|---|---|
| [`find_files_linux.sh`](./find_files_linux.sh) | Bash script with all navigation commands, outputs, and findings |

---

## 🧠 Key Concepts Applied

- **pwd** — Print working directory to confirm current location
- **ls** — List files and directories in the current location
- **cd** — Navigate between directories (relative and absolute paths)
- **cat** — Display full file contents
- **head** — Display only the first N lines of a file (default: 10)
- **Absolute vs relative paths** — `cd reports` (relative) vs `cd /home/analyst` (absolute)
- **Log analysis** — Reading and interpreting server log entries by severity level

---

## 📚 What I Learned

- How to navigate a Linux file system using `pwd`, `ls`, and `cd`
- The difference between **relative paths** (`cd reports`) and **absolute paths** (`cd /home/analyst`)
- How to use `cat` to read full file contents and `head` to preview the first lines
- How server logs are structured with **severity levels** — `info`, `error`, `warning`
- How file navigation skills apply directly to security tasks like reviewing user access reports and analyzing logs

---

## 🛠️ Commands Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![pwd](https://img.shields.io/badge/Command-pwd-blue?style=flat-square)
![ls](https://img.shields.io/badge/Command-ls-orange?style=flat-square)
![cd](https://img.shields.io/badge/Command-cd-green?style=flat-square)
![cat](https://img.shields.io/badge/Command-cat-purple?style=flat-square)
![head](https://img.shields.io/badge/Command-head-darkgreen?style=flat-square)
