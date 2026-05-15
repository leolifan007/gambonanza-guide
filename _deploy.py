import subprocess, os

def deploy():
    BASE = r'C:\Users\ROG\.qclaw\workspace-agent-d2068023\projects\gambonanza-guide'
    os.chdir(BASE)

    # 1. Verify public/ exists and has index.html
    if not os.path.exists(os.path.join(BASE, 'public', 'index.html')):
        print('ERROR: public/index.html not found! Run hugo first.')
        return False

    # 2. Git add public/
    subprocess.run(['git', 'add', 'public/'], check=True)

    # 3. Create tree from public/
    r = subprocess.run(['git', 'write-tree', '--prefix=public'], capture_output=True, text=True, check=True)
    tree = r.stdout.strip()
    print('Tree:', tree[:8])

    # 4. Create commit
    r = subprocess.run(['git', 'commit-tree', tree, '-m', 'deploy: gh-pages update'], capture_output=True, text=True, check=True)
    commit = r.stdout.strip()
    print('Commit:', commit[:8])

    # 5. Branch and push — NO delete step! Atomic force push only
    subprocess.run(['git', 'branch', '-f', 'gh-pages', commit], check=True)
    r = subprocess.run(['git', 'push', 'origin', 'gh-pages', '--force'], capture_output=True, text=True)
    for line in r.stdout.splitlines():
        print(' ', line)
    print('Deploy OK')
    return True

if __name__ == '__main__':
    deploy()
