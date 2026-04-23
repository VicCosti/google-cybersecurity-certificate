# 👤 Lab: Add and Manage Users with Linux Commands

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **User:** `analyst` (with sudo privileges)

---

## 📋 Scenario

A new employee (`researcher9`) joins the Research department. Over the course of a year, their role changes and they eventually leave the organization. This lab simulates the full **user lifecycle management** process: adding, modifying ownership, updating group membership, and finally deleting a user from the system.

---

## 👤 User Lifecycle Simulated

```
researcher9 joins → added to system + research_team (primary)
       ↓
researcher9 takes ownership of project_r.txt
       ↓
researcher9 joins Sales → added to sales_team (secondary)
       ↓
researcher9 leaves → deleted from system + group cleaned up
```

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | Add new user to system | `sudo useradd researcher9` |
| 1 | Set primary group | `sudo usermod -g research_team researcher9` |
| 2 | Assign file ownership | `sudo chown researcher9 /home/researcher2/projects/project_r.txt` |
| 3 | Add secondary group | `sudo usermod -a -G sales_team researcher9` |
| 4 | Delete user | `sudo userdel researcher9` |
| 4 | Delete orphaned group | `sudo groupdel researcher9` |

---

## 💡 Key Command Reference

### useradd / userdel
```bash
sudo useradd username      # create new user
sudo userdel username      # delete user
sudo groupdel groupname    # delete group
```

### usermod — primary vs secondary group
```bash
sudo usermod -g groupname username    # set PRIMARY group (-g lowercase)
sudo usermod -a -G groupname username # add SECONDARY group (-G uppercase)
```

> ⚠️ **Important:** Always use `-a` (append) with `-G` when adding a secondary group.
> Without `-a`, the `-G` flag **replaces** all existing secondary groups instead of adding to them.
> Options are **case-sensitive**: `-a` lowercase, `-G` uppercase.

### chown
```bash
sudo chown username /path/to/file    # change file owner
```

---

## 🔍 Key Observations

### Typo error on chown
```bash
sudo chown research9 /home/researcher2/projects/project_r.txt
# Error: chown: invalid user: 'research9'
```
A single missing character (`researcher9` → `research9`) causes the command to fail with an invalid user error. Linux usernames are exact strings — always verify the username before running ownership commands.

### userdel expected message
```
userdel: group researcher9 not removed because it is not the primary group of user researcher9.
```
When a user is created in Linux, a group with the same name is automatically created. `userdel` removes the user but leaves this auto-created group behind if it is not set as the primary group. Always follow up with `groupdel` to clean up orphaned groups.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`manage_users_linux.sh`](./manage_users_linux.sh) | Bash script with full user lifecycle management commands |

---

## 🧠 Key Concepts Applied

- **Authentication vs Authorization** — Authentication proves who you are; authorization defines what you can access
- **useradd** — Create a new user on the system
- **usermod** — Modify user properties (group membership, etc.)
- **userdel / groupdel** — Remove users and clean up associated groups
- **chown** — Transfer file ownership to another user
- **Primary vs Secondary groups** — `-g` sets primary, `-a -G` appends secondary
- **sudo** — Required for all user management commands (root-level operations)
- **User lifecycle management** — Adding, modifying, and removing users as their role changes

---

## 📚 What I Learned

- How to manage the full **user lifecycle** in Linux — from creation to deletion
- The critical difference between `-g` (primary group) and `-G` (secondary group) in `usermod`
- Why `-a` must always accompany `-G` to avoid accidentally removing existing group memberships
- How `chown` transfers file ownership and why exact username spelling matters
- Why `userdel` leaves behind auto-created groups and how to clean them up with `groupdel`
- That all user management commands require **sudo** as they are root-level operations

---

## 🛠️ Commands Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![useradd](https://img.shields.io/badge/Command-useradd-blue?style=flat-square)
![usermod](https://img.shields.io/badge/Command-usermod-orange?style=flat-square)
![userdel](https://img.shields.io/badge/Command-userdel-red?style=flat-square)
![chown](https://img.shields.io/badge/Command-chown-purple?style=flat-square)
![sudo](https://img.shields.io/badge/Command-sudo-darkgreen?style=flat-square)
