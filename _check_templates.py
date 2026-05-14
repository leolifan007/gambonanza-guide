import pathlib
cwd = pathlib.Path('C:/Users/ROG/.qclaw/workspace-agent-d2068023/projects/gambonanza-guide')
for fname in ['baseof.html', 'index.html', 'header.html', 'footer.html']:
    for p in cwd.rglob(fname):
        content = p.read_bytes()
        has_font = b'Press Start' in content or b'Press+Start' in content
        has_hero = b'hero-bg' in content
        print(f'{p.relative_to(cwd)}: fonts={has_font}, hero={has_hero}, size={len(content)}')
