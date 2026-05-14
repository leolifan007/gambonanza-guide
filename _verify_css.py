c = open('C:/Users/ROG/.qclaw/workspace-agent-d2068023/projects/gambonanza-guide/themes/gambonanza-theme/static/css/style.css', encoding='utf-8').read()
checks = [
    ('Press Start 2P font var', 'Press Start 2P' in c),
    ('hero-bg in page-hero', 'hero-bg.webp' in c),
    ('page-hero min-height 45vh', '45vh' in c),
    ('guide-card gradient bg 1a0f1a', '26,15,26' in c),
    ('guide-card full click area', '.guide-card a {' in c and 'absolute' in c),
    ('card-title gold border', 'border-left: 4px solid var(--gold)' in c),
    ('guide-card hover translateY(-4px)', 'translateY(-4px)' in c),
    ('h1 pixel size 1.8rem', '1.8rem' in c),
]
all_ok = True
for name, status in checks:
    marker = 'OK' if status else 'MISSING'
    if not status:
        all_ok = False
    print(f'[{marker}] {name}')
print(f'All checks: {"PASS" if all_ok else "FAIL"}')
