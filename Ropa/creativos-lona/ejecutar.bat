@echo off
cd /d "%~dp0"
python generar.py %*
if errorlevel 1 py generar.py %*
pause
