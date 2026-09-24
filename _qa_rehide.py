#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Idempotent: force hidden:true + staggered publishDate on the 10 v1.5.x articles."""
import os, re

CONTENT = "content"
ARTICLES = [
    "v150-patch-breakdown.md", "v151-153-hotfix-breakdown.md", "steam-deck-settings-guide.md",
    "barter-gambit-guide.md", "enemy-powers-warning-guide.md", "controller-gamepad-guide.md",
    "strain-system-guide.md", "graveyard-stalemate-reset-guide.md", "post-15-new-player-guide.md",
    "ui-text-readability-guide.md",
]
DATES = [
    "2026-09-25", "2026-09-26", "2026-09-27", "2026-09-29", "2026-09-30",
    "2026-10-02", "2026-10-03", "2026-10-05", "2026-10-07", "2026-10-09",
]
for name, pd in zip(ARTICLES, DATES):
    path = os.path.join(CONTENT, name)
    t = open(path, encoding="utf-8").read()
    t = re.sub(r'hidden:\s*(true|false)', "hidden: true", t)
    if re.search(r'publishDate:', t):
        t = re.sub(r'publishDate: "[^"]+"', 'publishDate: "%s"' % pd, t)
    else:
        t = re.sub(r'(hidden: true\n)', r'\1publishDate: "%s"\n' % pd, t, count=1)
    open(path, "w", encoding="utf-8", newline="\n").write(t)
print("re-hid 10 articles with staggered publishDate")
