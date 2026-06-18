"""Check advanced page template usage"""
import re

path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public\advanced\index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

checks = [
    ("page-hero", "page-hero" in html),
    ("content-body", "content-body" in html),
    ("main-content", "main-content" in html),
    ("site-header", "site-header" in html),
    ("sidebar", "sidebar" in html),
    ("h1", "<h1>" in html),
]
for name, ok in checks:
    print(f"  {name}: {ok}")

# Find where h1 content starts
m = re.search(r"<h1[^>]*>([^<]+)</h1>", html)
if m:
    print(f"\n  H1 content: {m.group(1)}")

# Check title
m = re.search(r"<title>(.*?)</title>", html)
if m:
    print(f"  Title: {m.group(1)}")
