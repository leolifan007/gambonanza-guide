import os
root = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
skip = {"_index.md","contact.md","privacy.md"}
files = [f for f in sorted(os.listdir(root)) if f.endswith(".md") and f not in skip]
print(f"Total: {len(files)}")
for f in files:
    print(f"  {f}")
