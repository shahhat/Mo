# Knooz jewelry & rings (JWL) - compare the photos in THIS folder with what is already on Google Drive.
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
