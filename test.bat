




@echo off
cd /d %~dp0

set "UI_DIR=.\ui_files"
set "PY_DIR=.\main"

for %%f in ("%UI_DIR%\*.ui") do (
    pyuic5 "%%f" -o "%PY_DIR%\%%~nf.py"
)

echo Conversion complete.
pause









