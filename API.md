# 🔌 Публичное API выборок ключей и подписок (Public REST & Subscription API)

Документация публичного API проекта **[vpnkeys.me](https://vpnkeys.me)** / **[freevpnkeys.com](https://freevpnkeys.com)** ([GitHub Mirror](https://github.com/TelegaVPN/free-vpn-keys)) для разработчиков роутерных шлюзов (`sing-box`, `Xray-core`, `Mihomo / Clash.Meta`, OpenWrt / Keenetic / Podkop, `razdacha`), клиентских приложений и исследовательских утилит.

---

## 🤝 Авторство и правила использования (Attribution & Fair Use)

API предоставляется **бесплатно и без ключей авторизации** для open-source проектов и некоммерческих интеграций. Если вы используете наш API или зеркала подписок в своём проекте, скрипте, прошивке, боте или веб-интерфейсе, пожалуйста:

1. **Указывайте источник (Attribution):**
   - В README / документации / списке источников вашего проекта укажите активную ссылку на **[vpnkeys.me](https://vpnkeys.me)** (для русскоязычной аудитории), **[freevpnkeys.com](https://freevpnkeys.com)** (для международной аудитории) и/или репозиторий **[github.com/TelegaVPN/free-vpn-keys](https://github.com/TelegaVPN/free-vpn-keys)**.
   - По возможности сохраняйте штатный суффикс в названии узла (`#fragment`, например `🇩🇪 DE · vpnkeys.me · 42ms`) или указывайте источник пула в UI вашего приложения.
2. **Соблюдайте интервалы опроса (Rate Limits & Caching):**
   - Ответы API кешируются на уровне SWR-кеша (`60 секунд`), а полный цикл перепроверки пула двухконтурным чекером (`Xray-core` + российский зонд ТСПУ) составляет `15–30 минут`.
   - Запрашивайте пул **одним пакетным HTTP-запросом** (`limit=50..240`) не чаще **1 раза в 10–30 минут** (не обходите постранично карточки HTML на сайте).
   - Передавайте осмысленный заголовок `User-Agent` с названием вашего проекта (например, `User-Agent: my-gateway/1.0 (+https://github.com/org/repo)`).

---

## 1. Эндпоинт живых ключей с мульти-фильтрацией: GET /api/v1/keys

Позволяет за **1 HTTP-запрос** получить до **240 дедуплицированных по бэкенду (host:port) живых узлов** с комбинируемой (AND) фильтрацией по протоколам, странам выхода, пингу, EWMA-репутации, аптайму, проверке ТСПУ РФ и разблокируемым сервисам.

- **Основной адрес (RU / СНГ):** https://vpnkeys.me/api/v1/keys
- **Международное зеркало:** https://freevpnkeys.com/api/v1/keys

### Поддерживаемые Query-параметры (комбинируются через AND)

| Параметр | Тип / Формат | Примеры | Описание |
| :--- | :--- | :--- | :--- |
| protocol | string (CSV) | vless,ss,trojan, vless, hysteria2 | Фильтр по протоколам (одиночный или список через запятую): vless, ss (shadowsocks, outline), trojan, vmess, hysteria2 (hy2), mtproxy, webproxy, telegram. |
| country | string (CSV ISO-2) | DE, DE,NL,FI,SE | Выборка по реальной стране выходного IP (exit_ip), определённой через MaxMind GeoLite2 после поднятия туннеля (а не из текста в #fragment). |
| exclude_country | string (CSV ISO-2) | RU,IR,CN | Исключить указанные страны выхода из выборки. |
| for_russia | bool (1 / true) | for_russia=1 | Только узлы, обходящие ТСПУ / белые списки РФ и не помеченные как ru_blocked. |
| ru_verified | bool (1 / true) | ru_verified=1 | Только узлы, напрямую верифицированные с российской RU-ноды (прокачка > 64 КБ данных без зависания ТСПУ 64KB TCP Freeze). |
| security | string (CSV) | reality, reality,tls | Фильтр по криптографии транспорта (reality, tls, none). |
| transport | string (CSV) | tcp, tcp,grpc,ws,xhttp | Фильтр по транспорту (tcp, grpc, ws, xhttp, httpupgrade, quic). |
| max_ping | int (мс) | 150, 250, 500 | Максимальный измеренный RTT в миллисекундах (алиас: max_latency). |
| min_reputation | float (0..1 или 1..100) | 0.75 (или 75) | Минимальный скор репутации узла по алгоритму EWMA от 0.0 до 1.0 (алиас: min_ewma). |
| min_uptime | float (0..1 или 1..100) | 0.90 (или 90) | Минимальная доля успешных проверок за последние 24 часа от 0.0 до 1.0. |
| min_checks | int | 5, 10 | Минимальное количество проверок за последние 24 часа. |
| service | string (CSV) | chatgpt,claude,gemini, youtube_premium, ai, streaming | Только узлы, прошедшие geocheck для указанных сервисов (chatgpt, claude, gemini, notebooklm, youtube_premium, netflix, tiktok, ai, streaming). |
| asn | int | 24940, 16276 | Фильтр по номеру автономной системы (ASN) выходного IP. |
| sort | string | reputation, ping, uptime, fresh | Сортировка: reputation (EWMA + аптайм + пинг), ping (от минимального RTT), uptime, fresh. |
| limit / offset | int | limit=100&offset=0 | До 240 ключей за один запрос. |
| format | string | json, plain, base64 | Формат ответа: json (по умолчанию), plain (построчный список URI text/plain), base64. |

---

### Примеры готовых запросов

1) Общий пул для РФ под sing-box (VLESS + Shadowsocks + Trojan, без VMess, отсортированные по репутации):
    https://vpnkeys.me/api/v1/keys?protocol=vless,ss,trojan&for_russia=1&min_reputation=0.6&min_uptime=0.8&sort=reputation&limit=100

2) Страновой пул (DE, NL, FI) с отсечкой по пингу:
    https://vpnkeys.me/api/v1/keys?protocol=vless,ss,trojan&country=DE,NL,FI&max_ping=250&min_reputation=0.7&sort=ping&limit=50

3) Узлы под конкретные сервисы (ChatGPT / Claude / Gemini / YouTube Premium):
    https://vpnkeys.me/api/v1/keys?protocol=vless,ss,trojan&service=chatgpt,claude,gemini&min_reputation=0.7&sort=reputation&limit=50

