$ErrorActionPreference = "Stop"
$OutputEncoding = [Text.Encoding]::UTF8
$dir = "C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide"
Set-Location $dir

# 1. Git backup
git add -A
git commit -m "redesign backup: new-badge + page-hero bg + top-btn fix" 2>&1
Write-Host "=== git backup done ==="

# 2. Clean + rebuild
if (Test-Path "public") { Remove-Item -Recurse -Force "public" }
npx --yes hugo-bin --minify -d public 2>&1
Write-Host "=== hugo build done ==="

# 3. Verify built CSS
$cssPath = Join-Path $dir "public\css\style.css"
$css = Get-Content $cssPath -Raw
Write-Host "VERIFY:"
Write-Host "  new-badge: $($css.Contains('.new-badge'))"
Write-Host "  page-hero bg: $($css.Contains('hero-bg.webp'))"
Write-Host "  dot-home hide: $($css.Contains('.home .btn-back-to-top'))"
Write-Host "  right 32px: $($css.Contains('right: 32px'))"

# 4. Kill old servers on port 1313/1314
Get-NetTCPConnection -LocalPort 1313 -ErrorAction SilentlyContinue | ForEach-Object {
    taskkill /F /PID $_.OwningProcess 2>&1 | Out-Null
}
Get-NetTCPConnection -LocalPort 1314 -ErrorAction SilentlyContinue | ForEach-Object {
    taskkill /F /PID $_.OwningProcess 2>&1 | Out-Null
}
Start-Sleep 2

# 5. Start new server on 1314
Start-Process -WindowStyle Hidden -FilePath "cmd.exe" -ArgumentList "/c cd /d $dir\public && npx serve -l 1314"
Start-Sleep 4

# 6. Verify HTTP
try {
    $wc = New-Object System.Net.WebClient
    $html = $wc.DownloadString('http://127.0.0.1:1314/')
    Write-Host "`n=== HTTP VERIFY ==="
    Write-Host "  body class: $($html.Contains('body class=home'))"
    Write-Host "  no top btn: $(-not $html.Contains('btn-back-to-top'))"
    # inner page
    $inner = $wc.DownloadString('http://127.0.0.1:1314/pawn-economy-loop/')
    Write-Host "  inner has top btn: $($inner.Contains('btn-back-to-top'))"
} catch {
    Write-Host "HTTP check failed: $($_.Exception.Message)"
}
