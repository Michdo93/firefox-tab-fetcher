import os
import subprocess
import pyautogui
import time

def minimize_firefox_windows():
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

def close_tab_by_title(title):
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)
    
    for _ in range(10):
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        window_title = result.stdout.strip()
        if title in window_title:
            pyautogui.hotkey('ctrl', 'w')  # Close the tab
            return f"Closed tab with title: {window_title}"
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)
    return "No tab with the title found."

if __name__ == "__main__":
    print(close_tab_by_title("Google"))
