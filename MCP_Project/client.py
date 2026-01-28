from openai import OpenAI
from config import MODEL
from schemas import TOOLS

client = OpenAI()  # API Key - must be an environment variable

def send_to_model(messages):
    return client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS
    )
