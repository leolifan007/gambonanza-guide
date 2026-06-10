"""Check how-to-play build for em-dashes"""
import re

path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public\how-to-play\index.html"
with open(path, "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

# Find em-dashes
positions = [i for i, ch in enumerate(html) if ch == "\u2014"]
print(f"Total em-dashes: {len(positions)}")
for pos in positions[:5]:
    ctx = html[max(0,pos-50):pos+50]
    print(f"  {ctx}")

# Title tag
m = re.search(r"<title>(.*?)</title>", html)
if m:
    print(f"\nTitle: {m.group(1)}")

# og:title
m = re.search(r'og:title.*?content="(.*?)"', html)
if m:
    print(f"og:title: {m.group(1)}")
