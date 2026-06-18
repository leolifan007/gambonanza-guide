import os, glob

for f in sorted(glob.glob('content/*.md')):
    with open(f, 'r', encoding='utf-8', errors='replace') as fh:
        content = fh.read()
    lines = content.split('\n')
    title = ''
    for l in lines:
        if l.startswith('title:'):
            title = l.replace('title:', '', 1).strip().strip('"').strip("'")
            break
    name = os.path.basename(f)
    if name != '_index.md':
        print(f'  {name}: "{title}"')
