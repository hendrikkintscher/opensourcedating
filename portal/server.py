#!/usr/bin/env python3
"""Colleague portal: read-only dashboard, file browser and live chat feed.

Stdlib only. Run:  python3 portal/server.py   (prints the magic link)

Auth: a random token lives in .portal-token. Opening  /?k=<token>  sets an
HttpOnly cookie and redirects to a clean URL, so the link is also the login.
Bind to the Tailscale address (PORTAL_HOST) so only your tailnet can reach it.
"""
import hmac
import json
import os
import re
import secrets
import subprocess
import time
from http import cookies
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
STATIC = HERE / "static"
TOKEN_FILE = ROOT / ".portal-token"
COOKIE = "portal_session"
MAX_FILE = 512 * 1024

# Never show these in the file browser, whatever the path.
HIDDEN_NAMES = {".git", ".portal-token", "__pycache__", "node_modules", ".venv", ".DS_Store"}
HIDDEN_PATTERNS = re.compile(r"(^\.env|\.pem$|\.key$|id_rsa|id_ed25519|secret|credential|\.p12$)", re.I)

# Redaction for the chat feed. Order matters: tokens before generic numbers.
REDACTIONS = [
    (re.compile(r"\b(sk|ghp|gho|ghs|github_pat|xox[bp]|AKIA)[-_A-Za-z0-9]{12,}"), "[secret]"),
    (re.compile(r"(?i)(api[_-]?key|token|password|secret)\s*[=:]\s*\S+"), r"\1=[redacted]"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "[email]"),
    (re.compile(r"\+?\d[\d\s().-]{8,}\d"), "[phone]"),
]


def redact(text: str) -> str:
    for pat, repl in REDACTIONS:
        text = pat.sub(repl, text)
    return text


def load_token() -> str:
    env = os.environ.get("PORTAL_TOKEN")
    if env:
        return env
    if TOKEN_FILE.exists():
        return TOKEN_FILE.read_text().strip()
    tok = secrets.token_urlsafe(32)
    TOKEN_FILE.write_text(tok)
    TOKEN_FILE.chmod(0o600)
    return tok


TOKEN = load_token()
# Session cookie value is derived, so the raw link token is never stored client-side.
SESSION = hmac.new(TOKEN.encode(), b"portal-session", "sha256").hexdigest()
# Set only when served over HTTPS (Tailscale Funnel terminates TLS in front of us);
# on the plain-HTTP tailnet-only path it would stop the browser ever sending the
# cookie back.
SECURE_COOKIE = os.environ.get("PORTAL_SECURE_COOKIE") == "1"


def safe_path(rel: str):
    """Resolve rel inside ROOT; None if outside, hidden or secret-like."""
    p = (ROOT / rel).resolve()
    try:
        parts = p.relative_to(ROOT).parts
    except ValueError:
        return None
    for part in parts:
        if part in HIDDEN_NAMES or HIDDEN_PATTERNS.search(part):
            return None
    return p


def list_dir(rel: str):
    p = safe_path(rel)
    if not p or not p.is_dir():
        return None
    items = []
    for c in sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower())):
        if c.name in HIDDEN_NAMES or HIDDEN_PATTERNS.search(c.name):
            continue
        items.append({"name": c.name, "dir": c.is_dir(),
                      "size": c.stat().st_size if c.is_file() else None})
    return items


def git(*args):
    try:
        return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                              text=True, timeout=10).stdout.strip()
    except Exception:
        return ""


def overview():
    content = json.loads((HERE / "content.json").read_text())
    log = git("log", "-n", "15", "--pretty=%h\t%an\t%ar\t%s")
    commits = [dict(zip(("hash", "author", "when", "subject"), l.split("\t", 3)))
               for l in log.splitlines() if l.count("\t") == 3]
    files = [f for f in git("ls-files").splitlines() if not f.startswith("portal/")]
    content["repo"] = {
        "commits_total": int(git("rev-list", "--count", "HEAD") or 0),
        "branch": git("rev-parse", "--abbrev-ref", "HEAD"),
        "files": len(files),
        "recent_commits": commits,
    }
    return content


# ---- live feed -------------------------------------------------------------
def feed_dir() -> Path:
    return Path(os.environ.get("PORTAL_FEED_DIR", Path.home() / ".claude" / "projects")).expanduser()


def feed_files():
    d = feed_dir()
    return sorted(d.rglob("*.jsonl"), key=lambda f: f.stat().st_mtime) if d.exists() else []


