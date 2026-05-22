#!/usr/bin/env python3
"""
Encoding Fix Script for Gambonanza Guide - Simplified Version
Converts all text files to UTF-8 without BOM and fixes garbled characters
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

def detect_bom(file_path: str) -> Tuple[str, int]:
    """Detect BOM and return encoding and BOM length"""
    with open(file_path, 'rb') as f:
        raw = f.read(4)
    
    # Check for BOMs
    if raw.startswith(b'\xef\xbb\xbf'):
        return 'utf-8-sig', 3
    elif raw.startswith(b'\xff\xfe'):
        return 'utf-16-le', 2
    elif raw.startswith(b'\xfe\xff'):
        return 'utf-16-be', 2
    else:
        return 'utf-8', 0

def fix_emoji_garbage(text: str) -> str:
    """Fix garbled emoji characters caused by encoding issues"""
    # Common emoji replacements based on context in header.html
    replacements = {
        # Logo icon (likely a game die or chess piece)
        '鈾?': '🎲',
        
        # Navigation emojis
        '馃弳': '🏆',  # Trophy for Tier List
        '馃尡': '🎯',  # Target for Seeds
        '馃挕': '💡',  # Light bulb for Tips
        '馃憫': '♠️',  # Spade for King of Spades
        '馃幉': '♟️',  # Chess pawn for Gambit Picks
        '馃幃': '🎮',  # Game controller for Steam
        
        # Common garbled em-dash and special characters
        '鈥?': '—',
        '鈥?': '–',
        '鈥?': '"',
        '鈥?': '"',
        '鈥?': ''',
        '鈥?': ''',
    }
    
    for garbled, correct in replacements.items():
        text = text.replace(garbled, correct)
    
    return text

def convert_file_to_utf8(file_path: str) -> bool:
    """Convert a single file to UTF-8 without BOM"""
    try:
        # Detect current encoding and BOM
        encoding, bom_len = detect_bom(file_path)
        
        # Read file with detected encoding
        with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
            content = f.read()
        
        # Fix garbled characters
        content = fix_emoji_garbage(content)
        
        # Write back as UTF-8 without BOM
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"  Error processing {file_path}: {e}")
        return False

def main():
    print("Starting comprehensive encoding fix...")
    
    # Define directories and file extensions to process
    extensions = ['.md', '.html', '.toml', '.yaml', '.yml', '.css', '.js']
    
    # Start from current directory
    base_dir = Path('.')
    
    converted_count = 0
    error_count = 0
    
    print("\nConverting files to UTF-8 without BOM...")
    
    # Process all matching files
    for ext in extensions:
        for file_path in base_dir.rglob(f'*{ext}'):
            # Skip .git directory
            if '.git' in file_path.parts:
                continue
            
            print(f"  Processing: {file_path}")
            if convert_file_to_utf8(str(file_path)):
                converted_count += 1
            else:
                error_count += 1
    
    print(f"\n  Converted {converted_count} files to UTF-8")
    if error_count > 0:
        print(f"  {error_count} files had errors")
    
    # Fix Hugo config
    print("\nChecking Hugo configuration...")
    hugo_config = Path('hugo.toml')
    if hugo_config.exists():
        content = hugo_config.read_text(encoding='utf-8')
        
        if 'hasCJKLanguage' not in content:
            # Add hasCJKLanguage setting
            content = '\n# Encoding settings for proper UTF-8 support\nhasCJKLanguage = true\n\n' + content
            hugo_config.write_text(content, encoding='utf-8')
            print("  Added hasCJKLanguage = true to hugo.toml")
        else:
            print("  hasCJKLanguage already configured")
    
    # Create .gitattributes
    print("\nCreating .gitattributes to enforce UTF-8...")
    gitattributes = Path('.gitattributes')
    gitattributes_content = """# Enforce UTF-8 encoding for all text files
* text=auto charset=utf-8

# Markdown files should always be UTF-8
*.md text charset=utf-8

# HTML files should always be UTF-8
*.html text charset=utf-8

# Configuration files should be UTF-8
*.toml text charset=utf-8
*.yaml text charset=utf-8
*.yml text charset=utf-8

# CSS and JS should be UTF-8
*.css text charset=utf-8
*.js text charset=utf-8
"""
    gitattributes.write_text(gitattributes_content, encoding='utf-8')
    print("  Created .gitattributes")
    
    print("\nEncoding fix complete!")
    print("\nNext steps:")
    print("1. Run: git add -A")
    print('2. Run: git commit -m "Fix encoding issues - convert all files to UTF-8 without BOM"')
    print("3. Run: git push")
    print("4. Check the live site to verify the fix")

if __name__ == '__main__':
    main()
