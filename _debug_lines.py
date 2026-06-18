"""Debug: check specific lines in how-to-play.md"""
path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content\how-to-play.md"
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i in range(77, 86):
    line = lines[i] if i < len(lines) else "(EOF)"
    stripped = line.strip()
    print(f"Line {i+1}: repr={repr(line)}")
    print(f"  stripped: {repr(stripped)}")
    print(f"  starts='|': {stripped.startswith('|')}")
    print(f"  ends='|': {stripped.endswith('|')}")
    is_sep = '|' in stripped and '-' in stripped
    print(f"  is_separator: {is_sep}")
    print()
