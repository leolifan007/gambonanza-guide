"""Fix last 2 encoding issues"""
import os

# Fix 1: Advanced page - check and fix source
adv_path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content\advanced.md"
if os.path.exists(adv_path):
    with open(adv_path, "r", encoding="utf-8") as f:
        t = f.read()
    for c in "\u2014\u2013":
        if c in t:
            t = t.replace(c, "-")
            with open(adv_path, "w", encoding="utf-8") as f:
                f.write(t)
            print("Fixed advanced.md")
else:
    # Check if it's a Hugo redirect
    print("advanced.md not found, checking redirect...")
    for item in os.listdir(os.path.join(os.environ["USERPROFILE"], ".qclaw", "workspace-x74fgmx0vyb8p5is", "gambonanza-guide", "content")):
        if "advanced" in item.lower():
            print(f"Found: {item}")

# Fix 2: gambit-chain-recovery-guide - curly quotes
gcr_path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content\gambit-chain-recovery-guide.md"
with open(gcr_path, "r", encoding="utf-8") as f:
    t = f.read()

fixed = False
curly_single = "\u2018\u2019"
curly_double = "\u201C\u201D"

for c in curly_single:
    if c in t:
        t = t.replace(c, "'")
        fixed = True
        print(f"Fixed curly single in gambit-chain-recovery-guide.md")

for c in curly_double:
    if c in t:
        t = t.replace(c, '"')
        fixed = True
        print(f"Fixed curly double in gambit-chain-recovery-guide.md")

if fixed:
    with open(gcr_path, "w", encoding="utf-8") as f:
        f.write(t)
