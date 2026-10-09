# 🛡️ Lab: Examine Alerts, Logs, and Rules with Suricata

> **Course:** Google Cybersecurity Professional Certificate — Course 6: Sound the Alarm: Detection and Response  
> **Platform:** Google Skills / Qwiklabs (Debian-based VM)  
> **Tool:** Suricata 7.0.10 (IDS/IPS/NSM)  
> **Input:** `sample.pcap` (200 packets, 54,238 bytes) + `custom.rules`

---

## 📋 Scenario Overview

As a security analyst, I was tasked with configuring and running Suricata against a sample packet capture to explore IDS rule structure, alert triggering, and log analysis. The lab involved examining a pre-written Suricata rule, triggering it against network traffic, and analyzing the output in both `fast.log` and `eve.json` formats.

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | Examine the custom Suricata rule | `cat custom.rules` |
| 2 | Verify log directory is empty before run | `ls -l /var/log/suricata` |
| 2 | Run Suricata against sample pcap | `sudo suricata -r sample.pcap -S custom.rules -k none` |
| 2 | Verify log files were created | `ls -l /var/log/suricata` |
| 2 | Read triggered alerts from fast.log | `cat /var/log/suricata/fast.log` |
| 3 | Inspect raw eve.json output | `cat /var/log/suricata/eve.json` |
| 3 | Pretty-print eve.json with jq | `jq . /var/log/suricata/eve.json \| less` |
| 3 | Extract specific fields (compact view) | `jq -c "[.timestamp,.flow_id,.alert.signature,.proto,.dest_ip]" /var/log/suricata/eve.json` |
| 3 | Filter all events by flow_id | `jq "select(.flow_id==695533784871914)" /var/log/suricata/eve.json` |

---

## 🔍 Task 1 — Suricata Rule Breakdown

```bash
cat custom.rules
```

```
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"GET on wire"; flow:established,to_server; content:"GET"; http_method; sid:12345; rev:3;)
```

A Suricata rule has three components: **action**, **header**, and **rule options**.

| Component | Value | Meaning |
|---|---|---|
| **Action** | `alert` | Generate an alert when all conditions match |
| **Protocol** | `http` | Inspect HTTP traffic only |
| **Source** | `$HOME_NET any` | Any port on the internal network (`172.21.224.0/20`) |
| **Direction** | `->` | Outbound traffic (home → external) |
| **Destination** | `$EXTERNAL_NET any` | Any external IP, any port |
| `msg` | `"GET on wire"` | Alert label shown in logs |
| `flow` | `established,to_server` | Match packets from client to server in an established session |
| `content` | `"GET"` in `http_method` | Trigger on HTTP GET requests |
| `sid` | `12345` | Unique signature identifier |
| `rev` | `3` | Rule revision version |

**Summary:** This rule alerts whenever Suricata detects an outbound HTTP GET request from the internal network to any external destination.

---

## 🚨 Task 2 — Trigger the Rule and Read fast.log

```bash
sudo suricata -r sample.pcap -S custom.rules -k none
# i: pcap: read 1 file, 200 packets, 54238 bytes
```

| Flag | Meaning |
|---|---|
| `-r sample.pcap` | Read traffic from a packet capture file |
| `-S custom.rules` | Use only the specified rules file |
| `-k none` | Disable checksum validation (not needed for pcap replay) |

After running, four log files were created in `/var/log/suricata/`:

```
-rw-r--r-- 1 root root 1673  eve.json
-rw-r--r-- 1 root root  292  fast.log
-rw-r--r-- 1 root root 4029  stats.log
-rw-r--r-- 1 root root 2008  suricata.log
```

### fast.log — 2 Alerts Triggered

```
11/23/2022-12:38:34.624866  [**] [1:12345:3] GET on wire [**] [Classification: (null)] [Priority: 3] {TCP} 172.21.224.2:49652 -> 142.250.1.139:80
11/23/2022-12:38:58.958203  [**] [1:12345:3] GET on wire [**] [Classification: (null)] [Priority: 3] {TCP} 172.21.224.2:58494 -> 142.250.1.102:80
```

Both alerts originated from internal host `172.21.224.2` connecting to two different Google IPs on port 80. The format is: `[gid:sid:rev] message {proto} src_ip:port -> dst_ip:port`

> ⚠️ **Note:** `fast.log` is a **deprecated format** — not recommended for incident response or threat hunting. It is useful for quick rule validation and QA checks only.

