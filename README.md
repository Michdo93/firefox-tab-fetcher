# Firefox Tab Fetcher

This repository contains Python scripts to extract the titles or URLs of all open tabs of a running Firefox browser. It uses `xdotool` to perform window actions and `pyautogui` to simulate input.

## Funktionen

- **Get tab titles**: A script collects the titles of all open tabs in Firefox.
- **Get tab URLs**: Another script copies the URLs of the open tabs from the address bar.

## Voraussetzungen

- **Python** 3.x
- **Dependecies**:
  - `xdotool` (Install with `sudo apt install xdotool`)
  - `pyautogui` (Install with `pip install pyautogui`)

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

