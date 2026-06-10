"""Compare title rendering between pages"""
import re

pages = [
    (r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public\how-to-play\index.html", "how-to-play"),
    (r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public\advanced\index.html", "advanced"),
]

for path, name in pages:
    with open(path, "rb") as f:
        data = f.read()
    
    hex_d = data.hex()
    has_dash = "e28094" in hex_d
    text = data.decode("utf-8", errors="replace")
    m = re.search(r"<title>(.*?)</title>", text)
    title = m.group(1) if m else "NOT FOUND"
    
    # Check Source Template
    tmpl = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\layouts\_default\baseof.html"
    with open(tmpl, "rb") as f:
        tmpl_data = f.read()
    tmpl_has_em = b"\xe2\x80\x94" in tmpl_data
    
    print(f"{name}:")
    print(f"  Has em-dash: {has_dash}")
    print(f"  Title: {title}")
    print()
