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

def search_google_in_url(url):
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)
    
    for _ in range(10):
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.2)
        current_url = pyperclip.paste()
        
        if current_url.startswith(url):
            pyautogui.write("bitcoin price")
            pyautogui.press("enter")
            return f"Started search in tab with URL: {current_url}"
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)
    
    return "No tab with the URL found."

if __name__ == "__main__":
    print(search_google_in_url("https://www.google.de"))
