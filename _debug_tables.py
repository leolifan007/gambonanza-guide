"""Debug: test table detection on how-to-play.md"""
import re

path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content\how-to-play.md"
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
print(f"Total lines: {len(lines)}")
print(f"File has \\r: {'\r' in ''.join(lines[:5])}")

plain_tables = []
in_synergy = False
in_frontmatter = False
in_table = False
table_start = -1

for i, line in enumerate(lines):
    stripped = line.strip()
    
    # Track frontmatter
    if stripped == '---' and not in_frontmatter and i < 20:
        in_frontmatter = True
        continue
    if stripped == '---' and in_frontmatter:
        in_frontmatter = False
        continue
    if in_frontmatter:
        continue
    
    # Track synergy-table wrapper
    if 'synergy-table' in stripped:
        in_synergy = True
        in_table = False
        continue
    if in_synergy and '</div>' in stripped:
        in_synergy = False
        continue
    if in_synergy:
        continue
    
    # Detect markdown table
    is_table_row = stripped.startswith('|') and stripped.endswith('|')
    is_table_separator = '|' in stripped and '-' in stripped and bool(re.match(r'^[\s\|,\-:]+$', stripped))
    
    if is_table_separator:
        if not in_table:
            table_start = i - 1
            in_table = True
            print(f"  Table start at line {i} (header at {i})")
        continue
    
    if is_table_row:
        if not in_table:
            table_start = i
            in_table = True
            print(f"  Table start at line {i+1}")
        continue
    
    if in_table:
        print(f"  Table ends at line {i+1} (start was {table_start+1})")
        plain_tables.append(table_start)
        in_table = False
        table_start = -1

if in_table:
    plain_tables.append(table_start)

print(f"\nPlain tables found: {len(plain_tables)}")
print(f"Plain table start lines (1-indexed): {[t+1 for t in plain_tables]}")
