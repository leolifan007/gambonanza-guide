# -*- coding: utf-8 -*-
"""Resolve rebase conflicts: keep our side (categories + tags), drop HEAD side."""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\ROG\Documents\GitHub\gambonanza-guide"
CONFLICTED = [
    "content/achievements.md", "content/board-clutter-priority.md",
    "content/bosses.md", "content/dark-tile-gambit-blocks.md",
    "content/decision-framework-guide.md", "content/deterministic-gambits-guide.md",
    "content/final-boss-hidden-phase.md", "content/king-difficulty-hidden-changes.md",
    "content/king-of-spades-guide.md", "content/pawn-promotion-sustainability-guide.md",
    "content/pawn-promotion-troubleshooting.md", "content/post-boss-economy-restart.md",
    "content/self-destructive-loop-guide.md", "content/stage-4-economy-wall.md",
    "content/strategy.md", "content/tips.md",
]
PAT = re.compile(r"^<<<<<<< HEAD\n(.*?)^=======\n(.*?)^>>>>>>> [^\n]*\n", re.M | re.S)

for rel in CONFLICTED:
    path = os.path.join(BASE, rel)
    with open(path, "r", encoding="utf-8-sig") as f:
        t = f.read()
    before = t.count("<<<<<<<")
    t2 = PAT.sub(lambda m: m.group(2), t)
    after = t2.count("<<<<<<<")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(t2)
    print("%s: blocks %d -> %d" % (rel, before, after))
print("done")
