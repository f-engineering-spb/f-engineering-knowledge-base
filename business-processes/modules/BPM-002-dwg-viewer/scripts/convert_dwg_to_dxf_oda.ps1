param(
  [Parameter(Mandatory = $true)]
  [string]$InputDir,

  [Parameter(Mandatory = $true)]
  [string]$OutputDir,

  [string]$OdaExe = "C:\Program Files\ODA\ODAFileConverter 27.1.0\ODAFileConverter.exe",
  [string]$Version = "ACAD2018",
  [string]$Filter = "*.DWG",
  [switch]$Recursive,
  [switch]$NoAudit
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $OdaExe)) {
  throw "ODA File Converter executable was not found: $OdaExe"
}

if (-not (Test-Path -LiteralPath $InputDir)) {
  throw "Input directory was not found: $InputDir"
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$recursiveFlag = if ($Recursive) { "1" } else { "0" }
$auditFlag = if ($NoAudit) { "0" } else { "1" }

& $OdaExe $InputDir $OutputDir $Version "DXF" $recursiveFlag $auditFlag $Filter

$dxfCount = @(Get-ChildItem -LiteralPath $OutputDir -Recurse -Filter "*.dxf" -File -ErrorAction SilentlyContinue).Count

if (($null -ne $LASTEXITCODE) -and ($LASTEXITCODE -ne 0)) {
  throw "ODA File Converter failed with exit code $LASTEXITCODE"
}

if ($dxfCount -eq 0) {
  throw "ODA File Converter finished but no DXF files were created in $OutputDir"
}

Write-Host "Created DXF files: $dxfCount"
