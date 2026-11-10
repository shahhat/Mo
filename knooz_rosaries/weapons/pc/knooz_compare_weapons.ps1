# Knooz Islamic weapons (S) - compare the photos in THIS folder with what is already on Google Drive.
# Read-only on your photos: it only reads them and COPIES the ones missing on Drive into "_missing_on_drive".
$ErrorActionPreference = 'Continue'
if ($PSScriptRoot) { $root = $PSScriptRoot } else { $root = (Get-Location).Path }
$out = Join-Path $root '_missing_on_drive'
[void][System.IO.Directory]::CreateDirectory($out)

function U16([byte[]]$b, [int]$o, [bool]$le) {
  if ($le) { return [int]$b[$o] + 256 * [int]$b[$o + 1] } else { return 256 * [int]$b[$o] + [int]$b[$o + 1] }
}
function U32([byte[]]$b, [int]$o, [bool]$le) {
  if ($le) { return [int64]$b[$o] + 256 * [int64]$b[$o + 1] + 65536 * [int64]$b[$o + 2] + 16777216 * [int64]$b[$o + 3] }
  else { return 16777216 * [int64]$b[$o] + 65536 * [int64]$b[$o + 1] + 256 * [int64]$b[$o + 2] + [int64]$b[$o + 3] }
}
function Get-ExifDate([byte[]]$b, [int]$n) {
  if ($n -lt 12 -or $b[0] -ne 0xFF -or $b[1] -ne 0xD8) { return '' }
  $p = 2
  while ($p + 10 -lt $n) {
    if ($b[$p] -ne 0xFF) { return '' }
    $mk = $b[$p + 1]
    if ($mk -eq 0xD9 -or $mk -eq 0xDA) { return '' }
    $len = 256 * [int]$b[$p + 2] + [int]$b[$p + 3]
    if ($mk -eq 0xE1 -and $b[$p + 4] -eq 0x45 -and $b[$p + 5] -eq 0x78 -and $b[$p + 6] -eq 0x69 -and $b[$p + 7] -eq 0x66) {
      $t = $p + 10
      $le = ($b[$t] -eq 0x49)
      $ifd = $t + (U32 $b ($t + 4) $le)
      if ($ifd + 2 -gt $n) { return '' }
      $exif = 0
      $cnt = U16 $b $ifd $le
      for ($k = 0; $k -lt $cnt; $k++) {
        $e = $ifd + 2 + 12 * $k
        if ($e + 12 -gt $n) { break }
        if ((U16 $b $e $le) -eq 0x8769) { $exif = $t + (U32 $b ($e + 8) $le) }
      }
      if ($exif -eq 0 -or $exif + 2 -gt $n) { return '' }
      $cnt = U16 $b $exif $le
      for ($k = 0; $k -lt $cnt; $k++) {
        $e = $exif + 2 + 12 * $k
        if ($e + 12 -gt $n) { break }
        if ((U16 $b $e $le) -eq 0x9003) {
          $o = $t + (U32 $b ($e + 8) $le)
          if ($o + 19 -le $n) { return [System.Text.Encoding]::ASCII.GetString($b, $o, 19) }
        }
      }
      return ''
    }
    $p += 2 + $len
  }
  return ''
}

