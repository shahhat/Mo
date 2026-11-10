# Knooz Islamic weapons (S) - FINAL CHECK: is this PC folder exactly the same as Google Drive?
# Put it in the folder "S - الأسلحة الإسلامية" and run:
#   powershell -ExecutionPolicy Bypass -File .\knooz_verify_weapons.ps1
# Part 1 (read-only): compares every photo here with the 573 photos on Drive (by the date/number stored inside the photo).
#   Writes _verify_report.csv and prints a summary. Changes nothing.
# Part 2 (only if you type YES): downloads from Drive the photos that are missing here, straight into the right
#   <category>\<code>\<name>.jpg place, and copies photos that are here but not on Drive into _missing_on_drive (to upload).
$ErrorActionPreference = 'Continue'
if ($PSScriptRoot) { $root = $PSScriptRoot } else { $root = (Get-Location).Path }
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

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

$mapB64 = @'
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
/hUrGz7vVAQm1whCok75331yQT2Z9wAA
'@
$gzBytes = [Convert]::FromBase64String(($mapB64 -replace '\s', ''))
$ms = New-Object System.IO.MemoryStream(, $gzBytes)
$gs = New-Object System.IO.Compression.GZipStream($ms, [System.IO.Compression.CompressionMode]::Decompress)
$sr = New-Object System.IO.StreamReader($gs, [System.Text.Encoding]::UTF8)
$mapText = $sr.ReadToEnd(); $sr.Dispose()
$targets = New-Object System.Collections.ArrayList
$byKey = @{}; $byDate = @{}; $byPath = @{}
foreach ($line in ($mapText -split "`n")) {
  $l = $line.Trim(); if (-not $l) { continue }
  $p = $l.Split('|')
  $t = [pscustomobject]@{ key = ($p[0] + '|' + $p[1]); dto = $p[0]; path = [System.IO.Path]::Combine($p[2], $p[3], $p[4]); id = $p[5]; found = $false }
  [void]$targets.Add($t)
  $byPath[$t.path.ToLower()] = $t
  if (-not $byKey.ContainsKey($t.key)) { $byKey[$t.key] = New-Object System.Collections.ArrayList }
  [void]$byKey[$t.key].Add($t)
  if (-not $byDate.ContainsKey($t.dto)) { $byDate[$t.dto] = New-Object System.Collections.ArrayList }
  [void]$byDate[$t.dto].Add($t)
}

