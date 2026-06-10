"""Check king-of-spades-guide.md structure"""
path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content\king-of-spades-guide.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
count = 0
for i, line in enumerate(lines):
    s = line.strip()
    if s.startswith("|") and s.endswith("|"):
        count += 1
        if i > 0 and lines[i-1].strip() == "":
            # This could be a table header
            print(f"Table header at line {i+1}: {s[:60]}")
        elif i > 0 and lines[i-1].strip().startswith("|"):
            pass  # continuation
        elif i > 0:
            # New single-line table row
            print(f"Single row at line {i+1}: {s[:60]}")
print(f"\nTotal pipe-lines: {count}")
