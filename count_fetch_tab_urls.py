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

def fetch_all_tab_urls():
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)

    tab_checked = set()
    tab_count = 0

    while True:
        pyautogui.hotkey("ctrl", "l")  # Focus on the address bar
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.2)
        current_url = pyperclip.paste()

        if current_url not in tab_checked:
            tab_count += 1

        if current_url in tab_checked:
            break

        tab_checked.add(current_url)
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)

    return tab_count

if __name__ == "__main__":
    print(f"Total number of open tabs: {fetch_all_tab_urls()}")
