import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# Load environment variables from a .env file, if it exists
load_dotenv(find_dotenv())

# Folders for file handling, with default values if not set in the .env file
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "user_files/uploads")
PROCESSED_FOLDER = os.getenv("PROCESSED_FOLDER", "user_files/extracted")
REPORT_FOLDER = os.getenv("REPORT_FOLDER", "user_files/reports")

# Model selection
model = os.getenv("MODEL", "gpt-4o")


def load_env_vars():
    # Load API keys and other secrets
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    fast_api_key = os.getenv("FAST_API_KEY")
    if not fast_api_key:
        raise ValueError("FAST_API_KEY environment variable not set")

    # Assign the OpenAI API key
    OpenAI.api_key = openai_api_key

    return fast_api_key
