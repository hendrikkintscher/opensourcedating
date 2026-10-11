#!/usr/bin/env bash
# Stop the portal server and make sure Tailscale Funnel is turned back off.
#
# Use this to stop the portal -- don't rely on `kill`ing run.sh's process
# directly. Its cleanup trap is best-effort and confirmed unreliable in some
# shells (sending a signal to a backgrounded run.sh does not reliably run the
# trap on Windows/Git Bash), which could leave Funnel on with a dead server
# behind it.
set -uo pipefail
cd "$(dirname "$0")/.."

if command -v tailscale >/dev/null 2>&1; then
  tailscale funnel --https=443 off >/dev/null 2>&1 \
    && echo "Tailscale Funnel disabled." \
    || echo "Tailscale Funnel was already off (or tailscale errored silently)."
else
  echo "!! tailscale not found on PATH -- check manually with 'tailscale funnel status'." >&2
fi

if command -v powershell.exe >/dev/null 2>&1; then
  # Git Bash's kill/pkill cannot reliably reach native Windows python.exe
  # processes (confirmed: neither matches nor signals them), so use
  # PowerShell to find and stop the exact portal/server.py process(es).
  PSFILE="$(mktemp --suffix=.ps1)"
  cat > "$PSFILE" <<'PS'
$procs = Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'portal[\\/]server\.py' }
if ($procs) {
  $procs | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
  Write-Output "Portal server stopped."
} else {
  Write-Output "No running portal server found."
}
PS
  powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$(cygpath -w "$PSFILE")"
  rm -f "$PSFILE"
elif pkill -f "portal/server.py" 2>/dev/null; then
  echo "Portal server stopped."
else
  echo "No running portal server found."
fi
