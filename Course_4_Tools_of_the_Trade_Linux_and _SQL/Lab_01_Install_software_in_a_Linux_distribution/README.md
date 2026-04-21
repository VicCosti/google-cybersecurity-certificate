# 🐧 Lab: Install Software in a Linux Distribution

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **Package manager:** APT (Advanced Package Tool)  

---

## 📋 Scenario

As a security analyst, having the right tools installed on your system is essential. In this lab, the goal was to install and manage two network security applications — **Suricata** and **tcpdump** — using the APT package manager on a Debian-based Linux distribution.

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | Confirm APT is installed | `apt` |
| 2 | Install Suricata | `sudo apt install suricata` |
| 2 | Verify Suricata installation | `suricata` |
| 2 | Uninstall Suricata | `sudo apt remove suricata` |
| 2 | Verify Suricata uninstalled | `suricata` |
| 3 | Install tcpdump | `sudo apt install tcpdump` |
| 4 | List all installed applications | `apt list --installed` |
| 5 | Reinstall Suricata | `sudo apt install suricata` |
| 5 | Verify both apps installed | `apt list --installed` |

---

## 🔍 Key Observations

**APT version installed:**
```
apt 2.2.4 (amd64)
```

**Suricata version installed:**
```
Suricata 6.0.1
```

**tcpdump version installed:**
```
tcpdump/oldoldstable,now 4.99.0-2+deb11u1 amd64 [installed]
```

**Final installed state (both apps confirmed):**
```
suricata/oldoldstable-security,now 1:6.0.1-3+deb11u1 amd64 [installed]
tcpdump/oldoldstable,now 4.99.0-2+deb11u1 amd64 [installed]
```

**Note on tcpdump permission error:**  
Running `tcpdump` directly returned:
```
tcpdump: eth0: You don't have permission to capture on that device
(socket: Operation not permitted)
```
This is expected behavior in a sandboxed lab environment. The error confirms tcpdump is correctly installed — capturing live network traffic requires elevated privileges (`sudo tcpdump`).

**Note on dependencies:**  
Installing Suricata automatically pulled in 26 additional dependency packages (libraries like `libpcap`, `libhyperscan5`, `libyaml`, etc.). These are required for Suricata to function and are managed automatically by APT.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`install_software_linux.sh`](./install_software_linux.sh) | Bash script with all commands used in the lab, with comments and expected outputs |

---

## 🧠 Key Concepts Applied

- **APT (Advanced Package Tool)** — Debian-based package manager for installing, removing, and listing software
- **sudo** — Elevating privileges for install/remove operations
- **Dependencies** — How APT automatically resolves and installs required libraries
- **Package verification** — Using `apt list --installed` to confirm installed software
- **Suricata** — Open-source network intrusion detection/prevention system (IDS/IPS)
- **tcpdump** — Command-line packet capture and analysis tool

---

## 📚 What I Learned

- How to use **APT** to install, uninstall, and reinstall packages on Debian-based Linux systems
- The role of **sudo** when managing system-level software
- How to **verify installations** by running the application and checking its version output
- How **package dependencies** work — installing one tool can pull in many supporting libraries
- The difference between a **permission error** (tool installed but needs elevated privileges) and a **missing binary error** (tool not installed)

---

## 🛠️ Tools & Commands Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![APT](https://img.shields.io/badge/Tool-APT-orange?style=flat-square)
![Suricata](https://img.shields.io/badge/Tool-Suricata-blue?style=flat-square)
![tcpdump](https://img.shields.io/badge/Tool-tcpdump-darkgreen?style=flat-square)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
