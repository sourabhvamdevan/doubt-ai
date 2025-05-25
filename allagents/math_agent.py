

from tools.calculator import MathCalculator
from utilities.llm import GeminiLLM

class MathAgent:
    def __init__(self):
        self.calculator = MathCalculator()
        self.llm = GeminiLLM()
        
    def answer(self, question: str, memory) -> str:
        # First try direct calculation
        calc_result = self.calculator.calculate(question)
        if "error" not in calc_result:
            explanation = self.llm.generate(
                f"Explain this math solution in simple terms: {question} = {calc_result['result']}",
                temperature=0.3
            )
            return f"**Solution:** {calc_result['result']}\n\n**Explanation:** {explanation}"
        
        # If calculation fails, use LLM
        prompt = f"""
        You are a math tutor. Answer this question clearly with step-by-step explanation:
        Question: {question}
        Context from previous conversation: {memory.get_context()}
        """
        return self.llm.generate(prompt)