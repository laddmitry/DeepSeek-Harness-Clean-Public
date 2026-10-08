[CmdletBinding()]
param([ValidateSet('web','headless')][string]$Profile='web',[string]$Task)
$ErrorActionPreference='Stop'
$entry='C:\DSH\source\deepseek-harness-master\apps\cli\lib\bin.js'
if (!(Test-Path -LiteralPath $entry)) { throw 'Build/install Harness first.' }
if ($env:NODE_OPTIONS) { throw 'Use a clean launch environment without NODE_OPTIONS.' }
if ($Profile -eq 'headless' -and !$Task) { throw 'Headless requires a task.' }
Push-Location 'C:\DSH\workspace'
try {
  if ($Profile -eq 'headless') { & node $entry --profile headless $Task }
  else { & node $entry --profile web }
  if ($LASTEXITCODE -ne 0) { throw "Harness exit: $LASTEXITCODE" }
} finally { Pop-Location }
