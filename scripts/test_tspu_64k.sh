#!/bin/sh
# POSIX shell diagnostic to test whether an endpoint experiences ISP TSPU 64 KB TCP stream freezing.
HOST="${1:-1.1.1.1}"
PORT="${2:-443}"
SNI="${3:-cloudflare.com}"

echo "[*] Testing TLS handshake & >64KB payload transfer to ${HOST}:${PORT} (SNI: ${SNI})..."
BYTES=$(curl -sS --connect-timeout 5 --max-time 10 --resolve "${SNI}:${PORT}:${HOST}" "https://${SNI}/" | wc -c | tr -d ' ')
echo "[+] Received ${BYTES} bytes from ${SNI} (${HOST}:${PORT})."
