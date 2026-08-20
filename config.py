from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("IRONSCALES_API_KEY")
COMPANY_ID = os.getenv("IRONSCALES_COMPANY_ID")
SCOPE = os.getenv("IRONSCALES_SCOPE")