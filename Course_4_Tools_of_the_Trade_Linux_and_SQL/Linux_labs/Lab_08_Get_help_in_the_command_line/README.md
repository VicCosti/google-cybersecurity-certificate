# 🐧 Lab: Get Help in the Command Line

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **Shell:** Bash  

---

## 📋 Scenario

As a security analyst, you won't always remember every command and its options. Linux provides built-in help tools accessible directly from the command line. In this lab, the goal was to use `whatis`, `man`, and `apropos` to find information about commands and discover new ones.

---

## 🆘 Linux Help Commands Reference

| Command | Purpose | Best used when |
|---|---|---|
| `whatis` | One-line description of a command | You need a quick reminder of what a command does |
| `man` | Full manual page with all options | You need details about a specific command's options |
| `apropos` | Search manual pages by keyword | You don't know which command to use for a task |

---

## ✅ Tasks Completed

| Task | Command used | Finding |
|---|---|---|
| 1 | `whatis cat` | cat = "concatenate files and print on the standard output" |
| 1 | `man cat` | `-n` option numbers all output lines |
| 1 | `apropos -a first part file` | `head` returns the first part of a file |
| 2 | `man useradd` | `-e` option sets expiration date (format: YYYY-MM-DD) |
| 3 | `whatis rm` | removes files or directories |
| 3 | `whatis rmdir` | removes **empty** directories only |
| 4 | `apropos -a create new group` | `groupadd` creates a new group |

---

## 🔍 Key Findings

### cat options (from man cat)
```
-n, --number           number all output lines
-b, --number-nonblank  number nonempty output lines only
-A, --show-all         show all non-printing characters
-s, --squeeze-blank    suppress repeated empty lines
```

### useradd -e option (from man useradd)
```
-e, --expiredate EXPIRE_DATE
    The date on which the user account will be disabled.
    Format: YYYY-MM-DD
    Example: sudo useradd -e 2024-12-31 tempuser
```

### rm vs rmdir
```bash
whatis rm     # remove files or directories
whatis rmdir  # remove empty directories
```
`rmdir` → only works on **empty** directories  
`rm -r` → removes directories and all their contents recursively

### apropos results
```bash
apropos -a first part file   # → head (1)
apropos -a create new group  # → groupadd (8)
```

---

## ⚠️ Key Observation — man page navigation

```bash
# ❌ Typed in the shell (outside man) — does not work
Q     # Error: -bash: Q: command not found
q     # Error: -bash: q: command not found

# ✅ Correct — Q only works INSIDE the man pager
man cat   # open manual, then press Q to quit
```

`Q` is a navigation key for the man pager (`less`), not a shell command. It must be pressed **while inside** the man page, not after returning to the shell prompt.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`get_help_command_line.sh`](./get_help_command_line.sh) | Bash script with all help commands, outputs, and findings |

---

## 🧠 Key Concepts Applied

- **whatis** — Quick one-line command descriptions
- **man** — Full manual pages with complete option reference
- **apropos** — Keyword-based command discovery
- **apropos -a** — Restricts results to commands matching ALL keywords
- **man page navigation** — ENTER (one line), SPACE (one page), Q (quit)

---

## 📚 What I Learned

- How to use `whatis`, `man`, and `apropos` to find help without leaving the terminal
- The difference between `whatis` (quick lookup) and `man` (full reference)
- How `apropos -a` uses multiple keywords to narrow down command searches
- That `Q` to exit man pages only works **inside** the pager, not in the shell
- How to find unknown commands using keyword searches with `apropos`
- Key distinction between `rm` (files/directories) and `rmdir` (empty directories only)

---

## 🛠️ Commands Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![whatis](https://img.shields.io/badge/Command-whatis-blue?style=flat-square)
![man](https://img.shields.io/badge/Command-man-orange?style=flat-square)
![apropos](https://img.shields.io/badge/Command-apropos-green?style=flat-square)
