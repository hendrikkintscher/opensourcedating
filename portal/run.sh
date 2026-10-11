#!/usr/bin/env bash
# Start the colleague portal bound to this machine's Tailscale address.
# Usage: portal/run.sh [port]      (env: PORTAL_PORT, PORTAL_FEED_DIR, PORTAL_HOST)
set -euo pipefail
cd "$(dirname "$0")/.."

PORT="${1:-${PORTAL_PORT:-8787}}"
HOST="${PORTAL_HOST:-}"

if [ -z "$HOST" ]; then
  if command -v tailscale >/dev/null 2>&1; then
    HOST="$(tailscale ip -4 2>/dev/null | head -n1 || true)"
  fi
  if [ -z "$HOST" ]; then
    echo "!! Tailscale address not found (is tailscale installed and 'tailscale up' done?)." >&2
    echo "!! Falling back to 127.0.0.1: only this machine can open the link." >&2
    HOST="127.0.0.1"
  fi
fi

command -v python3 >/dev/null 2>&1 || { echo "python3 is required" >&2; exit 1; }

# Prefer the MagicDNS name in the printed link when available (nicer to share).
NAME=""
if [ "$HOST" != "127.0.0.1" ] && command -v tailscale >/dev/null 2>&1; then
  NAME="$(tailscale status --json 2>/dev/null | python3 -c \
    'import sys,json; print(json.load(sys.stdin)["Self"]["DNSName"].rstrip("."))' 2>/dev/null || true)"
fi

export PORTAL_HOST="$HOST" PORTAL_PORT="$PORT"
[ -n "$NAME" ] && echo "MagicDNS name: $NAME  (replace the IP in the link below to use it)"
exec python3 portal/server.py
