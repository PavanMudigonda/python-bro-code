# ============================================
# Chapter 6: Arithmetic Operations & Math Functions
# ============================================
# Python supports various arithmetic operations and mathematical functions

# ============================================
# AUGMENTED ASSIGNMENT OPERATORS
# ============================================
# These operators combine an operation with assignment

friends: int = 0

# Addition assignment: adds value and assigns result
friends = friends + 1  # Long form
friends += 1           # Short form (augmented) - same result

# Subtraction assignment
friends = friends - 2  # Long form
friends -= 2           # Short form (augmented) - same result

friends: int = 5

# Multiplication assignment
friends = friends * 3  # Long form
friends *= 3           # Short form (augmented) - multiplies friends by 3

# Division assignment
friends /= 3  # Divides friends by 3

# Exponentiation (power) assignment
friends = friends ** 2  # Long form: friends to the power of 2
friends **= 2           # Short form: squares the value

# Modulus (remainder) assignment
remainder = friends % 2  # Gets remainder when friends is divided by 2
# print(remainder)  # Useful for checking if number is even (0) or odd (1)

# ============================================
# BUILT-IN MATH FUNCTIONS
# ============================================
x: float = 3.14
y: int = 4
z: int = 15

# round() - rounds a number to nearest integer
result = round(x)  # Result: 3 (3.14 rounds to 3)

# abs() - returns absolute value (always positive)
result = abs(y)    # Result: 4 (abs(-4) would also be 4)

# pow() - raises number to a power
result = pow(z, 3)  # Result: 15^3 = 3375

# max() - returns the largest value
result = max(x, y, z)  # Result: 15 (largest of 3.14, 4, 15)

# min() - returns the smallest value
result = min(x, y, z)  # Result: 3.14 (smallest of 3.14, 4, 15)

# print(result)

# ============================================
# OTHER USEFUL MATH OPERATIONS
# ============================================
# Addition: a + b
# Subtraction: a - b
# Multiplication: a * b
# Division: a / b (always returns float)
# Floor Division: a // b (division rounded down to integer)
# Modulus: a % b (remainder of division)
# Exponentiation: a ** b (a to the power of b)