#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Broken internal-link checker across the built _hugo_preview site."""
import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = "_hugo_preview"
pages = set()
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if f == "index.html":
            rel = os.path.relpath(dp, ROOT).replace("\\", "/")
            pages.add("/" if rel == "." else "/%s/" % rel)

broken = {}
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if not f.endswith(".html"):
            continue
        fp = os.path.join(dp, f)
        html = open(fp, encoding="utf-8").read()
        for m in re.findall(r'href="(/[^"#?]*)"', html):
            if m.startswith("//"):
                continue
            if m not in pages and not m.endswith(".xml") and not m.endswith(".svg") and not m.endswith(".css") and not m.endswith(".js") and not m.endswith(".txt") and not m.endswith(".webp") and not m.endswith(".png") and not m.endswith(".ico"):
                broken.setdefault(m, set()).add(os.path.relpath(fp, ROOT))

if broken:
    print("BROKEN INTERNAL LINKS (%d):" % len(broken))
    for k in sorted(broken):
        print("  %-45s  <- %s" % (k, list(broken[k])[:2]))
else:
    print("No broken internal links found.")
