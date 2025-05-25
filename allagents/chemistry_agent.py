

from utilities.llm import GeminiLLM

class ChemistryAgent:
    def __init__(self):
        self.llm = GeminiLLM()
        
    def answer(self, question: str, memory) -> str:
        prompt = f"""
        You are a chemistry tutor. Answer this question with clear explanations:
        Question: {question}
        Include relevant chemical equations if applicable.
        Previous conversation context: {memory.get_context()}
        """
        return self.llm.generate(prompt, temperature=0.5)