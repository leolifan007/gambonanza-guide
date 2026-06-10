import os, sys
sys.stdout.reconfigure(encoding='utf-8')
print("hello")
x = os.listdir(r'C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content')
print(f"Found {len(x)} files")
print(x[:3])
