#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA helper: temporarily unhide the 10 v1.5.x articles so Hugo renders them for inspection."""
import os, re

CONTENT = "content"
ARTICLES = [
    "v150-patch-breakdown.md", "v151-153-hotfix-breakdown.md", "steam-deck-settings-guide.md",
    "barter-gambit-guide.md", "enemy-powers-warning-guide.md", "controller-gamepad-guide.md",
    "strain-system-guide.md", "graveyard-stalemate-reset-guide.md", "post-15-new-player-guide.md",
    "ui-text-readability-guide.md",
]
for name in ARTICLES:
    path = os.path.join(CONTENT, name)
    t = open(path, encoding="utf-8").read()
    t = t.replace("hidden: true", "hidden: false")
    t = re.sub(r'\npublishDate: "[^"]+"', "", t)
    open(path, "w", encoding="utf-8", newline="\n").write(t)
print("unhid 10 articles for QA render")
