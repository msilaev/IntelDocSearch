import openai
from dotenv import load_dotenv
import os

load_dotenv()

class SummarizationService:
    def __init__(self):
        openai.api_key = os.getenv("OPEN_AI_KEY")

    def summarize(self, text: str) -> str:
        response = openai.Completion.create(
            engine="gpt-4-turbo",  # You can use a different engine if needed
            prompt=f"Summarize the following text:\n\n{text}",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].text.strip()