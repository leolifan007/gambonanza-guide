"""Fix remaining SOP violations in specific files"""
import os

# Fix 1: gambit-chain-recovery-guide - curly quotes
path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content\gambit-chain-recovery-guide.md"
with open(path, "r", encoding="utf-8") as f:
    t = f.read()
for c, r in [("\u2018", "'"), ("\u2019", "'"), ("\u201C", '"'), ("\u201D", '"')]:
    t = t.replace(c, r)
with open(path, "w", encoding="utf-8") as f:
    f.write(t)
print("Fixed curly quotes in gambit-chain-recovery-guide.md")

# Fix 2: gambonanza-tier-list - remaining ?? 
path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content\gambonanza-tier-list.md"
with open(path, "r", encoding="utf-8") as f:
    t = f.read()
for grade in ["S", "A", "B", "C"]:
    t = t.replace("?? " + grade, grade)
with open(path, "w", encoding="utf-8") as f:
    f.write(t)
print("Fixed ?? in gambonanza-tier-list.md")
