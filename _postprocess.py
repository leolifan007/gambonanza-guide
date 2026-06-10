"""Post-process: strip em-dash/en-dash/curly quotes from all built files"""
import os, glob

ROOT = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public"
dash_fixes = 0
curly_fixes = 0
file_fixes = 0

dash_chars = "\u2014\u2013"
single_curly = "\u2018\u2019"
double_curly = "\u201C\u201D"

for dirpath, dirs, files in os.walk(ROOT):
    for fname in files:
        if not (fname.endswith(".html") or fname.endswith(".xml") or fname.endswith(".css")):
            continue
        path = os.path.join(dirpath, fname)
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
        except:
            continue
        
        changed = False
        
        # Dash fixes
        for ch in dash_chars:
            if ch in text:
                text = text.replace(ch, "-")
                dash_fixes += 1
                changed = True
        
        # Curly quote fixes
        for ch in single_curly:
            if ch in text:
                text = text.replace(ch, "'")
                curly_fixes += 1
                changed = True
        for ch in double_curly:
            if ch in text:
                text = text.replace(ch, '"')
                curly_fixes += 1
                changed = True
        
        if changed:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            file_fixes += 1

print(f"Files fixed: {file_fixes}")
print(f"Dash/em-dash fixes: {dash_fixes}")
print(f"Curly quote fixes: {curly_fixes}")
