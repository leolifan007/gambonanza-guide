"""Replace table-wrap shortcodes with raw HTML div wrappers"""
import os, glob

CONTENT_DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
OPEN_TAG = '{{< table-wrap >}}'
CLOSE_TAG = '{{< /table-wrap >}}'
HTML_OPEN = '<div class="synergy-table" style="overflow-x:auto">\n'
HTML_CLOSE = '\n</div>'

count = 0
for filepath in sorted(glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    if OPEN_TAG not in text and CLOSE_TAG not in text:
        continue
    text = text.replace(OPEN_TAG, HTML_OPEN)
    text = text.replace(CLOSE_TAG, HTML_CLOSE)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    count += 1
    print(f"  Fixed: {os.path.basename(filepath)}")

print(f"\n{count} files updated")
