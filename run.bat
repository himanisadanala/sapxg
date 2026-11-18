@echo off
echo Starting SAPXG local web server on http://localhost:8000 ...
start "" http://localhost:8000
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0serve.ps1"
