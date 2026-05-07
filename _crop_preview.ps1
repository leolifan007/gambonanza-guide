Add-Type -AssemblyName System.Drawing
$src = "C:\Users\ROG\.qclaw\media\inbound\paste_1778170578513_s8ent4.png"
$img = [System.Drawing.Image]::FromFile($src)
$cw = [int]($img.Width / 2)
$ch = [int]($img.Height / 4)
$tmp = "C:\Users\ROG\.qclaw\workspace-agent-d2068023\projects\gambonanza-guide\tmp\"
New-Item -ItemType Directory -Force -Path $tmp | Out-Null

$names = @('beginner','gambits','bosses','economy','achievements','cards','strategy','faq')

for ($row = 0; $row -lt 4; $row++) {
    for ($col = 0; $col -lt 2; $col++) {
        $idx = $row * 2 + $col
        $bmp = New-Object System.Drawing.Bitmap($cw, $ch)
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $destR = New-Object System.Drawing.Rectangle(0, 0, $cw, $ch)
        $srcR = New-Object System.Drawing.Rectangle($col * $cw, $row * $ch, $cw, $ch)
        $g.DrawImage($img, $destR, $srcR, [System.Drawing.GraphicsUnit]::Pixel)
        $g.Dispose()
        $bmp.Save("$tmp\$($names[$idx])_full.png", [System.Drawing.Imaging.ImageFormat]::Png)
        $bmp.Dispose()
    }
}
$img.Dispose()
Write-Host "Cropped 8 cells to tmp/"
Get-ChildItem $tmp | ForEach-Object { Write-Host "$($_.Name) : $([math]::Round($_.Length/1024,1))KB" }