def parse_line(line: str):
    """Keep only plain user/assistant text; drop tool calls/results."""
    try:
        o = json.loads(line)
    except ValueError:
        return None
    role = o.get("type")
    if role not in ("user", "assistant"):
        return None
    msg = o.get("message", {})
    c = msg.get("content")
    if isinstance(c, list):
        c = "\n".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
    if not isinstance(c, str) or not c.strip():
        return None
    return {"role": role, "text": redact(c.strip())[:4000], "ts": o.get("timestamp", "")}


def recent_feed(limit=30):
    files = feed_files()
    if not files:
        return []
    out = []
    for line in files[-1].read_text(errors="replace").splitlines():
        m = parse_line(line)
        if m:
            out.append(m)
    return out[-limit:]


class Handler(BaseHTTPRequestHandler):
    server_version = "portal"

    def log_message(self, fmt, *a):  # quiet; never log query strings (token)
        pass

    # -- helpers
    def authed(self) -> bool:
        c = cookies.SimpleCookie(self.headers.get("Cookie", ""))
        return COOKIE in c and hmac.compare_digest(c[COOKIE].value, SESSION)

    def send(self, code, body=b"", ctype="text/plain; charset=utf-8", headers=()):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        for k, v in headers:
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def json(self, obj, code=200):
        self.send(code, json.dumps(obj).encode(), "application/json")

    # -- routes
    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)

        if "k" in q:  # magic link
            if hmac.compare_digest(q["k"][0], TOKEN):
                cookie = f"{COOKIE}={SESSION}; HttpOnly; SameSite=Strict; Path=/; Max-Age=2592000"
                if SECURE_COOKIE:
                    cookie += "; Secure"
                return self.send(302, headers=[("Location", u.path or "/"), ("Set-Cookie", cookie)])
            return self.send(403, b"Invalid link.")

        if not self.authed():
            return self.send(401, b"Open the shared link to sign in.")

        if u.path == "/api/overview":
            return self.json(overview())
        if u.path == "/api/tree":
            items = list_dir(q.get("path", [""])[0])
            return self.json(items) if items is not None else self.json({"error": "not found"}, 404)
        if u.path == "/api/file":
            p = safe_path(q.get("path", [""])[0])
            if not p or not p.is_file():
                return self.json({"error": "not found"}, 404)
            data = p.read_bytes()[:MAX_FILE]
            if b"\0" in data:
                return self.json({"binary": True, "size": p.stat().st_size})
            return self.json({"text": data.decode("utf-8", "replace"),
                              "truncated": p.stat().st_size > MAX_FILE})
        if u.path == "/api/feed":
            return self.json(recent_feed())
        if u.path == "/api/stream":
            return self.stream()

        name = "index.html" if u.path == "/" else u.path.lstrip("/")
        f = (STATIC / name).resolve()
        if STATIC in f.parents and f.is_file():
            ctype = {".html": "text/html", ".js": "text/javascript", ".css": "text/css",
                     ".svg": "image/svg+xml"}.get(f.suffix, "application/octet-stream")
            return self.send(200, f.read_bytes(), ctype + "; charset=utf-8")
        self.send(404, b"Not found")

    def stream(self):
        """Server-sent events: poll the newest log file and push new messages."""
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        pos, current = {}, None
        try:
            while True:
                files = feed_files()
                if files:
                    f = files[-1]
                    size = f.stat().st_size
                    if f != current:
                        current, pos[f] = f, size  # new session file: start from now
                    elif size > pos.get(f, 0):
                        with f.open("rb") as fh:
                            fh.seek(pos[f])
                            chunk = fh.read().decode("utf-8", "replace")
                        pos[f] = size
                        for line in chunk.splitlines():
                            m = parse_line(line)
                            if m:
                                self.wfile.write(f"data: {json.dumps(m)}\n\n".encode())
                        self.wfile.flush()
                self.wfile.write(b": ping\n\n")
                self.wfile.flush()
                time.sleep(1.5)
        except (BrokenPipeError, ConnectionResetError):
            pass


def main():
    host = os.environ.get("PORTAL_HOST", "127.0.0.1")
    port = int(os.environ.get("PORTAL_PORT", "8787"))
    srv = ThreadingHTTPServer((host, port), Handler)
    print(f"Portal on http://{host}:{port}\nMagic link: http://{host}:{port}/?k={TOKEN}")
    if host in ("127.0.0.1", "localhost"):
        print("Tip: set PORTAL_HOST to your Tailscale IP (tailscale ip -4) to share with colleagues.")
    srv.serve_forever()


if __name__ == "__main__":
    main()
