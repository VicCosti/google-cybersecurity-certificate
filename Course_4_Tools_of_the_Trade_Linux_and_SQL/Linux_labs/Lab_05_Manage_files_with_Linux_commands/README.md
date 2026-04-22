# 🐧 Lab: Manage Files with Linux Commands

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **Shell:** Bash  

---

## 📋 Scenario

As a security analyst, keeping data well organized is essential for detecting issues and maintaining security. In this lab, the goal was to reorganize the `/home/analyst` directory structure by creating and removing directories, moving and deleting files, and documenting completed tasks using the nano text editor.

---

## 🗂️ Directory Structure

### Before
```
/home/analyst/
├── notes/
│   ├── Q3patches.txt
│   └── tempnotes.txt
├── reports/
│   ├── Q1patches.txt
│   └── Q2patches.txt
└── temp/
```

### After
```
/home/analyst/
├── logs/
├── notes/
│   └── tasks.txt
└── reports/
    ├── Q1patches.txt
    ├── Q2patches.txt
    └── Q3patches.txt
```

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | Create logs directory | `mkdir logs` |
| 2 | Remove temp directory | `rmdir temp` |
| 3 | Move Q3patches.txt to reports | `mv Q3patches.txt /home/analyst/reports/` |
| 4 | Remove tempnotes.txt | `rm tempnotes.txt` |
| 5 | Create empty tasks.txt | `touch tasks.txt` |
| 6 | Edit tasks.txt with nano | `nano tasks.txt` |
| 6 | Verify file contents | `head tasks.txt` |

---

## 🔍 Key Observations

### tasks.txt final content
```
Completed tasks
1. Managed file structure in /home/analyst
```

### rmdir vs rm -r
```bash
rmdir temp      # ✅ Removes an EMPTY directory
rm -r dirname   # ✅ Removes a directory and all its contents
```
`rmdir` only works on empty directories. In this lab, `temp` was confirmed empty before removal.

### nano save sequence
```
CTRL+X  →  Y  →  ENTER
```
In web-based lab environments, `CTRL+O` (the standard nano save shortcut) is intercepted by the browser. The sequence above is the recommended alternative: exit → confirm save → confirm filename.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`manage_files_linux.sh`](./manage_files_linux.sh) | Bash script with all file management commands, outputs, and notes |

---

## 🧠 Key Concepts Applied

- **mkdir** — Create a new directory
- **rmdir** — Remove an empty directory
- **rm** — Remove a file
- **mv** — Move a file to a different directory
- **touch** — Create a new empty file
- **nano** — Text editor for creating and editing file contents
- **Case sensitivity** — Linux commands and filenames are always case-sensitive
- **Directory structure management** — Organizing files for security and clarity

---

## 📚 What I Learned

- How to create and remove directories with `mkdir` and `rmdir`
- How to move files between directories with `mv`
- How to delete files with `rm` and the difference between `rmdir` and `rm -r`
- How to create empty files with `touch` and edit them with `nano`
- How to use the nano text editor in a web-based environment with the `CTRL+X → Y → ENTER` save sequence

---

## 🛠️ Commands Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![mkdir](https://img.shields.io/badge/Command-mkdir-blue?style=flat-square)
![rmdir](https://img.shields.io/badge/Command-rmdir-red?style=flat-square)
![rm](https://img.shields.io/badge/Command-rm-red?style=flat-square)
![mv](https://img.shields.io/badge/Command-mv-orange?style=flat-square)
![touch](https://img.shields.io/badge/Command-touch-green?style=flat-square)
![nano](https://img.shields.io/badge/Editor-nano-purple?style=flat-square)
