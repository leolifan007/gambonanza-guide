#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add hidden:true + staggered publishDate to the 10 v1.5.x articles (SOP 04/12 progressive release)."""
import os, re

CONTENT = "content"
ARTICLES = [
    "v150-patch-breakdown.md",
    "v151-153-hotfix-breakdown.md",
    "steam-deck-settings-guide.md",
    "barter-gambit-guide.md",
    "enemy-powers-warning-guide.md",
    "controller-gamepad-guide.md",
    "strain-system-guide.md",
    "graveyard-stalemate-reset-guide.md",
    "post-15-new-player-guide.md",
    "ui-text-readability-guide.md",
]
# stagger across ~2 weeks: 2026-09-25 .. 2026-10-10 (one per day, skipping some)
DATES = [
    "2026-09-25", "2026-09-26", "2026-09-27", "2026-09-29", "2026-09-30",
    "2026-10-02", "2026-10-03", "2026-10-05", "2026-10-07", "2026-10-09",
]

for name, pd in zip(ARTICLES, DATES):
    path = os.path.join(CONTENT, name)
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    # replace hidden: false -> hidden: true and add publishDate
    txt = txt.replace("hidden: false\n", "hidden: true\npublishDate: \"%s\"\n" % pd)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(txt)
    print("patched", name, "-> publishDate", pd)

# verify
print("\n--- verify ---")
for name in ARTICLES:
    txt = open(os.path.join(CONTENT, name), encoding="utf-8").read()
    fm = txt.split("---")[1]
    h = "hidden: true" in fm
    p = re.search(r'publishDate: "([^"]+)"', fm)
    d = re.search(r'date: "([^"]+)"', fm)
    print("%-45s hidden=%s publish=%s date=%s" % (name, h, p.group(1) if p else None, d.group(1) if d else None))
