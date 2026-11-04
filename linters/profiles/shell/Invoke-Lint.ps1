<#
.SYNOPSIS
Fails on every PSScriptAnalyzer diagnostic, including suppressed diagnostics.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$Path,

    [string]$Settings = (Join-Path $PSScriptRoot 'PSScriptAnalyzerSettings.psd1')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

try {
    Import-Module PSScriptAnalyzer -ErrorAction Stop
    if (-not (Test-Path -LiteralPath $Path -PathType Container)) {
        throw 'Path must be an existing directory containing PowerShell sources.'
    }
    $files = @(Get-ChildItem -LiteralPath $Path -Recurse -File |
        Where-Object { $_.Extension -in @('.ps1', '.psm1', '.psd1') })
    if ($files.Count -eq 0) {
        throw 'No PowerShell sources found; an empty scan is not a passing check.'
    }
    $issues = @(Invoke-ScriptAnalyzer -Path $Path -Recurse -Settings $Settings -IncludeSuppressed)
    $issues | Format-Table -AutoSize
    if ($issues.Count -gt 0) {
        exit 1
    }
    exit 0
}
catch {
    [Console]::Error.WriteLine($_.Exception.Message)
    exit 2
}
