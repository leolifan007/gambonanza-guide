#!/usr/bin/env python3
"""
Auto-publish script: find all hidden articles with publishDate <= today,
unhide them, remove publishDate, and commit+push.
"""

import os
import re
import subprocess
from datetime import datetime, timezone, timedelta

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(REPO_DIR, "content")
TZ_CN = timezone(timedelta(hours=8))
TODAY = datetime.now(TZ_CN).strftime("%Y-%m-%d")


def parse_front_matter(text):
    """Extract YAML front matter from markdown text."""
    match = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not match:
        return None, text
    return match.group(1), text[match.end():]


def unhide_article(filepath):
    """Remove hidden: true and publishDate from article."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    fm_raw, body = parse_front_matter(text)
    if fm_raw is None:
        return False

    lines = fm_raw.split('\n')
    new_lines = []
    changed = False
    for line in lines:
        if re.match(r'^hidden:\s*true\s*$', line):
            changed = True
            continue  # remove this line
        if re.match(r'^publishDate:\s*.+$', line):
            changed = True
            continue  # remove this line
        new_lines.append(line)

    if not changed:
        return False

    new_fm = '\n'.join(new_lines).strip()
    new_text = f"---\n{new_fm}\n---\n{body}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    return True


def main():
    now = datetime.now(TZ_CN)
    published = []

    for fname in os.listdir(CONTENT_DIR):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(CONTENT_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            text = f.read()
        fm_raw, _ = parse_front_matter(text)
        if not fm_raw:
            continue

        # Check if hidden: true
        if not re.search(r'^hidden:\s*true\s*$', fm_raw, re.MULTILINE):
            continue

        # Check publishDate
        m = re.search(r'^publishDate:\s*["\']?(\d{4}-\d{2}-\d{2})["\']?\s*$', fm_raw, re.MULTILINE)
        if not m:
            continue

        pub_date = datetime.strptime(m.group(1), "%Y-%m-%d").replace(tzinfo=TZ_CN)
        if pub_date > now:
            continue

        # Ready to publish
        print(f"[auto-publish] Publishing: {fname}")
        if unhide_article(fpath):
            published.append(fname)

    if not published:
        print("[auto-publish] No articles to publish today.")
        return

    # Git commit and push
    subprocess.run(["git", "config", "user.name", "Auto-Publish Bot"], check=True, cwd=REPO_DIR)
    subprocess.run(["git", "config", "user.email", "bot@gambonanzaguide.com"], check=True, cwd=REPO_DIR)
    subprocess.run(["git", "add", "content/"], check=True, cwd=REPO_DIR)
    msg = f"auto-publish: {', '.join(published)}"
    subprocess.run(["git", "commit", "-m", msg], check=True, cwd=REPO_DIR)
    subprocess.run(["git", "push", "origin", "content-polishing"], check=True, cwd=REPO_DIR)
    print(f"[auto-publish] Pushed {len(published)} article(s).")


if __name__ == "__main__":
    main()
