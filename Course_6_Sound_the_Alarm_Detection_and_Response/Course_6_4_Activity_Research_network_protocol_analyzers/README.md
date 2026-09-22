# 🔬 Research: Network Protocol Analyzers — Wireshark vs tcpdump

> **Course:** Google Cybersecurity Professional Certificate — Course 6: Sound the Alarm: Detection and Response  
> **Type:** Research Activity / Comparison Diagram  
> **Tools compared:** Wireshark and tcpdump

---

## 📋 Activity Overview

A cybersecurity analyst was asked to research the differences and similarities between Wireshark and tcpdump and create a comparison diagram. Network protocol analyzers (packet sniffers) are essential tools for capturing and analyzing network traffic — a core skill in detection and incident response.

---

## 🔀 Comparison Diagram

```
┌─────────────────────────┬────────────────────────────────┬─────────────────────────┐
│       Wireshark         │        Similarities            │        tcpdump          │
├─────────────────────────┼────────────────────────────────┼─────────────────────────┤
│ • GUI + CLI versions    │ • Capture live network traffic │ • CLI only              │
│ • Deep visual clarity   │ • Interchangeable readability  │ • Fast and lightweight  │ 
│ • Heavier on system     │   (pcap files readable by both)│                         │
│   resources with large  │ • Open-source and free         │                         │
│   packet captures       │                                │                         │
└─────────────────────────┴────────────────────────────────┴─────────────────────────┘
```

---

## 🔍 Differences

### Wireshark
- **GUI + CLI versions** — available with a full graphical interface (GUI) for visual analysis, as well as a command-line version (`tshark`) for scripting and automation
- **Deep visual clarity** — color-coded packets, expandable protocol layers, conversation streams, and IO graphs make complex traffic easy to visualize
- **Resource intensive** — can become slow or memory-heavy with very large pcap files (hundreds of thousands of packets)

### tcpdump
- **CLI only** — runs entirely in the terminal with no graphical interface; ideal for remote servers, headless systems, and automation scripts
- **Fast and lightweight** — minimal system resource usage; can run on low-resource systems and embedded devices

---

## 🤝 Similarities

| Similarity | Description |
|---|---|
| **Capture live network traffic** | Both tools can capture packets in real time from a network interface |
| **Interchangeable readability** | Both use the `.pcap` file format — files captured by tcpdump can be opened in Wireshark and vice versa |
| **Open-source and free** | Both tools are free to use and open-source — available to anyone without licensing costs |

---

## 📊 Extended Comparison

| Feature | Wireshark | tcpdump |
|---|---|---|
| Interface | GUI + CLI (tshark) | CLI only |
| Platform | Windows, macOS, Linux | Linux, macOS, Unix |
| File format | .pcap / .pcapng | .pcap |
| Best for | Deep analysis, visual inspection | Quick captures, remote systems, scripting |
| Resource usage | Higher (GUI-heavy) | Low |
| Learning curve | Moderate | Steeper (CLI-only) |
| Protocol support | 3000+ protocols | Core protocols |
| Open-source | ✅ | ✅ |
| Free | ✅ | ✅ |
| Live capture | ✅ | ✅ |
| Filter language | Display filters (Wireshark syntax) | BPF (Berkeley Packet Filter) |

---

## 💡 When to Use Each Tool

**Use Wireshark when:**
- You need a detailed visual inspection of packets
- You are analyzing complex protocols with many layers
- You want to follow TCP streams or view conversation statistics
- You are working on a local machine with a GUI

**Use tcpdump when:**
- You are working on a remote server via SSH with no GUI
- You need a quick capture with minimal resource usage
- You are writing automated scripts for traffic analysis
- You are working on embedded or low-resource systems

---

## 📁 Project Files

| File | Description |
|---|---|
| [`assets/1_mycompletedwork_Diagram_template.pdf`](./assets/1_mycompletedwork_Diagram_template.pdf) | My completed comparison diagram (PDF) |

---

## 🧠 Key Concepts Applied

- **Network protocol analyzer** — tool that captures and inspects data packets traveling across a network
- **Packet sniffer** — another name for a network protocol analyzer
- **pcap file format** — standard file format for storing captured network packets, used by both tools
- **BPF (Berkeley Packet Filter)** — the filter language used by tcpdump for capturing specific traffic
- **GUI vs CLI** — graphical vs command-line interface, key distinction between the two tools
- **Open-source** — software whose source code is publicly available and free to use

---

## 📚 What I Learned

- The key distinction between Wireshark (GUI-capable, resource-heavy) and tcpdump (CLI-only, lightweight)
- That both tools use the `.pcap` format — making them **interoperable**: capture with one, analyze with the other
- When to choose each tool based on the environment and the analysis task
- That both tools are **free and open-source** — widely used in the security community without licensing costs

---

## 🛠️ Tools Referenced

![Wireshark](https://img.shields.io/badge/Tool-Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white)
![tcpdump](https://img.shields.io/badge/Tool-tcpdump-darkgreen?style=flat-square)
![pcap](https://img.shields.io/badge/Format-pcap-blue?style=flat-square)
![Open Source](https://img.shields.io/badge/License-Open_Source-orange?style=flat-square)
