import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read BASE_URL
BACKEND_URL = os.getenv("BASE_URL")