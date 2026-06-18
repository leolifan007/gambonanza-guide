"""SOP QA: Full encoding audit per CONTENT-RULES.md"""
import os, glob, re

CONTENT_DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
SKIP_FILES = {"_index.md"}

# SOP violations
# 1. em-dash (U+2014) → forbidden
# 2. en-dash (U+2013) → forbidden
# 3. curly quotes (U+2018/U+2019/U+201C/U+201D) → forbidden
# 4. ? in HTML context → encoding corruption (should not appear inside tags)
# 5. emoji in content → should use text description instead

re_em_dash = re.compile(r'\u2014')
re_en_dash = re.compile(r'\u2013')
re_curly_single = re.compile(r'[\u2018\u2019]')
re_curly_double = re.compile(r'[\u201C\u201D]')
re_html_q = re.compile(r'>[^<]*\?[^<]*<')  # ? inside HTML tags

results = []

for filepath in sorted(glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)):
    fname = os.path.basename(filepath)
    if fname in SKIP_FILES:
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    violations = []
    for i, line in enumerate(lines, 1):
        stripped = line.rstrip()
        # Skip frontmatter
        if i == 1 and stripped.startswith("---"):
            continue
        if stripped == "---" and any(l.startswith("---") for l in lines[:i]):
            continue  # rough frontmatter end detection
        
        checks = [
            ("em-dash", re_em_dash),
            ("en-dash", re_en_dash),
            ("curly single quote", re_curly_single),
            ("curly double quote", re_curly_double),
        ]
        
        for name, pattern in checks:
            for m in pattern.finditer(stripped):
                ctx_start = max(0, m.start() - 20)
                ctx_end = min(len(stripped), m.end() + 20)
                ctx = stripped[ctx_start:ctx_end]
                violations.append(f"  L{i} [{name}]: ...{ctx}...")
        
        # Check for ? in content (not in URLs/scripts)
        if '?' in stripped and not stripped.strip().startswith('<script'):
            # Check if ? is inside HTML or in markdown content
            # Ignore URLs with query params
            if '?/' not in stripped:  # Not a URL path
                for m in re.finditer(r'\?', stripped):
                    ctx_start = max(0, m.start() - 20)
                    ctx_end = min(len(stripped), m.end() + 20)
                    ctx = stripped[ctx_start:ctx_end]
                    violations.append(f"  L{i} [? char]: ...{ctx}...")
    
    if violations:
        print(f"\n{os.path.relpath(filepath, CONTENT_DIR)}:")
        for v in violations:
            print(v)

print("\n=== Full scan complete ===")
