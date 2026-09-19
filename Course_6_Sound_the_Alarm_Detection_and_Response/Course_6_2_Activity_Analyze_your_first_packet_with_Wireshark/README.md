# 🦈 Lab: Analyze Your First Packet with Wireshark

> **Course:** Google Cybersecurity Professional Certificate — Course 6: Sound the Alarm: Detection and Response  
> **Platform:** Google Skills / Qwiklabs (Windows VM)  
> **Tool:** Wireshark  
> **File analyzed:** `sample.pcap` (200 packets total)

---

## 📋 Scenario Overview

As a security analyst, you need to analyze network traffic to identify potential security issues. In this lab, the goal was to open a packet capture file in Wireshark, apply various display filters to isolate specific traffic, and inspect individual packets at multiple protocol layers to extract meaningful information.

---

## ✅ Tasks Completed

| Task | Filter / Action | Packets Displayed |
|---|---|---|
| 1 | No filter — full traffic overview | 200 (100%) |
| 2 | `ip.addr == 142.250.1.139` | 16 (8.0%) |
| 2 | `ip.src == 142.250.1.139` | 7 (3.5%) |
| 2 | `ip.dst == 142.250.1.139` | 9 (4.5%) |
| 3 | `eth.addr == 42:01:ac:15:e0:02` | 200 (100%) |
| 3 | `udp.port == 53` | 22 (11.0%) |
| 4 | `tcp.port == 80` | 26 (13.0%) |
| 5 | `tcp contains "curl"` | 2 (1.0%) |

---

## 🔍 Task-by-Task Analysis

### Task 1 — Explore data with Wireshark (no filter)

Full traffic view — all 200 packets. Protocols identified:

| Protocol | Participants |
|---|---|
| SSH | `172.21.224.2` ↔ `35.235.244.34` |
| TCP | Supporting SSH and HTTP connections |
| DNS | `172.21.224.2` → `169.254.169.254` |
| ICMP | `172.21.224.2` ↔ `142.250.1.139` |

---

### Task 2 — Apply basic Wireshark filters

**Filter: `ip.addr == 142.250.1.139`** — 16 packets (bidirectional traffic)

| Protocol | Traffic |
|---|---|
| ICMP | 3 ping request/reply sequences (seq=1/256, seq=2/512, seq=3/768) |
| TCP | Three-way handshake (SYN, SYN/ACK, ACK) on port 80 |
| HTTP | `GET / HTTP/1.1` → `HTTP/1.1 301 Moved Permanently` |

**Packet 64 — TCP SYN detail:**
```
Transmission Control Protocol
  Source Port: 49652 → Destination Port: 80
  Flags: 0x002 (SYN)
  Sequence Number: 0
  Window: 65320
```

**Filter: `ip.src == 142.250.1.139`** — 7 packets (traffic FROM Google)
- ICMP replies, TCP SYN/ACK, HTTP 301 response

**Filter: `ip.dst == 142.250.1.139`** — 9 packets (traffic TO Google)
- ICMP requests, TCP SYN, HTTP GET request, FIN/ACK

---

### Task 3 — Use filters to select packets

**Filter: `eth.addr == 42:01:ac:15:e0:02`** — 200 packets (all traffic from/to this MAC address)

**Packet 1 — SSH detail (IPv4 layer):**
```
Internet Protocol Version 4
  Source: 172.21.224.2 → Destination: 35.235.244.34
  Protocol: TCP (6)
  Time to Live: 64
  Total Length: 196
  Identification: 0xda77 (55927)
```

**Filter: `udp.port == 53`** — 22 packets (11.0%) — DNS traffic only

**Packet 12 — DNS response detail:**
```
Domain Name System (response)
  Transaction ID: 0x0c26
  Flags: Standard query response, No error
  Answers: 6
  Queries: opensource.google.com type A, class IN
  Answers:
    opensource.google.com → 142.250.1.139
    opensource.google.com → 142.250.1.138
    opensource.google.com → 142.250.1.102
    opensource.google.com → 142.250.1.113
    opensource.google.com → 142.250.1.100
    opensource.google.com → 142.250.1.101
```

---

### Task 4 — Use filters to explore DNS and TCP packets

**Filter: `tcp.port == 80`** — 26 packets (13.0%) — HTTP traffic

**Packet 37 — IPv4 layer detail:**
```
Internet Protocol Version 4
  Version: 4
  Header Length: 20 bytes (5)
  Total Length: 40
  Time to Live: 64
  Protocol: TCP (6)
  Source: 172.21.224.2 → Destination: 169.254.169.254
  Frame 37: 54 bytes on wire (432 bits)
  Arrival Time: Nov 23, 2022 12:38:27 GMT
```

Notable packets:
- Packet 130: `HTTP/1.1 200 OK, JSON (application/json)`
- Packet 132: `GET /computeMetadata/v1/?recursive=true&alt=json...`

---

### Task 5 — Use filters to explore UDP, TCP, and HTTP packets

**Filter: `tcp contains "curl"`** — 2 packets (1.0%)

**Packet 67 — HTTP GET detail:**
```
Hypertext Transfer Protocol
  GET / HTTP/1.1
  Host: opensource.google.com
  User-Agent: curl/7.74.0
  Accept: */*
  Source: 172.21.224.2 → Destination: 142.250.1.139
  Src Port: 49652 → Dst Port: 80
```

