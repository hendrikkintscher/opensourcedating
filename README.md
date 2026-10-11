# opensourcedating

## Colleague portal

A read-only dashboard (features, two-stage architecture, suggestions, design mockups), file browser and
live chat feed. Stdlib-only Python, nothing to install.

### Public copy (no login, always current)

**https://hendrikkintscher.github.io/opensourcedating/** shows the Overview, Architecture, Suggestions,
Mockups and Files tabs to anyone. GitHub Actions (`.github/workflows/portal-pages.yml`)
rebuilds it with `portal/build_static.py` on every push to `main`, so any merged commit,
from a laptop or a cloud session, updates it within a minute or two. It is built only from
files tracked in git (the same files the public repo shows) and has **no Live chat tab**:
local Claude Code logs never leave the machine running the private portal below.
Preview locally: `python3 portal/build_static.py && python3 -m http.server -d _site`.

### Private portal (with live chat)

```
portal/run.sh         # publishes via Tailscale Funnel and prints the public magic link
portal/stop.sh        # stops it -- use this, not Ctrl+C/kill (see note below)
```

Only the machine running `portal/run.sh` needs Tailscale (with Funnel enabled — the script
walks you through the one-time approval the first time). Colleagues need no Tailscale of
their own: it prints a **magic link** (`https://<tailnet-name>.ts.net/?k=<token>`) that works
from any browser. Opening it logs the browser in via a 30-day HttpOnly+Secure cookie and
redirects to a clean URL. Since the link now works for anyone, not just your tailnet, treat
it like a password: don't post it anywhere public. The token lives in `.portal-token`
(git-ignored); delete the file and restart to revoke every link.

Set `PORTAL_FUNNEL=0` to fall back to the old tailnet-only link (binds to your Tailscale IP;
only colleagues already on your tailnet can open it, no public exposure).

**Stopping it:** run `portal/stop.sh`, not Ctrl+C or `kill` on `run.sh` directly -- on some
shells (confirmed on Windows/Git Bash) a signal to the backgrounded process does not reliably
disable Funnel or stop the server, which can leave the portal publicly reachable with nothing
answering, or leave orphaned processes running.

| Setting | Default | Purpose |
|---|---|---|
| `PORTAL_PORT` | `8787` | local bind port |
| `PORTAL_FUNNEL` | `1` | `0` to fall back to tailnet-only (no Funnel, no public exposure) |
| `PORTAL_FEED_DIR` | `~/.claude/projects` | where Claude Code session logs (`*.jsonl`) are read; newest file is streamed |
| `PORTAL_TOKEN` | generated | fixed token instead of `.portal-token` |

- **Dashboard content** is `portal/content.json`. Everything is marked *Guess* until you set its
  `status` to `"decided"`; the diagram and tables update on reload.
- **Files tab** hides `.git`, `.env*`, keys, `*secret*`/`*credential*` and the token file.
- **Live chat** shows only plain user/assistant text (no tool output), with emails, phone numbers
  and token/key patterns masked. Redaction is best-effort: enter test data only.
