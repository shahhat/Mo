# Knooz rosaries - compare the photos in THIS folder with what is already on Google Drive.
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
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
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
