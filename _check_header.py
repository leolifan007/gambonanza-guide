import pathlib
cwd = pathlib.Path('C:/Users/ROG/.qclaw/workspace-agent-d2068023/projects/gambonanza-guide')
h = cwd / 'layouts' / 'partials' / 'header.html'
print(f'Exists: {h.exists()}')
if h.exists():
    content = h.read_bytes()
    print(f'Size: {len(content)} bytes')
    print(f'Has Press Start: {"Press Start" in content.decode("utf-8")}')
    print(f'Has googleapis: {"googleapis" in content.decode("utf-8")}')
else:
    # Check alternative locations
    for p in cwd.rglob('header.html'):
        print(f'Found at: {p.relative_to(cwd)}')
