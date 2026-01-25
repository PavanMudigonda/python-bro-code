# If __name__ == '__main__': (this script can be imported OR run standalone)
#                            Functions and classes in this modeule can be reused
#                            when imported without executing the main block.
#                            This is useful for creating reusable modules.

# ex. library = Import library for functionality
#               When running library directly, display a help page

"""
calculator.py - A simple arithmetic library

Provides functions for basic math operations:
- add
- subtract
- multiply
- divide
- calculate (dispatches based on operator)

Can be imported as a library OR run standalone.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def calculate(operator, a, b):
    match operator:
        case '+':
            return add(a, b)
        case '-':
            return subtract(a, b)
        case '*':
            return multiply(a, b)
        case '/':
            return divide(a, b)
        case _:
            raise ValueError(f"Invalid operator: {operator}")

def main():
    try:
        operator = input("Enter operation (+, -, *, /): ").strip()
        a = float(input("Input value for a: "))
        b = float(input("Input value for b: "))
        result = calculate(operator, a, b)
        print(f"{a} {operator} {b} = {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()
