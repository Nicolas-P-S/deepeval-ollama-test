import os
from dotenv import load_dotenv
from deepeval.models import OpenAIModel

load_dotenv()

def create_judge():
    api_key = os.getenv("GROQ_API_KEY")

    return OpenAIModel(
        model="openai/gpt-oss-120b",
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        temperature=0
    )