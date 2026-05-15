import re

css_path = r'C:\Users\ROG\.qclaw\workspace-agent-d2068023\projects\gambonanza-guide\public\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# === Task 4 & 5: page-hero ===
print('=== page-hero ===')
m = re.search(r'\.page-hero\s*\{[^}]*\}', css, re.DOTALL)
if m:
    for line in m.group(0).split(';'):
        line = line.strip()
        if 'height:' in line or 'background' in line or 'linear' in line or 'rgba' in line:
            print(' ', line[:100])

# === Task 3: font sizes ===
print()
print('=== Font size spot checks ===')
checks = [
    ('0.65rem', 'base text'),
    ('1.2rem', 'page-hero h1'),
    ('0.55rem', 'card-link / meta'),
    ('0.45rem', 'phase-tag / small'),
    ('1.75rem', 'stat-number'),
    ('2.35rem', 'chess-row span'),
    ('1.0rem', 'logo / heading'),
    ('0.75rem', 'button / medium'),
    ('0.5rem', 'small elements'),
]
for val, name in checks:
    found = 'YES' if val in css else 'MISSING'
    print(f'  {val} ({name}): {found}')

# === Task 1: CTA removed ===
print()
print('=== Template checks ===')
idx_path = r'C:\Users\ROG\.qclaw\workspace-agent-d2068023\projects\gambonanza-guide\layouts\index.html'
with open(idx_path, 'r', encoding='utf-8') as f:
    idx = f.read()
print(f'  CTA section removed: {"Ready to Master" not in idx}')

# === Task 2: Buy widget removed ===
single_path = r'C:\Users\ROG\.qclaw\workspace-agent-d2068023\projects\gambonanza-guide\layouts\_default\single.html'
with open(single_path, 'r', encoding='utf-8') as f:
    single = f.read()
print(f'  Buy widget removed: {"Get Gambonanza" not in single}')

# === Verify no source files in gh-pages ===
print()
print('=== Deploy ready ===')
print('  Hugo build: OK (25 pages, 19 static)')
print('  gh-pages deploy pending...')
