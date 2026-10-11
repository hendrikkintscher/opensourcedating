# opensourcedating: instructions for Claude Code

Open-source, peer-to-peer dating app (early concept stage). Only test data is ever
entered; nothing personal.

## Colleague portal (`portal/`)

A read-only site colleagues open via a Tailscale link: dashboard of features, P2P
architecture diagram, design mockups, file browser and a live feed of Claude Code chats.
Stdlib-only Python, no installs. Details are in `README.md` ("Colleague portal").

### First-time setup on this machine (the one running Tailscale)
1. `git pull` the branch that contains `portal/` (`claude/brave-franklin-qlvnt3` until it is merged).
2. Check Tailscale is up: `tailscale status` and `tailscale ip -4`. If not, tell the owner to run
   `tailscale up`; do not try to log in for them.
3. Start it: `portal/run.sh` (foreground) or in the background:
   `nohup portal/run.sh > /tmp/portal.log 2>&1 &`. The log then holds the **magic link**.
4. Print the magic link to the owner. They send it to colleagues; opening it logs the browser in.
   Test it yourself with `curl -sI "<link>"`: expect `302` with a `Set-Cookie`.
5. Live chat reads `~/.claude/projects/**/*.jsonl` by default. Check that folder exists on this
   machine; if the owner keeps logs elsewhere, set `PORTAL_FEED_DIR`.

### Rules
- The link is the password. Never paste it into commits, issues, PRs or docs. `.portal-token` is
  git-ignored; keep it that way. To revoke all links: delete `.portal-token`, restart.
- Bind only to the Tailscale IP (the launcher does this). Never bind `0.0.0.0` or use Tailscale
  Funnel / any public tunnel: access control depends on the tailnet.
- The chat feed redaction is best-effort. If the owner starts discussing anything personal in a
  chat, remind them the feed is visible to colleagues.
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
