import os
import subprocess
import pyautogui
import time
import pyperclip

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

def close_tab_by_url(url):
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)
    
    # Track if we've checked all available tabs
    tab_checked = set()

    while True:
        pyautogui.hotkey("ctrl", "l")  # Focus on the address bar
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.2)
        current_url = pyperclip.paste()

        # If the tab with the desired URL is found
        if current_url.startswith(url):
            pyautogui.hotkey('ctrl', 'w')  # Close the tab
            return f"Closed tab with URL: {current_url}"

        # If this tab has already been checked, stop
        if current_url in tab_checked:
            return "No more tabs to check or tab with URL not found."

        tab_checked.add(current_url)
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)

if __name__ == "__main__":
    print(close_tab_by_url("https://www.google.de"))
