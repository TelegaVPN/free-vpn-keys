#!/usr/bin/env python3
"""
Standalone CLI Subscription & Proxy URI Security Auditor.
Decodes Base64 or plain-text proxy subscriptions (vless://, vmess://, trojan://, ss://, hysteria2://),
rejects insecure TLS configurations (allowInsecure=1), and optionally benchmarks TCP handshake RTT.
"""
import argparse
import base64
import json
import socket
import sys
import time
import urllib.parse
import urllib.request


def load_lines(source: str) -> list[str]:
    if source.startswith(("http://", "https://")):
        req = urllib.request.Request(source, headers={"User-Agent": "vpnkeys-cli-auditor/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8", errors="replace").strip()
    else:
        with open(source, "r", encoding="utf-8", errors="replace") as f:
            raw = f.read().strip()

    if "://" not in raw:
        try:
            padded = raw + "=" * (-len(raw) % 4)
            raw = base64.b64decode(padded).decode("utf-8", errors="replace")
        except Exception:
            pass
    return [line.strip() for line in raw.splitlines() if line.strip() and not line.startswith("#")]


def audit_uri(uri: str) -> dict:
    scheme = uri.split("://", 1)[0].lower() if "://" in uri else "unknown"
    result = {"scheme": scheme, "host": "", "port": 0, "security": "none", "sni": "", "issues": []}

    if scheme == "vmess":
        b64_part = uri[8:].split("#", 1)[0]
        try:
            padded = b64_part + "=" * (-len(b64_part) % 4)
            data = json.loads(base64.b64decode(padded).decode("utf-8", errors="replace"))
            result["host"] = str(data.get("add", ""))
            result["port"] = int(data.get("port", 0) or 0)
            result["security"] = str(data.get("tls", "none") or "none")
            result["sni"] = str(data.get("sni", "") or data.get("host", ""))
            if str(data.get("allowInsecure", "")).lower() in ("1", "true"):
                result["issues"].append("allowInsecure enabled (MITM risk)")
        except Exception as exc:
            result["issues"].append(f"invalid vmess base64 JSON: {exc}")
        return result

    parsed = urllib.parse.urlSplit(uri) if hasattr(urllib.parse, "urlSplit") else urllib.parse.urlsplit(uri)
    result["host"] = parsed.hostname or ""
    result["port"] = parsed.port or 443
    qs = urllib.parse.parse_qs(parsed.query)

    sec = (qs.get("security", [""])[0] or ("tls" if scheme in ("trojan", "hysteria2", "hy2") else "none")).lower()
    result["security"] = sec
    result["sni"] = qs.get("sni", qs.get("peer", [""]))[0]

    allow_insecure = qs.get("allowInsecure", qs.get("insecure", ["0"]))[0].lower()
    if allow_insecure in ("1", "true"):
        result["issues"].append("allowInsecure=1 (vulnerable to active MITM)")
    if sec == "reality" and not qs.get("pbk", [""])[0]:
        result["issues"].append("REALITY missing public key (pbk)")
    return result


def tcp_rtt_ms(host: str, port: int, timeout: float = 2.5) -> int | None:
    if not host or port <= 0:
        return None
    t0 = time.perf_counter()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return int(round((time.perf_counter() - t0) * 1000))
    except OSError:
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit VLESS/VMess/Trojan/SS/Hy2 subscription security & TCP RTT.")
    parser.add_argument("source", help="Path to subscription file or https:// URL")
    parser.add_argument("--limit", type=int, default=20, help="Maximum nodes to test (default: 20)")
    parser.add_argument("--no-ping", action="store_true", help="Skip TCP connect latency check")
    args = parser.parse_args()

    uris = load_lines(args.source)[: args.limit]
    print(f"Loaded {len(uris)} URIs from {args.source}\n")
    print(f"{'#':<4} {'PROTO':<10} {'SECURITY':<10} {'ENDPOINT':<28} {'SNI':<24} {'RTT':<8} {'STATUS'}")
    print("-" * 100)

    for idx, uri in enumerate(uris, 1):
        info = audit_uri(uri)
        endpoint = f"{info['host']}:{info['port']}"
        rtt_str = "skip"
        if not args.no_ping:
            ms = tcp_rtt_ms(info["host"], info["port"])
            rtt_str = f"{ms}ms" if ms is not None else "timeout"
        status = "OK" if not info["issues"] else "WARN: " + "; ".join(info["issues"])
        print(f"{idx:<4} {info['scheme'].upper():<10} {info['security'].upper():<10} {endpoint:<28} {info['sni'][:23]:<24} {rtt_str:<8} {status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
