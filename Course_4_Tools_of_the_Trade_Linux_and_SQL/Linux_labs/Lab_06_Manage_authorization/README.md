# 🔐 Lab: Manage Authorization

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **User:** `researcher2` | **Group:** `research_team`

---

## 📋 Scenario

As a security analyst, setting correct file permissions is critical to protecting sensitive data. In this lab, the goal was to audit and fix file and directory permissions in the `/home/researcher2/projects` directory — ensuring that only authorized users and groups could read, write, or execute each file.

---

## 🔑 Permission String Reference

```
- r w x | r w x | r w x
│ └─┬─┘   └─┬─┘   └─┬─┘
│  user    group   other
└── file type: d=directory, -=regular file
```

| Character | Meaning |
|---|---|
| `r` | Read permission |
| `w` | Write permission |
| `x` | Execute permission |
| `-` | Permission not granted |
| `d` | Directory |

---

## ✅ Tasks Completed

| Task | File/Dir | Issue found | Fix applied |
|---|---|---|---|
| 1 | all files | Audited permissions and found hidden file | `ls -la`, `ls -a` |
| 2 | `project_k.txt` | `other` had write permission | `chmod o=r project_k.txt` |
| 2 | `project_m.txt` | `group` had read permission | `chmod g-r project_m.txt` |
| 3 | `.project_x.txt` | `user` and `group` had write permission | `chmod u=r,g=r .project_x.txt` |
| 4 | `drafts/` | `group` had execute permission | `chmod g-x drafts/` |

---

## 🔍 Permission Changes

### project_k.txt
```
Before: -rw-rw-rw-   (other had write access)
After:  -rw-rw-r--   (other can only read)
```

### project_m.txt
```
Before: -rw-r-----   (group had read access)
After:  -rw-------   (user only)
```

### .project_x.txt (hidden file)
```
Before: -rw--w----   (user had write, group had write)
After:  -r--r-----   (user and group read only)
```

### drafts/ (directory)
```
Before: drwx--x---   (group had execute access)
After:  drwx------   (user only)
```

---

## 📊 Final Permission State

```
-r--r----- researcher2 research_team  .project_x.txt
drwx------ researcher2 research_team  drafts/
-rw-rw-r-- researcher2 research_team  project_k.txt
-rw------- researcher2 research_team  project_m.txt
-rw-rw-r-- researcher2 research_team  project_r.txt
-rw-rw-r-- researcher2 research_team  project_t.txt
```

---

## 💡 chmod Syntax Reference

```bash
# Symbolic mode — add/remove specific permissions
chmod o-w filename      # remove write from other
chmod g-r filename      # remove read from group
chmod g-x dirname/      # remove execute from group on directory

# Assignment mode — set exact permissions
chmod o=r filename      # set other to read only
chmod u=r,g=r filename  # set user=read, group=read simultaneously
```

---

## 📁 Project Files

| File | Description |
|---|---|
| [`manage_authorization.sh`](./manage_authorization.sh) | Bash script with all permission audit and chmod commands |

---

## 🧠 Key Concepts Applied

- **ls -la** — List all files including hidden ones with full permission details
- **ls -a** — List all files including hidden ones (no permission details)
- **chmod** — Change file and directory permissions
- **Permission types** — Read (`r`), Write (`w`), Execute (`x`)
- **Owner types** — User (`u`), Group (`g`), Other (`o`)
- **Hidden files** — Files starting with `.` are hidden by default in Linux
- **Principle of Least Privilege** — Only grant the minimum permissions necessary

---

## 📚 What I Learned

- How to read and interpret the **10-character Linux permission string**
- How to use `ls -la` to audit permissions on all files including hidden ones
- How to use `chmod` in both **symbolic mode** (`o-w`) and **assignment mode** (`o=r`)
- How to apply the **principle of least privilege** by removing unnecessary permissions
- How **directory execute permission** controls whether users can enter and access a directory's contents
- How **hidden files** (starting with `.`) work in Linux and why they matter for security audits

---

## 🛠️ Commands Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![chmod](https://img.shields.io/badge/Command-chmod-red?style=flat-square)
![ls-la](https://img.shields.io/badge/Command-ls_--la-blue?style=flat-square)
![Least Privilege](https://img.shields.io/badge/Principle-Least_Privilege-orange?style=flat-square)
