#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Strip the literal kramdown-style link attribute syntax {target=... rel=...}
from all content .md files. External-link target/rel is now handled by the
Hugo render-link hook (layouts/_default/_markup/render-link.html)."""
import os, re, glob

CONTENT = "content"
pat = re.compile(r'\{target="_blank" rel="noopener noreferrer"\}')
total_files = 0
total_hits = 0
for path in glob.glob(os.path.join(CONTENT, "*.md")):
    t = open(path, encoding="utf-8").read()
    hits = len(pat.findall(t))
    if hits:
        t2 = pat.sub("", t)
        open(path, "w", encoding="utf-8", newline="\n").write(t2)
        total_files += 1
        total_hits += hits
        print("cleaned %-45s %d" % (os.path.basename(path), hits))
print("\ncleaned %d files, %d occurrences" % (total_files, total_hits))
