"""
SOP-COMPLIANT encoding repair for all content files.
Per CONTENT-RULES.md:
- Replace em-dash/en-dash with hyphen
- Replace curly quotes with straight quotes
- Replace corrupted emoji ? with nothing (they were decorative emoji)
- Keep genuine question marks in question text
"""
import os, glob, re

CONTENT_DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
SKIP_FILES = {"_index.md"}

stats = {"dash": 0, "curly": 0, "emoji_q": 0}

def fix_file(filepath):
    global stats
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    original = text
    
    # 1. em-dash / en-dash → hyphen
    for dash in ["\u2014", "\u2013"]:
        count = text.count(dash)
        if count:
            text = text.replace(dash, "-")
            stats["dash"] += count
    
    # 2. curly quotes → straight quotes
    curly_map = {
        "\u2018": "'", "\u2019": "'",  # single
        "\u201C": '"', "\u201D": '"',  # double
    }
    for curly, straight in curly_map.items():
        count = text.count(curly)
        if count:
            text = text.replace(curly, straight)
            stats["curly"] += count
    
    # 3. Corrupted emoji ? that appear in specific patterns
    # Pattern: ? before uppercase text inside HTML (was an emoji like 🔥💥⚡♟)
    # Pattern: ? inside table cells | ?|
    # Pattern: ?? before h3 ### headers  
    # Pattern: emoji before h3 ### headers like ### ?
    
    # Fix "?WORD" patterns where ? is clearly a corrupted emoji before text
    text = re.sub(r'\?([A-Z][A-Z .!?STOP]{2,})', r'\1', text)  # ?VERDICT → VERDICT
    
    # Fix "### ??" patterns (double corrupted emoji before headings)
    text = re.sub(r'(###\s*)\?\?\s*', r'\1', text)
    
    # Fix "### ?" patterns (single corrupted emoji before headings)
    text = re.sub(r'(###\s*)\?\s*', r'\1', text)
    
    # Fix "## ?" patterns  
    text = re.sub(r'(##\s*)\?\s*', r'\1', text)
    
    # Fix "| ?|" in tables (corrupted icon in first column)
    text = re.sub(r'\|\s*\?\s*\|', r'| |', text)
    
    # Fix "| ?? **S**" patterns in tables
    text = re.sub(r'\|\s*\?\?\s+\*\*', r'| **', text)
    text = re.sub(r'\|\s*\?\s+\*\*', r'| **', text)
    
    # Fix "?. " or "? . " at line start (corrupted bullet)
    text = re.sub(r'^\s*\?\s*\.\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\?\s+', '', text, flags=re.MULTILINE)
    
    # Fix adjacent ? strips: remove all remaining orphan ? that are clearly emoji corruption
    # These are ? followed by space then text, not part of a question
    text = re.sub(r'\?\s+STOP', 'STOP', text)
    text = re.sub(r'\?\s+THE ', 'THE ', text)
    text = re.sub(r'\?\s+DO ', 'DO ', text)
    text = re.sub(r'\?\s+DON', 'DON', text)
    text = re.sub(r'\?\s+AVOID', 'AVOID', text)
    text = re.sub(r'\?\s+PROMOTION', 'PROMOTION', text)
    text = re.sub(r'\?\s+NOT', 'NOT', text)
    
    # Fix emoji in callout strong text like <strong>?STOP → <strong>STOP
    text = re.sub(r'(<strong>)\?\s*', r'\1', text)
    text = re.sub(r'(<strong>\s*)\?\s', r'\1', text)
    
    # Fix double ?? in h3 titles
    text = re.sub(r'(###\s+\d+)\?\?\s', r'\1 ', text)
    
    # Fix emoji before links: <a href="...">?Text → <a href="...">Text
    text = re.sub(r'(<a[^>]*>)\?\s*', r'\1', text)
    
    # Fix remaining ? at start of HTML tag content that were emoji
    # e.g. <h3>?Rook Rook → <h3>Rook Rook
    text = re.sub(r'(<h[1-6][^>]*>)\?\s*', r'\1', text)
    text = re.sub(r'(<span[^>]*>)\?\s*', r'\1', text)
    
    # Fix "??? CONTENTS" → "CONTENTS"
    text = re.sub(r'\?\?\?\s+', '', text)
    
    if text != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    return False

modified = 0
for filepath in sorted(glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)):
    fname = os.path.basename(filepath)
    if fname in SKIP_FILES:
        continue
    if fix_file(filepath):
        modified += 1
        print(f"  Fixed: {os.path.relpath(filepath, CONTENT_DIR)}")

print(f"\nModified: {modified} files")
print(f"Dash fixes: {stats['dash']}, Curly quote fixes: {stats['curly']}")
