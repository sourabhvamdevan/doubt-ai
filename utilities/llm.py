

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiLLM:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def generate(self, prompt, temperature=0.7):
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": temperature,
                    "max_output_tokens": 2048,
                }
            )
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"