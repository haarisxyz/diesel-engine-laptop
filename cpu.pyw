import psutil
import time
import threading
import pygame
import os

# Tracks CPU usage and plays engine sounds based on load.

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SEARCH_PATHS = [
    os.path.join(BASE_PATH, "truck-sounds"),
    os.path.expanduser("~/Documents/diesel-engine")
]

SOUND_FILES = {
    'low':  '40',
    'med':  '70',
    'high': '100'
}

CHECK_INTERVAL = 2.0

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.music.set_volume(1.0)

current_band = None

def find_sound(name):
    for path in SEARCH_PATHS:
        for ext in ['.mp3', '.wav']:
            full_path = os.path.join(path, f"{name}{ext}")
            if os.path.exists(full_path):
                return full_path
    return None

def get_cpu_band():
    cpu = psutil.cpu_percent(interval=1)
    if cpu <= 40:
        return 'low'
    elif cpu <= 90:
        return 'med'
    else:
        return 'high'

def play_looping_sound(band):
    try:
        path = find_sound(SOUND_FILES[band])
        if not path:
            return
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
    except Exception:
        pass

def main():
    global current_band
    while True:
        band = get_cpu_band()
        
        if band != current_band:
            current_band = band
            threading.Thread(target=play_looping_sound, args=(band,), daemon=True).start()
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()