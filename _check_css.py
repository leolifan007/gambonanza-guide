import pathlib
c = pathlib.Path('themes/gambonanza-theme/static/css/style.css').read_text(encoding='utf-8')
checks = {
    'font Press Start 2P': 'Press Start 2P',
    'hero-bg in page-hero': 'hero-bg.webp',
    'card gradient 1a0f1a': '1a0f1a',
    'card-link-overlay': 'card-link-overlay',
    'h1 size 1.8rem': '1.8rem',
}
for k, v in checks.items():
    print(f'{k}: {"YES" if v in c else "NO"}')
print(f'Size: {len(c)} bytes')
print(f'First 50 chars: {c[:50]}')
