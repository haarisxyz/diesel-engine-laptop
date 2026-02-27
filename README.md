# Diesel Engine Laptop

Turn your CPU usage into a diesel engine experience.

## Quick Start (Windows)

1. **Install Python**: Make sure you have Python installed.
2. **Clone/Download**: Get this repository on your PC.
3. **Run Setup**:
   - Double-click `setup.bat` in the project folder.
   - This will install dependencies (psutil, pygame) and copy the audio files to Documents\diesel-engine.
4. **Start the Engine**:
   - Double-click `cpu.pyw` or run `python cpu.pyw`.
   - The .pyw extension means it runs in the background without a console window.

## How it Works

The script monitors your CPU usage every 2 seconds:
- **Low (<= 40%)**: Idle engine sound.
- **Medium (41% - 90%)**: Working engine sound.
- **High (> 90%)**: Revving engine sound.

## Customizing Sounds

You can replace the sounds in truck-sounds\ or Documents\diesel-engine\:
- 40.mp3 or 40.wav: Low load.
- 70.mp3 or 70.wav: Medium load.
- 100.mp3 or 100.wav: High load.

## Stopping the Script

Since it runs in the background (.pyw), you can stop it via Task Manager:
1. Search for pythonw.exe.
2. Right-click and End Task.

---
Created for those who want their laptop to sound as hard-working as it feels.
