#!/usr/bin/env python3
"""
Comprehensive Encoding Fix for Gambonanza Guide
- Converts all text files to UTF-8 without BOM
- Fixes garbled special characters
- Adds proper Hugo configuration
- Creates .gitattributes and pre-commit hook
"""

import os
import sys
from pathlib import Path
import chardet

def detect_encoding(file_path: str) -> str:
    """Detect file encoding using chardet"""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    
    # Check for BOM first
    if raw_data.startswith(b'\xef\xbb\xbf'):
        return 'utf-8-sig'
    elif raw_data.startswith(b'\xff\xfe'):
        return 'utf-16-le'
    elif raw_data.startswith(b'\xfe\xff'):
        return 'utf-16-be'
    
    # Use chardet for detection
    result = chardet.detect(raw_data)
    encoding = result['encoding'] if result['confidence'] > 0.7 else 'utf-8'
    
    # Map common encodings
    encoding_map = {
        'ascii': 'utf-8',
        'windows-1252': 'windows-1252',
        'windows-1251': 'windows-1251',
        'gb2312': 'gbk',
        'gbk': 'gbk',
        'gb18030': 'gb18030',
        'iso-8859-1': 'iso-8859-1',
        'iso-8859-2': 'iso-8859-2',
        'utf-8': 'utf-8',
    }
    
    return encoding_map.get(encoding.lower(), 'utf-8')

def fix_garbled_chars(text: str) -> str:
    """Fix common garbled character patterns"""
    # Patterns caused by encoding mismatch (UTF-8 bytes interpreted as Windows-1252 or vice versa)
    replacements = {
        # Em-dash and en-dash (UTF-8 -> Windows-1252 misinterpretation)
        '\u2013': '–',  # en-dash
        '\u2014': '—',  # em-dash
        
        # Curly quotes
        '\u2018': ''',  # left single quote
        '\u2019': ''',  # right single quote
        '\u201c': '"',  # left double quote
        '\u201d': '"',  # right double quote
        
        # Common Windows-1252 to UTF-8 issues
        'â€"': '—',  # em-dash
        'â€"': '–',  # en-dash
        'â€˜': ''',  # left single quote
        'â€™': ''',  # right single quote
        'â€œ': '"',  # left double quote
        'â€': '"',  # right double quote
        
        # Unicode replacement character patterns
        '�?': '—',
        '�?': '–',
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

def convert_file(file_path: str) -> bool:
    """Convert a single file to UTF-8 without BOM"""
    try:
        # Detect encoding
        encoding = detect_encoding(file_path)
        
        # Read file with detected encoding
        with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
            content = f.read()
        
        # Fix garbled characters
        content = fix_garbled_chars(content)
        
        # Write back as UTF-8 without BOM
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"  [ERROR] {file_path}: {e}", file=sys.stderr)
        return False

def fix_hugo_config():
    """Add encoding settings to hugo.toml"""
    config_path = Path('hugo.toml')
    if not config_path.exists():
        print("[INFO] hugo.toml not found, skipping config update")
        return
    
    content = config_path.read_text(encoding='utf-8')
    
    if 'hasCJKLanguage' not in content:
        # Add encoding settings at the beginning
        encoding_config = '\n# Encoding settings\nhasCJKLanguage = true\n\n'
        content = encoding_config + content
        config_path.write_text(content, encoding='utf-8')
        print("[OK] Added hasCJKLanguage to hugo.toml")
    else:
        print("[INFO] hasCJKLanguage already present in hugo.toml")

def create_gitattributes():
    """Create .gitattributes to enforce UTF-8"""
    content = """# Enforce UTF-8 encoding for text files
* text=auto charset=utf-8

# Markdown files
*.md text charset=utf-8

# HTML files
*.html text charset=utf-8

# Configuration files
*.toml text charset=utf-8
*.yaml text charset=utf-8
*.yml text charset=utf-8

# CSS and JavaScript
*.css text charset=utf-8
*.js text charset=utf-8
"""
    
    with open('.gitattributes', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("[OK] Created .gitattributes")

def create_precommit_hook():
    """Create pre-commit hook to prevent encoding issues"""
    hook_dir = Path('.git/hooks')
    if not hook_dir.exists():
        hook_dir.mkdir(parents=True)
    
    hook_path = hook_dir / 'pre-commit'
    
    content = """#!/bin/sh
# Pre-commit hook to check for encoding issues

echo "Checking file encoding..."

# Check for non-UTF-8 files (if 'file' command is available)
if command -v file >//dev/null 2>&1; then
    for file in $(git diff --cached --name-only --diff-filter=ACM | grep -E '\\.(md|html|toml|yaml|yml|css|js)$'); do
        if [ -f "$file" ]; then
            encoding=$(file -b --mime-encoding "$file" 2>/dev/null)
            if [ $? -eq 0 ] && ! echo "$encoding" | grep -q "utf-8"; then
                echo "ERROR: $file is not UTF-8 encoded (detected: $encoding)"
                echo "Please convert it to UTF-8 without BOM"
                exit 1
            fi
        fi
    done
else
    echo "WARNING: 'file' command not found, skipping encoding check"
fi

echo "Encoding check passed"
exit 0
"""
    
    with open(hook_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Make executable on Unix-like systems
    try:
        hook_path.chmod(0o755)
    except:
        pass
    
    print("[OK] Created pre-commit hook")

def main():
    print("=== Gambonanza Guide Encoding Fix ===")
    print()
    
    # Get all text files
    extensions = ['.md', '.html', '.toml', '.yaml', '.yml', '.css', '.js']
    base_dir = Path('.')
    
    files_to_process = []
    for ext in extensions:
        files_to_process.extend(base_dir.rglob(f'*{ext}'))
    
    # Filter out .git directory
    files_to_process = [f for f in files_to_process if '.git' not in f.parts]
    
    print(f"Found {len(files_to_process)} files to process")
    print()
    
    # Process files
    success_count = 0
    error_count = 0
    
    for file_path in files_to_process:
        print(f"Processing: {file_path}")
        if convert_file(str(file_path)):
            success_count += 1
        else:
            error_count += 1
    
    print()
    print(f"=== Results ===")
    print(f"Successfully processed: {success_count}")
    print(f"Errors: {error_count}")
    print()
    
    # Fix Hugo config
    print("Fixing Hugo configuration...")
    fix_hugo_config()
    print()
    
    # Create .gitattributes
    print("Creating .gitattributes...")
    create_gitattributes()
    print()
    
    # Create pre-commit hook
    print("Creating pre-commit hook...")
    create_precommit_hook()
    print()
    
    print("=== Next Steps ===")
    print("1. Review the changes: git diff")
    print("2. Stage all changes: git add -A")
    print("3. Commit: git commit -m 'Fix encoding: convert all files to UTF-8 without BOM'")
    print("4. Push: git push")
    print("5. Check the live site to verify the fix")

if __name__ == '__main__':
    main()
