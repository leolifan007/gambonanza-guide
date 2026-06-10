$ErrorActionPreference = "Stop"
$OutputEncoding = [Text.Encoding]::UTF8
$root = "C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide"

# Build
Set-Location $root
Remove-Item -Recurse -Force public -ErrorAction SilentlyContinue
$build = npx --yes hugo-bin --minify -d public 2>&1
Write-Host "=== Build ==="
Write-Host $build

# Spot check
Write-Host "`n=== Spot check ==="
$pages = @("how-to-play", "bosses", "strategy", "economy", "cards", "gambits", "beginner", "faq", "tips", "10-common-mistakes", "rook-gambit-build-guide", "complete-walkthrough", "faq")
$ok = 0
$fail = 0
foreach ($p in $pages) {
    $path = Join-Path $root "public\$p\index.html"
    if (-not (Test-Path $path)) {
        Write-Host "  [$p] NOT FOUND"
        $fail++
        continue
    }
    $html = Get-Content $path -Raw -Encoding UTF8
    
    $badges = @()
    # Check for unreplaced HTML
    if ($html -match '<div class=\\"callout|class=''callout') { $badges += "raw-callout" }
    if ($html -match '<div class=\\"pro-tip') { $badges += "raw-protip" }
    # Check for Hugo error markers
    if ($html -match 'Zgotmplz|"error"|shortcode was not rendered') { $badges += "HUGO-ERROR" }
    # Check components rendered
    $hasCallout = $html -match 'callout-'
    $hasProTip = $html -match 'pro-tip'
    $hasDivider = $html -match 'section-divider'
    $hasTable = $html -match '<table'
    
    if ($badges.Count -eq 0) {
        Write-Host "  [$p] OK | callout=$hasCallout pro-tip=$hasProTip divider=$hasDivider table=$hasTable"
        $ok++
    } else {
        Write-Host "  [$p] ISSUES: $($badges -join ', ')"
        $fail++
    }
}
Write-Host "`nResult: $ok pass, $fail fail"
