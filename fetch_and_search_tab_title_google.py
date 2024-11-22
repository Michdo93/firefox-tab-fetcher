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

def get_firefox_tab_title_google_search():
    """Durchläuft die Tabs, sucht nach einem Tab, dessen Titel 'Google' enthält und führt eine Suche durch."""
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)

    for _ in range(10):  # Annahme: Maximal 10 Tabs
        # Hole den Fenstertitel des aktiven Tabs
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        window_title = result.stdout.strip()

        # Prüfe, ob "Google" im Titel enthalten ist
        if "Google" in window_title:
            pyautogui.write("bitcoin price")
            pyautogui.press("enter")
            return f"Suche nach 'bitcoin price' im Tab mit Titel 'Google' gestartet."

        # Wechsle zum nächsten Tab
        pyautogui.hotkey("ctrl", "tab")
        time.sleep(0.5)  # Warte kurz, damit der nächste Tab geladen wird

    return "Kein Tab mit 'Google' im Titel gefunden."

if __name__ == "__main__":
    try:
        result = get_firefox_tab_title_google_search()
        print(result)
    except RuntimeError as e:
        print(f"Fehler: {e}")
