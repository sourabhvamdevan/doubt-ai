

from utilities.llm import GeminiLLM

class SubjectClassifier:
    def __init__(self):
        self.llm = GeminiLLM()
        
    def classify(self, query: str) -> str:
        prompt = f"""
        Classify this academic question into one of these categories:
        - Math
        - Physics
        - Chemistry
        - General
        
        Question: {query}
        
        Respond ONLY with one of the category names.
        """
        
        response = self.llm.generate(prompt, temperature=0.1)
        return response.strip()