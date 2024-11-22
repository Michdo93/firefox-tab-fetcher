import os
import subprocess
import pyautogui
import time
import pyperclip  # Zum Abrufen der URL aus der Zwischenablage

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

def get_firefox_tab_urls():
    """Hole die URLs der offenen Firefox-Tabs und vermeide doppelte Zählungen."""
    minimize_firefox_windows()  # Minimiere alle Firefox-Fenster
    activate_firefox()  # Aktiviere Firefox
    time.sleep(1)  # Gib dem System Zeit, den Fokus zu setzen

    tab_urls = set()  # Set für eindeutige URLs
    max_attempts = 20  # Maximal 20 Versuche (keine feste Grenze mehr)
    attempts = 0

    while attempts < max_attempts:
        # Setze den Fokus auf die Adressleiste und kopiere die URL
        pyautogui.hotkey("ctrl", "l")  # Fokus auf die Adressleiste setzen
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")  # URL in die Zwischenablage kopieren
        time.sleep(0.2)

        # Hole die URL aus der Zwischenablage
        url = pyperclip.paste()

        # Vermeide doppelte URLs
        if url in tab_urls:
            break  # Wenn die URL bereits in der Liste ist, beende die Schleife
        tab_urls.add(url)  # Füge die URL zur Liste hinzu

        # Wechsle zum nächsten Tab
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)  # Warte kurz, damit der nächste Tab geladen wird

        attempts += 1

    return list(tab_urls)

if __name__ == "__main__":
    try:
        urls = get_firefox_tab_urls()
        print("URLs der offenen Firefox-Tabs:")
        for idx, url in enumerate(urls, start=1):
            print(f"Tab {idx}: {url}")
    except RuntimeError as e:
        print(f"Fehler: {e}")