---

## 🔍 Task 3 — Examine eve.json

`eve.json` is Suricata's main structured log. It captures richer event data in JSON, making it ideal for SIEM ingestion and automated analysis.

### Pretty-print with jq

```bash
jq . /var/log/suricata/eve.json | less
```

**Key fields from the first alert:**

| Field | Value |
|---|---|
| `timestamp` | `2022-11-23T12:38:34.624866+0000` |
| `event_type` | `alert` |
| `src_ip` | `172.21.224.2` |
| `dest_ip` | `142.250.1.139` |
| `dest_port` | `80` |
| `proto` | `TCP` |
| `alert.signature` | `GET on wire` |
| `alert.severity` | **3** |
| `http.hostname` | `opensource.google.com` |
| `http.method` | `GET` |
| `http.status` | `301` (redirect to HTTPS) |
| `http.redirect` | `https://opensource.google/` |
| `http_user_agent` | `curl/7.74.0` |

### Extract Specific Fields (Compact View)

```bash
jq -c "[.timestamp,.flow_id,.alert.signature,.proto,.dest_ip]" /var/log/suricata/eve.json
```

```
["2022-11-23T12:38:34.624866+0000",695533784871914,"GET on wire","TCP","142.250.1.139"]
["2022-11-23T12:38:58.958203+0000",726728852993465,"GET on wire","TCP","142.250.1.102"]
```

- **Alert signature (both events):** `GET on wire`
- **Last event destination IP:** `142.250.1.102`

### Filter by flow_id

```bash
jq "select(.flow_id==695533784871914)" /var/log/suricata/eve.json
```

The `flow_id` is a unique identifier assigned by Suricata to each network flow. All log entries sharing the same `flow_id` belong to the same connection — useful for correlating related packets and reconstructing a full traffic session.

**Flow `695533784871914` summary:**

| Metric | Value |
|---|---|
| Packets to server | 4 |
| Packets from server | 3 |
| Bytes to server | 357 |
| Bytes from server | 788 |

---

## ⚠️ Note on Checksum Validation (`-k none`)

The `-k none` flag disables Suricata's checksum validation. When replaying a pcap file, checksums may appear incorrect due to checksum offloading — the same behavior seen with tcpdump in virtualized environments. Disabling this check prevents false positives that would cause Suricata to skip valid packets.

---

## 📁 Project Files

| File | Description |
|---|---|
| [`suricata_lab.sh`](./assets/suricata_lab.sh) | Full terminal session with all commands, outputs, and annotations |

---

## 🧠 Key Concepts Applied

- **Suricata rule structure** — Action, header (protocol/IPs/direction), and rule options (msg, flow, content, sid, rev)
- **IDS alert actions** — `alert`, `drop`, `pass`, `reject` and when each is used
- **fast.log** — Deprecated quick-check format; one line per alert
- **eve.json** — Standard Suricata log in JSON format; full event metadata including HTTP fields, flow stats, and severity
- **jq** — JSON processor used to pretty-print, filter, and extract fields from eve.json
- **flow_id** — Unique per-connection identifier that links all log entries for the same network flow
- **`-k none`** — Disabling checksum validation when running Suricata against pcap files

---

## 📚 What I Learned

- How to read and interpret a Suricata rule, breaking down each component (action, header, options)
- How to run Suricata in offline mode (`-r`) against a pcap file to test rules without live traffic
- The difference between `fast.log` (deprecated, human-readable) and `eve.json` (structured, production-ready)
- How to use `jq` to parse and extract specific fields from JSON log output
- How `flow_id` can be used to correlate multiple log entries belonging to the same network session
- That `eve.json` contains rich application-layer data (HTTP method, hostname, redirect, user agent) beyond just raw packet headers

---

## 🛠️ Tools & Concepts Referenced

![Suricata](https://img.shields.io/badge/Tool-Suricata-orange?style=flat-square)
![IDS](https://img.shields.io/badge/Concept-IDS%2FIPS-red?style=flat-square)
![JSON](https://img.shields.io/badge/Format-JSON-lightgrey?style=flat-square)
![jq](https://img.shields.io/badge/Tool-jq-blue?style=flat-square)
![TCP](https://img.shields.io/badge/Protocol-TCP-blue?style=flat-square)
![HTTP](https://img.shields.io/badge/Protocol-HTTP-orange?style=flat-square)
![Linux](https://img.shields.io/badge/OS-Debian-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
