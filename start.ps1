$venvPath = ".\venv"
$requirementsPath = ".\src\requirements.txt"
$mainScript = ".\main.py"

if (!(Test-Path $venvPath)) {
    Write-Host "creating enviroment: $venvPath..."
    python -m venv $venvPath
    if ($?) {
        Write-Host "env successfully created."
    } else {
        Write-Host "error creating the enviroment." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "enviroment already created."
}

Write-Host "activating enviroment..."
& "$venvPath\Scripts\Activate.ps1"
if (-not $?) {
    Write-Host "error activating the enviroment." -ForegroundColor Red
    exit 1
}

if (Test-Path $requirementsPath) {
    Write-Host "installing requirements at: $requirementsPath..."
    pip install -r $requirementsPath
    if ($?) {
        Write-Host "requirements successfully installed."
    } else {
        Write-Host "error installing requirements." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "requirements.txt not found :: $requirementsPath" -ForegroundColor Red
    exit 1
}

if (Test-Path $mainScript) {
    Write-Host "project: $mainScript running..."
    python $mainScript
    if (-not $?) {
        Write-Host "error during initialization." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "main.py not found in: $mainScript" -ForegroundColor Red
    exit 1
}

# Write-Host "deactivating env..."
# deactivate
# Write-Host "process successfully done." -ForegroundColor Green