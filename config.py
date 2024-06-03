from core.utilities.json_settings_file import JsonSettingsFile
from dotenv import load_dotenv
import os

load_dotenv()
settings = JsonSettingsFile("config.json")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
BASE_API_URL = settings.get_value("BASE_API_URL")
TOKEN_URL = settings.get_value("TOKEN_URL")
