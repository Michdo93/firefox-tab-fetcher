import os
import subprocess
import pyautogui
import time

def minimize_firefox_windows():
    """Minimize all Firefox windows."""
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
    """Activate the first Firefox window."""
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

def fetch_and_open_tab_by_title(title, url="https://www.google.de"):
    """Search for a tab by title, and open a new tab if not found."""
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)

    tab_checked = set()
    tab_found = False

    while True:
        # Get the title of the active tab
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        window_title = result.stdout.strip()

        # Check for duplicate tabs
        if window_title in tab_checked:
            break

        tab_checked.add(window_title)

        # Check if the title matches
        if title in window_title:
            tab_found = True
            break

        # Switch to the next tab
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)

    if not tab_found:
        # Open a new tab and go to the specified URL
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)
        pyautogui.write(url, interval=0.1)
        pyautogui.press('enter')

if __name__ == "__main__":
    title_keyword = "Google"
    try:
        fetch_and_open_tab_by_title(title_keyword)
        print(f"Ensured a tab with '{title_keyword}' exists.")
    except RuntimeError as e:
        print(f"Error: {e}")
