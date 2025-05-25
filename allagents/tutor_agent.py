

from utilities.classifier import SubjectClassifier
from utilities.memory import MemoryBuffer
from allagents.math_agent import MathAgent
from allagents.physics_agent import PhysicsAgent
from allagents.chemistry_agent import ChemistryAgent

class TutorAgent:
    def __init__(self, temperature=0.7):
        self.classifier = SubjectClassifier()
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()
        self.chemistry_agent = ChemistryAgent()
        self.temperature = temperature
        
    def ask(self, question: str, memory: MemoryBuffer) -> str:
        subject = self.classifier.classify(question)
        memory.add("user", question)
        
        if "math" in subject.lower():
            response = self.math_agent.answer(question, memory)
        elif "physics" in subject.lower():
            response = self.physics_agent.answer(question, memory)
        elif "chemistry" in subject.lower():
            response = self.chemistry_agent.answer(question, memory)
        else:
            response = f"I can help with Math, Physics, and Chemistry questions. Your question seems to be about {subject}. Please try again with a more specific question."
        
        memory.add("assistant", response)
        return response