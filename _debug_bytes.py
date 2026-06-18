"""Debug: find em-dash bytes in built file"""
import re

path = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public\advanced\index.html"
with open(path, "rb") as f:
    data = f.read()

# Search for the bytes E2 80 94 (UTF-8 encoding of U+2014 em-dash)
target = b"\xe2\x80\x94"
idx = data.find(target)
if idx >= 0:
    start = max(0, idx - 20)
    end = min(len(data), idx + 40)
    context_bytes = data[start:end]
    print(f"Found at byte offset {idx}")
    print(f"Hex: {context_bytes.hex(' ')}")
    print(f"Text: {context_bytes.decode('utf-8', errors='replace')}")
    
    # Also check what's in the config/site params
    with open(r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\hugo.toml", "rb") as f:
        cfg = f.read()
    idx2 = cfg.find(target)
    if idx2 >= 0:
        print(f"\nAlso found in hugo.toml at byte {idx2}")
        print(f"In config: {cfg[idx2-20:idx2+40].decode('utf-8', errors='replace')}")
    else:
        print("\nNot in hugo.toml")
else:
    print("No em-dash found in built file!")
