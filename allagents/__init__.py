

"""
AI Tutor Package

A multi-agent tutoring system for Math, Physics, and Chemistry.
"""

__version__ = "1.0.0"
__author__ = "SV"


from .tutor_agent import TutorAgent
from .math_agent import MathAgent
from .physics_agent import PhysicsAgent
from .chemistry_agent import ChemistryAgent

__all__ = [
    'TutorAgent',
    'MathAgent',
    'PhysicsAgent',
    'ChemistryAgent'
]