$keysB64 = @'
H4sIAK3F8moC/22bW5btrAqF308rdhNU8ELa9jf+MMGkkul6q+FXKgICalYrrV6lXW38a+Uq/Sryn5m1/7UPqOOS/l8tpS0iTa46QfQg42oLpCsRbVdXkDWZ+GgWhEdTvWSA
WDlJjz5WP8T/EJ/KSSWp61XlKgWEZHOiu8/oTMalM4ht4sK2f3X5Yq5e/6vS+5fYVeulHWRUJj5P9BmDiQ84QGYh4ovtM4gSEbePa1RGWUzW1YJUHk3rJTVIJ9LdeJB6tIO0
qywQaUzU1RRkMum50iEf2eBuzcUD6Y1JdwUFmUxG6nqMzmT5gCBfvYFY2NSJEqn4A2QJE73KDMJSux/kPGZM1lXdq2SWQcT/Vqx01sqkXWpBWDbfWW0GOUZzjUI7s7He2rxq
D8J6E7c2pJ7C84g7eBBlvbnvFNh0dta1ltTbHCyBrrT2PHTtXlVC6smyue+ogBiP1t2vQzuka/+jpgTr69dJ+gqiTEbaZ7Wjz0qPX+2Yx9LjlwiR6nqD1EsHk4wuThYTjRgi
a7AEIR7IaifRJLwe94PsY9zHLdexHhOWANESerNDNrWUzWhnVVghvNcm66Cv3PU2WQfdcm/b+q60hX1CtjWYWFhBS+E+tUQucSJM7j5k7YZoCU/U0ni0UGqQo0+PCKtFD7Iu
EZBeiUiNeKCF9OZkRvTXsng0sfBrLXavxxUZRDvigdQ/CW6C/TNAnizzkI5Y5WQsJv5HjPbYJ4nAChp91kE8whYntQgTpCCQysTznARpL6nlX52elvZowkQn4o6Tx0MeYrnS
+pYtiOvA4xuIMRFYwYktJh6VMVpr3z5IFy44iAwmkZ2daGHSsX9AlIjvbY87TvpBJuKBkyFMDH7tZFYikbaC8GjICwKyjj4d8U2qlIPM9BApi4iUtKlU1o5s+8ihN48uoTcR
Xo/WtJw8VcBDGnKWEz36DEQKJ51lcz9oMdrg9bgf9JBg8mheoYS1PWUwEew5QVDcxIfXqKs6qk7Rqkw8N3pmcvLI9hBBPnXyRPKbQAfRZx6kI5eAjJNoSPDkxodMxCoQI9Ir
qmgnT937ENkSWGcStZhoKyxbj2odRJlAdSD1M0/WbzWJMoka1kkTIp4b/SThRCaTyI1OtDGx8F5tnSVAqot5Oo/WNHXQBsvWoqYAWUw8XMU8s5+kR5+vFUAM5x8ni2WTEn7t
ZBDxvYB4oFILk46aHIR14H4d/va35x6iyDIgXx34HyX2gooqk5orFT366JagCxHXW415hhGRe55ZmXRkTZDOZKR95LsXQGxrZ66TxC6RxfP4ubFHn8XzeHTR0Nvi0XTlrhc7
RrP0RLFGxHdW7B8xHs13VsNu1MJ663FeAGHZeuZTJ9/RWpx/oFGtB1moxZy0zsQyVmmbRCJpgCiTnWVUaWdlvQMd6De+geDwGkSISEsrKO25Bj+I6KKTRxO7CffRsqUmD2mw
aY8+6+gz00P0vlmoOLdHHWJhn2G3Rh+CCFtA2jyJV4Mg9iFIfyHBeKroPxI3GE7uKuCPpE2dvEabEd9y169yR9iHeK6HFdZTw74J8qmTo0+cckD6SZBPnYyToKpxMpnMiP6r
3Cf+h6DuDdmE+0jWO6vcMeRNcj2dZcsTpZPBfTwmpgRTmbjHxzzG2vH6QGMe45ViB7vl/NjIVugoRUDkGA2JM8hXgoiwu89k0iLuODEiNeP1qp37oGDHSp+7pz+isUvWU1O8
Say0zkrE7RM2faqAP6K4WcAx+CA9qo3VqjAZ4ddOFhHNXb+asGwelbHnnLDecI8Uow0eze3Tgty7Hsfs9a/Eri/9P4+iz96+SQ8J/AB234f8kYWKy4nWD8FhAfkHh7bJJHaW
kzvy/ZGJ6O8kM1OLu8H2D04w4Qcq7SQLFQqIEUENKyB59/QmCH4gmX/eZCKGeKrPKu1NVo4mGUPexHA3WH624v+/s4fnem3tpDUmin0AYkziRqr8bEXJUplEvAHhkXx3NKxd
hjIZOHWgzKknydEmrwWBP0bL+uNFkMhCk+sggqjvxHg9rec8WlgziLkSpJ8kdKBlMpnIb04qrweRtQZh7eA0Dam1HX1meLqXJu0kOoMMJmuvR3mlyJbRR3k9ClcLcnu6F9oa
5+yJmxjP8PKDeFZ2ooOJhQSzDPuQFRWqgDz28QVW3DVInHt6q7Mx6aiAQCYTHGNAViGicIUgPA+iVwkymMQtkRN7zbN2lVHRZz1+/SIh29JCBPc6kGDfCb5JzXnWGEziNADC
8yB+VpBnlzwE1wAgq33IinNC9MlKOIJj67e19b8xe1aObzLgb04yKz8kY270yej1JZ79QfpJeoyWdfWbWM4z8sT6Je5vIF8J4m4rSa1MBLEN5J4n/a2jfgcxe2R7SHjvLKVU
JnHfDyIfMuIhLYjUk7hGQSaTCY93krvkS3zXz/uN7U1QVoL0QqQWxGon4ya4BtvVput6rj4akRY1mJPHpg/BUSFIZ4KrHZA1iGQt4eTxqofEuwLIJKIoAJyMwvNovBU5qbwe
vFYZiPA8uAeJPnr06biFcNKFiasu+vQtW8Wdxb4/8qyMUk+ZdPQBGUxipQvPBx9i8X5RnWgdTCRH09tHUX9YxJC4oynculBL/Wj1eMOtiquZszVeUI/Wgcj4o1V+tM6nxni3
xosct/Y410VrjyuksW/a/H9trtxlb4KL5yDKJOpYEGOysJud5MvvmxjqfyeZJ18EHiZBBhNFdWdwciYdO8bJGCfJPpNXqnPPsz5k36ehj311ALJXallFfEmHBFaPPvmY76Qx
iTOdE+U+cfAHyUrqTTRXanMxGXse43kkR3OT8ko9NnjF7qQdfeKsZfd580VynztRY5JWuE+VbzLg2U4GrxR5RUCOlWZlDGInSanXd7SoZ32fO7l1gPNMRRxuUbHXNksdhBAg
e6BWCWmJ7y0ciTCKUBxoMdJ4vXKkLIbGkRyoF0ZxqxZoEupxlQ00WIz+zLUO1OO5EMgYjXhVd2S85J6PZUDfdU1oNwes1RiFuwC1QQjfXsSSq3RG+WGIIxVG/e5FisIt0TZK
HcpI423b0Tx6RWkDtCYjw+kkEK9LxlZvK7yuvD0GqpVRXBcFYh26b5Swcmt6oqaJWEKPYi17ySHG2L7RxE5UQ1FNDwntnkvtRJKo/+jVc67O9oIfZq/RGI14oAfSE+FtGOi7
5Dh4tNiwbSmjyMyBFqO5rSylMsqXY6BjQNvBQWo5kbREQgiOnajxXO7YqSgRHrDeRtnvBC8UHwwE6ixhW9vZZPKAHt1raF4ObcjafrjP0C+k+VoOtE7UQxv7FP1GbbuNFhYe
Pp+9KgsPxw4ra2uM+rayNh7QPaqGz6tyrywOgfo6UQ9F6WCj4ODVEh29DHdaQKucKOO8rq8YUSFm3FDTE20xbDKKLOmok7PhdW1ro7cD3QG2U4CNj9tS+C6Vkex42PUHSh12
7Yzi7Qmo64k0JeyHGLfm9+d3b3Srtw8esMUtF9Bk9eJKNYU/NC9xnwh0qFfWjjbdWAzcCkSvUViMx7FHZUXhXcISyYlSG/vbvTdaO26Mxr1w6RpLHsJi4A0x5+osBlL2RjyX
p+y01/hqPkvZDERjVkbxDh9oMpo7+Y7VCdWyfX4YD7g/sgTiAfc3Wm3O0hjJDsuzLEbx2gv0DSn5FJ2xd1ZecjzBBfrulERZOcx29JKtwynjRKmNKbwufAE4Ex0D3pXDVB4Q
L9LhNvNb2+RjTupw9qOX7DJ1HlZ21FMbg9XrZ7NMbXP0E2lqfrDm5S5T5/yBsgicix0AuzKXvA4x7Dal8ZJx8xdirHKgtiP2KvNEqcPn0PmH7mizGkuI7LDRd8C4bs+EuEi9
gbIiWqTD+JIsvXfR/opb+kz0ax3ortnWshOletc3p+D9o2zfsMLCP6WI0SaKjyAzfNmx5KpbDPueboD6XpfJPJFudMw1d2Tb77GBWtyDxSd1jtZ4zbWR5CZaQycjjS8rHb3i
4UY9hV/veLjRyA27xivdbIRDR6BXHfWgyESOBiHflaHDNQuL4YfHHHDWxmhkTnHE2pB9Gl3vGLXRrjfWO6Qkwjt4CzR5QN3lwZrGA/ZdH7obsoS4SgvhV2Nt4DuKkug714xC
OpEoIbzHJyKjTKSASNlrjXqiKFPXe389qKeEYzLq2zcW2WtGjR32WuvoZRlSlhUWHomvJOIl7++5HbV5oohsy4SFl7KFty6MaoYURzygh+WSc412otwpRt47480lxVi8Lpxh
U4xljG4/NPsaJU43cRixQtpYYRQLVAujXTk44l5thy8rpMM8+CQij4qvLGvORdshPqZsicjZ4rgUPm/vC5ONLN3GymAJpeVetv2JwwvhGjElXAfaR2kra55Icq5Dvdiw2ctY
QjxEpRjG6+r5a5VmtemJIjhYpZASx4qSSBqhx5S1G6N9oLM6eMC6LzGsznqilhJO+YFyQFJvngLC2eoqjCQ3rKOj18gNa9Umo7l12CovWXSvqzUWXlYmX9tfFb+R7XW13n4g
TSQnihrbWmcJ8YlhznWoV/MXW46OJeu+MLH31ccfyiUvNqWuPKdYM57L3SZStklj4fE5e2heDrfJr+wC6Ylyp7zvNx6UVhZhCfvMeOhBtJyop4SH5vMpNVA/UcRDR/NEfaND
DNshRTJujLiGkn2Z5r5BjflbgLPRizFu7DiJfxrjw3d3Km6M5MWNEUmoMXcoN8amoMZ8T+DG+NEVN/6aSOLQx43xcrYbEaXjhw74HcbRiKf6o7EjpXIj7k6PxvXSZzbihz0w
Ije2lzmeRkUAORt7PRrjLeJsbPqjUY6JUAbbj0YPy/8HAmPKmd85AAA=
'@
$gzBytes = [Convert]::FromBase64String(($keysB64 -replace '\s', ''))
$ms = New-Object System.IO.MemoryStream(, $gzBytes)
$gs = New-Object System.IO.Compression.GZipStream($ms, [System.IO.Compression.CompressionMode]::Decompress)
$sr = New-Object System.IO.StreamReader($gs)
$keysText = $sr.ReadToEnd()
$sr.Dispose()
$drive = @{}
foreach ($line in ($keysText -split "`r?`n")) {
  $l = $line.Trim(); if (-not $l) { continue }
  $p = $l.Split('|')
  if (-not $drive.ContainsKey($p[0])) { $drive[$p[0]] = New-Object System.Collections.ArrayList }
  [void]$drive[$p[0]].Add($p[1])
}

