# -*- coding: utf-8 -*-
"""Audit: every article must have categories (plural) front matter; report issues."""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\ROG\Documents\GitHub\gambonanza-guide\content"

issues = []
no_cat = []
for fname in sorted(os.listdir(BASE)):
    if not fname.endswith(".md"):
        continue
    path = os.path.join(BASE, fname)
    t = open(path, encoding="utf-8-sig").read()
    if not t.startswith("---"):
        issues.append("%s: no front matter opener" % fname)
        continue
    fm_end = t.find("\n---", 3)
    if fm_end == -1:
        issues.append("%s: no closing ---" % fname)
        continue
    fm = t[:fm_end]
    if not re.search(r"(?m)^categories:", fm):
        no_cat.append(fname)
    if re.search(r"(?m)^category:", fm):
        issues.append("%s: still has singular category:" % fname)
    if "<<" in t:
        issues.append("%s: conflict marker leftover" % fname)

print("files without categories: %d" % len(no_cat))
for f in no_cat:
    print("  NO CAT: %s" % f)
print("issues:")
for i in issues:
    print("  %s" % i)
print("done")
