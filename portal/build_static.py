#!/usr/bin/env python3
"""Build a public, static copy of the portal into _site/ (for GitHub Pages).

Stdlib only. Run from anywhere:  python3 portal/build_static.py [outdir]

The public copy has the Overview, Peer-to-peer, Mockups and Files tabs. It has
no Live chat tab and no login: local Claude Code logs never leave the machine
running server.py. Files are taken from `git ls-files` only (never untracked
or ignored files), filtered by the same hidden-name rules as the server, so
the site shows nothing the public GitHub repo doesn't already show.
"""
import json
import os
import shutil
import sys
from pathlib import Path

# server.py reads a token at import; the static build never uses it, and must
# not create .portal-token as a side effect.
os.environ.setdefault("PORTAL_TOKEN", "static-build-unused")
import server  # noqa: E402

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else server.ROOT / "_site").resolve()


def tracked_files():
    for rel in server.git("ls-files").splitlines():
        parts = Path(rel).parts
        if any(p in server.HIDDEN_NAMES or server.HIDDEN_PATTERNS.search(p) for p in parts):
            continue
        if (server.ROOT / rel).is_file():
            yield rel


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "data").mkdir(parents=True)

    overview = server.overview()
    overview["repo"]["branch"] = os.environ.get("GITHUB_REF_NAME") or overview["repo"]["branch"]
    overview["repo"]["built"] = server.git("log", "-1", "--format=%cI")

    tree, files = {}, {}
    for rel in tracked_files():
        p = server.ROOT / rel
        parts = rel.split("/")
        for i in range(len(parts)):
            parent, name = "/".join(parts[:i]), parts[i]
            is_dir = i < len(parts) - 1
            items = tree.setdefault(parent, {})
            items.setdefault(name, {"name": name, "dir": is_dir,
                                    "size": None if is_dir else p.stat().st_size})
        data = p.read_bytes()[:server.MAX_FILE]
        if b"\0" in data:
            files[rel] = {"binary": True, "size": p.stat().st_size}
        else:
            files[rel] = {"text": data.decode("utf-8", "replace"),
                          "truncated": p.stat().st_size > server.MAX_FILE}
    tree = {k: sorted(v.values(), key=lambda x: (not x["dir"], x["name"].lower()))
            for k, v in tree.items()}

    for name, obj in (("overview", overview), ("tree", tree), ("files", files)):
        (OUT / "data" / f"{name}.json").write_text(json.dumps(obj, ensure_ascii=False))

    html = (server.STATIC / "index.html").read_text()
    html = html.replace("<script>", "<script>window.PORTAL_STATIC = true;</script>\n<script>", 1)
    (OUT / "index.html").write_text(html)
    (OUT / ".nojekyll").write_text("")
    print(f"Built {OUT} ({len(files)} files)")


if __name__ == "__main__":
    build()
