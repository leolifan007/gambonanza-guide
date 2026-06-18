"""Fixed table wrapper - handles all frontmatter formats"""
import re, os, glob

CONTENT_DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
SKIP_FILES = {"_index.md"}
STATS = {"scanned": 0, "wrapped": 0, "errors": 0}

def find_plain_tables(text):
    lines = text.split("\n")
    plain_tables = []
    in_synergy = False
    in_frontmatter = False
    if len(lines) > 0 and lines[0].strip().startswith("---"):
        in_frontmatter = True
    in_table = False
    table_start = -1

    for i, line in enumerate(lines):
        stripped = line.strip()
        if in_frontmatter and stripped == "---":
            in_frontmatter = False
            continue
        if in_frontmatter:
            continue
        if "synergy-table" in stripped:
            in_synergy = True
            in_table = False
            continue
        if in_synergy and "</div>" in stripped:
            in_synergy = False
            continue
        if in_synergy:
            continue

        is_table_row = stripped.startswith("|") and stripped.endswith("|")
        is_table_sep = "|" in stripped and "-" in stripped and bool(re.match(r'^[\s\|,\-:]+$', stripped))

        if is_table_sep:
            if not in_table:
                table_start = i - 1
                in_table = True
            continue

        if is_table_row:
            if not in_table:
                table_start = i
                in_table = True
            continue

        if in_table:
            plain_tables.append(table_start)
            in_table = False
            table_start = -1

    if in_table:
        plain_tables.append(table_start)
    return plain_tables

def wrap_table(lines, table_start_idx):
    end_idx = table_start_idx
    while end_idx < len(lines):
        s = lines[end_idx].strip()
        is_table = s.startswith("|") and (s.endswith("|") or bool(re.match(r'^[\s\|,\-:]+$', s)))
        if not is_table and end_idx > table_start_idx:
            break
        end_idx += 1
    if table_start_idx > 0 and "table-wrap" in lines[table_start_idx - 1]:
        return None
    new_lines = lines[:table_start_idx]
    new_lines.append("{{% table-wrap %}}")
    new_lines.extend(lines[table_start_idx:end_idx])
    new_lines.append("{{% /table-wrap %}}")
    new_lines.extend(lines[end_idx:])
    return new_lines

for filepath in sorted(glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)):
    fname = os.path.basename(filepath)
    if fname in SKIP_FILES:
        continue
    STATS["scanned"] += 1
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    plain_tables = find_plain_tables(text)
    if not plain_tables:
        continue
    modified = False
    for start in reversed(sorted(set(plain_tables))):
        result = wrap_table(lines, start)
        if result:
            lines = result
            modified = True
            STATS["wrapped"] += 1
            rel = os.path.relpath(filepath, CONTENT_DIR)
            print(f"  wrapped: {rel} line {start+1}")
    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

print(f"\nScanned: {STATS['scanned']}, Wrapped: {STATS['wrapped']}, Errors: {STATS['errors']}")
