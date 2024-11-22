import os
import subprocess
import pyautogui
import time

def minimize_firefox_windows():
    """Minimiert alle geöffneten Firefox-Fenster."""
    result = subprocess.run(
        ["xdotool", "search", "--class", "firefox"],
        stdout=subprocess.PIPE,
        text=True,
    )
    window_ids = result.stdout.strip().split("\n")

    if not window_ids:
        raise RuntimeError("Kein Firefox-Fenster gefunden.")

    for window_id in window_ids:
        os.system(f"xdotool windowminimize {window_id}")

def activate_firefox():
    """Aktiviere Firefox, auch wenn es minimiert ist."""
    result = subprocess.run(
        ["xdotool", "search", "--class", "firefox"],
        stdout=subprocess.PIPE,
        text=True,
    )
    window_ids = result.stdout.strip().split("\n")

    if not window_ids:
        raise RuntimeError("Kein Firefox-Fenster gefunden.")

    for window_id in window_ids:
        os.system(f"xdotool windowmap {window_id}")
        os.system(f"xdotool windowactivate {window_id}")
        time.sleep(0.5)
        break

def get_firefox_tab_titles():
    """Hole die Titel der offenen Firefox-Tabs und vermeide doppelte Zählungen."""
    minimize_firefox_windows()  # Minimiere alle Firefox-Fenster
    activate_firefox()  # Aktiviere Firefox
    time.sleep(1)  # Gib dem System Zeit, den Fokus zu setzen

    tab_titles = set()  # Set für eindeutige Titel
    max_attempts = 20  # Maximal 20 Versuche (keine feste Grenze mehr)
    attempts = 0

    while attempts < max_attempts:
        # Hole den Fenstertitel des aktiven Tabs
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        window_title = result.stdout.strip()

        # Vermeide doppelte Titel
        if window_title in tab_titles:
            break  # Wenn der Titel bereits in der Liste ist, beende die Schleife
        tab_titles.add(window_title)  # Füge den Titel zur Liste hinzu

        # Wechsle zum nächsten Tab
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)  # Warte kurz, damit der nächste Tab geladen wird

        attempts += 1

    return list(tab_titles)

if __name__ == "__main__":
    try:
        titles = get_firefox_tab_titles()
        print("Titel der offenen Firefox-Tabs:")
        for idx, title in enumerate(titles, start=1):
            print(f"Tab {idx}: {title}")
    except RuntimeError as e:
        print(f"Fehler: {e}")
