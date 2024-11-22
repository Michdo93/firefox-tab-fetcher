import os
import subprocess
import pyautogui
import time

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
    """Activates Firefox, even if minimized."""
    result = subprocess.run(
        ["xdotool", "search", "--class", "firefox"],
        stdout=subprocess.PIPE,
        text=True,
    )
    window_ids = result.stdout.strip().split("\n")

    if not window_ids:
        raise RuntimeError("No Firefox windows found.")

    for window_id in window_ids:
        os.system(f"xdotool windowmap {window_id}")
        os.system(f"xdotool windowactivate {window_id}")
        time.sleep(0.5)
        break

def get_firefox_tab_title_google():
    """Loops through open tabs and searches for a tab with 'Google' in the title."""
    minimize_firefox_windows()  # Minimize all Firefox windows
    activate_firefox()  # Activate Firefox and bring it to the foreground
    time.sleep(1)

    for tab_index in range(10):  # Assume a maximum of 10 tabs
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        window_title = result.stdout.strip()

        if "Google" in window_title:
            pyautogui.hotkey("ctrl", "1")  # Switch to the tab with Google in the title
            return window_title  # Return the title if "Google" is found

        pyautogui.hotkey("ctrl", "tab")  # Switch to the next tab
        time.sleep(0.5)

    # If not found, open a new Google tab
    pyautogui.hotkey("ctrl", "t")  # Open a new tab
    time.sleep(0.5)
    #url="https://www.google.de"
    #pyautogui.write(url, interval=0.1)  # Write Google URL
    pyautogui.write("https:", interval=0.1)  # Tippt 'https'
    pyautogui.hotkey("shift", "7")  # Tippt '/' (Shift + 7 für '/')
    pyautogui.hotkey("shift", "7")  # Tippt '/' (Shift + 7 für '/')
    pyautogui.write("www.google.de", interval=0.1)  # Tippt die restliche URL
    pyautogui.press("enter")  # Press Enter to load Google
    return "New Google Tab Opened"

if __name__ == "__main__":
    try:
        title = get_firefox_tab_title_google()
        print(f"Tab found with title containing 'Google': {title}")
    except RuntimeError as e:
        print(f"Error: {e}")
