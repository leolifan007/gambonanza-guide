$content = Get-Content "content/tutorial-revamp-guide.md" -Raw
Write-Host "Total file length: $($content.Length) chars"
# Manual close read of body section
$fmEnd = $content.IndexOf("---", 1)
$fmEnd2 = $content.IndexOf("---", $fmEnd + 1)
Write-Host "Front matter ends at char: $fmEnd2"
$bodySection = $content.Substring($fmEnd2)
Write-Host "Body section length: $($bodySection.Length) chars"
# Check the last ~200 chars
Write-Host "Last 200 chars:"
$bodySection.Substring([Math]::Max(0, $bodySection.Length - 200))