"""Check Hugo page count for the site"""
import os, re, glob

root = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public"
pages = []
for item in os.listdir(root):
    path = os.path.join(root, item, "index.html")
    if os.path.exists(path) and item not in ("page", "tags", "categories"):
        pages.append(item)

print(f"Built pages: {len(pages)}")
for p in sorted(pages):
    print(f"  {p}")
