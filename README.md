# 🌐 Open Proxy Telemetry, Anti-DPI Rulesets & Verified Xray/Sing-Box Feeds

[![Updated Every 30m](https://img.shields.io/badge/sync-every_30_min-10b981?style=flat-square)](#)
[![Xray-Core Audited](https://img.shields.io/badge/audit-Xray--core_%26_sing--box-0ea5e9?style=flat-square)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-f59e0b?style=flat-square)](LICENSE)

> **Last Automated Probe Snapshot:** `2026-10-24 19:26 UTC`
> **Documentation & Web Diagnostics:** [vpnkeys.me](https://vpnkeys.me) (RU / CIS Telemetry) • [freevpnkeys.com](https://freevpnkeys.com) (Global EN / FA / ZH)

An open-access dataset of continuously audited proxy configurations (`VLESS Reality`, `Hysteria2`, `Trojan`, `VMess`, `Shadowsocks`), split-tunneling routing rules, and CLI verification scripts. Every node in the pool is tested every 15–30 minutes via real `Xray-core` / `sing-box` handshakes from two independent vantage points (a domestic Russian ISP probe in Kemerovo for TSPU/whitelist resilience and a global probe for AI/streaming reachability).

---

## 🛠️ Repository Structure & Included Open-Source Utilities

| Path | Description |
| :--- | :--- |
| [`sub/happ/`](sub/happ/) | Native JSON subscriptions with embedded Xray `leastPing` auto-balancers for **Happ** & **Incy** |
| [`sub/singbox/`](sub/singbox/) | Structured `sing-box` (`SFA` / `SFI` / Linux daemon) outbounds with `urltest` groups |
| [`sub/clash/`](sub/clash/) | **Clash Meta (Mihomo / FlClashX)** YAML profiles with automatic health-check groups |
| [`sub/base64/`](sub/base64/) | Standard Base64 URI lists compatible with **v2RayTun**, **v2rayNG**, **Streisand**, and custom parsers |
| [`telemetry/snapshot.json`](telemetry/snapshot.json) | Machine-readable 10-minute telemetry snapshot (protocol survival rates, RTT, top transit ASNs) |
| [`scripts/audit_sub.py`](scripts/audit_sub.py) | Standalone Python 3 CLI utility to decode subscriptions, reject `allowInsecure=1`, and benchmark TCP/TLS RTT |
| [`scripts/test_tspu_64k.sh`](scripts/test_tspu_64k.sh) | POSIX shell script to detect ISP TSPU 64 KB TCP-connection freeze on any target host |
| [`rules/singbox-ru-direct.json`](rules/singbox-ru-direct.json) | Reference `sing-box` split-tunneling ruleset keeping domestic `.ru`/banking traffic on `direct` |

---

## 🔬 Verification Architecture & Online Diagnostic Suite

Rather than publishing unverified scraped links, the platform provides a full suite of interactive network diagnostics and protocol research tools:

    [Open Sources] ──► [URI & TLS Security Filter] ──► [Domestic RU Probe (TSPU / Whitelist)] ──┐
                       (Rejects allowInsecure=1)   ──► [Global Probe (Claude/ChatGPT/Netflix)] ──┴──► [Verified Pool & Telemetry API]

### 1. Browser TSPU 64KB Freeze & IP / DNS / WebRTC Leak Scanner
- **RU / CIS Scanner:** [vpnkeys.me/proverka/](https://vpnkeys.me/proverka/) — tests connectivity to 24 restricted services (YouTube, Discord, Telegram, AI platforms), detects TSPU 64 KB stream freezing directly in the browser, and compares domestic vs. international IP/EDNS resolvers.
- **Global Leak & Reachability Suite:** [freevpnkeys.com/tools/](https://freevpnkeys.com/tools/) — multi-endpoint IP/ASN comparison, WebRTC STUN leak test, and smart subscription generator.

### 2. Mobile Carrier Whitelist & Regional DPI Matrix (RU)
- **Whitelist Bypass Hub:** [vpnkeys.me/belye-spiski/](https://vpnkeys.me/belye-spiski/) — filters `VLESS Reality` nodes whose `SNI` and subnet ranges pass strict regional mobile carrier whitelists.
- **ISP-Specific Telemetry Hubs:** [MTS](https://vpnkeys.me/operator/mts/) • [MegaFon](https://vpnkeys.me/operator/megafon/) • [Beeline](https://vpnkeys.me/operator/beeline/) • [T2 / Tele2](https://vpnkeys.me/operator/tele2/) • [Rostelecom GPON](https://vpnkeys.me/operator/rostelecom/) • [Yota](https://vpnkeys.me/operator/yota/) • [Dom.ru](https://vpnkeys.me/operator/domru/).

### 3. Split-Tunneling & Platform Setup Guides
- **Split-Tunneling for Domestic Services:** [vpnkeys.me/sajt-ne-rabotaet-vpn/](https://vpnkeys.me/sajt-ne-rabotaet-vpn/) — how to route Russian banks, Gosuslugi, and marketplaces directly without turning off the VPN tunnel.
- **OS & Router Profiles:** [Android TV](https://vpnkeys.me/platform/android-tv/) • [iOS / iPhone](https://vpnkeys.me/platform/ios/) • [Windows 10/11](https://vpnkeys.me/platform/windows/) • [macOS Apple Silicon](https://vpnkeys.me/platform/macos/) • [Keenetic & OpenWrt Routers](https://vpnkeys.me/platform/routers/).
- **Client Documentation:** [Happ](https://vpnkeys.me/instrukcii/happ/) • [Incy](https://vpnkeys.me/instrukcii/incy/) • [v2RayTun](https://vpnkeys.me/instrukcii/v2raytun/) • [FlClashX / Mihomo](https://vpnkeys.me/instrukcii/flclash/) • [Sing-box](https://vpnkeys.me/instrukcii/singbox/) ([Global Client Comparison](https://freevpnkeys.com/apps/)).

### 4. Client-Side URI Decoder, Telegram Fake-TLS Proxies & Open Telemetry
- **Interactive URI Decoder & Auditor:** [vpnkeys.me/tools/key-checker/](https://vpnkeys.me/tools/key-checker/) • [freevpnkeys.com/tools/key-checker/](https://freevpnkeys.com/tools/key-checker/) — zero-upload browser parser for `vless://`, `vmess://`, `trojan://`, `ss://`, `hysteria2://`, and `tg://`.
- **1-Click Fake-TLS Telegram Proxies:** [vpnkeys.me/telegram-proxy/](https://vpnkeys.me/telegram-proxy/) • [freevpnkeys.com/protocol/webproxy/](https://freevpnkeys.com/protocol/webproxy/) — audited MTProto and WebProxy links for Telegram calls and media.
- **Methodology & Live ASN Radar:** [vpnkeys.me/kak-my-proveryaem/](https://vpnkeys.me/kak-my-proveryaem/) • [freevpnkeys.com/network-statistics/](https://freevpnkeys.com/network-statistics/).
- **Machine-Readable LLM & API Feeds:** [vpnkeys.me/llms.txt](https://vpnkeys.me/llms.txt) • [freevpnkeys.com/llms.txt](https://freevpnkeys.com/llms.txt) • [`telemetry/snapshot.json`](telemetry/snapshot.json).

---

## 📡 Sample Verified Nodes (Live Xray-Core Telemetry)

| Location | Protocol | Transport & TLS | RTT | Verified Unlocks | Telemetry & Audit Report |
| :---: | :--- | :--- | :---: | :--- | :--- |
| 🇩🇪 DE | WEBPROXY | WS TLS | 668 ms | — | [RU #14706694](https://vpnkeys.me/key/14706694/) · [EN #14706694](https://freevpnkeys.com/key/14706694/) |
| 🇫🇮 FI | WEBPROXY | WS TLS | 642 ms | — | [RU #14706692](https://vpnkeys.me/key/14706692/) · [EN #14706692](https://freevpnkeys.com/key/14706692/) |
| 🇩🇪 DE | WEBPROXY | WS TLS | 655 ms | — | [RU #14706690](https://vpnkeys.me/key/14706690/) · [EN #14706690](https://freevpnkeys.com/key/14706690/) |
| 🇫🇮 FI | VLESS | TCP REALITY | 314 ms | ru_verified, ai_unlock, netflix_ok, tiktok_ok, gemini_ok, youtube_premium_ok, notebooklm_ok, chatgpt_ok | [RU #19300714](https://vpnkeys.me/key/19300714/) · [EN #19300714](https://freevpnkeys.com/key/19300714/) |
| 🇺🇸 US | VLESS | WS TLS | 392 ms | ru_verified, ai_unlock, netflix_ok, tiktok_ok, gemini_ok, youtube_premium_ok, notebooklm_ok | [RU #19296924](https://vpnkeys.me/key/19296924/) · [EN #19296924](https://freevpnkeys.com/key/19296924/) |
| 🇷🇺 RU | VLESS | TCP REALITY | 238 ms | ru_verified, ru_whitelist | [RU #19293062](https://vpnkeys.me/key/19293062/) · [EN #19293062](https://freevpnkeys.com/key/19293062/) |
| 🇺🇸 US | VLESS | TCP REALITY | 594 ms | ru_verified, ru_whitelist, ai_unlock, netflix_ok, tiktok_ok, gemini_ok, youtube_premium_ok, notebooklm_ok, chatgpt_ok | [RU #19292228](https://vpnkeys.me/key/19292228/) · [EN #19292228](https://freevpnkeys.com/key/19292228/) |
| 🇺🇸 US | VLESS | TCP REALITY | 670 ms | ru_verified, ru_whitelist, ai_unlock, netflix_ok, tiktok_ok, gemini_ok, youtube_premium_ok, notebooklm_ok, chatgpt_ok | [RU #19292219](https://vpnkeys.me/key/19292219/) · [EN #19292219](https://freevpnkeys.com/key/19292219/) |
| 🇪🇸 ES | VLESS | TCP REALITY | 490 ms | ru_verified, ru_whitelist, ai_unlock, tiktok_ok, gemini_ok | [RU #19292200](https://vpnkeys.me/key/19292200/) · [EN #19292200](https://freevpnkeys.com/key/19292200/) |
| 🇵🇱 PL | VLESS | GRPC TLS | 890 ms | ru_verified, ru_whitelist, ai_unlock, netflix_ok, tiktok_ok, gemini_ok, youtube_premium_ok, notebooklm_ok, chatgpt_ok | [RU #19292199](https://vpnkeys.me/key/19292199/) · [EN #19292199](https://freevpnkeys.com/key/19292199/) |

---

## 📰 Latest Research & Network Advisories

- 📄 **[OpenAI возобновила обучение ИИ-моделей, но без доступа к интернету](https://vpnkeys.me/blog/openai-offline-training/)** ([EN](https://freevpnkeys.com/blog/openai-offline-training/)) — *ИИ и технологии* (24.10.2026)
- 📄 **[Samsung назвала устройства Galaxy, которые получат Android 17](https://vpnkeys.me/blog/samsung-galaxy-android17-update-list-confirmed/)** ([EN](https://freevpnkeys.com/blog/samsung-galaxy-android17-update-list-confirmed/)) — *tech* (24.10.2026)
- 📄 **[Softline о частных сетях 5G и edge: как Индонезия развивает промышленный интернет вещей](https://vpnkeys.me/blog/softline-indoneziya-5g-edge/)** ([EN](https://freevpnkeys.com/blog/softline-indoneziya-5g-edge/)) — *технологии* (23.10.2026)
- 📄 **[iPhone Duo 2: что уже известно?](https://vpnkeys.me/blog/iphone-duo-2-details/)** ([EN](https://freevpnkeys.com/blog/iphone-duo-2-details/)) — *gadgets* (23.10.2026)
- 📄 **[Критическая уязвимость в GitLab позволила взломать серверы без авторизации](https://vpnkeys.me/blog/critical-gitlab-flaw-cvss/)** ([EN](https://freevpnkeys.com/blog/critical-gitlab-flaw-cvss/)) — *Кибербезопасность* (22.10.2026)

---

## 🔗 CDN-Mirrored Subscription Endpoints

All endpoints below are synced every 30 minutes across **jsDelivr CDN**, **GitHub Raw**, and **Codeberg EU** so automated daemons, routers, and client apps can fetch updates reliably.

### 🇷🇺 Profile: Russia & CIS Anti-DPI + Whitelist SNI (`for-russia`)

| Format / Client | Primary Mirror (jsDelivr CDN) | GitHub Raw Fallback | Codeberg EU Mirror |
| :--- | :--- | :--- | :--- |
| **Happ / Incy (JSON + Balancers)** | `https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/happ/for-russia.json` | `https://raw.githubusercontent.com/TelegaVPN/free-vpn-keys/main/sub/happ/for-russia.json` | `https://codeberg.org/telegavpn/free-vpn-keys/raw/branch/main/sub/happ/for-russia.json` |
| **RU Mobile Whitelist Only (Happ)** | `https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/happ/ru-whitelist.json` | `https://raw.githubusercontent.com/TelegaVPN/free-vpn-keys/main/sub/happ/ru-whitelist.json` | `https://codeberg.org/telegavpn/free-vpn-keys/raw/branch/main/sub/happ/ru-whitelist.json` |
| **Base64 (v2RayTun / v2rayNG / Streisand)** | `https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/base64/for-russia.txt` | `https://raw.githubusercontent.com/TelegaVPN/free-vpn-keys/main/sub/base64/for-russia.txt` | `https://codeberg.org/telegavpn/free-vpn-keys/raw/branch/main/sub/base64/for-russia.txt` |
| **Clash Meta / Mihomo (YAML)** | `https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/clash/for-russia.yaml` | `https://raw.githubusercontent.com/TelegaVPN/free-vpn-keys/main/sub/clash/for-russia.yaml` | `https://codeberg.org/telegavpn/free-vpn-keys/raw/branch/main/sub/clash/for-russia.yaml` |
| **Sing-Box (SFA / SFI / JSON)** | `https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/singbox/for-russia.json` | `https://raw.githubusercontent.com/TelegaVPN/free-vpn-keys/main/sub/singbox/for-russia.json` | `https://codeberg.org/telegavpn/free-vpn-keys/raw/branch/main/sub/singbox/for-russia.json` |

### 🌍 Profile: Global Multi-Region (`all` — DE, NL, FI, US, SG, GB)

| Format / Client | Primary Mirror (jsDelivr CDN) | GitHub Raw Fallback |
| :--- | :--- | :--- |
| **Happ / Incy (JSON + Balancers)** | `https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/happ/all.json` | `https://raw.githubusercontent.com/TelegaVPN/free-vpn-keys/main/sub/happ/all.json` |
| **Universal Base64 (All Clients)** | `https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/base64/all.txt` | `https://raw.githubusercontent.com/TelegaVPN/free-vpn-keys/main/sub/base64/all.txt` |
| **Clash Meta / Mihomo (YAML)** | `https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/clash/all.yaml` | `https://raw.githubusercontent.com/TelegaVPN/free-vpn-keys/main/sub/clash/all.yaml` |
| **Sing-Box (JSON)** | `https://cdn.jsdelivr.net/gh/TelegaVPN/free-vpn-keys@main/sub/singbox/all.json` | `https://raw.githubusercontent.com/TelegaVPN/free-vpn-keys/main/sub/singbox/all.json` |

---

## 💻 Quick CLI Audit Usage

You can audit any subscription file in this repository (or your own custom feed) locally using the included zero-dependency Python 3 script:

    python3 scripts/audit_sub.py sub/base64/for-russia.txt --limit 15

Or test whether an endpoint is affected by ISP 64 KB TCP stream freezing:

    sh scripts/test_tspu_64k.sh 1.1.1.1 443 cloudflare.com

## 🤝 Community, Engineering Blog & Integration

- **Integration for Open-Source Routers & Gateways:** Third-party projects (`sing-box` daemons, OpenWrt/Podkop scripts, selective WireGuard gateways) are welcome to consume the CDN endpoints (`cdn.jsdelivr.net`) to avoid rate-limiting origin servers. See [CONTRIBUTING.md](CONTRIBUTING.md).
- **Engineering Deep Dives (Hashnode Lab — [vpnkeys.hashnode.dev](https://vpnkeys.hashnode.dev) & Telescope — [telescope.ac/vpnkeys](https://telescope.ac/vpnkeys)):**
  - [Multi-Vantage Xray-Core Probing: How We Detect Silent 64KB DPI TCP Freezes in Real Time](https://vpnkeys.hashnode.dev/multi-vantage-xray-core-probing-how-we-detect-silent-64kb-dpi-tcp-freezes-in-real-time) ([Telescope Mirror](https://telescope.ac/vpnkeys/multi-vantage-xray-core-probing-detecting-64kb-dpi-tcp-freezes))
  - [Zero-Server Proxy Auditing & Browser Network Diagnostics: Inspecting VLESS Reality, DNS Leaks & WebRTC](https://vpnkeys.hashnode.dev/zero-server-proxy-auditing-browser-network-diagnostics-inspecting-vless-reality-dns-leaks-webrtc) ([Telescope Mirror](https://telescope.ac/vpnkeys/zero-server-proxy-auditing-browser-network-diagnostics-vless-reality))
  - [Surviving Mobile Carrier SNI Whitelists & Engineering Domestic Split-Tunneling in sing-box and Clash Meta](https://vpnkeys.hashnode.dev/surviving-mobile-carrier-sni-whitelists-engineering-domestic-split-tunneling-in-sing-box-and-clash-meta) ([Telescope Mirror](https://telescope.ac/vpnkeys/surviving-mobile-carrier-sni-whitelists-split-tunneling-sing-box-clash))
  - [Архитектура VPNKeys (RU): детектор ТСПУ 64KB Freeze, обход белых списков и раздельное туннелирование](https://telescope.ac/vpnkeys/arhitektura-telemetrii-tspu-64kb-belye-spiski-split-tunneling)
- **Telegram Feed (Automated Node Stream):** [@free_outline_keys](https://t.me/free_outline_keys)
