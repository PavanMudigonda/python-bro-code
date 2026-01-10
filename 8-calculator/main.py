# ============================================
# Chapter 8: Simple Calculator Program
# ============================================
# This program demonstrates how to build a basic calculator
# using user input and conditional statements

# ============================================
# Step 1: Get the operator from user
# ============================================
# Ask user which mathematical operation they want to perform
operator = input("Enter operator: (+ or - or * or / or %): ")

# ============================================
# Step 2: Get the numbers from user
# ============================================
# Get two numbers and convert them to floats (to handle decimals)
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

# ============================================
# Step 3: Perform the calculation based on operator
# ============================================
# Use if-elif-else to determine which operation to perform

if operator == "+":
    # Addition
    print(number1, "+", number2, "=", number1 + number2)
elif operator == "-":
    # Subtraction
    print(number1, "-", number2, "=", number1 - number2)
elif operator == "*":
    # Multiplication
    print(number1, "*", number2, "=", number1 * number2)
elif operator == "/":
    # Division
    print(number1, "/", number2, "=", number1 / number2)
elif operator == "%":
    # Modulus (remainder)
    print(number1, "%", number2, "=", number1 % number2)
else:
    # Invalid operator
    print(f'Invalid operator: {operator}')

# ============================================
# How this program works:
# ============================================
# 1. User selects an operator (+, -, *, /, %)
# 2. User enters two numbers
# 3. Program checks which operator was entered
# 4. Performs the corresponding calculation
# 5. Displays the result
#
# Note: We use float() instead of int() to handle decimal numbers