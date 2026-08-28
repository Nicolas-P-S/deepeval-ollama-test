import os
from dotenv import load_dotenv
from deepeval.models import GeminiModel

load_dotenv()

def create_judge():
    api_key = os.getenv("GEMINI_API_KEY")

    return GeminiModel(
        #model="gemini-3.6-flash",
        model="gemini-3.5-flash-lite",
        api_key=api_key,
    )

