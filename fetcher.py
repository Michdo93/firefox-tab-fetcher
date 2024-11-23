import os
import subprocess
import pyautogui
import time


# --- Utility Functions ---
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


# --- Core Tab Functions ---
def list_tab_titles():
    """List all tab titles."""
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)

    titles = []
    checked_tabs = set()

    while True:
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        title = result.stdout.strip()

        if title in checked_tabs:
            break

        titles.append(title)
        checked_tabs.add(title)

        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)

    return titles


def list_tab_urls():
    """List all tab URLs."""
    # Requires a tool to extract the URL, such as a browser extension or specific scripts.
    raise NotImplementedError("Fetching URLs requires additional tooling.")


def count_tabs():
    """Count the number of open tabs."""
    return len(list_tab_titles())


def fetch_tab_by_title(title):
    """Fetch a tab by its title keyword."""
    titles = list_tab_titles()
    for tab_title in titles:
        if title in tab_title:
            return tab_title
    return None


def fetch_tab_by_url(url):
    """Fetch a tab by its URL keyword."""
    # Placeholder for URL-based fetching; requires additional tooling.
    raise NotImplementedError("Fetching URLs requires additional tooling.")


def close_tab_by_title(title):
    """Close a tab with the specified title."""
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)

    checked_tabs = set()

    while True:
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        window_title = result.stdout.strip()

        if window_title in checked_tabs:
            break

        if title in window_title:
            pyautogui.hotkey('ctrl', 'w')
            return f"Closed tab with title: {window_title}"

        checked_tabs.add(window_title)
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)

    return f"No tab with title containing '{title}' found."


def open_new_tab(url):
    """Open a new tab with the specified URL."""
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.write(url, interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)  # Allow the tab to load
    return f"Opened a new tab with URL: {url}"


def search_in_tab(title, search_term):
    """Search in a tab with a specific title."""
    minimize_firefox_windows()
    activate_firefox()
    time.sleep(1)

    checked_tabs = set()

    while True:
        result = subprocess.run(
            ["xdotool", "getactivewindow", "getwindowname"],
            stdout=subprocess.PIPE,
            text=True,
        )
        window_title = result.stdout.strip()

        if window_title in checked_tabs:
            break

        if title in window_title:
            pyautogui.click(x=300, y=50)  # Adjust coordinates for search bar
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.write(search_term, interval=0.1)
            pyautogui.press('enter')
            return f"Searched for '{search_term}' in tab: {window_title}"

        checked_tabs.add(window_title)
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5)

    return f"No tab with title containing '{title}' found."


# --- Main Function ---
def main():
    try:
        # Example workflow
        print("Listing all tab titles:")
        titles = list_tab_titles()
        print("\n".join(titles))

        print("\nCounting tabs:")
        print(f"Total open tabs: {count_tabs()}")

        print("\nSearching for a tab with 'Google' in the title:")
        google_tab = fetch_tab_by_title("Google")
        print(f"Found tab: {google_tab}" if google_tab else "No tab found.")

        print("\nClosing a tab with 'Google' in the title:")
        close_message = close_tab_by_title("Google")
        print(close_message)

        print("\nOpening a new Google tab:")
        open_message = open_new_tab("https://www.google.de")
        print(open_message)

        print("\nPerforming a search in a tab with 'Google' in the title:")
        search_message = search_in_tab("Google", "bitcoin price")
        print(search_message)

    except RuntimeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
