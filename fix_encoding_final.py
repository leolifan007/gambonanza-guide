#!/usr/bin/env python3
"""
Fix encoding by properly converting from incorrect encoding to UTF-8
This script handles files that were saved with wrong encoding
"""

import os
from pathlib import Path
import chardet

def try_multiple_encodings(file_path: str) -> str:
    """Try to read file with multiple encodings and return the correct content"""
    # Read file as bytes
    with open(file_path, 'rb') as f:
        raw_bytes = f.read()
    
    # List of encodings to try
    encodings = [
        'utf-8',
        'utf-8-sig',  # UTF-8 with BOM
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
            # Check if the content looks reasonable (no replacement characters)
            if '�' not in content:
                print(f"    Successfully decoded with: {encoding}")
                return content
        except:
            continue
    
    # If all else fails, use chardet to detect encoding
    try:
        detected = chardet.detect(raw_bytes)
        if detected['encoding']:
            content = raw_bytes.decode(detected['encoding'], errors='ignore')
            print(f"    Detected encoding: {detected['encoding']}")
            return content
    except:
        pass
    
    # Last resort: decode as utf-8 with ignore errors
    content = raw_bytes.decode('utf-8', errors='ignore')
    return content

def fix_special_characters(content: str) -> str:
    """Fix common encoding issues with special characters"""
    # Replace common garbled patterns
    replacements = {
        # Em-dash and en-dash
        'â€"': '—',  # em-dash
        'â€"': '–',  # en-dash
        'â€˜': ''',  # left single quote
        'â€™': ''',  # right single quote
        'â€œ': '"',  # left double quote
        'â€': '"',  # right double quote
        
        # Unicode replacement character + ? (from previous failed conversions)
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
                # Try to read with multiple encodings
                content = try_multiple_encodings(str(file_path))
                
                # Fix special characters
                content = fix_special_characters(content)
                
                # Write back as UTF-8 without BOM
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixed_count += 1
                print(f"  ✓ Fixed")
                
            except Exception as e:
                print(f"  ✗ Error: {e}")
    
    print(f"\nFixed {fixed_count} files")
    print("\nNext steps:")
    print("1. git add -A")
    print("2. git commit -m 'Fix encoding: convert all files to proper UTF-8'")
    print("3")

if __name__ == '__main__':
    main()
