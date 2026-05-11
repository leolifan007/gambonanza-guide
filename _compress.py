"""Compress all ss_*.jpg to WebP 80% quality"""
import pathlib
from PIL import Image

src = pathlib.Path("C:\\Users\\ROG\\.qclaw\\workspace-agent-d2068023\\projects\\gambonanza-guide\\static\\images\\screenshots")
for f in sorted(src.glob("ss_*.jpg")):
    img = Image.open(f).convert("RGB")
    out = src / f"{f.stem}.webp"
    img.save(out, "WEBP", quality=80)
    orig_kb = f.stat().st_size // 1024
    new_kb = out.stat().st_size // 1024
    print(f"{f.name}: {orig_kb}KB -> {new_kb}KB ({new_kb/orig_kb*100:.0f}%)")
print("DONE")
