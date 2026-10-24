# Knooz amber (AMB) - compare the photos in THIS folder with what is already on Google Drive.
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
