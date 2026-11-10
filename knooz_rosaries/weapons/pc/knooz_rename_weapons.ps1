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
  $byFull[$p[0] + '|' + $p[1]] = $target
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
  $target = $null
  if ($dto) {
    if ($byFull.ContainsKey($dto + '|' + $imgno)) { $target = $byFull[$dto + '|' + $imgno] }
    elseif ((-not $imgno) -and $byDate.ContainsKey($dto) -and $byDate[$dto].Count -eq 1) { $target = $byDate[$dto][0] }
  }
  if (-not $target) { $action = 'KEEP (not on Drive yet)'; $to = $rel; $nKeep++ }
  elseif (-not $used.ContainsKey($target)) { $used[$target] = 1; $action = 'RENAME'; $to = $target; $nRen++ }
  else { $action = 'DUPLICATE -> _للحذف'; $to = [System.IO.Path]::Combine('_للحذف', $rel); $nDup++ }
  [void]$plan.Add([pscustomobject]@{ action = $action; from = $rel; to = $to; dto = $dto; imgno = $imgno })
}
$plan | Export-Csv -LiteralPath (Join-Path $root '_rename_plan.csv') -NoTypeInformation -Encoding UTF8
Write-Host ""
Write-Host ("Will rename        : " + $nRen + "   (Drive has 330)")
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
