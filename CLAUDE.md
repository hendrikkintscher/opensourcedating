# opensourcedating: instructions for Claude Code

Open-source, peer-to-peer dating app (early concept stage). Only test data is ever
entered; nothing personal.

## Colleague portal (`portal/`)

A read-only site colleagues open via a public link (dashboard of features, P2P
architecture diagram, design mockups, file browser and a live feed of Claude Code chats).
Stdlib-only Python, no installs. Details are in `README.md` ("Colleague portal").

**Published via Tailscale Funnel** (decided 2026-10-11, overriding the earlier
tailnet-only design): only the host machine needs Tailscale; colleagues open a plain
`https://` link and need no Tailscale account or login of their own. This means the
**token in the link is the only access control** — there is no network-level
restriction anymore. Treat the link as a password, more strictly than before.

### First-time setup on this machine (the one running Tailscale)
1. `git pull` the branch that contains `portal/` (`claude/brave-franklin-qlvnt3` until it is merged).
2. Check Tailscale is up: `tailscale status`. If not, tell the owner to run `tailscale up`; do
   not try to log in for them.
3. Start it: `portal/run.sh` (foreground) or in the background:
   `nohup portal/run.sh > /tmp/portal.log 2>&1 &`. This enables Tailscale Funnel on the port and
   prints the public **magic link** (`https://<tailnet-name>.ts.net/?k=<token>`).
   - First Funnel use ever on this tailnet: the CLI may print a one-time browser approval link
     (or an admin can grant the `funnel` node attribute directly in the admin console's Access
     Controls page). Approve it, then re-run `portal/run.sh`.
   - To go back to the old tailnet-only link (no public exposure), run with `PORTAL_FUNNEL=0`.
4. Print the magic link to the owner. They send it to colleagues; opening it logs the browser in.
   Test it yourself with `curl -sI "<link>"`: expect `302` with a `Set-Cookie`.
5. Live chat reads `~/.claude/projects/**/*.jsonl` by default. Check that folder exists on this
   machine; if the owner keeps logs elsewhere, set `PORTAL_FEED_DIR`.
6. To stop the portal, run `portal/stop.sh` -- do not just `kill`/Ctrl+C `run.sh`'s process.
   Confirmed on this project: signaling a backgrounded `run.sh` does not reliably run its cleanup
   trap on Windows/Git Bash, which can leave Funnel on (publicly routable) with a dead server
   behind it, or leave orphaned `portal/server.py` processes running. `stop.sh` explicitly turns
   Funnel off and kills the server (via PowerShell process matching on Windows, since Git Bash's
   `kill`/`pkill` cannot reach native Windows python processes either). After stopping, verify
   with `tailscale funnel status` -> `No serve config`.

### Rules
- The link is the password — now more than ever, since it is the *only* gate (no tailnet
  membership required to reach it). Never paste it into commits, issues, PRs, docs, or chat
  logs. `.portal-token` is git-ignored; keep it that way. To revoke all links: delete
  `.portal-token`, restart.
- Funnel mode binds the server to `127.0.0.1` only (Tailscale's proxy forwards to it); never
  change that to `0.0.0.0`. `run.sh` sets `PORTAL_SECURE_COOKIE=1` in Funnel mode so the session
  cookie gets the `Secure` flag — don't set that flag in tailnet-only mode, where the connection
  is plain HTTP and a `Secure` cookie would never be sent back.
- The chat feed redaction is best-effort. If the owner starts discussing anything personal in a
  chat, remind them the feed is now visible to anyone with the link, not just the tailnet.
- Don't add dependencies to the portal without asking; keeping it stdlib-only is deliberate.

### Keeping the dashboard current
- All dashboard content lives in `portal/content.json`. When the owner decides something
  (for example the transport library), change that item's `status` from `"assumed"` to `"decided"`
  and update `choice`/`why`. No restart needed; the page reloads it.
- Add new features to `features`, new technology choices to `p2p.decisions`, new open
  questions to `p2p.open_questions`.
- If a decision changes the architecture, update the SVG in `portal/static/index.html`
  (function `diagram()`) so the picture matches the table. Mockups are the `SCREENS` object there.
- Mockups and diagrams are guesses until marked decided; keep that honest.

### Tests to run after changing `portal/server.py`
Start with `PORTAL_PORT=8799 PORTAL_FEED_DIR=<tmp dir> python3 portal/server.py`, then check:
no cookie gives 401; `/?k=wrong` gives 403; `/?k=<token>` gives 302 plus cookie; `/api/file?path=../x`,
`.env` and `.portal-token` give 404; a message appended to a `.jsonl` in the feed dir arrives on
`/api/stream` with emails and phone numbers masked.

## Git
- Work on a feature branch, commit small logical changes, and don't push or open PRs unless asked.
