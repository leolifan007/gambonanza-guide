#!/usr/bin/env python3
"""
Auto-publish script: find all hidden articles with publishDate <= today,
unhide them, remove publishDate, and commit+push.
"""

import os
import re
import subprocess
from datetime import datetime, timezone, timedelta

REPO_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT_DIR = os.path.join(REPO_DIR, "content")
TZ_CN = timezone(timedelta(hours=8))
TODAY = datetime.now(TZ_CN).strftime("%Y-%m-%d")


def parse_front_matter(text):
    """Extract YAML front matter from markdown text."""
    match = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not match:
        return None, text
    return match.group(1), text[match.end():]


def unhide_article(filepath, publish_date_str):
    """Remove hidden: true and publishDate from article.
    Ensure date field exists, update lastmod.
    Returns True if article was modified."""
    from datetime import datetime
    now = datetime.now(TZ_CN)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    fm_raw, body = parse_front_matter(text)
    if fm_raw is None:
        return False

    lines = fm_raw.split('\n')
    new_lines = []
    changed = False
    has_date = False
    
    for line in lines:
        stripped = line.strip()
        
        # Check if date field already exists (in any format)
        if re.match(r'^date:\s', line):
            has_date = True
        
        # Remove hidden: true
        if re.match(r'^hidden:\s*true\s*$', line):
            changed = True
            continue
        
        # Remove publishDate
        if re.match(r'^publishDate:\s*.+$', line):
            changed = True
            continue
        
        # Remove any draft: true field
        if re.match(r'^draft:\s*true\s*$', line):
            changed = True
            continue
        
        new_lines.append(line)
    
    if not changed and has_date:
        return False
    
    # If no date field, add one using publishDate
    if not has_date:
        # Use the publish date (which we just removed) or today as fallback
        date_val = publish_date_str if publish_date_str else now.strftime("%Y-%m-%d")
        # Add after the description line, or at the top of front matter
        date_line = f'date: "{date_val}"'
        # Add lastmod as well
        lastmod_line = f'lastmod: "{now.strftime("%Y-%m-%dT%H:%M:%S+08:00")}"'
        # Insert right after the second --- (end of what will be the new front matter header)
        # Actually insert between the last existing front matter line and the body
        # We rebuild the whole front matter
        new_fm = '\n'.join(new_lines).strip()
        # Check if lastmod already exists
        has_lastmod = False
        for line in new_lines:
            if re.match(r'^lastmod:\s', line):
                has_lastmod = True
                break
        
        if not has_lastmod:
            new_fm = new_fm + '\n' + lastmod_line
        new_fm = new_fm + '\n' + date_line
    else:
        # Update lastmod if it exists, add if not
        new_fm_lines = []
        has_lastmod = False
        for line in new_lines:
            if re.match(r'^lastmod:\s', line):
                has_lastmod = True
                new_fm_lines.append(f'lastmod: "{now.strftime("%Y-%m-%dT%H:%M:%S+08:00")}"')
            else:
                new_fm_lines.append(line)
        if not has_lastmod:
            new_fm_lines.append(f'lastmod: "{now.strftime("%Y-%m-%dT%H:%M:%S+08:00")}"')
        new_fm = '\n'.join(new_fm_lines).strip()
    
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
        pub_str = m.group(1)  # The publishDate value
        if unhide_article(fpath, pub_str):
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
