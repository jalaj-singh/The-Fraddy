import os
import configparser

# --- Configuration Setup ---
config = configparser.ConfigParser()
# Assume config.ini is in the parent directory of the src folder
config.read(os.path.join(os.path.dirname(__file__), '..', 'config.ini'))

# --- APIs and Services ---
WOLFRAMALPHA_APP_ID = config.get('WOLFRAMALPHA', 'APP_ID', fallback='YOUR_APP_ID')
OPENWEATHERMAP_API_KEY = config.get('OPENWEATHERMAP', 'API_KEY', fallback='YOUR_API_KEY')
NEWSAPI_API_KEY = config.get('NEWSAPI', 'API_KEY', fallback='YOUR_API_KEY')
GMAIL_EMAIL = config.get('GMAIL', 'EMAIL', fallback='YOUR_EMAIL@gmail.com')
GMAIL_PASSWORD = config.get('GMAIL', 'PASSWORD', fallback='YOUR_PASSWORD')
SSH_HOST = config.get('SSH', 'HOST', fallback=None)
SSH_USER = config.get('SSH', 'USER', fallback=None)
SSH_PASSWORD = config.get('SSH', 'PASSWORD', fallback=None)

# --- File Paths ---
HOME_DIR = os.path.expanduser("~")
PYCHARM_PATH = config.get('PATHS', 'PYCHARM', fallback=None)
VSCODE_PATH = config.get('PATHS', 'VSCODE', fallback=None)
CHROME_DRIVER_PATH = config.get('PATHS', 'CHROME_DRIVER', fallback=None)
MUSIC_FOLDER_PATH = config.get('PATHS', 'MUSIC_FOLDER', fallback=os.path.join(HOME_DIR, "Music"))
NOTEPAD_FILE = os.path.join(os.path.dirname(__file__), '..', 'notepad.txt')
