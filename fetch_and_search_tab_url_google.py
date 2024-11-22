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

def get_firefox_tab_url_google():
    """Durchläuft die Tabs und sucht nach einem Tab, dessen URL mit 'https://www.google.de/' beginnt."""
    minimize_firefox_windows()  # Minimiert alle Firefox-Fenster
    activate_firefox()  # Aktiviert Firefox und bringt es in den Vordergrund
    time.sleep(1)

    for _ in range(10):  # Annahme: Maximal 10 Tabs
        # Fokus auf die Adressleiste setzen und URL kopieren
        pyautogui.hotkey("ctrl", "l")  # Setzt den Fokus auf die Adressleiste
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")  # Kopiere die URL in die Zwischenablage
        time.sleep(0.2)

        # Hole die URL aus der Zwischenablage mit pyperclip
        url = pyperclip.paste()

        # Prüfe, ob die URL mit 'https://www.google.de/' beginnt
        if url.startswith("https://www.google.de/"):
            return url  # Gibt die URL zurück, wenn sie mit 'https://www.google.de/' beginnt

        # Wechsle zum nächsten Tab
        pyautogui.hotkey("ctrl", "tab")  # Wechselt zum nächsten Tab
        time.sleep(0.5)  # Warte kurz, damit der nächste Tab geladen wird

    return None  # Gibt None zurück, wenn kein Tab mit der gesuchten URL gefunden wird

def search_in_google():
    """Gibt 'bitcoin price' in das Google-Suchfeld ein und startet die Suche."""
    # Setze den Fokus auf das Google-Suchfeld (klicke darauf und gebe den Text ein)
    pyautogui.click(300, 300)  # Klicken auf das Suchfeld von Google
    time.sleep(0.2)
    pyautogui.write("bitcoin price")  # Gibt 'bitcoin price' in das Suchfeld ein
    pyautogui.press("enter")  # Drückt Enter, um die Suche zu starten

if __name__ == "__main__":
    try:
        url = get_firefox_tab_url_google()
        if url:
            print(f"Tab gefunden mit URL, die mit 'https://www.google.de/' beginnt: {url}")
            search_in_google()  # Starte die Google-Suche im gefundenen Tab
        else:
            print("Kein Tab mit einer URL, die mit 'https://www.google.de/' beginnt, gefunden.")
    except RuntimeError as e:
        print(f"Fehler: {e}")
