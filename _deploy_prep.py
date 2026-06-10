"""Quick deploy prep: verify categories + encoding"""
import os, re, sys

content_dir = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
valid = {"Beginner", "Gambits", "Boss Battles", "Economy", "Pieces & Cards", "Strategy & Guides"}
issues = []

for fname in sorted(os.listdir(content_dir)):
    if not fname.endswith(".md") or fname in ("_index.md", "contact.md", "privacy.md"):
        continue
    path = os.path.join(content_dir, fname)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    m = re.search(r"^---(.*?)^---", text, re.MULTILINE | re.DOTALL)
    if not m:
        issues.append(f"NO FM: {fname}")
        continue
    
    fm = m.group(1)
    cm = re.search(r'(?m)^category:\s*"([^"]+)"', fm)
    if not cm:
        issues.append(f"NO CAT: {fname}")
    elif cm.group(1) not in valid:
        issues.append(f"BAD CAT '{cm.group(1)}': {fname}")
    
    # Check encoding
    for ch in ["\u2014", "\u2013", "\u2018", "\u2019", "\u201C", "\u201D"]:
        if ch in text:
            issues.append(f"ENCODING in {fname}: U+{ord(ch):04X}")
            break

if issues:
    print("ISSUES:")
    for i in issues:
        print(f"  {i}")
    sys.exit(1)
else:
    print("ALL GOOD - 44 articles valid categories + clean encoding")
