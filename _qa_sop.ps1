# Gambonanza Guide QA Report
# Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm")

$root = "C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public"
$results = @{pass=0; fail=0; warn=0}
$checks = @()

function Check($name, $condition, $severity="fail") {
    $s = if ($condition) {"PASS"} else {if ($severity -eq "warn"){"WARN"}else{"FAIL"}}
    $results[$severity]++
    $checks += [PSCustomObject]@{Check=$name; Result=$s}
    Write-Host "  [$s] $name"
}

Write-Host "=== SOP QA: Visual Component Audit ==="
Write-Host ""

# 1. Page-level check
$pages = @("index.html", "tips/index.html", "beginner/index.html", "gambits/index.html", "economy/index.html", "strategy/index.html", "bosses/index.html", "cards/index.html", "faq/index.html", "pawn-economy-loop/index.html", "rook-gambit-build-guide/index.html", "afks-gambit-guide/index.html")
$pages = $pages | Where-Object { Test-Path "$root\$_" }

foreach ($page in $pages) {
    $path = "$root\$page"
    $html = Get-Content $path -Raw -Encoding UTF8
    $name = $page -replace '/index\.html$', '' -replace 'index\.html$', 'home'
    
    Write-Host "--- $name ---"
    
    # Shortcodes/components check
    Check "has content-body" ($html.Contains('content-body') -or $html.Contains('article-body')) "warn"
    Check "has page-hero" ($html.Contains('page-hero')) "warn"
    
    # Encoding check - no ?/span>
    Check "no broken ?/span>" (-not ($html -match '\?/span>'))
    Check "no encoding ? in HTML" (-not ($html -match '>[^<]*\?[^<]*<' -and $html -notmatch 'query|\?'))
    
    # Content components present
    if ($html.Contains('callout-verdict') -or $html.Contains('callout-tip') -or $html.Contains('callout-danger') -or $html.Contains('callout-synergy')) {
        Check "has callout component" $true
    } else {
        Check "has callout component" $false "warn"
    }
    
    # Section dividers or visual breaks
    $hrCount = [regex]::Matches($html, 'class="section-divider"').Count
    $totalH2 = [regex]::Matches($html, '<h2[ >]').Count
    if ($hrCount -ge ($totalH2 - 1)) {
        Check "section dividers ($hrCount for $totalH2 h2)" $true
    } else {
        Check "section dividers ($hrCount for $totalH2 h2)" ($hrCount -gt 0) "warn"
    }
    
    # Tables for data
    $tableCount = [regex]::Matches($html, '<table').Count
    if ($tableCount -gt 0) {
        Check "data tables ($tableCount)" $true
    } else {
        Check "data tables (0)" $false "warn"
    }
    
    # Buttons/CTA
    if ($html.Contains('btn-primary') -or $html.Contains('btn-secondary')) {
        Check "CTA buttons" $true
    } else {
        Check "CTA buttons" $false "warn"
    }
    
    # Active nav
    Check "active nav highlighted" ($html.Contains('class="active"') -or $html.Contains('class=active'))
}

Write-Host ""
Write-Host "=== Summary ==="
Write-Host "PASS: $($results.pass) | FAIL: $($results.fail) | WARN: $($results.warn)"
Write-Host "Score: $([math]::Round(100 * $results.pass / ($results.pass + $results.fail + $results.warn), 0))% pass rate"
