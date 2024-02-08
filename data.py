"""
Load data from config.ini
"""

import configparser
import os

SCRIPT_DIR = os.path.dirname(__file__)

# Load data from the config file
config = configparser.ConfigParser()
config.read('config.ini')

SESSIONS_FOLDER = config['FOLDERS']['SESSIONS_FOLDER']

OPENAI_API_KEY = config['OPENAI']['OPENAI_API_KEY']

ASSISTANT_ID = config['ASSISTANT']['ASSISTANT_ID']
THREAD_ID = config['ASSISTANT']['THREAD_ID']
SERVICE_GROUP = config['ASSISTANT']['SERVICE_GROUP']

SESSION_FILE = config['SESSION']['SESSION_FILE']
API_ID = config['SESSION']['API_ID']
API_HASH = config['SESSION']['API_HASH']

IP = config['PROXY']['IP']
PORT = config['PROXY']['PORT']
USERNAME = config['PROXY']['USERNAME']
PASSWORD = config['PROXY']['PASSWORD']
