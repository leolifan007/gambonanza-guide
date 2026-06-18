import sys
import re

path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content\gambits.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Fix all encoding-damaged characters

# 1. Nav items: ? -> ⚡
text = text.replace(
    '<span class="nav-label">? Quick nav:</span>',
    '<span class="nav-label">&#9889; Quick nav:</span>'
)
text = text.replace(
    '<a href="#teleport" class="nav-anchor">? Teleport</a>',
    '<a href="#teleport" class="nav-anchor">&#9889; Teleport</a>'
)
text = text.replace(
    '<a href="#ultimate-counter" class="nav-anchor">? Ultimate Counter</a>',
    '<a href="#ultimate-counter" class="nav-anchor">&#9889; Ultimate Counter</a>'
)
text = text.replace(
    '<a href="#heal-board" class="nav-anchor">? Heal Board</a>',
    '<a href="#heal-board" class="nav-anchor">&#9889; Heal Board</a>'
)

# 2. Synergy card icons - replace based on "Best with" context
# Teleport section: King, Queen, Rook
text = text.replace(
    '<div class="synergy-card-icon">?</div>\n        <div class="synergy-card-content">\n          <strong>Best with King</strong>',
    '<div class="synergy-card-icon">&#9812;</div>\n        <div class="synergy-card-content">\n          <strong>Best with King</strong>'
)
text = text.replace(
    '<div class="synergy-card-icon">?</div>\n        <div class="synergy-card-content">\n          <strong>Best with Queen</strong>',
    '<div class="synergy-card-icon">&#9813;</div>\n        <div class="synergy-card-content">\n          <strong>Best with Queen</strong>'
)
text = text.replace(
    '<div class="synergy-card-icon">?</div>\n        <div class="synergy-card-content">\n          <strong>Best with Rook</strong>',
    '<div class="synergy-card-icon">&#9814;</div>\n        <div class="synergy-card-content">\n          <strong>Best with Rook</strong>'
)
# Ultimate Counter: Any piece, King, Queen
text = text.replace(
    '<div class="synergy-card-icon">?</div>\n        <div class="synergy-card-content">\n          <strong>Best with Any piece</strong>',
    '<div class="synergy-card-icon">&#9823;</div>\n        <div class="synergy-card-content">\n          <strong>Best with Any piece</strong>'
)
# Heal Board: Sacrificed Knights, Sacrificed Pawns, Sacrificed Queen
text = text.replace(
    '<div class="synergy-card-icon">?</div>\n        <div class="synergy-card-content">\n          <strong>Best with Sacrificed Knights</strong>',
    '<div class="synergy-card-icon">&#9816;</div>\n        <div class="synergy-card-content">\n          <strong>Best with Sacrificed Knights</strong>'
)
text = text.replace(
    '<div class="synergy-card-icon">?</div>\n        <div class="synergy-card-content">\n          <strong>Best with Sacrificed Pawns</strong>',
    '<div class="synergy-card-icon">&#9817;</div>\n        <div class="synergy-card-content">\n          <strong>Best with Sacrificed Pawns</strong>'
)
text = text.replace(
    '<div class="synergy-card-icon">?</div>\n        <div class="synergy-card-content">\n          <strong>Best with Sacrificed Queen</strong>',
    '<div class="synergy-card-icon">&#9813;</div>\n        <div class="synergy-card-content">\n          <strong>Best with Sacrificed Queen</strong>'
)

# 3. PRO TIP emojis (all 4)
text = text.replace(
    '<div style="margin-top:8px;font-size:0.85rem;color:var(--gold)">?? PRO TIP:',
    '<div style="margin-top:8px;font-size:0.85rem;color:var(--gold)">&#128161; PRO TIP:'
)

# 4. Tier table header
text = text.replace('| Ti er |', '| Tier |')

# Verify no remaining ? in HTML content (outside markdown)
lines = text.split('\n')
remaining_q = 0
for i, line in enumerate(lines, 1):
    # Only check lines that contain HTML tags
    if '<' in line and '>' in line and '?' in line:
        print(f"  Line {i}: {line.strip()}")
        remaining_q += 1

print(f"\nRemaining ? in HTML: {remaining_q}")
print(f"All fixes applied!")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
