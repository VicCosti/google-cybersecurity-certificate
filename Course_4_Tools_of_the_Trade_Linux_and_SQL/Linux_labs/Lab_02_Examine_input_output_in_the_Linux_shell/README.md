# 🐧 Lab: Examine Input/Output in the Linux Shell

> **Course:** Google Cybersecurity Professional Certificate — Course 4: Tools of the Trade: Linux and SQL  
> **Platform:** Google Skills / Qwiklabs  
> **Environment:** Debian 11 (Bullseye) — Virtual Machine  
> **Shell:** Bash  

---

## 📋 Scenario

As a security analyst, understanding how to communicate with the operating system through the shell is fundamental. In this lab, the goal was to explore how the Bash shell receives **input** and returns **output**, using the `echo` and `expr` commands, and how to manage the terminal with `clear`.

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | Basic string output | `echo hello` |
| 1 | Output with quotes | `echo "hello"` |
| 1 | Output custom name | `echo "vittorio"` |
| 2 | Calculate false positives | `expr 32 - 8` |
| 2 | Calculate yearly logins | `expr 3500 * 12` |
| 3 | Clear the shell | `clear` |
| Optional | Echo a long string | `echo "time is changing..."` |
| Optional | Multi-operation calculation | `expr 26 * 6 + 15` |

---

## 🔍 Key Observations

### echo command
The `echo` command outputs any string passed to it. Quotes are optional for simple strings but are recommended when the string contains special characters or spaces, as they tell the shell to treat the content as a single grouped unit.

```bash
echo hello        # Output: hello
echo "hello"      # Output: hello (identical)
echo "vittorio"   # Output: vittorio
```

### expr command — spacing rule
The `expr` command requires **spaces between all terms and operators**. Without spaces, the expression is returned as a literal string instead of being evaluated.

```bash
expr 32-8     # ❌ Output: 32-8  (treated as a string, not calculated)
expr 32 - 8   # ✅ Output: 24
```

### expr command — no parentheses
The `expr` command does **not support parentheses** for grouping. Bash interprets `( )` as subshell syntax, causing a syntax error.

```bash
expr ( 26 * 6 ) + ( 46 / 2 )   # ❌ Error: syntax error near unexpected token
expr 26 * 6 + 15                # ✅ Output: 171 (evaluated left to right)
```

### expr command — integer only
`expr` performs **integer arithmetic only**. Decimal results are always rounded down to the nearest integer. Division of 7 / 2 returns 3, not 3.5.

---

## 💡 Real-world Security Use Cases

| Calculation | Context |
|---|---|
| `expr 32 - 8` | Calculate false positive alerts from a monitoring system |
| `expr 3500 * 12` | Estimate total yearly login attempts for baseline analysis |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`examine_input_output_linux.sh`](./examine_input_output_linux.sh) | Bash script with all commands, error examples, and explanations |

---

## 🧠 Key Concepts Applied

- **Shell input/output** — How the Bash shell receives commands and returns results
- **echo command** — Output strings to the terminal
- **expr command** — Perform integer arithmetic in the shell
- **clear command** — Clean the terminal window
- **Common errors** — Missing spaces in `expr`, unsupported parentheses

---

## 📚 What I Learned

- How **input and output** work in the Bash shell at a fundamental level
- The `echo` command outputs any string — quotes group characters and handle special cases
- The `expr` command requires **strict spacing** between all terms and operators
- Parentheses `( )` cannot be used with `expr` — Bash reserves them for subshell syntax
- `expr` only performs **integer arithmetic** — no decimal results
- How to use `clear` to manage terminal readability during long sessions

---

## 🛠️ Commands Referenced

![Linux](https://img.shields.io/badge/OS-Debian_11-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
![echo](https://img.shields.io/badge/Command-echo-blue?style=flat-square)
![expr](https://img.shields.io/badge/Command-expr-orange?style=flat-square)
![clear](https://img.shields.io/badge/Command-clear-lightgrey?style=flat-square)
