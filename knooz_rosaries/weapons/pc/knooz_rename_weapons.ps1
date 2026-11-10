# Knooz Islamic weapons (S) - rename the photos in THIS folder to the same codes used on Google Drive.
# Step 1 (always): preview only. It writes _rename_plan.csv and changes nothing.
# Step 2: you type YES and it MOVES each photo into  <category>\<code>\<code>-n.jpg  (same as Drive).
#   - Extra copies of the same shot go to  _للحذف\  (moved, never deleted).
#   - Photos that are not on Drive yet stay where they are (they will get codes later).
#   - Every move is written to _rename_log.csv.  To undo:  run this script with  -Undo
param([switch]$Undo)
$ErrorActionPreference = 'Continue'
if ($PSScriptRoot) { $root = $PSScriptRoot } else { $root = (Get-Location).Path }
$log = Join-Path $root '_rename_log.csv'

if ($Undo) {
  if (-not (Test-Path -LiteralPath $log)) { Write-Host "No _rename_log.csv - nothing to undo."; exit }
  $rows = @(Import-Csv -LiteralPath $log -Encoding UTF8)
  [array]::Reverse($rows)
  $n = 0
  foreach ($r in $rows) {
    $from = Join-Path $root $r.to; $to = Join-Path $root $r.from
    if ((Test-Path -LiteralPath $from) -and -not (Test-Path -LiteralPath $to)) {
      [void][System.IO.Directory]::CreateDirectory((Split-Path -Parent $to))
      Move-Item -LiteralPath $from -Destination $to; $n++
    }
  }
  Rename-Item -LiteralPath $log -NewName ('_rename_log_undone_' + (Get-Date -Format 'yyyyMMdd_HHmmss') + '.csv')
  Write-Host ("Undo done. Moved back: " + $n); exit
}

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
'@
$gzBytes = [Convert]::FromBase64String(($mapB64 -replace '\s', ''))
$ms = New-Object System.IO.MemoryStream(, $gzBytes)
$gs = New-Object System.IO.Compression.GZipStream($ms, [System.IO.Compression.CompressionMode]::Decompress)
$sr = New-Object System.IO.StreamReader($gs, [System.Text.Encoding]::UTF8)
$mapText = $sr.ReadToEnd(); $sr.Dispose()
$byFull = @{}; $byDate = @{}
foreach ($line in ($mapText -split "`n")) {
  $l = $line.Trim(); if (-not $l) { continue }
  $p = $l.Split('|')
  $target = [System.IO.Path]::Combine($p[2], $p[3], $p[4])
  $k = $p[0] + '|' + $p[1]
  if (-not $byFull.ContainsKey($k)) { $byFull[$k] = New-Object System.Collections.ArrayList }
  [void]$byFull[$k].Add($target)
  if (-not $byDate.ContainsKey($p[0])) { $byDate[$p[0]] = New-Object System.Collections.ArrayList }
  [void]$byDate[$p[0]].Add($target)
}

$skipDirs = @('S-J - ', 'S-KJ - ', 'S-X - ', '_للحذف', '_missing_on_drive')
Write-Host "Scanning: $root"
$photoExt = @('.jpg', '.jpeg', '.png')
$all = @(Get-ChildItem -LiteralPath $root -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $photoExt -contains $_.Extension.ToLower() } | Where-Object {
  $rel = $_.FullName.Substring($root.Length).TrimStart('\', '/')
  $bad = $false; foreach ($s in $skipDirs) { if ($rel.StartsWith($s)) { $bad = $true } }
  -not $bad
} | Sort-Object { $_.Name.ToUpper().StartsWith('S') -eq $false }, FullName)

$used = @{}; $plan = New-Object System.Collections.ArrayList
$buf = New-Object byte[] 196608
$nRen = 0; $nDup = 0; $nKeep = 0; $i = 0
foreach ($f in $all) {
  $i++; if ($i % 100 -eq 0) { Write-Host ("  checked " + $i + " / " + $all.Count) }
  $rel = $f.FullName.Substring($root.Length).TrimStart('\', '/')
  $dto = ''; $imgno = ''
  try {
    $fs = [System.IO.File]::OpenRead($f.FullName)
    try { $n = $fs.Read($buf, 0, $buf.Length) } finally { $fs.Dispose() }
    $dto = Get-ExifDate $buf $n
    $txt = [System.Text.Encoding]::ASCII.GetString($buf, 0, $n)
    $m = [regex]::Match($txt, 'aux:ImageNumber="(\d+)"'); if ($m.Success) { $imgno = $m.Groups[1].Value }
  } catch { }
  $cands = $null
  if ($dto) {
    if ($byFull.ContainsKey($dto + '|' + $imgno)) { $cands = $byFull[$dto + '|' + $imgno] }
    elseif ((-not $imgno) -and $byDate.ContainsKey($dto)) { $cands = $byDate[$dto] }
  }
  $target = $null
  if ($cands) { foreach ($t in $cands) { if (-not $used.ContainsKey($t)) { $target = $t; break } } }
  if (-not $cands) { $action = 'KEEP (not on Drive yet)'; $to = $rel; $nKeep++ }
  elseif ($target) { $used[$target] = 1; $action = 'RENAME'; $to = $target; $nRen++ }
  else { $action = 'DUPLICATE -> _للحذف'; $to = [System.IO.Path]::Combine('_للحذف', $rel); $nDup++ }
  [void]$plan.Add([pscustomobject]@{ action = $action; from = $rel; to = $to; dto = $dto; imgno = $imgno })
}
$plan | Export-Csv -LiteralPath (Join-Path $root '_rename_plan.csv') -NoTypeInformation -Encoding UTF8
Write-Host ""
Write-Host ("Will rename        : " + $nRen + "   (Drive has 573)")
Write-Host ("Duplicates to move : " + $nDup + "   (into _للحذف)")
Write-Host ("Left as they are   : " + $nKeep + "   (not on Drive yet)")
Write-Host "Full list: _rename_plan.csv"
Write-Host ""
$ans = Read-Host "Type YES to apply (anything else = stop, nothing changed)"
if ($ans -ne 'YES') { Write-Host "Stopped. Nothing changed."; exit }

$done = New-Object System.Collections.ArrayList; $err = 0
foreach ($r in $plan) {
  if ($r.action.StartsWith('KEEP')) { continue }
  $src = Join-Path $root $r.from; $dst = Join-Path $root $r.to
  try {
    if (Test-Path -LiteralPath $dst) { throw "target exists" }
    [void][System.IO.Directory]::CreateDirectory((Split-Path -Parent $dst))
    Move-Item -LiteralPath $src -Destination $dst -ErrorAction Stop
    [void]$done.Add([pscustomobject]@{ from = $r.from; to = $r.to })
  } catch { $err++; Write-Host ("  FAILED: " + $r.from + "  (" + $_.Exception.Message + ")") }
}
$done | Export-Csv -LiteralPath $log -NoTypeInformation -Encoding UTF8
Write-Host ""
Write-Host ("Done. Moved: " + $done.Count + "   Failed: " + $err)
Write-Host "Undo any time:  powershell -ExecutionPolicy Bypass -File .\knooz_rename_weapons.ps1 -Undo"
