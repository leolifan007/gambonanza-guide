"""Replace screenshot image refs .jpg -> .webp in all content files"""
import pathlib

content_dir = pathlib.Path("C:\\Users\\ROG\\.qclaw\\workspace-agent-d2068023\\projects\\gambonanza-guide\\content")
files = ["boss-strategy-guide.md", "recommended-seeds.md", "endgame-killer-tips.md", 
         "complete-walkthrough.md", "rook-bishop-guide.md"]

for fn in files:
    p = content_dir / fn
    text = p.read_text("utf-8")
    old_count = text.count("ss_")
    text = text.replace("ss_0.jpg", "ss_0.webp")
    text = text.replace("ss_1.jpg", "ss_1.webp")
    text = text.replace("ss_2.jpg", "ss_2.webp")
    text = text.replace("ss_3.jpg", "ss_3.webp")
    text = text.replace("ss_4.jpg", "ss_4.webp")
    text = text.replace("ss_5.jpg", "ss_5.webp")
    p.write_text(text, "utf-8")
    new_count = text.count("ss_")
    print(f"{fn}: {old_count} refs rewritten")

# Validate no .jpg refs remain in these files
for fn in files:
    text = (content_dir / fn).read_text("utf-8")
    has_jpg = "ss_" in text and ".jpg" in text
    if has_jpg:
        print(f"WARNING: {fn} still has .jpg refs!")
    
print("DONE")
