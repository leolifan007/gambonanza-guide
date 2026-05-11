"""Deploy public/ to gh-pages branch"""
import subprocess, pathlib, shutil

repo = pathlib.Path("C:\\Users\\ROG\\.qclaw\\workspace-agent-d2068023\\projects\\gambonanza-guide")
public = repo / "public"

assert public.is_dir(), "public dir missing"

def git(args, silent=False):
    r = subprocess.run(["git"] + args, cwd=repo, capture_output=True, text=True, timeout=30)
    if not silent:
        for line in (r.stdout + r.stderr).splitlines():
            print(line)
    return r

git(["fetch", "origin"])
r = git(["rev-parse", "--verify", "gh-pages"], silent=True)
if r.returncode == 0:
    git(["branch", "-D", "gh-pages"])

git(["checkout", "--orphan", "gh-pages"])
git(["rm", "-rf", "."], silent=True)

for item in public.iterdir():
    dest = repo / item.name
    if item.is_dir():
        shutil.copytree(item, dest, dirs_exist_ok=True)
    else:
        shutil.copy2(item, dest)

(repo / "CNAME").write_text("gambonanzaguide.com", "ascii")

git(["add", "-A"])
git(["commit", "-m", "Deploy v1.3.0: English rewrite, webp images, nav entries"])
git(["push", "origin", "HEAD:gh-pages", "--force"])
git(["checkout", "main"])

print("\n=== DEPLOYED v1.3.0 ===")
