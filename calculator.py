# calculator.py

import math
from typing import TypeVar, Union
import re

T = TypeVar('T', int, float)


class Calculator:
    def __init__(self):
        self.is_radians = True  # Default to radians

    def set_angle_mode(self, mode: str):
        """Sets the angle mode (radians or degrees)."""
        if mode.lower() == 'radians':
            self.is_radians = True
        elif mode.lower() == 'degrees':
            self.is_radians = False
        else:
            print("Invalid mode. Defaulting to radians.")
            self.is_radians = True

    def basic_operation(self, operation: str, a: T, b: T) -> Union[T, str]:
        """Performs basic arithmetic operations."""
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b if b != 0 else 'Error: Division by zero'
        else:
            return 'Error: Invalid operation'

    def advanced_function(self, func: str, value: T) -> Union[T, str]:
        """Performs advanced mathematical functions."""
        if not self.is_radians:  # Convert to radians if using degrees
            value = math.radians(value)

        functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'exp': math.exp,
            'fact': math.factorial
        }

        if func in functions:
            result = functions[func](value)
            if func in ['sin', 'cos', 'tan']:
                result = self._clean_trig_output(result)
            return result
        return 'Error: Invalid function'

    def unit_conversion(self, unit_from: str, unit_to: str, value: T) -> Union[T, str]:
        """Converts between different units."""
        conversions = {
            ('kg', 'lb'): 2.20462,
            ('lb', 'kg'): 1 / 2.20462,
            ('km', 'miles'): 0.621371,
            ('miles', 'km'): 1 / 0.621371
        }

        if (unit_from, unit_to) in conversions:
            return value * conversions[(unit_from, unit_to)]
        return 'Error: Invalid conversion'

    def evaluate_expression(self, expression: str) -> Union[T, str]:
        """Evaluate mathematical expression safely with angle mode consideration."""
        try:
            # Replace constants
            expression = expression.replace('pi', 'math.pi').replace('e', 'math.e')

            # Trig function adjustments
            def replace_trig(match):
                func = match.group(1)
                arg = match.group(2)
                if not self.is_radians:
                    return f"__clean_trig__(math.{func}(math.radians({arg})))"
                else:
                    return f"__clean_trig__(math.{func}({arg}))"

            expression = re.sub(r'\b(sin|cos|tan)\(([^()]+)\)', replace_trig, expression)

            # Replace ln() → math.log()
            expression = re.sub(r'\bln\(([^()]+)\)', r'math.log(\1)', expression)

            # Replace log() → math.log10()
            expression = re.sub(r'\blog\(([^()]+)\)', r'math.log10(\1)', expression)

            # Replace e^x → math.exp(x)
            expression = re.sub(r'\be\^([0-9.]+)', r'math.exp(\1)', expression)

            # Replace x! → math.factorial(x)
            expression = re.sub(r'(\d+)!', r'math.factorial(\1)', expression)

            # Replace other math functions
            for func in ['sqrt']:
                expression = re.sub(rf'\b{func}\b', f'math.{func}', expression)

            # Define trig cleanup
            def __clean_trig__(val):
                return 0.0 if abs(val) < 1e-10 else val

            result = eval(expression, {"math": math, "__clean_trig__": __clean_trig__})
            return result

        except (SyntaxError, NameError, ValueError) as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"

    def _clean_trig_output(self, val: float) -> float:
        """Rounds very small floating point results (e.g., sin(pi)) to 0.0."""
        return 0.0 if abs(val) < 1e-10 else val
