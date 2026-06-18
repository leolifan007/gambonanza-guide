"""Final encoding sweep - fix ALL content files for dash/curly"""
import os, glob

CONTENT_DIR = os.path.join(os.environ["USERPROFILE"], ".qclaw", "workspace-x74fgmx0vyb8p5is", "gambonanza-guide", "content")

dash_chars = "\u2014\u2013"
curly_chars = "\u2018\u2019\u201C\u201D"
dash_repl = "-"
curly_single = "'"
curly_double = '"'

fixed_files = 0
total_dash = 0
total_curly = 0

for filepath in sorted(glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    changed = False
    
    # Fix dashes
    for ch in dash_chars:
        cnt = text.count(ch)
        if cnt:
            text = text.replace(ch, dash_repl)
            total_dash += cnt
            changed = True
    
    # Fix curly quotes
    for ch in curly_chars:
        cnt = text.count(ch)
        if cnt:
            repl = curly_single if ch in "\u2018\u2019" else curly_double
            text = text.replace(ch, repl)
            total_curly += cnt
            changed = True
    
    if changed:
        fixed_files += 1
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)

print(f"Fixed: {fixed_files} files, {total_dash} dashes, {total_curly} curly quotes")
