# from dotenv import load_dotenv, find_dotenv
import os

# load_dotenv(verbose=True)

FROM_EMAIL = os.environ.get("FROM_EMAIL")
TO_EMAIL = os.environ.get("TO_EMAIL")
KEY = os.environ.get("KEY")
SMTP_SSL = os.environ.get("SMTP_SSL")

if not FROM_EMAIL or not KEY:
    raise SystemExit('FROM_EMAIL/KEY pair not set, check .env file')
