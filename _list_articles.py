import os, re
content_dir = 'content'
for f in sorted(os.listdir(content_dir)):
    if not f.endswith('.md') or f == '_index.md':
        continue
    fp = os.path.join(content_dir, f)
    with open(fp, 'r', encoding='utf-8') as fh:
        content = fh.read()
    match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        fm = match.group(1)
        title = ''
        date = ''
        category = ''
        for line in fm.split('\n'):
            if line.startswith('title:'):
                title = line.split(':',1)[1].strip().strip('"')
            elif line.startswith('date:'):
                date = line.split(':',1)[1].strip().strip('"')
            elif line.startswith('category:'):
                category = line.split(':',1)[1].strip().strip('"')
        print(f'{f:40s} | date={date:25s} | cat={category}')
