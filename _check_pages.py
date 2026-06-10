import os

files = [
    r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public\cheats-hidden-mechanics\index.html",
    r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public\meta-report\index.html",
    r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public\difficulty-guide\index.html",
    r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public\comeback-zero-stock\index.html",
]
for f in files:
    e = os.path.exists(f)
    sz = os.path.getsize(f) if e else 0
    print(f"{'OK' if e else 'MISSING'} {os.path.basename(os.path.dirname(f))}: {sz} bytes")
