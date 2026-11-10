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
H4sIAAAAAAAC/22ZW3r2KgiF7/coOgQV8JCxdfCbBYlNlv9dn7xFkbN+rbR6lXa1/tPKVewq8rvWav+1D6j9EvutpbRJpMlVB4gepF9tgpgS0XaZgszBxFdbQXg11Us6
yConsZBZ9UP8D/GtnFTSul5VrlJASDcnest0Y9IvHUHWTVzZ9lOnH+ay+lvF7EvWVeulBtIrE98nZHpn4gt2kFGI+GFtBFEi4v5xi0ovk8m8WpDKq2m9pAYxIubOg9a9
HaRdZYJIY6JupiCDieVJu3x0Q7g1Vw/EGhNzAwUZTHraundjMn1BkK/dQFb41IkSqfgDZAoTvcoIwlp7HOQ+azGZV/WoklE6Ef9bcdJRK5N26QrCunlmtRHkWM0tCuuM
xnZr46oWhO0m7m1oPYT3EQ/wIMp289gp8OkwtrWWtNvorIHO9PY4bO1RVULrwbp57KiALF7NPK7DOmRr/6OmBvMb10lsBlEmPf0z2yEzM+JnO/ZZGfFThEh1u0HrqZ1J
Vhcnk4lGDZHZWYNQD2S2k2gSPo/HQcoslnHPGc6zhDVAtYTd1qGbrtRtUWZVeCGidw22gc3M+jXYBrYyt9f8nrSFf0K32Zms8IKWwjK1RC9xIkweGfJ2Q7VEJGppvFoY
NcghY1FhtehB5iUCYpWI1KgHWshuTkZUfy2TV5MVca1lPedxQwZRQz2Q+qfBQ5A/HWR3mU0MtcpJn0z8j1ht+yeJwAsaMvMgXmGLk1qECVoQSGXifU6CtJfW8lOHt6V7
NWGiA3XHyY6QTVaetL51C+I28PoGspgIvOBkTSZelbFaa18ZtAtXHEQ6k+jOTrQwMeQPiBLx3Pa648QOMlAPnHRhshDXTkYlEm0rCK+GviAg85Ax1DepUg4yMkKkTCJS
0qdS2Tpy+0cOu3l1CbuJ8Hm0pudkTwGbNPQsJ3rIdFQKJ8a6eRy0WK3zeTwOLDQYvJpPKOFtbxlMBDknKIo38eU15irD1ClalYn3Ru9MTrZumwj6qZNdyR8CG4TMOIih
l4D0k2hosHvjJgO1CmQRsYop2smeezeRW4NlTGIWE22FdbOY1kGUCUwHUj/75PxWkyiTmGGdNCHivdFvEk5kMIne6EQbkxXRq81YA7S62Md4taZpg9ZZtxYzBchk4uUq
9hl2EguZrxdAFu4/TibrJiXi2kkn4rmAeqBSCxPDTA7CNvC4jnj7y7lNFF0G5GsD/6NELqioMql5UtFDRm8NTIi43Wrs0xcRefYZlYmha4IYk57+kW8ugKzbOmOeJLJE
Ju/j90YLmcn7eHXRsNvk1XRm1ss6VlsZibIaEc+syB9ZvJpnVkM2amG7WdwXQFg3y37q5Ltai/sPLKr1IBOzmJNmTFbWKm2DSDQNEGVydxlVyqycd2AD/dY3EFxegwgR
aekFpZxriIOoLjp4NVkPYRktt9YUIQ0+tZCZh8zICNHnZaHi3h5zyAr/9PVYdBNU2ALSxkl8GgRZH4L2Fxr0PUX/kXjBcPJMAX8kferktdqI+pZZP8tTYTfxXg8vzD3D
vgn6qZNDJm45IHYS9FMn/SSYapwMJiOq/yzPjX8TzL2hm7CM5Lwzy1ND3iTPY6xb3iiddJbxmpgaDGXiER/7LLaOzwca+yw+KTLYPefXRvaCYRQBkWM1NM4gXw2iwt4y
g0mLuuNkEalZr2c1lsHAjpPut6c/opElc88UbxInraMScf+ET/cU8EcULwu4Bh/EYtqYrQqTHnHtZBLRzPrZhHXzqoycc8J2wztSrNZ5NfdPC/JkPa7Z86dE1hf79Sq6
c/shFhr4Bex5D/kjExOXE60fgssC+g8ubYNJZJaTp/L9kYHq7yQ7U4u3wfaDIBiIA5V2kokJBWQRwQwrIPn29CYofiDZf95koIZ4q88p7U1mriZZQ95k4W3wnx/x79/N
I3B9tHbSGhNFGoAsJvEg9c+PGFgqk6g2ILyQ50bDyaUrk447B4acepJcbfBRUPZjtZw+XgRtLOw4DyKo+U6ypryJ5T5a2DCouBLEThI20DKYDHQ3J5XPg7pag7B1cJeG
1toOmRFx7oNJO4mOIJ3JvM+jfFL0ypBRPo8i0II8ce5jtsYte+Adxvu7/IN4T3ainckKDUbp60NmzKcCsv3jB6x4aZC49VirozExzD8ggwkuMSCzEFGEQhDeB7WrBOlM
4o3IyXrtM+8Zo0Jm7rh+kdBtaiGCVx1ocL8IvknNfWbvTOIuAML7oHpWkJ0lm+ARAGS2D5lxSwiZnIOjNDZ7vK2/fVjOjW/SEW9OsidvkhU3ZLJ2fYn3fhA7icVqOVW/
ycp9et5Xv8TjDeSrQbxsJamViaC0gTz7ZLwZpneQtbZum0T0jlJKZRKv/SDyIT1+Rgsi9SRuUZDBZCDinWSWfIln/Xh+YXsTDJUgVojUglLtpD8Ej2D3rOm2HtN6I9Ji
AnOyfboJLgpBjAkedkBmJ5KThJMdVZvErwogg4ii/TvphffR+KXISeXz4LeqBSK8D15BQkYPGcMbhBMTJm66kLFbt4oXi/v1yHsyBj1lYpAB6UzipBM/HnzIil8vqhOt
nYnkavrEKKaPFTUkXmj448QgdX70akMfFa8yx8f47ZQ/dhTF86OcH8czWrw/xu9w9NHiMoePFs9G/X5d8/9cY2ZuvQkem4Mok5hdQRaTiRx2kr/2vsnCzO8ku+OLIK4k
SGeimOgWQpuJIU+c9H6SlMkp/U3Gvc/8kPsNDTLrawOQ+6QrZ4cvMWiw6iGTP+A7aUziHudEWSYu+yA5P72J5knXmEz6vc/ifSRXc5fySb0i+JTupB0ycb9azx3zRTK7
nehikl54bpJv0hHTTjqfFN1EQI6T5jgMsk6SWs/vajHFenY7We1/kekIsEYhAAA=
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
