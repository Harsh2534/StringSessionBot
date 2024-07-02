import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "28132883").strip()
API_HASH = os.getenv("API_HASH", "22eefd902a5b8edfceeeab1487ed60c8").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7052387929:AAEBUp_d-7-PA7tXiQ7Y6I9XlCri9d6qrPQ").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "-1001948462404")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
