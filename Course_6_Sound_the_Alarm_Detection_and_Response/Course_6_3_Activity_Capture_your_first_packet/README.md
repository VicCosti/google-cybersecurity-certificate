# 📡 Lab: Capture Your First Packet

> **Course:** Google Cybersecurity Professional Certificate — Course 6: Sound the Alarm: Detection and Response  
> **Platform:** Google Skills / Qwiklabs (Debian-based VM)  
> **Tool:** tcpdump  
> **File produced:** `capture.pcap` (9 packets, 1401 bytes)

---

## 📋 Scenario Overview

As a security analyst, capturing and analyzing live network traffic is a fundamental skill for detecting threats and investigating incidents. In this lab, the goal was to identify network interfaces, capture live traffic with tcpdump, save it to a pcap file, and analyze the captured packets in both verbose and hex/ASCII format.

---

## ✅ Tasks Completed

| Task | Description | Command |
|---|---|---|
| 1 | Identify network interfaces | `sudo ifconfig` |
| 1 | List tcpdump-available interfaces | `sudo tcpdump -D` |
| 2 | Live capture — 5 packets verbose | `sudo tcpdump -i eth0 -v -c5` |
| 3 | Background capture — 9 packets port 80 → file | `sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &` |
| 3 | Generate HTTP traffic to capture | `curl opensource.google.com` |
| 3 | Verify pcap file created | `ls -l capture.pcap` |
| 4 | Read pcap with verbose output | `sudo tcpdump -nn -r capture.pcap -v` |
| 4 | Read pcap in hex + ASCII format | `sudo tcpdump -nn -r capture.pcap -X` |

---

## 🔍 Network Interface Identified

```
eth0: inet 172.17.0.2  netmask 255.255.0.0
      ether 02:42:ac:11:00:02
      RX packets 700 (14.0 MiB)
      TX packets 348 (32.7 KiB)
```

**Capture target:** `eth0` — primary Ethernet interface connected to the external network.

---

## 📦 TCP Connection — Full Packet Breakdown

All 9 captured packets represent a complete HTTP transaction with `173.194.43.101` (Google):

| # | Flags | Direction | Description |
|---|---|---|---|
| 1 | `[S]` | `172.17.0.2 → 173.194.43.101` | TCP SYN — connection request |
| 2 | `[S.]` | `173.194.43.101 → 172.17.0.2` | TCP SYN/ACK — connection accepted |
| 3 | `[.]` | `172.17.0.2 → 173.194.43.101` | TCP ACK — handshake complete |
| 4 | `[P.]` | `172.17.0.2 → 173.194.43.101` | HTTP GET / HTTP/1.1 |
| 5 | `[.]` | `173.194.43.101 → 172.17.0.2` | TCP ACK |
| 6 | `[P.]` | `173.194.43.101 → 172.17.0.2` | HTTP/1.1 301 Moved Permanently |
| 7 | `[.]` | `172.17.0.2 → 173.194.43.101` | TCP ACK |
| 8 | `[F.]` | `172.17.0.2 → 173.194.43.101` | TCP FIN — connection close |
| 9 | `[F.]` | `173.194.43.101 → 172.17.0.2` | TCP FIN — close confirmed |

---

## 🔍 Key Packet Contents

### Packet 4 — HTTP GET Request (visible in -X output)
```
GET / HTTP/1.1
Host: opensource.google.com
User-Agent: curl/7.88.1
Accept: */*
```

### Packet 6 — HTTP 301 Response (visible in -X output)
```
HTTP/1.1 301 Moved Permanently
Location: https://opensource.google/
Content-Type: text/html; charset=UTF-8
Server: sffe
Date: Mon, 21 Sep 2026 10:03:38 GMT
Cache-Control: public, max-age=1800
Content-Length: 223
```

---

## 💡 tcpdump Flags Reference

| TCP Flag | Symbol | Meaning |
|---|---|---|
| SYN | `[S]` | Initiate connection |
| SYN/ACK | `[S.]` | Connection accepted |
| ACK | `[.]` | Acknowledgment |
| PUSH/ACK | `[P.]` | Data packet |
| FIN | `[F.]` | Close connection |
| RST | `[R]` | Reset (abort connection) |

---

## 💡 tcpdump Options Reference

| Option | Meaning |
|---|---|
| `-i eth0` | Capture on interface eth0 |
| `-v` | Verbose — show TTL, flags, checksum |
| `-c5` | Capture exactly 5 packets |
| `-nn` | No hostname/port name resolution |
| `-w file.pcap` | Write packets to file |
| `-r file.pcap` | Read packets from file |
| `-X` | Show hex + ASCII payload |
| `port 80` | Filter: only traffic on port 80 |
| `&` | Run in background |

---

## ⚠️ Note on Checksum Warnings

The output shows `cksum (incorrect)` on many packets. This is **not a real error** — it is caused by **checksum offloading**: a feature of virtual network interfaces where the checksum is computed at the hardware level. tcpdump captures the packet before the checksum is applied, so it appears incorrect. This behavior is expected in virtualized lab environments.

---

## 🔐 Security Observation — HTTP vs HTTPS

The `-X` output reveals the **full HTTP request and response headers in plain text**. This demonstrates that:
- HTTP traffic is **completely unencrypted** — anyone capturing the traffic can read the content
- The response redirects to `https://opensource.google/` — confirming that HTTPS is the secure alternative
- In a real attack scenario, an attacker on the same network could intercept this traffic with a tool like tcpdump

---

## 📁 Project Files

| File | Description |
|---|---|
| [`capture_first_packet.sh`](./assets/capture_first_packet.sh) | Full bash script with all commands, outputs, and detailed explanations |

---

## 🧠 Key Concepts Applied

- **tcpdump** — Command-line packet analyzer for capturing and inspecting network traffic
- **pcap file format** — Standard format for storing captured network packets
- **Background processes** (`&`) — Running tcpdump in the background while generating traffic
- **TCP three-way handshake** — SYN → SYN/ACK → ACK visible in the capture
- **TCP connection teardown** — FIN → FIN/ACK sequence at connection close
- **HTTP in cleartext** — HTTP traffic fully readable in packet captures; underscores the need for HTTPS
- **Hex + ASCII output** (`-X`) — Reading raw packet bytes alongside human-readable content
- **Checksum offloading** — Understanding why checksums appear incorrect in virtualized environments

---

## 📚 What I Learned

- How to identify network interfaces with `ifconfig` and `tcpdump -D`
- How to capture live traffic with `tcpdump` and save it to a `.pcap` file
- How to use the `&` operator to run tcpdump in the background while generating traffic
- How to read a pcap file with `-v` (verbose) and `-X` (hex+ASCII) to extract packet details
- That the `-X` flag reveals **plaintext HTTP content** directly in the packet payload
- The full lifecycle of a TCP connection — from SYN handshake to FIN teardown
- Why **HTTP is insecure** — the full request and response are visible to anyone capturing traffic

---

## 🛠️ Tools & Concepts Referenced

![tcpdump](https://img.shields.io/badge/Tool-tcpdump-darkgreen?style=flat-square)
![pcap](https://img.shields.io/badge/File-pcap-blue?style=flat-square)
![TCP](https://img.shields.io/badge/Protocol-TCP-blue?style=flat-square)
![HTTP](https://img.shields.io/badge/Protocol-HTTP-orange?style=flat-square)
![curl](https://img.shields.io/badge/Tool-curl-073551?style=flat-square)
![Linux](https://img.shields.io/badge/OS-Debian-red?style=flat-square&logo=debian)
![Bash](https://img.shields.io/badge/Shell-Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white)
