"""
Find all .md files with markdown tables that aren't wrapped in synergy-table div.
Convert them to use {{% table-wrap %}} shortcode.
"""
import re
import os
import glob

CONTENT_DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
SKIP_FILES = {"_index.md"}
STATS = {"scanned": 0, "wrapped": 0, "already_wrapped": 0, "errors": 0}

def find_plain_tables(text):
    """Find markdown tables that are not inside a synergy-table wrapper."""
    lines = text.split('\n')
    plain_tables = []
    in_synergy = False
    in_frontmatter = False
    in_table = False
    table_start = -1
    
    for i, line in enumerate(lines):
        # Track frontmatter
        if line.strip() == '---' and not in_frontmatter and i < 20:
            in_frontmatter = True
            continue
        if line.strip() == '---' and in_frontmatter:
            in_frontmatter = False
            continue
        if in_frontmatter:
            continue
        
        # Track synergy-table wrapper
        if 'synergy-table' in line:
            in_synergy = True
            in_table = False
            continue
        if in_synergy and '</div>' in line:
            in_synergy = False
            continue
        
        if in_synergy:
            continue
        
        # Detect markdown table: line starts with | and has ----
        stripped = line.strip()
        is_table_row = stripped.startswith('|') and stripped.endswith('|')
        is_table_separator = '|' in stripped and '-' in stripped and re.match(r'^[\s\|,\-:]+$', stripped)
        
        if is_table_separator:
            # This is likely a table separator row
            if not in_table:
                table_start = i - 1  # Previous line was the header
                in_table = True
            continue
        
        if is_table_row:
            if not in_table:
                table_start = i
                in_table = True
            continue
        
        # If we were in a table and hit a non-table line
        if in_table:
            plain_tables.append(table_start)
            in_table = False
            table_start = -1
    
    # Handle table at end of file
    if in_table:
        plain_tables.append(table_start)
    
    return plain_tables


def wrap_table(text, table_start_idx, lines):
    """Wrap a markdown table in {{% table-wrap %}}."""
    # Find the table end
    end_idx = table_start_idx
    while end_idx < len(lines):
        stripped = lines[end_idx].strip()
        is_table = stripped.startswith('|') and (stripped.endswith('|') or re.match(r'^[\s\|,\-:]+$', stripped))
        if not is_table and end_idx > table_start_idx:
            break
        end_idx += 1
    
    # Check if there's a blank line separator needed
    # Add table-wrap before table start
    table_lines = lines[table_start_idx:end_idx]
    
    # Check if already wrapped (should not happen but safety check)
    if table_start_idx > 0 and 'table-wrap' in lines[table_start_idx - 1]:
        return None  # Already wrapped
    
    # Build new lines
    new_lines = lines[:table_start_idx]
    new_lines.append('{{% table-wrap %}}')
    new_lines.extend(table_lines)
    new_lines.append('{{% /table-wrap %}}')
    new_lines.extend(lines[end_idx:])
    
    return new_lines


# Main
md_files = sorted(glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True))
print(f"Scanning {len(md_files)} markdown files for plain tables...\n")

for filepath in md_files:
    fname = os.path.basename(filepath)
    if fname in SKIP_FILES:
        continue
    
    relpath = os.path.relpath(filepath, CONTENT_DIR)
    STATS["scanned"] += 1
    
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    plain_tables = find_plain_tables(text)
    
    if not plain_tables:
        continue
    
    # Process tables from end to start to preserve indices
    modified = False
    for start in reversed(plain_tables):
        result = wrap_table(text, start, lines)
        if result:
            lines = result
            modified = True
            STATS["wrapped"] += 1
            print(f"  wrapped table at line {start+1}: {relpath}")
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    else:
        STATS["already_wrapped"] += 1

print(f"\nDone. Scanned: {STATS['scanned']}, Tables wrapped: {STATS['wrapped']}, Already wrapped: {STATS['already_wrapped']}, Errors: {STATS['errors']}")
