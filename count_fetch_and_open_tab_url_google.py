import os
import subprocess
import pyautogui
import time
import pyperclip

def minimize_firefox_windows():
    """Minimizes all open Firefox windows."""
    result = subprocess.run(
        ["xdotool", "search", "--class", "firefox"],
        stdout=subprocess.PIPE,
        text=True,
    )
    window_ids = result.stdout.strip().split("\n")
    if not window_ids:
        raise RuntimeError("No Firefox windows found.")
    for window_id in window_ids:
        os.system(f"xdotool windowminimize {window_id}")

def activate_firefox():
    """Activates the first Firefox window, even if minimized."""
    result = subprocess.run(
        ["xdotool", "search", "--class", "firefox"],
        stdout=subprocess.PIPE,
        text=True,
    )
    window_ids = result.stdout.strip().split("\n")
    if not window_ids:
        raise RuntimeError("No Firefox windows found.")
    os.system(f"xdotool windowmap {window_ids[0]}")
    os.system(f"xdotool windowactivate {window_ids[0]}")
    time.sleep(0.5)

def fetch_and_open_tab_by_url(url):
    """Checks all tabs for a specific URL. If not found, opens a new tab."""
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)

    tab_checked = set()
    tab_found = False

    while True:
        # Focus on the address bar and copy the current URL
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.2)
        current_url = pyperclip.paste()

        if current_url.startswith(url):
            tab_found = True
            break

        if current_url in tab_checked:
            break

        tab_checked.add(current_url)
        pyautogui.hotkey('ctrl', 'tab')  # Switch to the next tab
        time.sleep(0.5)

    if not tab_found:
        # Open a new tab and navigate to the URL
        pyautogui.hotkey("ctrl", "t")
        time.sleep(0.5)
        pyautogui.write(url, interval=0.1)
        pyautogui.press("enter")

if __name__ == "__main__":
    # Specify the desired URL to search for or open
    fetch_and_open_tab_by_url("https://www.google.de/")
