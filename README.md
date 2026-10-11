# opensourcedating

## Colleague portal

A read-only dashboard (features, P2P architecture, design mockups), file browser and
live chat feed. Stdlib-only Python, nothing to install.

```
portal/run.sh        # binds to your Tailscale IP and prints the magic link
```

It prints a **magic link** (`http://<tailscale-ip>:8787/?k=<token>`). Opening it logs the
browser in via a 30-day HttpOnly cookie and redirects to a clean URL; share it only with
colleagues on your tailnet. The token lives in `.portal-token` (git-ignored); delete the
file and restart to revoke every link.

| Setting | Default | Purpose |
|---|---|---|
| `PORTAL_HOST` / `PORTAL_PORT` | `127.0.0.1` / `8787` | bind address |
| `PORTAL_FEED_DIR` | `~/.claude/projects` | where Claude Code session logs (`*.jsonl`) are read; newest file is streamed |
| `PORTAL_TOKEN` | generated | fixed token instead of `.portal-token` |

- **Dashboard content** is `portal/content.json`. Everything is marked *Guess* until you set its
  `status` to `"decided"`; the diagram and tables update on reload.
- **Files tab** hides `.git`, `.env*`, keys, `*secret*`/`*credential*` and the token file.
- **Live chat** shows only plain user/assistant text (no tool output), with emails, phone numbers
  and token/key patterns masked. Redaction is best-effort: enter test data only.
