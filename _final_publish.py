#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Final: release all 10 v1.5.x articles together (hidden: false),
matching the v1.4.0 cycle. Cross-links between the articles and the homepage
update-banner require them to go live as one batch (no 404s). Not pushed."""
import os, re

CONTENT = "content"
FILES = [
    "v150-patch-breakdown.md", "v151-153-hotfix-breakdown.md", "steam-deck-settings-guide.md",
    "barter-gambit-guide.md", "enemy-powers-warning-guide.md", "controller-gamepad-guide.md",
    "strain-system-guide.md", "graveyard-stalemate-reset-guide.md", "post-15-new-player-guide.md",
    "ui-text-readability-guide.md",
]
for name in FILES:
    p = os.path.join(CONTENT, name)
    t = open(p, encoding="utf-8").read()
    t = re.sub(r'hidden:\s*(true|false)', "hidden: false", t)
    t = re.sub(r'\npublishDate: "[^"]+"', "", t)
    open(p, "w", encoding="utf-8", newline="\n").write(t)
    print("ready:", name)
print("done (not pushed)")
