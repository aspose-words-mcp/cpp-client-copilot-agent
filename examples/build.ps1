param(
    [ValidateSet('Release','Debug')][string]$Configuration = 'Release',
    [string]$PackagesDirectory = (Join-Path $PSScriptRoot 'packages'),
    [string]$SourceFile = (Join-Path $PSScriptRoot 'main.cpp'),
    [string]$PlatformToolset = 'v142',
    [switch]$Run
)
$ErrorActionPreference = 'Stop'
$PackagesDirectory = (Resolve-Path -LiteralPath $PackagesDirectory).Path
$SourceFile = (Resolve-Path -LiteralPath $SourceFile).Path
foreach ($package in @('Aspose.Words.Cpp.26.9.0','CodePorting.Translator.Cs2Cpp.Framework.26.9.0')) {
    if (-not (Test-Path -LiteralPath (Join-Path $PackagesDirectory $package))) { throw "Missing $package; restore packages.config first." }
}
$vswhere = "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe"
if (-not (Test-Path -LiteralPath $vswhere)) { throw 'Install Visual Studio C++ Build Tools and the Windows SDK.' }
$msbuild = & $vswhere -latest -products '*' -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -find 'MSBuild\**\Bin\MSBuild.exe' | Select-Object -First 1
if (-not $msbuild) { throw 'C++ MSBuild not found.' }
Push-Location $PSScriptRoot
try {
    & $msbuild (Join-Path $PSScriptRoot 'WordsCppExamples.vcxproj') /t:Rebuild /m /nologo "/p:Configuration=$Configuration" /p:Platform=x64 "/p:PlatformToolset=$PlatformToolset" "/p:PackagesDirectory=$PackagesDirectory" "/p:ExampleSource=$SourceFile" /verbosity:minimal
    if ($LASTEXITCODE -ne 0) { throw 'Build failed.' }
    if ($Run) {
        $output = Join-Path $PSScriptRoot 'outputs'
        New-Item -ItemType Directory -Force $output | Out-Null
        Push-Location $output
        try {
            & (Join-Path $PSScriptRoot "build/x64/$Configuration/WordsCppExamples.exe")
            if ($LASTEXITCODE -ne 0) { throw "Program failed: $LASTEXITCODE" }
        } finally { Pop-Location }
    }
} finally { Pop-Location }
