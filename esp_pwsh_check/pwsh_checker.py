def checker(file_paths) -> str:
    return(
'[array]$filePaths = ' + '\"' + '\", \"'.join(file_paths) + '\"' + '''
if ($filePaths.Length -eq 0){
    Write-Output "No file paths were provided"
    exit 1
}

$finalResult = 0

function Checker {
	Write-Output "\nInstalling PSScriptAnalyzer"
	Install-Module PSScriptAnalyzer -Scope CurrentUser -Confirm:$False -Force

	foreach ($filepath in $filePaths) {
		Write-Output "Checking: $filepath"
		$result = Invoke-ScriptAnalyzer -Path $filepath
		if ($result.Length -gt 0) {
			Write-Output "PowerShell Script Error"
			Write-Output ($result | Format-Table | Out-String)
			$finalResult = 1
		} else {
			Write-Output "PowerShell Script OK\n"
		}
	}

	if ($finalResult -ne 0){
		exit 1
	}
}

Checker
''')
