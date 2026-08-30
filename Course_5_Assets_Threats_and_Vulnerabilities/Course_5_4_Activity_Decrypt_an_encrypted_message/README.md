# 🔐 Lab: Decrypt an Encrypted Message

> **Course:** Google Cybersecurity Professional Certificate — Course 5: Assets, Threats, and Vulnerabilities  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **Shell:** Bash  
> **Tools used:** `tr`, `openssl`  
> **Concepts:** Caesar cipher, AES-256-CBC symmetric encryption

---

## 📋 Scenario Overview

All files in the home directory have been encrypted. The goal was to:
1. Find a hidden file containing an encrypted message
2. Decrypt the **Caesar cipher** to reveal a command
3. Use that command to decrypt the main file with **OpenSSL AES-256-CBC**

---

## 🔑 Decryption Process

```
README.txt → clue → caesar/.leftShift3 (Caesar cipher)
                              ↓
              tr "d-za-cD-ZA-C" "a-zA-Z" (shift left 3)
                              ↓
         openssl aes-256-cbc ... -k ettubrute
                              ↓
                      Q1.recovered ✅
```

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | List home directory contents | `ls` |
| 1 | Read README instructions | `cat README.txt` |
| 2 | Navigate to caesar subdirectory | `cd caesar` |
| 2 | List hidden files | `ls -a` |
| 2 | Read the encrypted hidden file | `cat .leftShift3` |
| 2 | Decrypt the Caesar cipher | `cat .leftShift3 \| tr "d-za-cD-ZA-C" "a-zA-Z"` |
| 2 | Return to home directory | `cd ~` |
| 3 | Decrypt the encrypted file | `openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute` |
| 3 | Read the decrypted message | `cat Q1.recovered` |

---

## 🔍 Key Findings

### Caesar cipher — before and after

**Encrypted (left shift of 3):**
```
Lq rughu wr uhfryhu brxu ilohv brx zloo qhhg wr hqwhu wkh iroorzlqj frppdqg:
rshqvvo dhv-256-fef -sengi2 -d -g -lq T1.hqfubswhg -rxw T1.uhfryhuhg -n hwwxeuxwh
```

**Decrypted:**
```
In order to recover your files you will need to enter the following command:
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute
```

### Final decrypted message (Q1.recovered)
```
If you are able to read this, then you have successfully decrypted the classic
cipher text. You recovered the encryption key that was used to encrypt this file.
Great work!
```

---

## 💡 Command Reference

### Caesar cipher decryption with `tr`
```bash
cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"
```
The `tr` command maps characters from the first set to the second set:
- Input set: `"d-za-cD-ZA-C"` — alphabet starting from 'd' (shifted 3 right)
- Output set: `"a-zA-Z"` — normal alphabet
- Effect: shifts every letter **3 positions to the left** to restore the original text

### AES-256-CBC decryption with `openssl`
```bash
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute
```

| Flag | Meaning |
|---|---|
| `aes-256-cbc` | Symmetric cipher — AES with 256-bit key in CBC mode |
| `-pbkdf2` | Password-Based Key Derivation Function 2 — adds extra security |
| `-a` | Base64 encoding for the output |
| `-d` | Decrypt mode |
| `-in Q1.encrypted` | Input file to decrypt |
| `-out Q1.recovered` | Output file for decrypted content |
| `-k ettubrute` | Password/key used for decryption |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`decrypt_message.sh`](./decrypt_message.sh) | Bash script with all commands, outputs, and detailed explanations |

---

## 🧠 Key Concepts Applied

- **Caesar cipher** — One of the earliest encryption methods; substitutes each letter by shifting it a fixed number of positions in the alphabet
- **`tr` command** — Translates characters from one set to another; useful for simple cipher decryption
- **Hidden files in Linux** — Files starting with `.` are hidden by default; `ls -a` reveals them
- **AES-256-CBC** — Symmetric encryption standard using a 256-bit key in Cipher Block Chaining mode
- **OpenSSL** — Command-line tool for encryption, decryption, and certificate management
- **PBKDF2** — Password-Based Key Derivation Function that strengthens passwords by applying a hash function multiple times

---

## 📚 What I Learned

- How the **Caesar cipher** works and how to reverse it using Linux's `tr` command
- The difference between **classical ciphers** (Caesar) and **modern encryption** (AES-256-CBC)
- How to use **OpenSSL** to decrypt files encrypted with symmetric encryption
- That **hidden files** in Linux are a real technique used to conceal data — relevant for both security analysis and threat detection
- How **encryption keys** protect data — without the key `ettubrute`, the file cannot be decrypted

---

## 🛠️ Tools & Concepts Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![OpenSSL](https://img.shields.io/badge/Tool-OpenSSL-blue?style=flat-square)
![AES-256](https://img.shields.io/badge/Cipher-AES--256--CBC-orange?style=flat-square)
![Caesar](https://img.shields.io/badge/Cipher-Caesar-purple?style=flat-square)
![Cryptography](https://img.shields.io/badge/Concept-Cryptography-darkgreen?style=flat-square)
