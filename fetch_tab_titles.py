import os
import subprocess
import pyautogui
import time

def minimize_firefox_windows():
    """Minimiert alle geöffneten Firefox-Fenster."""
    # Suche nach Firefox-Fenster-IDs
    result = subprocess.run(
        ["xdotool", "search", "--class", "firefox"],
        stdout=subprocess.PIPE,
        text=True,
    )
    window_ids = result.stdout.strip().split("\n")

    if not window_ids:
        raise RuntimeError("Kein Firefox-Fenster gefunden.")

    # Minimiere alle Fenster
    for window_id in window_ids:
        os.system(f"xdotool windowminimize {window_id}")

def activate_firefox():
    """Aktiviere Firefox, auch wenn es minimiert ist."""
    # Suche nach Firefox-Fenster-IDs
    result = subprocess.run(
        ["xdotool", "search", "--class", "firefox"],
        stdout=subprocess.PIPE,
        text=True,
    )
    window_ids = result.stdout.strip().split("\n")

    if not window_ids:
        raise RuntimeError("Kein Firefox-Fenster gefunden.")

    # Versuche, das erste Fenster zu aktivieren
    for window_id in window_ids:
        # Bringe das Fenster in den Vordergrund und aus dem minimierten Zustand
        os.system(f"xdotool windowmap {window_id}")
        os.system(f"xdotool windowactivate {window_id}")
        time.sleep(0.5)  # Warte kurz, um sicherzustellen, dass Firefox aktiviert ist
        break

def get_firefox_tab_titles():
    """Hole die Titel der offenen Firefox-Tabs."""
    # Minimiere zuerst alle Firefox-Fenster
    minimize_firefox_windows()

    # Aktiviere Firefox
    activate_firefox()
    time.sleep(1)  # Gib dem System Zeit, den Fokus zu setzen

    tab_titles = []
    for _ in range(10):  # Annahme: Maximal 10 Tabs
        # Hole den Fenstertitel des aktiven Tabs
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        window_title = result.stdout.strip()

        # Vermeide doppelte Titel und beende die Schleife
        if window_title in tab_titles:
            break
        tab_titles.append(window_title)

        # Wechsle zum nächsten Tab
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)  # Warte kurz, damit der nächste Tab geladen wird

    return tab_titles

if __name__ == "__main__":
    try:
        titles = get_firefox_tab_titles()
        print("Titel der offenen Firefox-Tabs:")
        for idx, title in enumerate(titles, start=1):
            print(f"Tab {idx}: {title}")
    except RuntimeError as e:
        print(f"Fehler: {e}")