Write-Host "Checking: $root"
$skip = @('_للحذف', '_missing_on_drive')
$photoExt = @('.jpg', '.jpeg', '.png')
$all = @(Get-ChildItem -LiteralPath $root -Recurse -File -ErrorAction SilentlyContinue | Where-Object {
  $rel = $_.FullName.Substring($root.Length).TrimStart('\', '/')
  ($photoExt -contains $_.Extension.ToLower()) -and -not ($skip | Where-Object { $rel.StartsWith($_) })
})
$rows = New-Object System.Collections.ArrayList
$extra = New-Object System.Collections.ArrayList
$buf = New-Object byte[] 196608
$i = 0
# pass 1: files already at the right place
$pending = New-Object System.Collections.ArrayList
foreach ($f in $all) {
  $rel = $f.FullName.Substring($root.Length).TrimStart('\', '/')
  $t = $byPath[$rel.ToLower()]
  if ($t -and -not $t.found) { $t.found = $true; [void]$rows.Add([pscustomobject]@{ status = 'OK'; pc_file = $rel; drive_file = $t.path }) }
  else { [void]$pending.Add($f) }
}
# pass 2: everything else, matched by the date/number inside the photo
foreach ($f in $pending) {
  $i++; if ($i % 100 -eq 0) { Write-Host ("  checked " + $i + " / " + $pending.Count) }
  $rel = $f.FullName.Substring($root.Length).TrimStart('\', '/')
  $dto = ''; $imgno = ''
  try {
    $fs = [System.IO.File]::OpenRead($f.FullName)
    try { $n = $fs.Read($buf, 0, $buf.Length) } finally { $fs.Dispose() }
    $dto = Get-ExifDate $buf $n
    $txt = [System.Text.Encoding]::ASCII.GetString($buf, 0, $n)
    $m = [regex]::Match($txt, 'aux:ImageNumber="(\d+)"'); if ($m.Success) { $imgno = $m.Groups[1].Value }
  } catch { }
  $c = $null
  if ($dto -and $byKey.ContainsKey($dto + '|' + $imgno)) { $c = $byKey[$dto + '|' + $imgno] }
  elseif ($dto -and (-not $imgno) -and $byDate.ContainsKey($dto)) { $c = $byDate[$dto] }
  if (-not $c) {
    $st = 'NOT_ON_DRIVE'; if (-not $dto) { $st = 'NOT_ON_DRIVE (no date inside photo)' }
    [void]$rows.Add([pscustomobject]@{ status = $st; pc_file = $rel; drive_file = '' }); [void]$extra.Add($f); continue
  }
  $t = $null; foreach ($x in $c) { if (-not $x.found) { $t = $x; break } }
  if ($t) { $t.found = $true; [void]$rows.Add([pscustomobject]@{ status = 'WRONG_NAME'; pc_file = $rel; drive_file = $t.path }) }
  else { [void]$rows.Add([pscustomobject]@{ status = 'EXTRA_COPY'; pc_file = $rel; drive_file = $c[0].path }) }
}
$missing = @($targets | Where-Object { -not $_.found })
foreach ($t in $missing) { [void]$rows.Add([pscustomobject]@{ status = 'MISSING_ON_PC'; pc_file = ''; drive_file = $t.path }) }
$rows | Export-Csv -LiteralPath (Join-Path $root '_verify_report.csv') -NoTypeInformation -Encoding UTF8

$cOK = @($rows | Where-Object { $_.status -eq 'OK' }).Count
$cWN = @($rows | Where-Object { $_.status -eq 'WRONG_NAME' }).Count
$cEX = @($rows | Where-Object { $_.status -eq 'EXTRA_COPY' }).Count
$cND = $extra.Count
Write-Host ""
Write-Host ("Drive photos                    : " + $targets.Count)
Write-Host ("OK (same photo, same code)      : " + $cOK)
Write-Host ("WRONG_NAME (right photo, old name - run knooz_rename_weapons.ps1) : " + $cWN)
Write-Host ("EXTRA_COPY (duplicate on PC)    : " + $cEX)
Write-Host ("NOT_ON_DRIVE (more than Drive)  : " + $cND)
Write-Host ("MISSING_ON_PC (less than Drive) : " + $missing.Count)
Write-Host "Details: _verify_report.csv"
if ($cOK -eq $targets.Count -and $cWN -eq 0 -and $cEX -eq 0 -and $cND -eq 0) { Write-Host ""; Write-Host "PERFECT: this folder = Drive, same codes."; exit }
if ($missing.Count -eq 0 -and $cND -eq 0) { exit }
Write-Host ""
$ans = Read-Host ("Type YES to download the " + $missing.Count + " missing photos from Drive and copy the " + $cND + " not-on-Drive photos to _missing_on_drive")
if ($ans -ne 'YES') { Write-Host "Stopped. Nothing changed."; exit }
$ok = 0; $bad = 0
foreach ($t in $missing) {
  $dst = Join-Path $root $t.path
  if (Test-Path -LiteralPath $dst) { Write-Host ("  exists, skipped: " + $t.path); continue }
  [void][System.IO.Directory]::CreateDirectory((Split-Path -Parent $dst))
  try {
    Invoke-WebRequest -UseBasicParsing -Uri ("https://drive.usercontent.google.com/download?id=" + $t.id + "&export=download&confirm=t") -OutFile $dst -ErrorAction Stop
    if ((Get-Item -LiteralPath $dst).Length -lt 20000) { throw "download too small" }
    $ok++; Write-Host ("  downloaded " + $t.path)
  } catch { $bad++; Write-Host ("  FAILED " + $t.path + " (" + $_.Exception.Message + ")"); Remove-Item -LiteralPath $dst -ErrorAction SilentlyContinue }
}
$out = Join-Path $root '_missing_on_drive'
foreach ($f in $extra) {
  $rel = $f.FullName.Substring($root.Length).TrimStart('\', '/')
  $d = Join-Path $out $rel
  [void][System.IO.Directory]::CreateDirectory((Split-Path -Parent $d))
  [System.IO.File]::Copy($f.FullName, $d, $true)
}
Write-Host ""
Write-Host ("Downloaded: " + $ok + "   Failed: " + $bad + "   Copied to _missing_on_drive: " + $extra.Count)
Write-Host "Run this script again: it should say PERFECT (after you also ran knooz_rename_weapons.ps1 for WRONG_NAME/EXTRA_COPY)."
