@echo off
set "TARGET_DIR=%USERPROFILE%\Documents\diesel-engine"
set "SOURCE_DIR=.\truck-sounds"

echo Preparing Diesel Engine Laptop setup...

if not exist "%TARGET_DIR%" (
    echo Creating directory at %TARGET_DIR%...
    mkdir "%TARGET_DIR%"
)

echo Transferring truck sounds...
if exist "%SOURCE_DIR%" (
    copy "%SOURCE_DIR%\*" "%TARGET_DIR%\" >nul
    echo Sounds transferred to %TARGET_DIR%
) else (
    echo Error: %SOURCE_DIR% not found!
    exit /b 1
)

echo Installing Python dependencies (psutil, pygame)...
pip install psutil pygame --quiet

echo Setup complete! You can now run cpu.pyw.
pause
