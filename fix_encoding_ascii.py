#!/usr/bin/env python3
"""
Fix encoding - ASCII output version
"""

import os
from pathlib import Path
import chardet

def try_multiple_encodings(file_path: str) -> str:
    """Try to read file with multiple encodings"""
    with open(file_path, 'rb') as f:
        raw_bytes = f.read()
    
    encodings = [
        'utf-8',
        'utf-8-sig',
        'gbk',
        'gb2312',
        'gb18030',
        'windows-1252',
        'iso-8859-1',
        'cp1252',
        'latin-1'
    ]
    
    for encoding in encodings:
        try:
            content = raw_bytes.decode(encoding)
            if '�' not in content:
                print(f"    Decoded with: {encoding}")
                return content
        except:
            continue
    
    # Use chardet as fallback
    try:
        detected = chardet.detect(raw_bytes)
        if detected['encoding']:
            content = raw_bytes.decode(detected['encoding'], errors='ignore')
            print(f"    Detected encoding: {detected['encoding']}")
            return content
    except:
        pass
    
    # Last resort
    content = raw_bytes.decode('utf-8', errors='ignore')
    return content

def fix_special_characters(content: str) -> str:
    """Fix common encoding issues"""
    replacements = {
        # UTF-8 encoded em-dash/oct-dash interpreted as Windows-1252
        'â€"': '—',  # em-dash
        'â€"': '–',  # en-dash
        'â€˜': ''',  # left single quote
        'â€™': ''',  # right single quote
        'â€œ': '"',  # left double quote
        'â€': '"',  # right double quote
        
        # Garbled patterns from previous failed conversions
        '�?': '—',
        '�?': '–',
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    return content

def main():
    print("Starting encoding fix...")
    
    base_dir = Path('.')
    extensions = ['.md', '.html', '.toml', '.yaml', '.yml', '.css', '.js']
    
    fixed_count = 0
    
    for ext in extensions:
        for file_path in base_dir.rglob(f'*{ext}'):
            if '.git' in file_path.parts:
                continue
            
            print(f"Processing: {file_path}")
            
            try:
                content = try_multiple_encodings(str(file_path))
                content = fix_special_characters(content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixed_count += 1
                print("  [OK] Fixed")
                
            except Exception as e:
                print(f"  [ERROR] {e}")
    
    print(f"\nFixed {fixed_count} files")
    print("\nNext steps:")
    print("1. git add -A")
    print("2. git commit -m 'Fix encoding: convert all files to proper UTF-8'")
    print("3. git push")

if __name__ == '__main__':
    main()
