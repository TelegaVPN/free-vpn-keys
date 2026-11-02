# Contributing & Third-Party Integration Guide

This repository provides open-access proxy telemetry, split-tunneling rulesets, and verified subscription feeds for researchers, router firmware maintainers (OpenWrt / Keenetic / Podkop), and selective VPN gateways.

## 1. Consuming Feeds & Public API in Automated Daemons

If you maintain an open-source client, router script, or `sing-box` / `Xray-core` pool manager:
- **Public REST API ([API.md](API.md)):** You can fetch up to 240 live deduplicated keys in a single HTTP request via `GET https://vpnkeys.me/api/v1/keys` (or `https://freevpnkeys.com/api/v1/keys`) with combinable filters (`protocol=vless,ss,trojan`, `country=DE,NL,FI`, `for_russia=1`, `max_ping=250`, `min_reputation=0.7`, `min_uptime=0.9`, `service=chatgpt,claude`, `sort=reputation`, `format=json|plain|base64`). See **[API.md](API.md)** for full documentation.
- **Attribution / Указание авторства:** When integrating our API or subscription feeds into third-party software, bots, or router packages, please include attribution with a link to **[vpnkeys.me](https://vpnkeys.me)** / **[freevpnkeys.com](https://freevpnkeys.com)** and **[github.com/TelegaVPN/free-vpn-keys](https://github.com/TelegaVPN/free-vpn-keys)** in your project README and UI, and preserve node remarks where applicable.
- **Prefer CDN Endpoints for Static Feeds:** For static subscription files, please fetch via **jsDelivr CDN** (`https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/...`) or **GitHub Raw** rather than scraping HTML pages.
- **Pre-built `sing-box` & `Clash` Profiles:** Consume `sub/singbox/for-russia.json` or `sub/clash/for-russia.yaml` directly — all nodes in these feeds have already passed TLS/Reality parameter validation and handshake checks.
- **Machine-Readable Telemetry:** Live protocol survival rates and ASN distribution are updated in `telemetry/snapshot.json`.

## 2. Submitting Diagnostic Scripts or Routing Rules

Pull requests improving:
- `scripts/audit_sub.py` (URI parsing, cipher checks, Reality validation)
- `scripts/test_tspu_64k.sh` (DPI packet drop detection)
- `rules/singbox-ru-direct.json` (domestic split-tunneling domain/CIDR accuracy)

are welcome. Please ensure scripts remain dependency-free (standard library Python 3 or POSIX `sh`).

## 3. Technical Architecture Notes & External References

- **Hashnode Engineering Blog ([vpnkeys.hashnode.dev](https://vpnkeys.hashnode.dev)):**
  - [Multi-Vantage Xray-Core Probing & Detecting 64KB DPI TCP Freezes](https://vpnkeys.hashnode.dev/multi-vantage-xray-core-probing-how-we-detect-silent-64kb-dpi-tcp-freezes-in-real-time)
  - [Zero-Server Proxy Auditing & Browser Network Diagnostics (VLESS Reality, DNS & WebRTC)](https://vpnkeys.hashnode.dev/zero-server-proxy-auditing-browser-network-diagnostics-inspecting-vless-reality-dns-leaks-webrtc)
  - [Surviving Mobile Carrier SNI Whitelists & Engineering Domestic Split-Tunneling](https://vpnkeys.hashnode.dev/surviving-mobile-carrier-sni-whitelists-engineering-domestic-split-tunneling-in-sing-box-and-clash-meta)
- **RU Architecture Overview (TSPU 64KB Freeze, Mobile Carrier Whitelists & Split-Tunneling):** [telegra.ph/Arhitektura-diagnostiki-TSPU-64KB-Freeze-belyh-spiskov-i-razdelnogo-tunnelirovaniya-VLESS-Reality-2026-10-21](https://telegra.ph/Arhitektura-diagnostiki-TSPU-64KB-Freeze-belyh-spiskov-i-razdelnogo-tunnelirovaniya-VLESS-Reality-2026-10-21)
- **EN Architecture Overview (Dual-Vantage Xray-Core Telemetry & Browser Leak Diagnostics):** [telegra.ph/Multi-Probe-Xray-Core-Telemetry-Browser-Leak-Diagnostics--VLESS-Reality-Architecture-2026-10-21](https://telegra.ph/Multi-Probe-Xray-Core-Telemetry-Browser-Leak-Diagnostics--VLESS-Reality-Architecture-2026-10-21)