The filter reveals that the HTTP requests were made using **curl** — a command-line HTTP client. This confirms the traffic was generated programmatically from the VM, not a browser.

---

## 📊 Filters Reference Summary

| Filter | Purpose |
|---|---|
| `ip.addr == X` | Bidirectional traffic to/from IP X |
| `ip.src == X` | Traffic FROM IP X only |
| `ip.dst == X` | Traffic TO IP X only |
| `eth.addr == X` | Traffic to/from MAC address X |
| `udp.port == 53` | DNS traffic only |
| `tcp.port == 80` | HTTP traffic only |
| `tcp contains "curl"` | TCP packets containing the string "curl" |

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/Task_1_1_full_traffic.png`](./assets/Task_1_1.png) | Full traffic view — 200 packets, no filter |
| [`assets/Task_1_3_filtered_ip_addr.png`](./assets/Task_1_3.png) | Filter `ip.addr == 142.250.1.139` — 16 packets |
| [`assets/Task_2_1_packet64_syn_popup.png`](./assets/Task_2_1.png) | Packet 64 popup — TCP SYN flags detail |
| [`assets/Task_2_3_ip_src_filter.png`](./assets/Task_2_3.png) | Filter `ip.src == 142.250.1.139` — 7 packets |
| [`assets/Task_2_7_ip_dst_filter.png`](./assets/Task_2_7.png) | Filter `ip.dst == 142.250.1.139` — 9 packets |
| [`assets/Task_3_1_eth_addr_filter.png`](./assets/Task_3_1.png) | Filter `eth.addr == 42:01:ac:15:e0:02` — packet 1 SSH |
| [`assets/Task_3_4_packet1_ssh_detail.png`](./assets/Task_3_4.png) | Packet 1 IPv4 detail — SSH to `35.235.244.34` |
| [`assets/Task_3_7_udp_port_53_filter.png`](./assets/Task_3_7.png) | Filter `udp.port == 53` — 22 DNS packets |
| [`assets/Task_3_12_packet12_dns_detail.png`](./assets/Task_3_12.png) | Packet 12 DNS response — 6 answers for `opensource.google.com` |
| [`assets/Task_4_1_tcp_port_80_filter.png`](./assets/Task_4_1.png) | Filter `tcp.port == 80` — 26 HTTP packets |
| [`assets/Task_4_9_packet37_ttl_detail.png`](./assets/Task_4_9.png) | Packet 37 IP detail — TTL and header length highlighted |
| [`assets/Task_5_1_tcp_contains_curl.png`](./assets/Task_5_1.png) | Filter `tcp contains "curl"` — 2 packets |
| [`assets/Task_5_3_1_packet67_http_detail.png`](./assets/Task_5_3_1.png) | Packet 67 HTTP GET — curl User-Agent, frame detail |
| [`assets/Task_5_3_2_packet67_ip_layer.png`](./assets/Task_5_3_2.png) | Packet 67 IPv4 layer expanded |
| [`assets/Task_5_3_3_packet67_http_layer.png`](./assets/Task_5_3_3.png) | Packet 67 HTTP layer — Hypertext Transfer Protocol highlighted |
| [`assets/Task_5_6_curl_http_full.png`](./assets/Task_5_6.png) | Full view of curl HTTP packets with packet detail |

---

## 🧠 Key Concepts Applied

- **Wireshark display filters** — Isolating traffic by IP, MAC, port, protocol, and content
- **IP address filters** — `ip.addr` (bidirectional) vs `ip.src` / `ip.dst` (directional)
- **MAC address filter** — `eth.addr` filters at the Ethernet layer regardless of IP
- **Port filters** — `udp.port == 53` for DNS, `tcp.port == 80` for HTTP
- **Content filter** — `tcp contains "curl"` searches packet payload for a string
- **DNS resolution** — Reading query/response pairs and multiple A record answers
- **TCP flags** — Identifying SYN, ACK, FIN packets in the three-way handshake
- **TTL (Time to Live)** — Packet hop limit field in the IPv4 header
- **curl User-Agent** — Identifying the tool used to generate HTTP traffic

---

## 📚 What I Learned

- How to apply **multiple Wireshark filter types** to isolate specific traffic
- The difference between `ip.addr` (both directions) and `ip.src`/`ip.dst` (one direction)
- How **MAC address filters** (`eth.addr`) work at a lower layer than IP filters
- How **DNS responses** carry multiple IP addresses for the same domain (load balancing)
- How to identify the **HTTP client tool** from the User-Agent header (`curl/7.74.0`)
- How to read **IPv4 header fields** — TTL, header length, total length, protocol number
- How **`tcp contains`** searches inside packet payloads — useful for finding specific strings in traffic

---

## 🛠️ Tools & Protocols Referenced

![Wireshark](https://img.shields.io/badge/Tool-Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white)
![ICMP](https://img.shields.io/badge/Protocol-ICMP-red?style=flat-square)
![TCP](https://img.shields.io/badge/Protocol-TCP-blue?style=flat-square)
![HTTP](https://img.shields.io/badge/Protocol-HTTP-orange?style=flat-square)
![DNS](https://img.shields.io/badge/Protocol-DNS-green?style=flat-square)
![SSH](https://img.shields.io/badge/Protocol-SSH-purple?style=flat-square)
![UDP](https://img.shields.io/badge/Protocol-UDP-lightblue?style=flat-square)
![curl](https://img.shields.io/badge/Tool-curl-073551?style=flat-square)
