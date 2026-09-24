#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 10 v1.5.x SVG diagrams for gambonanzaguide.com.
Style must match existing site VI: dark bg, gold/teal accents, VT323 headings, 12.5px body.
No UTF-8 BOM. All text XML-escaped.
"""
import os
from xml.sax.saxutils import escape

OUT = os.path.join("static", "images", "diagrams")
BG = "#1A0F1A"; PANEL = "#2D1A2D"; GOLD = "#D4A84A"; TEAL = "#4A9B9B"
CREAM = "#E8D5C0"; TITLE = "#F5E6D3"

def head(w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif" '
            f'width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
            f'<rect width="{w}" height="{h}" fill="{BG}" rx="12"/>\n'
            f'<defs><marker id="ar" markerWidth="10" markerHeight="10" refX="8" refY="3" '
            f'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L8,3 L0,6 Z" fill="{GOLD}"/></marker></defs>\n'
            f'<text x="{w/2}" y="34" fill="{GOLD}" font-family="\'VT323\',monospace" '
            f'font-size="22" text-anchor="middle">{escape(title)}</text>\n')

def panel(x, y, w, h, accent, label, lines):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{PANEL}" stroke="{accent}" stroke-width="1.5"/>\n'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="24" rx="8" fill="{accent}" opacity="0.18"/>\n'
    cx = x + w/2
    s += (f'<text x="{cx}" y="{y+17}" fill="{accent}" font-family="\'VT323\',monospace" '
          f'font-size="15" text-anchor="middle">{escape(label)}</text>\n')
    yy = y + 42
    for ln in lines:
        s += (f'<text x="{cx}" y="{yy}" fill="{CREAM}" font-size="12.5" '
              f'text-anchor="middle">{escape(ln)}</text>\n')
        yy += 18
    return s

def arrow(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GOLD}" stroke-width="2" marker-end="url(#ar)"/>\n'

def save(name, body):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(body)
    print("wrote", path, len(body), "bytes")

# 1. v150-change-map.svg
def s1():
    s = head(700, 440, "v1.5.x Change Map")
    s += f'<text x="350" y="250" fill="{TITLE}" font-family="\'VT323\',monospace" font-size="18" text-anchor="middle">1.5.0 - 1.5.3</text>\n'
    s += panel(40, 60, 190, 150, TEAL, "UI Revamp", ["Text easier to read", "Mainly Steam Deck", "Clearer board state"])
    s += panel(255, 60, 190, 150, GOLD, "Enemy Power", ["Clear trigger warning", "Before power fires", "Read threats faster"])
    s += panel(470, 60, 190, 150, TEAL, "Achievements", ["Several bug fixes", "Conditions now", "fire correctly"])
    s += panel(255, 250, 190, 150, GOLD, "Steam Deck", ["Officially Verified", "Cursor + font fixes", "Strains navigation"])
    s += arrow(230, 135, 255, 135) + arrow(445, 135, 470, 135) + arrow(350, 210, 350, 250)
    return s + "</svg>\n"

# 2. v151-153-timeline.svg
def s2():
    s = head(720, 300, "1.5.1 to 1.5.3 Timeline")
    s += f'<line x1="50" y1="150" x2="670" y2="150" stroke="{GOLD}" stroke-width="3"/>\n'
    pts = [("1.5.1", "9/4", "Stalemate resets", "the Graveyard"), ("1.5.2b", "9/11", "Linux cursor", "visibility fix"), ("1.5.3", "9/17", "Hover info fix +", "Strains navigation")]
    for i, (v, d, l1, l2) in enumerate(pts):
        cx = 140 + i * 220
        s += f'<circle cx="{cx}" cy="150" r="9" fill="{GOLD}"/>\n'
        s += f'<text x="{cx}" y="120" fill="{TEAL}" font-family="\'VT323\',monospace" font-size="18" text-anchor="middle">{escape(v)}</text>\n'
        s += f'<text x="{cx}" y="100" fill="{CREAM}" font-size="12.5" text-anchor="middle">{escape(d)}</text>\n'
        s += f'<text x="{cx}" y="190" fill="{CREAM}" font-size="12.5" text-anchor="middle">{escape(l1)}</text>\n'
        s += f'<text x="{cx}" y="208" fill="{CREAM}" font-size="12.5" text-anchor="middle">{escape(l2)}</text>\n'
    return s + "</svg>\n"

# 3. steamdeck-settings-flow.svg
def s3():
    s = head(700, 420, "Steam Deck Setup Flow")
    s += panel(255, 55, 190, 90, GOLD, "Text Readability", ["UI revamp in 1.5", "Larger, sharper text"])
    s += panel(60, 200, 180, 120, TEAL, "Display", ["Check letterboxing", "Match Deck aspect", "No black bars"])
    s += panel(260, 200, 180, 120, GOLD, "Controls", ["Controller nav", "Strains menus", "Trackpad clicks"])
    s += panel(460, 200, 180, 120, TEAL, "In-Game", ["Settings / Extras", "Skip animations", "Algebraic notation"])
    s += arrow(350, 145, 350, 200)
    s += arrow(300, 260, 260, 260) + arrow(400, 260, 460, 260)
    return s + "</svg>\n"

# 4. barter-cycle.svg
def s4():
    s = head(700, 380, "Barter's Gambit Reset Cycle")
    s += panel(50, 70, 170, 110, GOLD, "Barter Active", ["Sell a BISHOP", "grants a random", "piece (5 uses)"])
    s += panel(265, 70, 170, 110, TEAL, "Reward", ["Extra piece", "enters the Stock", "Counts down"])
    s += panel(480, 70, 170, 110, GOLD, "Enter the Shop", ["Uses reset to 5", "Fresh cycle", "common path"])
    s += panel(265, 240, 170, 110, TEAL, "Graveyard (1.5.1)", ["Trade also resets", "after a Graveyard", "New in 1.5.1"])
    s += arrow(220, 125, 265, 125) + arrow(435, 125, 480, 125)
    s += arrow(565, 180, 565, 220) + arrow(565, 220, 435, 295)
    return s + "</svg>\n"

# 5. enemy-power-warning.svg
def s5():
    s = head(700, 340, "Enemy Power Trigger Warning")
    s += panel(60, 80, 250, 180, TEAL, "Before 1.5", ["Power fires with", "little visual cue", "Easy to miss", "Punishing surprises"])
    s += panel(390, 80, 250, 180, GOLD, "After 1.5", ["Clear prompt appears", "before the power", "triggers - react", "in time"])
    s += arrow(310, 170, 390, 170)
    return s + "</svg>\n"

# 6. controller-nav-map.svg
def s6():
    s = head(700, 400, "Controller Navigation Map")
    s += panel(255, 50, 190, 90, GOLD, "Main Menu", ["Settings / Extras", "Play / Continue"])
    s += panel(60, 200, 175, 130, TEAL, "Strains Menu", ["Improved in 1.5.3", "Select / deselect", "all modifiers"])
    s += panel(263, 200, 175, 130, GOLD, "Gambit Collection", ["Smoother tab nav", "Browse all gambits"])
    s += panel(466, 200, 175, 130, TEAL, "In-Run HUD", ["Pause / Info hover", "now on top"])
    s += arrow(350, 140, 350, 200)
    s += arrow(300, 265, 263, 265) + arrow(400, 265, 466, 265)
    return s + "</svg>\n"

# 7. strain-ladder.svg
def s7():
    s = head(700, 440, "Difficulty, Strains and the Graveyard")
    rows = [("PAWN", "No Strains - Graveyard on", TEAL), ("ROOK", "Strains begin - Graveyard gone", GOLD),
            ("KNIGHT", "Enemy plays first - no buyback", TEAL), ("BISHOP", "Harder prices and Stock", GOLD),
            ("QUEEN", "Tiles once per run", TEAL), ("KING", "Maximum challenge", GOLD)]
    y = 60
    for name, desc, ac in rows:
        s += f'<rect x="70" y="{y}" width="560" height="52" rx="8" fill="{PANEL}" stroke="{ac}" stroke-width="1.5"/>\n'
        s += f'<text x="100" y="{y+32}" fill="{ac}" font-family="\'VT323\',monospace" font-size="18">{escape(name)}</text>\n'
        s += f'<text x="250" y="{y+32}" fill="{CREAM}" font-size="12.5">{escape(desc)}</text>\n'
        y += 60
    return s + "</svg>\n"

# 8. graveyard-stalemate-reset.svg
def s8():
    s = head(700, 340, "Stalemate Resets the Graveyard")
    s += panel(60, 80, 240, 170, TEAL, "Before 1.5.1", ["A Stalemate did not", "clear the Graveyard", "Lost pieces stayed", "as a running list"])
    s += panel(400, 80, 240, 170, GOLD, "After 1.5.1", ["Stalemate now resets", "the Graveyard", "Clean slate each", "stalemate event"])
    s += arrow(300, 165, 400, 165)
    return s + "</svg>\n"

# 9. post15-beginner-path.svg
def s9():
    s = head(700, 300, "New Player Path After 1.5")
    steps = [("1", "Start on PAWN", TEAL), ("2", "Tune Settings", GOLD), ("3", "Learn Powers", TEAL), ("4", "Climb Strains", GOLD)]
    x = 60
    for num, label, ac in steps:
        s += f'<rect x="{x}" y="110" width="130" height="110" rx="8" fill="{PANEL}" stroke="{ac}" stroke-width="1.5"/>\n'
        s += f'<text x="{x+65}" y="150" fill="{ac}" font-family="\'VT323\',monospace" font-size="26" text-anchor="middle">{escape(num)}</text>\n'
        s += f'<text x="{x+65}" y="185" fill="{CREAM}" font-size="12.5" text-anchor="middle">{escape(label)}</text>\n'
        if num != "4":
            s += arrow(x+130, 165, x+150, 165)
        x += 150
    return s + "</svg>\n"

# 10. ui-readability-compare.svg
def s10():
    s = head(700, 340, "UI Readability After 1.5")
    s += panel(60, 80, 250, 180, TEAL, "Before 1.5", ["Smaller text on", "handheld screens", "Hard to scan at", "a glance"])
    s += panel(390, 80, 250, 180, GOLD, "After 1.5", ["Revamped text", "Larger and sharper", "Faster to read", "on Steam Deck"])
    s += arrow(310, 170, 390, 170)
    return s + "</svg>\n"

os.makedirs(OUT, exist_ok=True)
for name, fn in [
    ("v150-change-map.svg", s1),
    ("v151-153-timeline.svg", s2),
    ("steamdeck-settings-flow.svg", s3),
    ("barter-cycle.svg", s4),
    ("enemy-power-warning.svg", s5),
    ("controller-nav-map.svg", s6),
    ("strain-ladder.svg", s7),
    ("graveyard-stalemate-reset.svg", s8),
    ("post15-beginner-path.svg", s9),
    ("ui-readability-compare.svg", s10),
]:
    save(name, fn())
print("done")
