"""
Batch convert inline HTML components to Hugo shortcodes across all content files.
Safe: only modifies known patterns, leaves unknown HTML untouched.
"""
import re
import os
import glob

CONTENT_DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
SKIP_FILES = {"_index.md"}
STATS = {"scanned": 0, "modified": 0, "errors": 0}

# ── Callout: <div class='callout callout-xxx'> → {{< callout type="xxx" >}} ──
def convert_callouts(text):
    """Convert callout divs to shortcodes"""
    # Match opening: <div class='callout callout-xxx'>
    # or <div class="callout callout-xxx">
    pattern = r'<div\s+class=[\'"](callout\s+callout-(\w+))[\'"]\s*>'
    
    def replace_open(m):
        ctype = m.group(2)
        return '{{< callout type="' + ctype + '" >}}'
    
    # Close: </div> after callout content → {{< /callout >}}
    # We need to match callout divs specifically, not all </div>
    
    # Strategy: find opening callout, count div depth until matching close
    # For simplicity, assume callouts don't contain nested divs (which is true in current content)
    
    result = []
    i = 0
    while i < len(text):
        m = re.search(pattern, text[i:])
        if not m:
            result.append(text[i:])
            break
        
        # Add text before this match
        result.append(text[i:i + m.start()])
        
        # Replace opening tag
        ctype = m.group(2)
        result.append('{{< callout type="' + ctype + '" >}}')
        
        # Find the matching </div>
        start = i + m.end()
        close_idx = text.find('</div>', start)
        if close_idx == -1:
            result.append(text[start:])
            break
        
        # Get content between opening and closing div
        content = text[start:close_idx]
        # Remove leading newline/space
        content = content.lstrip('\n\r ')
        # Remove trailing newline/space
        content = content.rstrip('\n\r ')
        # Fix <br> tags → newlines
        content = content.replace('<br>', '\n')
        content = content.replace('<br/>', '\n')
        content = content.replace('<br />', '\n')
        
        result.append(content)
        result.append('{{< /callout >}}')
        
        i = close_idx + len('</div>')
    
    return ''.join(result)


# ── Pro Tip: <div class="pro-tip"> → {{< pro-tip >}} ──
def convert_protips(text):
    """Convert pro-tip divs to shortcodes"""
    result = []
    i = 0
    pattern = r'<div\s+class=[\'"]pro-tip[\'"]\s*>'
    
    while i < len(text):
        m = re.search(pattern, text[i:])
        if not m:
            result.append(text[i:])
            break
        
        result.append(text[i:i + m.start()])
        result.append('{{< pro-tip >}}')
        
        start = i + m.end()
        close_idx = text.find('</div>', start)
        if close_idx == -1:
            result.append(text[start:])
            break
        
        content = text[start:close_idx].strip()
        # Remove <strong>Only 10h+ players know:</strong><br> prefix if present
        content = re.sub(r'<strong>Only 10h\+ players know:</strong><br>\s*', '', content)
        
        result.append(content)
        result.append('{{< /pro-tip >}}')
        
        i = close_idx + len('</div>')
    
    return ''.join(result)


# ── Section divider: <hr class="section-divider"> → {{< section-divider >}} ──
def convert_section_dividers(text):
    """Convert section-divider HR to shortcode"""
    text = text.replace('<hr class="section-divider">', '{{< section-divider >}}')
    text = text.replace("<hr class='section-divider'>", '{{< section-divider >}}')
    return text


# ── Meta rating: <div class="meta-rating"> → {{< meta-rating >}} ──
def convert_meta_ratings(text):
    """Convert meta-rating divs to shortcodes"""
    result = []
    i = 0
    pattern = r'<div\s+class=[\'"]meta-rating[\'"]\s*>'
    
    while i < len(text):
        m = re.search(pattern, text[i:])
        if not m:
            result.append(text[i:])
            break
        
        result.append(text[i:i + m.start()])
        
        start = i + m.end()
        close_idx = text.find('</div>', start)
        if close_idx == -1:
            result.append(text[start:])
            break
        
        inner = text[start:close_idx]
        
        # Extract grade and label
        grade_match = re.search(r'<span\s+class=[\'"]meta-badge\s+meta-(\w+)[\'"]\s*>(.*?)</span>', inner)
        label_match = re.search(r'<span\s+class=[\'"]meta-label[\'"]\s*>(.*?)</span>', inner)
        
        if grade_match:
            grade = grade_match.group(1).upper()
            # Ensure grade is S/A/B/C
            if grade not in ('S', 'A', 'B', 'C'):
                grade = 'S' if 'S' in grade else grade[0]
            
            label = ''
            if label_match:
                label = label_match.group(1).strip()
            
            result.append('{{< meta-rating grade="' + grade + '" label="' + label.replace('"', '&quot;') + '" >}}')
        else:
            # Can't parse, keep original
            result.append(text[i:i + m.end()])
            result.append(inner)
            result.append('</div>')
        
        i = close_idx + len('</div>')
    
    return ''.join(result)


# ── Phase tags: <span class="phase-tag phase-xxx"> → {{< phase-tag "xxx" >}} ──
def convert_phase_tags(text):
    """Convert phase-tag spans to shortcodes"""
    def replace_phase(m):
        phase = m.group(1)
        # Remove trailing " GAME" from content if present
        return '{{< phase-tag "' + phase + '" >}}'
    
    text = re.sub(
        r'<span\s+class=[\'"]phase-tag\s+phase-(\w+)[\'"]\s*>\s*.*?\s*</span>',
        replace_phase,
        text
    )
    return text


# ── Chain-capture problem: some content has "???- <span id=...>" that should be "### <span id=...>" ──
def fix_bad_heading_markers(text):
    """Fix ???- formatting artifacts"""
    text = re.sub(r'###- <span', '### <span', text)
    return text


# ── Main ──
def process_file(filepath):
    relpath = os.path.relpath(filepath, CONTENT_DIR)
    fname = os.path.basename(filepath)
    
    if fname in SKIP_FILES:
        return
    
    STATS["scanned"] += 1
    
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    original = text
    
    # Apply conversions in order
    text = fix_bad_heading_markers(text)
    text = convert_section_dividers(text)
    text = convert_callouts(text)
    text = convert_protips(text)
    text = convert_meta_ratings(text)
    text = convert_phase_tags(text)
    
    if text != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        STATS["modified"] += 1
        print(f"  MODIFIED: {relpath}")
    else:
        print(f"  unchanged: {relpath}")


# Run
md_files = glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)
print(f"Scanning {len(md_files)} markdown files in {CONTENT_DIR}")
print()

for f in md_files:
    process_file(f)

print(f"\nDone. Scanned: {STATS['scanned']}, Modified: {STATS['modified']}, Errors: {STATS['errors']}")