Write-Host "Scanning: $root"
$photoExt = @('.jpg', '.jpeg', '.png')
$all = @(Get-ChildItem -LiteralPath $root -Recurse -File -ErrorAction SilentlyContinue | Where-Object { -not $_.FullName.StartsWith($out) })
$rows = New-Object System.Collections.ArrayList
$i = 0; $nMiss = 0; $nOn = 0; $nNo = 0; $nOther = 0; $bytes = [int64]0
$buf = New-Object byte[] 196608
foreach ($f in $all) {
  $i++
  if ($i % 100 -eq 0) { Write-Host ("  checked " + $i + " / " + $all.Count) }
  $rel = $f.FullName.Substring($root.Length).TrimStart('\', '/')
  $ext = $f.Extension.ToLower()
  $dto = ''; $imgno = ''; $status = ''
  if ($photoExt -notcontains $ext) {
    $status = 'OTHER_FILE'; $nOther++
  } else {
    try {
      $fs = [System.IO.File]::OpenRead($f.FullName)
      try { $n = $fs.Read($buf, 0, $buf.Length) } finally { $fs.Dispose() }
      $dto = Get-ExifDate $buf $n
      $txt = [System.Text.Encoding]::ASCII.GetString($buf, 0, $n)
      $m = [regex]::Match($txt, 'aux:ImageNumber="(\d+)"')
      if ($m.Success) { $imgno = $m.Groups[1].Value }
    } catch { $dto = '' }
    if (-not $dto) { $status = 'NO_EXIF' }
    elseif ($drive.ContainsKey($dto)) {
      $c = $drive[$dto]
      if ((-not $imgno) -or ($c -contains $imgno) -or ($c -contains '')) { $status = 'ON_DRIVE' } else { $status = 'MISSING' }
    } else { $status = 'MISSING' }
    if ($status -eq 'ON_DRIVE') { $nOn++ } else {
      if ($status -eq 'NO_EXIF') { $nNo++ } else { $nMiss++ }
      $dest = Join-Path $out $rel
      [void][System.IO.Directory]::CreateDirectory((Split-Path -Parent $dest))
      [System.IO.File]::Copy($f.FullName, $dest, $true)
      $bytes += $f.Length
    }
  }
  [void]$rows.Add([pscustomobject]@{ path = $rel; size = $f.Length; dto = $dto; imgno = $imgno; status = $status })
}
$rows | Export-Csv -LiteralPath (Join-Path $out '_manifest.csv') -NoTypeInformation -Encoding UTF8

Write-Host ""
Write-Host "Done."
Write-Host ("Photos in this folder : " + ($nOn + $nMiss + $nNo))
Write-Host ("Already on Drive      : " + $nOn)
Write-Host ("Missing on Drive      : " + $nMiss + "   (copied to _missing_on_drive)")
Write-Host ("No date inside photo  : " + $nNo + "   (copied too - will be checked by eye)")
Write-Host ("Other files           : " + $nOther + "   (listed in the report only)")
Write-Host ("Size to upload        : " + [math]::Round($bytes / 1MB, 1) + " MB")
Write-Host ""
Write-Host "Upload the folder _missing_on_drive to the Drive folder you were given."
