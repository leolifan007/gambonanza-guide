"""Fix: remove blank lines between pipe-rows inside synergy-table divs"""
import re, os, glob

CONTENT_DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"
pattern = re.compile(r'<div class="synergy-table"[^>]*>.*?</div>', re.DOTALL)

fixed = 0
for filepath in sorted(glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    if "synergy-table" not in text:
        continue
    
    def fix_div(m):
        content = m.group(0)
        # Remove blank lines between pipe-rows inside the div
        new_content = re.sub(
            r'(\|[^\n]*\|)\n\s*\n(?=\|)',
            r'\1\n',
            content
        )
        return new_content
    
    new_text = pattern.sub(fix_div, text)
    if new_text != text:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_text)
        fixed += 1
        print(f"  Fixed: {os.path.basename(filepath)}")

print(f"\n{fixed} files updated")
