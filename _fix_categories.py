# -*- coding: utf-8 -*-
"""Convert singular `category: X` front matter to plural `categories: [X]`.

Handles both `---category: "X"` (same line) and standard `category: "X"` line
formats. Front matter only. Writes UTF-8 without BOM.
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def clean(v):
    v = v.strip()
    if v.startswith('"') and v.endswith('"') and len(v) >= 2:
        v = v[1:-1]
    elif v.startswith("'") and v.endswith("'") and len(v) >= 2:
        v = v[1:-1]
    return v.strip()

def front_matter_region(text):
    """Return (start, end) of front matter if file starts with ---, else None."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        end = len(text)
    return (0, end)

def main():
    changed = 0
    for fname in sorted(os.listdir(CONTENT_DIR)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(CONTENT_DIR, fname)
        with open(path, "r", encoding="utf-8-sig") as f:
            text = f.read()
        if text.startswith("\ufeff"):
            text = text[1:]
        region = front_matter_region(text)
        if region is None:
            print("SKIP (no front matter): %s" % fname)
            continue
        start, end = region
        fm = text[start:end]
        new_fm = fm

        # format 1: `---category: "X"` on the same line as the opening marker
        def rep1(m):
            return '---\ncategories: ["%s"]' % clean(m.group(1))

        new_fm2 = re.sub(r"(?m)^---category:\s*(.+?)\s*$", rep1, new_fm, count=1)

        # format 2: standalone `category: "X"` line
        def rep2(m):
            return 'categories: ["%s"]' % clean(m.group(1))

        new_fm2 = re.sub(r"(?m)^category:\s*(.+?)\s*$", rep2, new_fm2, count=1)

        if new_fm2 == fm:
            print("NOCHANGE: %s" % fname)
            continue
        text = text[:start] + new_fm2 + text[end:]
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("OK: %s" % fname)
        changed += 1
    print("done: %d changed" % changed)

if __name__ == "__main__":
    main()
