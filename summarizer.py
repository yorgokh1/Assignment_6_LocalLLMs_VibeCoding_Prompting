import requests
from openai import OpenAI

class OllamaSummarizer:
    def __init__(self, model="llama3.1", instruction = "Create a concise summary of this text"):
        self.client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama'  # Required string but not used by Ollama
        )
        self.model = model
        self.instruction = instruction

    def summarize_text(self, text, max_tokens=500):
        """Summarize a given text"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{
                "role": "user",
                "content": f"{self.instruction}:\n\n{text}"
            }],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content

    def summarize_file(self, file_path):
        """Summarize content from a file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return self.summarize_text(text)
