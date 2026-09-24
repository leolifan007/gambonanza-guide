#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix pro-tip usage to the paired shortcode form required by layouts/shortcodes/pro-tip.html (.Inner)."""
import os, re

CONTENT = "content"
FILES = [
    "v150-patch-breakdown.md","v151-153-hotfix-breakdown.md","steam-deck-settings-guide.md",
    "barter-gambit-guide.md","enemy-powers-warning-guide.md","controller-gamepad-guide.md",
    "strain-system-guide.md","graveyard-stalemate-reset-guide.md","post-15-new-player-guide.md",
    "ui-text-readability-guide.md",
]
pat = re.compile(r'\{\{< pro-tip "([^"]*)" >\}\}')
for name in FILES:
    path = os.path.join(CONTENT, name)
    t = open(path, encoding="utf-8").read()
    t2 = pat.sub(lambda m: "{{< pro-tip >}}%s{{< /pro-tip >}}" % m.group(1), t)
    if t2 != t:
        open(path, "w", encoding="utf-8", newline="\n").write(t2)
        print("fixed", name)
    else:
        print("no change", name)
