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

def search_google_in_tab(title):
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)
    
    # Track if we've checked all available tabs
    tab_checked = set()

    while True:
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        window_title = result.stdout.strip()

        # If the tab with the desired title is found
        if title in window_title:
            pyautogui.hotkey("ctrl", "l")  # Focus address bar
            pyautogui.write("bitcoin price")
            pyautogui.press("enter")
            return f"Started search in tab with title: {window_title}"

        # If this tab has already been checked, stop
        if window_title in tab_checked:
            return "No more tabs to check or tab with title not found."

        tab_checked.add(window_title)
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)

if __name__ == "__main__":
    print(search_google_in_tab("Google"))
