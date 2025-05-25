

from tools.constants_lookup import PhysicsConstants
from utilities.llm import GeminiLLM

class PhysicsAgent:
    def __init__(self):
        self.constants = PhysicsConstants()
        self.llm = GeminiLLM()
        
    def answer(self, question: str, memory) -> str:
        # Check for physical constants
        if "constant" in question.lower():
            for const in self.constants.PHYSICS_CONSTANTS:
                if const in question.lower():
                    const_data = self.constants.lookup(const)
                    return f"The {const} is {const_data['value']} {const_data['unit']}"
        
        # General physics question
        prompt = f"""
        You are a physics tutor. Answer this question with proper formulas and units:
        Question: {question}
        Previous conversation context: {memory.get_context()}
        """
        return self.llm.generate(prompt, temperature=0.5)