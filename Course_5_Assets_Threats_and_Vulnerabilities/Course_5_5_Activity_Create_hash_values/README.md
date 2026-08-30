# #️⃣ Lab: Create Hash Values

> **Course:** Google Cybersecurity Professional Certificate — Course 5: Assets, Threats, and Vulnerabilities  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **Shell:** Bash  
> **Tools used:** `sha256sum`, `cat`, `cmp`  
> **Concept:** Data integrity verification through hashing

---

## 📋 Scenario Overview

Two files appear to contain identical content when viewed with `cat`. The goal was to generate SHA-256 hash values for each file and compare them to determine whether the files are truly identical — demonstrating why visual inspection alone is insufficient for verifying data integrity.

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | List home directory | `ls` |
| 1 | Display file1.txt contents | `cat file1.txt` |
| 1 | Display file2.txt contents | `cat file2.txt` |
| 1 | Generate SHA-256 hash for file1.txt | `sha256sum file1.txt` |
| 1 | Generate SHA-256 hash for file2.txt | `sha256sum file2.txt` |
| 2 | Write file1 hash to file1hash | `sha256sum file1.txt >> file1hash` |
| 2 | Write file2 hash to file2hash | `sha256sum file2.txt >> file2hash` |
| 2 | Display both hash files | `cat file1hash` / `cat file2hash` |
| 2 | Compare hash files byte by byte | `cmp file1hash file2hash` |

---

## 🔍 Key Findings

### File contents — visually identical

```
file1.txt: X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
file2.txt: X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

Both files appear **identical** when displayed with `cat`. A hidden character (invisible byte) in file2.txt is not shown.

### Hash values — completely different

```
file1.txt → 131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267
file2.txt → 2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b
```

The SHA-256 hashes are **entirely different** — proving the files are not identical despite appearing the same visually.

### cmp result

```
file1hash file2hash differ: char 1, line 1
```

The very first character of the two hash strings is different — confirming the files differ at the byte level.

---

## 💡 Key Insight — Why This Matters for Security

This lab demonstrates a critical security concept: **you cannot verify data integrity with visual inspection alone.**

A malicious actor could:
- Replace a legitimate file with a slightly modified version (e.g. malware)
- Add an invisible character to a file to alter its behavior
- Modify a single byte in a binary that changes its execution entirely

In all these cases, `cat` would show identical-looking content — but `sha256sum` would immediately reveal the difference. This is why hash verification is used to:
- Validate downloaded software integrity
- Detect tampered files in incident response
- Verify backups are uncorrupted
- Authenticate digital signatures

---

## 📊 EICAR Test File

The content in both files is the **EICAR standard antivirus test string** — a harmless, industry-standard string used to test whether antivirus software is functioning correctly. It is safe to use and universally recognized.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`create_hash_values.sh`](./create_hash_values.sh) | Bash script with all hashing commands, outputs, and explanations |

---

## 🧠 Key Concepts Applied

- **SHA-256** — Secure Hash Algorithm producing a 256-bit (64 hex character) digest; any change to the input produces a completely different hash
- **Hash function properties** — Deterministic, one-way, collision-resistant; identical inputs always produce identical outputs
- **`sha256sum`** — Linux command to generate SHA-256 hashes for files
- **`>>`** — Output redirection operator that appends to a file (vs `>` which overwrites)
- **`cmp`** — Byte-by-byte file comparison tool that reports the exact position of the first difference
- **Data integrity** — Ensuring data has not been altered, corrupted, or tampered with

---

## 📚 What I Learned

- How to generate and compare **SHA-256 hash values** using Linux command-line tools
- That **visually identical files can have completely different hashes** due to hidden or invisible characters
- How `cmp` pinpoints the exact byte and line where two files first differ
- Why **hash verification is essential** for detecting file tampering — a single changed byte produces a completely different hash
- The real-world application of hashing in **malware detection**, **file integrity monitoring**, and **incident response**

---

## 🛠️ Tools & Concepts Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![SHA-256](https://img.shields.io/badge/Algorithm-SHA--256-blue?style=flat-square)
![Hashing](https://img.shields.io/badge/Concept-Hashing-orange?style=flat-square)
![Data Integrity](https://img.shields.io/badge/Concept-Data_Integrity-green?style=flat-square)
![sha256sum](https://img.shields.io/badge/Command-sha256sum-purple?style=flat-square)
![cmp](https://img.shields.io/badge/Command-cmp-darkgreen?style=flat-square)
