import calculator
# from calculator import *

# Direct function calls
print(calculator.add(10, 5))        # ➝ 15
print(calculator.subtract(10, 5))   # ➝ 5
print(calculator.multiply(10, 5))   # ➝ 50
print(calculator.divide(10, 5))     # ➝ 2.0

# Using the dispatcher
result = calculator.calculate('*', 7, 3)
print(result)  # ➝ 21
