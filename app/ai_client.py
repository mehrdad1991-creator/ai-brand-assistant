import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Read configuration from environment variables
API_KEY = os.getenv("AI_API_KEY")
BASE_URL = os.getenv("AI_BASE_URL")
MODEL_NAME = os.getenv("AI_MODEL", "gpt-4o")

# Validate that the API key is set
if not API_KEY:
    raise ValueError("AI_API_KEY is not set in the .env file")

# Create the OpenAI client, pointing to the Iranian gateway
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
)