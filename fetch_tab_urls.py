import os
import subprocess
import pyautogui
import time
import pyperclip  # Importiere pyperclip für Zwischenablageoperationen

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
    """Hole die URLs der offenen Firefox-Tabs."""
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)

    tab_urls = []
    for _ in range(10):  # Annahme: Maximal 10 Tabs
        # Fokus auf die Adressleiste setzen und URL kopieren
        pyautogui.hotkey("ctrl", "l")  # Fokus auf die Adressleiste
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")  # Kopiere die URL
        time.sleep(0.2)

        # Hole die URL aus der Zwischenablage mit pyperclip
        url = pyperclip.paste()

        # Vermeide doppelte URLs und beende die Schleife
        if url in tab_urls:
            break
        tab_urls.append(url)

        # Wechsle zum nächsten Tab
        pyautogui.hotkey("ctrl", "tab")
        time.sleep(0.5)

    return tab_urls

if __name__ == "__main__":
    try:
        urls = get_firefox_tab_urls()
        print("URLs der offenen Firefox-Tabs:")
        for idx, url in enumerate(urls, start=1):
            print(f"Tab {idx}: {url}")
    except RuntimeError as e:
        print(f"Fehler: {e}")
