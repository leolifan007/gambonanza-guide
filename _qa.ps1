# QA Script for Gambonanza Redesign
param()
$public = "C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\public"
$passed = 0
$failed = 0
$errors = @()
function Assert {
    param($Desc, $Cond)
    if ($Cond) { $global:passed++ }
    else { $global:failed++; $global:errors += "FAIL: $Desc" }
}

# 1. Homepage
Write-Host "=== HOMEPAGE ===" -ForegroundColor Cyan
$html = Get-Content "$public\index.html" -Raw -Encoding UTF8
Assert "8 cards" ([regex]::Matches($html, 'latest-article-card').Count -eq 8)
Assert "4col" $html.Contains('latest-articles-4col')
Assert "6 cats" ([regex]::Matches($html, 'category-card-link').Count -eq 6)
Assert "cat-stats" $html.Contains('cat-stat')
Assert "NEW badge" $html.Contains('category-new-badge')
Assert "hero" $html.Contains('hero-kv')
Assert "nav Beginner" $html.Contains('href="/beginner/"')
Assert "nav Gambits" $html.Contains('href="/gambits/"')
Assert "nav Boss" $html.Contains('href="/bosses/"')
Assert "nav Economy" $html.Contains('href="/economy/"')
Assert "nav Cards" $html.Contains('href="/cards/"')
Assert "nav Strategy" $html.Contains('href="/strategy/"')
Assert "nav FAQ" $html.Contains('href="/faq/"')
Assert "top btn" $html.Contains('btn-back-to-top')
Assert "NEW on cards" $html.Contains('new-badge')

# 2. Inner page
Write-Host "=== INNER PAGE ===" -ForegroundColor Cyan
$inner = Get-Content "$public\pawn-economy-loop\index.html" -Raw -Encoding UTF8
Assert "6 side btns" ([regex]::Matches($inner, 'sidebar-article-link').Count -eq 6)
Assert "active" $inner.Contains('sidebar-article-link active')
Assert "NEW dot" $inner.Contains('sidebar-new-dot')
Assert "no ToC" (-not $inner.Contains('On This Page'))
Assert "top btn" $inner.Contains('btn-back-to-top')
Assert "page-header" $inner.Contains('page-hero')
Assert "content-layout" $inner.Contains('content-layout')
Assert "main-content" $inner.Contains('id="main-content"')
Assert "category-sidebar" $inner.Contains('id="category-sidebar"')

# 3. CSS
Write-Host "=== CSS ===" -ForegroundColor Cyan
$css = Get-Content "$public\css\style.css" -Raw -Encoding UTF8
Assert "4col" $css.Contains('.latest-articles-4col')
Assert "repeat(4" $css.Contains('repeat(4')
Assert "clamp" $css.Contains('-webkit-line-clamp')
Assert "cat-grid" $css.Contains('.category-grid')
Assert "cat-card" $css.Contains('.category-card')
Assert "cat-stats" $css.Contains('category-card-stats')
Assert "NEW css" $css.Contains('category-new-badge')
Assert "side-link" $css.Contains('sidebar-article-link')
Assert "border1" $css.Contains('border: 1px')
Assert "ellipsis" $css.Contains('text-overflow: ellipsis')
Assert "top css" $css.Contains('btn-back-to-top')

# 4. JS
Write-Host "=== JS ===" -ForegroundColor Cyan
$jsPath = "$public\js\redesign.js"
Assert "js exists" (Test-Path $jsPath)
if (Test-Path $jsPath) {
    $js = Get-Content $jsPath -Raw -Encoding UTF8
    Assert "nav" $js.Contains('nav-toggle')
    Assert "click" $js.Contains('sidebar-article-link')
    Assert "fetch" $js.Contains('fetch')
    Assert "pushState" $js.Contains('pushState')
}

# Results
Write-Host "=== RESULTS ===" -ForegroundColor Cyan
if ($failed -eq 0) {
    Write-Host "ALL $passed CHECKS PASSED!" -ForegroundColor Green
} else {
    Write-Host "$passed passed, $failed failed" -ForegroundColor Red
    $errors | % { Write-Host "  $_" -ForegroundColor Red }
}
