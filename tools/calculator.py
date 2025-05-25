

from sympy import symbols, sympify, solve, simplify, latex
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication
from sympy.parsing.sympy_parser import parse_expr

class MathCalculator:
    def __init__(self):
        self.transformations = standard_transformations + (implicit_multiplication,)
        
    def calculate(self, expression: str):
        try:
            expr = parse_expr(expression, transformations=self.transformations)
            simplified = simplify(expr)
            return {
                "result": str(simplified),
                "latex": latex(simplified),
                "steps": f"Simplified: {latex(expr)} → {latex(simplified)}"
            }
        except Exception as e:
            return {"error": str(e)}
    
    def solve_equation(self, equation: str, variable='x'):
        try:
            x = symbols(variable)
            solutions = solve(equation, x)
            return {
                "solutions": [str(sol) for sol in solutions],
                "latex": latex(solutions),
                "steps": f"Solved {equation} for {variable}"
            }
        except Exception as e:
            return {"error": str(e)}