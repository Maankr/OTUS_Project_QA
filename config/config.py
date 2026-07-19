from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")
UI_URL = os.getenv("UI_URL")