# Fix Encoding Script for Gambonanza Guide
# This script converts all Markdown files to UTF-8 without BOM and adds proper encoding settings

Write-Host "🔧 Starting encoding fix..." -ForegroundColor Cyan

# 1. Convert all Markdown files to UTF-8 without BOM
Write-Host "📝 Converting all Markdown files to UTF-8 without BOM..." -ForegroundColor Yellow

$contentDir = "content"
$mdFiles = Get-ChildItem -Path $contentDir -Recurse -Filter "*.md"

$convertedCount = 0
foreach ($file in $mdFiles) {
    $filePath = $file.FullName
    
    # Read file as bytes to detect BOM
    $bytes = [System.IO.File]::ReadAllBytes($filePath)
    
    # Check if file has BOM
    $hasBom = $bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF
    
    # Read content with proper encoding
    if ($hasBom) {
        # Remove BOM and read as UTF-8
        $content = [System.Text.Encoding]::UTF8.GetString($bytes, 3, $bytes.Length - 3)
        $convertedCount++
        Write-Host "  ✓ Fixed BOM in: $($file.Name)" -ForegroundColor Green
    } else {
        # Try to read as UTF-8 first, fallback to system default
        try {
            $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
        } catch {
            # If UTF-8 fails, read with system default encoding
            $content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::Default)
            $convertedCount++
            Write-Host "  ✓ Converted to UTF-8: $($file.Name)" -ForegroundColor Green
        }
    }
    
    # Write back as UTF-8 without BOM
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($filePath, $content, $utf8NoBom)
}

Write-Host "  ✅ Converted $convertedCount files to UTF-8 without BOM" -ForegroundColor Green

# 2. Add encoding settings to hugo.toml if not present
Write-Host "⚙️ Checking Hugo configuration..." -ForegroundColor Yellow

$hugoConfig = "hugo.toml"
$configContent = Get-Content $hugoConfig -Raw

# Check if hasCJKLanguage is already set
if ($configContent -notmatch "hasCJKLanguage") {
    # Add encoding settings before [markup] section
    $encodingSettings = @"

# Encoding settings for proper UTF-8 support
hasCJKLanguage = true

"@
    
    # Insert before [markup] section
    $configContent = $configContent -replace "(?=\[markup\])", $encodingSettings
    Set-Content $hugoConfig -Value $configContent -Encoding UTF8
    Write-Host "  ✓ Added hasCJKLanguage = true to hugo.toml" -ForegroundColor Green
} else {
    Write-Host "  ✓ hasCJKLanguage already configured" -ForegroundColor Green
}

# 3. Check and fix HTML templates
Write-Host "🔍 Checking HTML templates for charset declaration..." -ForegroundColor Yellow

$headerFile = "layouts\partials\header.html"
if (Test-Path $headerFile) {
    $headerContent = Get-Content $headerFile -Raw
    
    if ($headerContent -notmatch "charset=utf-8") {
        # Add meta charset tag at the beginning of head section
        $headerContent = $headerContent -replace "(<head>)", '$1' + "`n  <meta charset=`"utf-8`">"
        Set-Content $headerFile -Value $headerContent -Encoding UTF8
        Write-Host "  ✓ Added charset declaration to header.html" -ForegroundColor Green
    } else {
        Write-Host "  ✓ Charset declaration already present in header.html" -ForegroundColor Green
    }
} else {
    Write-Host "  ⚠️  header.html not found, skipping template check" -ForegroundColor Yellow
}

# 4. Create .gitattributes to enforce UTF-8 encoding
Write-Host "📋 Creating .gitattributes to enforce UTF-8..." -ForegroundColor Yellow

$gitattributesContent = @"
# Enforce UTF-8 encoding for all text files
* text=auto charset=utf-8

# Markdown files should always be UTF-8
*.md text charset=utf-8

# HTML files should always be UTF-8
*.html text charset=utf-8

# Configuration files should be UTF-8
*.toml text charset=utf-8
*.yaml text charset=utf-8
*.yml text charset=utf-8
"@

Set-Content ".gitattributes" -Value $gitattributesContent -Encoding UTF8
Write-Host "  ✓ Created .gitattributes to enforce UTF-8 encoding" -ForegroundColor Green

# 5. Create pre-commit hook to prevent future encoding issues
Write-Host "🎣 Creating pre-commit hook..." -ForegroundColor Yellow

$hooksDir = ".git\hooks"
if (!(Test-Path $hooksDir)) {
    New-Item -ItemType Directory -Path $hooksDir -Force | Out-Null
}

$preCommitScript = @"
#!/bin/sh
# Pre-commit hook to check for encoding issues

echo "Checking file encoding..."

# Check for non-UTF-8 files
find content -name "*.md" -type f | while read file; do
    if ! file -b --mime-encoding "$file" | grep -q "utf-8"; then
        echo "ERROR: $file is not UTF-8 encoded!"
        echo "Please convert it to UTF-8 without BOM"
        exit 1
    fi
done

echo "✅ All files are properly encoded"
exit 0
"@

Set-Content "$hooksDir\pre-commit" -Value $preCommitScript -Encoding UTF8
Write-Host "  ✓ Created pre-commit hook to prevent encoding issues" -ForegroundColor Green

Write-Host "`n🎉 Encoding fix complete!" -ForegroundColor Cyan
Write-Host "`nNext steps:" -ForegroundColor Yellow
Write-Host "1. Run: git add -A" -ForegroundColor White
Write-Host "2. Run: git commit -m `"Fix encoding issues - convert all files to UTF-8 without BOM`"" -ForegroundColor White
Write-Host "3. Run: git push" -ForegroundColor White
Write-Host "4. Check the live site to verify the fix" -ForegroundColor White