4) Построчный список URI (text/plain) с теми же фильтрами:
    https://vpnkeys.me/api/v1/keys?protocol=vless,ss,trojan&country=DE,NL,FI&min_reputation=0.7&sort=reputation&limit=100&format=plain

---

### Поля каждого элемента items[] (при format=json)

- id (int64) — уникальный идентификатор ключа
- uri (string) — полный рабочий URI ключа со всеми параметрами (pbk, sid, sni, fp, flow, type, security)
- protocol (string), transport (string), security (string)
- host (string), port (int)
- country (string) — двухбуквенный ISO-код реальной страны выхода (DE, NL, FI, US и т.д.)
- latency_ms (int) — измеренный RTT в мс
- reputation (float64) — EWMA-репутация от 0.0 до 1.0
- uptime24 (float64) — доля успешных проверок за 24 часа (0.0..1.0)
- checks24 (int) — количество проверок за 24 часа
- ru_verified (bool) — подтверждена ли прокачка трафика с российской RU-ноды
- exit_asn (int), exit_asn_org (string) — номер и название автономной системы выходного IP
- services ([]string) — теги проверенных сервисов (chatgpt_ok, youtube_premium_ok, ru_verified и т.д.)
- categories ([]string) — категории источника (for_russia, ru_whitelist)

---

## 2. Готовые профили подписок (/sub/...) с поддержкой Query-фильтров

- Sing-Box (urltest JSON):
  https://vpnkeys.me/sub/singbox/for-russia.json?protocol=vless,ss,trojan&min_reputation=0.7&limit=100
- Clash.Meta / Mihomo (YAML):
  https://vpnkeys.me/sub/clash/for-russia.yaml?protocol=vless,ss,trojan&min_reputation=0.7&limit=100
- Happ / Incy (Xray JSON + leastPing):
  https://vpnkeys.me/sub/happ/for-russia.json
- Base64 (v2RayTun / v2rayNG / Streisand):
  https://vpnkeys.me/sub/base64/for-russia.txt?protocol=vless,ss,trojan&limit=100
