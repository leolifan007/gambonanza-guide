import os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'C:\Users\ROG\Documents\GitHub\gambonanza-guide'
for f in sorted(os.listdir(os.path.join(base, 'content'))):
    if not f.endswith('.md') or f == '_index.md':
        continue
    fp = os.path.join(base, 'content', f)
    with open(fp, 'r', encoding='utf-8', errors='replace') as fh:
        content = fh.read()
    lines = content.split('\n')
    title = ''
    for l in lines:
        if l.startswith('title:'):
            title = l.replace('title:', '', 1).strip().strip('"').strip("'")
            break
    print(f'{f}:  {title}')
