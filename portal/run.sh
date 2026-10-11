#!/usr/bin/env bash
# Start the colleague portal and publish it with Tailscale Funnel: colleagues open a
# plain https:// link and need no Tailscale of their own. Only this host needs
# Tailscale (with Funnel enabled once -- see README.md / CLAUDE.md).
#
# Usage: portal/run.sh [port]      (env: PORTAL_PORT, PORTAL_FEED_DIR, PORTAL_FUNNEL)
# Set PORTAL_FUNNEL=0 to fall back to the old tailnet-only link (works only for
# colleagues already on your tailnet; no public exposure).
set -euo pipefail
cd "$(dirname "$0")/.."

PORT="${1:-${PORTAL_PORT:-8787}}"
FUNNEL="${PORTAL_FUNNEL:-1}"

command -v python3 >/dev/null 2>&1 || { echo "python3 is required" >&2; exit 1; }

if [ "$FUNNEL" = "1" ]; then
  command -v tailscale >/dev/null 2>&1 || {
    echo "!! tailscale is required on this host to publish a public link (visitors need none)." >&2
    echo "!! Install it / run 'tailscale up' here, or set PORTAL_FUNNEL=0 for tailnet-only mode." >&2
    exit 1
  }

  export PORTAL_HOST="127.0.0.1" PORTAL_PORT="$PORT" PORTAL_SECURE_COOKIE="1"
  python3 portal/server.py &
  SERVER_PID=$!

  cleanup() {
    kill "$SERVER_PID" 2>/dev/null || true
    tailscale funnel "$PORT" off >/dev/null 2>&1 || true
  }
  trap cleanup EXIT INT TERM

  # Wait for the server to create/load .portal-token before we read it.
  for _ in $(seq 1 50); do
    [ -f .portal-token ] && break
    sleep 0.1
  done
  [ -f .portal-token ] || { echo "!! server didn't start (no .portal-token written)" >&2; exit 1; }
  TOKEN="$(cat .portal-token)"

  echo "Enabling Tailscale Funnel on port $PORT..."
  echo "(First time ever on this tailnet: this may print a one-time browser approval link --"
  echo " open it, approve, then re-run this script.)"
  tailscale funnel --bg "$PORT"

  NAME="$(tailscale status --json 2>/dev/null | python3 -c \
    'import sys,json; print(json.load(sys.stdin)["Self"]["DNSName"].rstrip("."))' 2>/dev/null || true)"

  echo ""
  if [ -n "$NAME" ]; then
    echo "Magic link (public -- no Tailscale needed to open): https://$NAME/?k=$TOKEN"
  else
    echo "!! Could not determine this tailnet's MagicDNS name; run 'tailscale status' to find it," >&2
    echo "!! then share: https://<that-name>/?k=$TOKEN" >&2
  fi

  wait "$SERVER_PID"
else
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

  # Prefer the MagicDNS name in the printed link when available (nicer to share).
  NAME=""
  if [ "$HOST" != "127.0.0.1" ] && command -v tailscale >/dev/null 2>&1; then
    NAME="$(tailscale status --json 2>/dev/null | python3 -c \
      'import sys,json; print(json.load(sys.stdin)["Self"]["DNSName"].rstrip("."))' 2>/dev/null || true)"
  fi

  export PORTAL_HOST="$HOST" PORTAL_PORT="$PORT"
  [ -n "$NAME" ] && echo "MagicDNS name: $NAME  (replace the IP in the link below to use it)"
  exec python3 portal/server.py
fi
