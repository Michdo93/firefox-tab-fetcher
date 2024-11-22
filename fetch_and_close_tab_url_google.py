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

def fetch_and_close_tab_url_google():
    """Durchläuft die Tabs, sucht nach dem Tab mit 'https://www.google.de/' im URL und schließt ihn."""
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)

    for _ in range(10):  # Annahme: Maximal 10 Tabs
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.2)

        url = pyperclip.paste()

        if url.startswith("https://www.google.de/"):  # Wenn URL mit Google beginnt
            pyautogui.hotkey("ctrl", "w")  # Tab schließen
            return f"Tab mit URL {url} geschlossen."

        pyautogui.hotkey("ctrl", "tab")
        time.sleep(0.5)

    return "Kein Tab mit einer URL, die mit 'https://www.google.de/' beginnt, gefunden."

if __name__ == "__main__":
    try:
        result = fetch_and_close_tab_url_google()
        print(result)
    except RuntimeError as e:
        print(f"Fehler: {e}")
