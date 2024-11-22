# Firefox Tab Fetcher

This repository contains Python scripts to extract the titles or URLs of all open tabs of a running Firefox browser. It uses `xdotool` to perform window actions and `pyautogui` to simulate input.

## Functions

- **Get tab titles**: A script collects the titles of all open tabs in Firefox.
- **Get tab URLs**: Another script copies the URLs of the open tabs from the address bar.

### Descriptions
| **Filename**                          | **Description**                                                                                     |
|---------------------------------------|-----------------------------------------------------------------------------------------------------|
| fetch_and_close_tab_title_google.py   | Loops through open tabs, searches for a tab with "Google" in the title, and closes the tab if found. |
| fetch_and_close_tab_url_google.py     | Loops through open tabs, searches for a tab with a URL starting with "https://www.google.de/" and closes the tab if found. |
| fetch_and_search_tab_title_google.py  | Loops through open tabs, searches for a tab with "Google" in the title, and performs a Google search for "bitcoin price" in that tab if found. |
| fetch_and_search_tab_url_google.py    | Loops through open tabs, searches for a tab with a URL starting with "https://www.google.de/", and performs a Google search for "bitcoin price" in that tab if found. |
| fetch_tab_title_google.py             | Loops through open tabs, searches for a tab with "Google" in the title, and returns the title of the found tab. |
| fetch_tab_titles.py                   | Loops through all open tabs and returns the titles of the tabs.                                      |
| fetch_tab_url_google.py               | Loops through open tabs, searches for a tab with a URL starting with "https://www.google.de/", and returns the URL of the found tab. |
| fetch_tab_urls.py                     | Loops through all open tabs and returns the URLs of the tabs.                                       |
| fetch_and_open_tab_title_google.py    | Loops through open tabs, searches for a tab with "Google" in the title. If not found, opens a new Google tab. |
| fetch_and_open_tab_url_google.py      | Loops through open tabs, searches for a tab with a URL starting with "https://www.google.de/". If not found, opens a new Google tab. |
| count_fetch_and_close_tab_title_google.py | Counts all tabs, searches for a tab with "Google" in the title, and closes it if found. Stops after checking all tabs without duplication. |
| count_fetch_and_close_tab_url_google.py   | Counts all tabs, searches for a tab with a URL starting with "https://www.google.de/", and closes it if found. Stops after checking all tabs without duplication. |
| count_fetch_and_search_tab_title_google.py | Counts all tabs, searches for a tab with "Google" in the title, and performs a Google search for "bitcoin price" in that tab if found. Stops after checking all tabs without duplication. |
| count_fetch_and_search_tab_url_google.py   | Counts all tabs, searches for a tab with a URL starting with "https://www.google.de/", and performs a Google search for "bitcoin price" in that tab if found. Stops after checking all tabs without duplication. |
| count_fetch_and_open_tab_title_google.py   | Counts all tabs, searches for a tab with "Google" in the title. If not found, opens a new Google tab. Stops after checking all tabs without duplication. |
| count_fetch_and_open_tab_url_google.py     | Counts all tabs, searches for a tab with a URL starting with "https://www.google.de/". If not found, opens a new Google tab. Stops after checking all tabs without duplication. |

## Prerequisites/Requirements

- **Python** 3.x
- **Dependecies**:
  - `xdotool` (install with `sudo apt install xdotool`)
  - `pyautogui` (install with `pip install pyautogui`)
  - `pyperclip` (install with `pip install pyperclip`)

## Installation

1. Clone the Repository:

```bash
git clone https://github.com/dein-benutzername/firefox-tab-fetcher.git
cd firefox-tab-fetcher
```

2. Install the Python dependencies:

```
pip install -r requirements.txt
```

## Usage

### Reading tab titles

Execute the script `fetch_tab_titles.py`:

```
python fetch_tab_titles.py
```

### Reading tab URLs

Execute the script `fetch_tab_urls.py`:

```
python fetch_tab_urls.py
```

## Hints

    The Firefox window must be minimized when starting the script, as xdotool works better with minimized windows.
    Tested on Ubuntu with Firefox.

## License

MIT License. See [LICENSE](LICENSE) for more information.

