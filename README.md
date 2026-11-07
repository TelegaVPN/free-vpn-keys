# 🌐 Open Proxy Telemetry, Anti-DPI Rulesets & Verified Xray/Sing-Box Feeds

[![Updated Every 30m](https://img.shields.io/badge/sync-every_30_min-10b981?style=flat-square)](#)
[![Xray-Core Audited](https://img.shields.io/badge/audit-Xray--core_%26_sing--box-0ea5e9?style=flat-square)](#)
[![License: MIT](https://img.shields.io/badge/license-MIT-f59e0b?style=flat-square)](LICENSE)

> **Last Automated Probe Snapshot:** `2026-11-07 15:30 UTC`
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
| [`guides/`](guides/) | **Static Client Installation & Store Bypass Guides** (App Store Region Change KZ/BY, Happ APK/GitHub, Incy TestFlight/Play, UxWay iOS) |
| [`API.md`](API.md) | **Public REST & Subscription API Specification** (multi-parameter Geo/RTT/EWMA/Protocol filtering & attribution policy) |
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

### 3. Split-Tunneling, Official Client Downloads & App Store / Google Play Bypass Guides
- **🚨 Official Client Downloads & Store Unavailability Guides (Static Repo + Web Mirrors):**
  - **🍏 [Смена региона в App Store на Беларусь / Казахстан и создание второго профиля Apple ID](guides/smena-regiona-app-store-kazahstan-belarus-iphone.md)** ([vpnkeys.me](https://vpnkeys.me/blog/smena-regiona-app-store-kazahstan-belarus-iphone/) • [v-p-n.trade](https://v-p-n.trade/blog/smena-regiona-app-store-kazahstan-belarus-iphone/) • [EN](https://freevpnkeys.com/blog/smena-regiona-app-store-kazahstan-belarus-iphone/))
  - **📲 [Happ не доступен в App Store и Google Play — что делать?](guides/happ-ne-dostupen-v-app-store-i-google-play-chto-delat.md)** ([vpnkeys.me](https://vpnkeys.me/blog/happ-ne-dostupen-v-app-store-i-google-play-chto-delat/) • [v-p-n.trade](https://v-p-n.trade/blog/happ-ne-dostupen-v-app-store-i-google-play-chto-delat/)) — Official Android downloads: [GitHub Releases (`Happ-proxy/happ-android`)](https://github.com/Happ-proxy/happ-android/releases) • [Direct APK (`files-hub.com/?p=android`)](https://files-hub.com/?p=android) • [Global App Store](https://apps.apple.com/us/app/happ-proxy-utility-plus/id6746188973)
  - **💚 [Incy не доступен в App Store — что делать?](guides/incy-ne-dostupen-v-app-store-rossiya-kak-ustanovit.md)** ([vpnkeys.me](https://vpnkeys.me/blog/incy-ne-dostupen-v-app-store-rossiya-kak-ustanovit/) • [v-p-n.trade](https://v-p-n.trade/blog/incy-ne-dostupen-v-app-store-rossiya-kak-ustanovit/)) — Official links: [iOS TestFlight for RU (No Region Change)](https://testflight.apple.com/join/dFw66h3a) • [Android Google Play](https://play.google.com/store/apps/details?id=llc.itdev.incy) • [GitHub (`INCY-DEV/incy-platforms`)](https://github.com/INCY-DEV/incy-platforms) • [Global App Store](https://apps.apple.com/ru/app/incy/id6756943388)
  - **🚀 [UxWay — новое приложение для iOS (iPhone / iPad): обзор и настройка](guides/uxway-novoe-prilozhenie-vless-dlya-iphone-ios-obzor-i-nastrojka.md)** ([vpnkeys.me](https://vpnkeys.me/blog/uxway-novoe-prilozhenie-vless-dlya-iphone-ios-obzor-i-nastrojka/) • [v-p-n.trade](https://v-p-n.trade/blog/uxway-novoe-prilozhenie-vless-dlya-iphone-ios-obzor-i-nastrojka/)) — [App Store (`id6762559624`)](https://apps.apple.com/us/app/uxway/id6762559624) • [Official Docs (`docs.uxway.app`)](https://docs.uxway.app)
  - **💎 Private Multi-Key & Mobile Carrier Whitelist Bypass (Free Trial on Registration):** [@yavpn_robot](https://t.me/yavpn_robot?start=ref_JE5ETCF8) — multi-key for all devices, carrier whitelist bypass, free subscription upon registration, and detailed setup instructions on the subscription page.
- **Split-Tunneling for Domestic Services:** [vpnkeys.me/sajt-ne-rabotaet-vpn/](https://vpnkeys.me/sajt-ne-rabotaet-vpn/) — how to route Russian banks, Gosuslugi, and marketplaces directly without turning off the VPN tunnel.
- **OS & Router Profiles:** [Android TV](https://vpnkeys.me/platform/android-tv/) • [iOS / iPhone](https://vpnkeys.me/platform/ios/) • [Windows 10/11](https://vpnkeys.me/platform/windows/) • [macOS Apple Silicon](https://vpnkeys.me/platform/macos/) • [Keenetic & OpenWrt Routers](https://vpnkeys.me/platform/routers/).
- **Client Documentation:** [Happ](https://vpnkeys.me/instrukcii/happ/) • [Incy](https://vpnkeys.me/instrukcii/incy/) • [UxWay](https://vpnkeys.me/instrukcii/uxway/) • [v2RayTun](https://vpnkeys.me/instrukcii/v2raytun/) • [FlClashX / Mihomo](https://vpnkeys.me/instrukcii/flclash/) • [Sing-box](https://vpnkeys.me/instrukcii/singbox/) ([Global Client Comparison](https://freevpnkeys.com/apps/)).

### 4. Client-Side URI Decoder, Telegram Fake-TLS Proxies & Open Telemetry
- **Interactive URI Decoder & Auditor:** [vpnkeys.me/tools/key-checker/](https://vpnkeys.me/tools/key-checker/) • [freevpnkeys.com/tools/key-checker/](https://freevpnkeys.com/tools/key-checker/) — zero-upload browser parser for `vless://`, `vmess://`, `trojan://`, `ss://`, `hysteria2://`, and `tg://`.
- **1-Click Fake-TLS Telegram Proxies:** [vpnkeys.me/telegram-proxy/](https://vpnkeys.me/telegram-proxy/) • [freevpnkeys.com/protocol/webproxy/](https://freevpnkeys.com/protocol/webproxy/) — audited MTProto and WebProxy links for Telegram calls and media.
- **Methodology & Live ASN Radar:** [vpnkeys.me/kak-my-proveryaem/](https://vpnkeys.me/kak-my-proveryaem/) • [freevpnkeys.com/network-statistics/](https://freevpnkeys.com/network-statistics/).
- **Machine-Readable LLM & API Feeds:** [vpnkeys.me/llms.txt](https://vpnkeys.me/llms.txt) • [freevpnkeys.com/llms.txt](https://freevpnkeys.com/llms.txt) • [`telemetry/snapshot.json`](telemetry/snapshot.json).

---

## 📡 Sample Verified Nodes (Live Xray-Core Telemetry)

| Location | Protocol | Transport & TLS | RTT | Verified Unlocks | Telemetry & Audit Report |
| :---: | :--- | :--- | :---: | :--- | :--- |
| 🇩🇪 DE | WEBPROXY | WS TLS | 661 ms | — | [RU #14706694](https://vpnkeys.me/key/14706694/) · [EN #14706694](https://freevpnkeys.com/key/14706694/) |
| 🇫🇮 FI | WEBPROXY | WS TLS | 647 ms | ru_blocked | [RU #14706692](https://vpnkeys.me/key/14706692/) · [EN #14706692](https://freevpnkeys.com/key/14706692/) |
| 🇩🇪 DE | WEBPROXY | WS TLS | 650 ms | ru_blocked | [RU #14706690](https://vpnkeys.me/key/14706690/) · [EN #14706690](https://freevpnkeys.com/key/14706690/) |
| 🇩🇪 DE | VLESS | TCP REALITY | 2998 ms | ru_verified | [RU #25424185](https://vpnkeys.me/key/25424185/) · [EN #25424185](https://freevpnkeys.com/key/25424185/) |
| 🇺🇸 US | VLESS | TCP REALITY | 457 ms | ru_verified, ai_unlock, netflix_ok, tiktok_ok, claude_ok, chatgpt_ok | [RU #25424156](https://vpnkeys.me/key/25424156/) · [EN #25424156](https://freevpnkeys.com/key/25424156/) |
| 🇺🇸 US | VLESS | TCP REALITY | 1306 ms | ru_verified, ai_unlock, netflix_ok, tiktok_ok, gemini_ok, youtube_premium_ok, notebooklm_ok, claude_ok, chatgpt_ok | [RU #25424039](https://vpnkeys.me/key/25424039/) · [EN #25424039](https://freevpnkeys.com/key/25424039/) |
| 🇺🇸 US | VLESS | TCP REALITY | 1139 ms | ru_verified, ai_unlock, netflix_ok, tiktok_ok, claude_ok, chatgpt_ok | [RU #25423852](https://vpnkeys.me/key/25423852/) · [EN #25423852](https://freevpnkeys.com/key/25423852/) |
| 🇨🇭 CH | VLESS | XHTTP REALITY | 817 ms | ru_verified, ai_unlock, netflix_ok, tiktok_ok, gemini_ok, youtube_premium_ok, notebooklm_ok, claude_ok, chatgpt_ok | [RU #25406015](https://vpnkeys.me/key/25406015/) · [EN #25406015](https://freevpnkeys.com/key/25406015/) |
| 🇩🇪 DE | VLESS | TCP REALITY | 753 ms | ru_verified, ai_unlock, netflix_ok, tiktok_ok, gemini_ok, youtube_premium_ok, notebooklm_ok, claude_ok, chatgpt_ok | [RU #25405875](https://vpnkeys.me/key/25405875/) · [EN #25405875](https://freevpnkeys.com/key/25405875/) |
| 🇦🇱 AL | VLESS | XHTTP REALITY | 1652 ms | ru_verified, ai_unlock, claude_ok | [RU #25405759](https://vpnkeys.me/key/25405759/) · [EN #25405759](https://freevpnkeys.com/key/25405759/) |

---

## 📰 Latest Research & Network Advisories

- 📄 **[В клавиатуре iPhone нашли скрытый чёрный список из 100 000 фраз](https://vpnkeys.me/blog/iphone-keyboard-blacklist-100k-phrases/)** ([EN](https://freevpnkeys.com/blog/iphone-keyboard-blacklist-100k-phrases/)) — *privacy* (07.11.2026)
- 📄 **[США отрезали криптобиржу MEXC от своей финансовой системы из-за обхода санкций](https://vpnkeys.me/blog/usa-cuts-off-mexc-crypto-exchange/)** ([EN](https://freevpnkeys.com/blog/usa-cuts-off-mexc-crypto-exchange/)) — *crypto* (07.11.2026)
- 📄 **[Интернет-трафик в России вырастет на 20% из-за смены маршрутов](https://vpnkeys.me/blog/internet-trafik-rossiya-20/)** ([EN](https://freevpnkeys.com/blog/internet-trafik-rossiya-20/)) — *Новости* (06.11.2026)
- 📄 **[Патч для опасной уязвимости в Paint не доходит до пользователей Windows 11](https://vpnkeys.me/blog/paint-vulnerability-patch-not-delivered/)** ([EN](https://freevpnkeys.com/blog/paint-vulnerability-patch-not-delivered/)) — *Рунет и сервисы* (06.11.2026)
- 📄 **[Билайн запустил 5G ещё в 13 городах: что это значит для пользователей](https://vpnkeys.me/blog/beeline-5g-13-cities/)** ([EN](https://freevpnkeys.com/blog/beeline-5g-13-cities/)) — *Новости* (05.11.2026)

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

## 🤝 Community, Public API, Attribution & Engineering Blog

- **🔌 Public REST API for Gateways & Routers ([API.md](API.md)):**
  - External projects (`sing-box` gateways, `razdacha`, OpenWrt/Keenetic/Podkop scripts, custom pool managers) can query live deduplicated nodes in 1 HTTP request via `GET https://vpnkeys.me/api/v1/keys` (or `https://freevpnkeys.com/api/v1/keys`) with combinable (`AND`) filters: `?protocol=vless,ss,trojan&country=DE,NL,FI&for_russia=1&max_ping=250&min_reputation=0.7&min_uptime=0.8&sort=reputation&limit=100` (supports `format=json`, `format=plain`, and `format=base64`).
  - **Attribution Policy (Указание авторства):** The API and mirrored feeds are free for open-source and non-commercial use. If you integrate our API or subscription feeds into your project, bot, firmware, or web UI, **please credit [vpnkeys.me](https://vpnkeys.me) / [freevpnkeys.com](https://freevpnkeys.com) and link to [github.com/TelegaVPN/free-vpn-keys](https://github.com/TelegaVPN/free-vpn-keys)** in your README, documentation, or source list. See full specification in **[API.md](API.md)** and **[CONTRIBUTING.md](CONTRIBUTING.md)**.
- **RU Domestic Datacenter Mirrors (67hosting RU):**
  - [freekeys.host67.com](https://freekeys.host67.com) — Emergency Russian domestic mirror with zero-server key decoder, WebRTC scanner, and local subscription feeds
  - [redirect.host67.com](https://redirect.host67.com) — Smart latency router & 1-click deep-link launcher (`?app=happ` / `v2raytun` / `hiddify`)
- **Engineering Deep Dives (Telescope — [telescope.ac/vpnkeys](https://telescope.ac/vpnkeys) & Hashnode — [vpnkeys.hashnode.dev](https://vpnkeys.hashnode.dev)):**
  - [Multi-Vantage Xray-Core Probing: How We Detect Silent 64KB DPI TCP Freezes in Real Time](https://telescope.ac/vpnkeys/multi-vantage-xray-core-probing-detecting-64kb-dpi-tcp-freezes) ([Telegra.ph EN Mirror](https://telegra.ph/Multi-Vantage-Xray-Core-Probing-Detecting-Silent-64KB-DPI-TCP-Freezes--Mobile-Carrier-SNI-Whitelists-10-25))
  - [Zero-Server Proxy Auditing & Browser Network Diagnostics: Inspecting VLESS Reality, DNS Leaks & WebRTC](https://telegra.ph/Zero-Server-Proxy-URI-Auditing-Browser-WebRTC-Leak-Detection--Domestic-Split-Tunneling-in-sing-box-10-25)
- **Russian Technical Articles (Glas.su & Telegra.ph Mirrors):**
  - [Архитектура VPNKeys: детектор ТСПУ 64KB Freeze, обход белых списков SNI и автообновляемые подписки (Telegra.ph)](https://telegra.ph/Arhitektura-VPNKeys-detektor-TSPU-64KB-Freeze-obhod-belyh-spiskov-SNI-i-avtoobnovlyaemye-podpiski-10-25)
  - [Диагностика сетевых маршрутов: аудит утечек WebRTC (STUN), Split-DNS и проверка ASN через GeoLite2 (Glas.su)](https://glas.su/s/xpTgyd)
  - [Локальный криптографический аудит транспортных URI и параметров TLS 1.3 в браузере (Glas.su)](https://glas.su/s/flS9gi) ([Telegra.ph](https://telegra.ph/Lokalnyj-kriptograficheskij-audit-VLESS-Reality-i-diagnostika-utechek-WebRTC--DNS-v-brauzere-10-25))
  - [Раздельная маршрутизация (Split-Horizon) и Split-DNS для прямой работы банков и Госуслуг (Glas.su)](https://glas.su/s/XhR1Yn) ([Telegra.ph](https://telegra.ph/Obhod-belyh-spiskov-operatorov-MTS-MegaFon-Bilajn-T2-i-razdelnoe-tunnelirovanie-v-Sing-Box--Happ--v2RayTun-10-25))
  - [Оптимизация параметров MTU, QUIC/UDP и TLS 1.3 в сетях мобильных операторов МТС, МегаФон, Билайн, Т2 (Glas.su)](https://glas.su/s/9jbx2d)
  - [Централизованная маршрутизация на роутерах Keenetic, OpenWrt и приставках Android TV (Glas.su)](https://glas.su/s/RfapKi) ([Telegra.ph](https://telegra.ph/Nastrojka-routerov-Keenetic-OpenWrt-pristavok-Android-TV-i-1-Click-Fake-TLS-proksi-dlya-Telegram-10-25))
  - [Архитектура протокола MTProto Fake-TLS (ee-префикс) для Telegram без системного туннеля (Glas.su)](https://glas.su/s/zb9isn)
- **Telegram Feed (Automated Node Stream):** [@free_outline_keys](https://t.me/free_outline_keys)
