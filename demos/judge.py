import os
from dotenv import load_dotenv
from deepeval.models import GeminiModel

load_dotenv()

def create_judge():
    api_key = os.getenv("API_KEY")
