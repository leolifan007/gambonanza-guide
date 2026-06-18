import re
import sys

def resolve_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def resolve_block(match):
        theirs = match.group(1).strip()

        # Remove ? at start of table cells or start of lines
        theirs_fixed = re.sub(r'^(\| *)\?', r'\1', theirs, flags=re.MULTILINE)
        theirs_fixed = re.sub(r'^\?', '', theirs_fixed, flags=re.MULTILINE)

        return theirs_fixed + '\n'

    content = re.sub(
        r'<<<<<<< HEAD\n.*?=======\n(.*?)>>>>>>> [^\n]+\n',
        resolve_block,
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Resolved: {filepath}")

for f in sys.argv[1:]:
    resolve_file(f)
