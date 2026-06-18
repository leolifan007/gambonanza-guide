# -*- coding: utf-8 -*-
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

root = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
skip = {"_index.md", "contact.md", "privacy.md"}
valid = {"Beginner", "Gambits", "Boss Battles", "Economy", "Pieces & Cards", "Strategy & Guides"}
issues = []

for fname in sorted(os.listdir(root)):
    if not fname.endswith(".md") or fname in skip:
        continue
    path = os.path.join(root, fname)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    m = re.search(r"^---(.*?)^---", text, re.MULTILINE | re.DOTALL)
    if not m:
        issues.append(f"{fname}: NO FRONTMATTER")
        continue
    
    fm = m.group(1)
    cm = re.search(r'(?m)^category:\s*"([^"]+)"', fm)
    if not cm:
        issues.append(f"{fname}: NO CATEGORY")
        continue
    
    cat = cm.group(1)
    if cat not in valid:
        issues.append(f"{fname}: INVALID CAT '{cat}'")

if issues:
    print("ISSUES FOUND:")
    for i in issues:
        print(f"  {i}")
else:
    print("ALL 44 ARTICLES HAVE VALID CATEGORIES")
