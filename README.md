# Roman Numerals to Integer

## Linux or MacOS
```shell
python3 -m venv .venv && . .venv/bin/activate
python test_convert.py
```

```shell
watch -n 3 'clear; python test_convert.py'
```

## Windoof (Powershell)
```shell
.\.venv\Scripts\Activate.ps1
python test_convert.py
```

### Test watching in Powershell (every 3 seconds)

```shell
while ($true) { Clear-Host; Get-Date -Format "HH:mm:ss"; python .\test_convert.py; Start-Sleep -Seconds 3 }
```