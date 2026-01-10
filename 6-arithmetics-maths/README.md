# Chapter 6: Arithmetic Operations & Math Functions

## 📚 What You'll Learn
Master mathematical operations in Python, from basic arithmetic to useful built-in functions!

## 🎯 Learning Objectives
- Understand basic arithmetic operators (+, -, *, /, %, **, //)
- Learn augmented assignment operators (+=, -=, *=, etc.)
- Use built-in math functions (round, abs, pow, max, min)
- Apply mathematical operations to solve problems

## 📖 Concept Explanation

### Basic Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 2` | `3.0` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulus | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Augmented Assignment Operators
These combine an operation with assignment:

```python
x = 10

# Instead of: x = x + 5
x += 5  # Shorter way (x is now 15)

# Instead of: x = x - 3
x -= 3  # Shorter way (x is now 12)

# Instead of: x = x * 2
x *= 2  # Shorter way (x is now 24)

# Instead of: x = x / 4
x /= 4  # Shorter way (x is now 6.0)

# Instead of: x = x ** 2
x **= 2  # Shorter way (x is now 36.0)

# Instead of: x = x % 5
x %= 5  # Shorter way (x is now 1.0)
```

### Built-in Math Functions

#### `round(number)` - Round to Nearest Integer
```python
print(round(3.14))    # Output: 3
print(round(3.7))     # Output: 4
print(round(3.5))     # Output: 4 (rounds to nearest even)
print(round(4.5))     # Output: 4 (rounds to nearest even)
```

#### `abs(number)` - Absolute Value
```python
print(abs(-5))    # Output: 5
print(abs(5))     # Output: 5
print(abs(-3.14)) # Output: 3.14
```

#### `pow(base, exponent)` - Power
```python
print(pow(2, 3))   # Output: 8 (2^3)
print(pow(5, 2))   # Output: 25 (5^2)
print(2 ** 3)      # Output: 8 (alternative syntax)
```

#### `max()` - Maximum Value
```python
print(max(1, 5, 3))        # Output: 5
print(max(10, 20, 15, 8))  # Output: 20
```

#### `min()` - Minimum Value
```python
print(min(1, 5, 3))        # Output: 1
print(min(10, 20, 15, 8))  # Output: 8
```

## 💡 Examples

### Example 1: Calculator Operations
```python
a = 10
b = 3

print(f"{a} + {b} = {a + b}")   # 10 + 3 = 13
print(f"{a} - {b} = {a - b}")   # 10 - 3 = 7
print(f"{a} * {b} = {a * b}")   # 10 * 3 = 30
print(f"{a} / {b} = {a / b}")   # 10 / 3 = 3.333...
print(f"{a} // {b} = {a // b}") # 10 // 3 = 3 (floor division)
print(f"{a} % {b} = {a % b}")   # 10 % 3 = 1 (remainder)
print(f"{a} ** {b} = {a ** b}") # 10 ** 3 = 1000
```

### Example 2: Augmented Operators in Action
```python
score = 0
score += 10  # Player earned 10 points (score = 10)
score += 5   # Player earned 5 more points (score = 15)
score -= 3   # Player lost 3 points (score = 12)
score *= 2   # Double points bonus! (score = 24)
```

### Example 3: Useful Math Functions
```python
# Find the largest number
numbers = [45, 23, 67, 12, 89, 34]
largest = max(numbers)
print(f"Largest: {largest}")  # 89

# Round prices
price = 19.99
tax = price * 0.07  # 7% tax = 1.3993
total = round(price + tax, 2)  # Round to 2 decimals
print(f"Total: ${total}")
```

## ✍️ Practice Exercises

### Exercise 1: Basic Calculator
Create variables for two numbers and display all operations:
```python
num1 = 15
num2 = 4
# Print: addition, subtraction, multiplication, division, modulus, power
```

### Exercise 2: Temperature Converter
```python
# Use formula: Fahrenheit = (Celsius * 9/5) + 32
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

### Exercise 3: Even or Odd Checker
```python
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

### Exercise 4: Area Calculator
```python
# Circle area: π * r²
import math
radius = 5
area = math.pi * (radius ** 2)
print(f"Area: {round(area, 2)}")
```

### Exercise 5: Grade Calculator
```python
# Calculate average of 5 test scores
test1, test2, test3, test4, test5 = 85, 90, 78, 92, 88
average = (test1 + test2 + test3 + test4 + test5) / 5
print(f"Average: {round(average, 1)}")
```

## 🔍 Important Concepts

### Division: / vs //
```python
print(7 / 2)   # Regular division: 3.5 (float)
print(7 // 2)  # Floor division: 3 (integer, rounded down)
```

### Modulus (%) - Remainder
```python
print(10 % 3)  # 1 (10 ÷ 3 = 3 remainder 1)
print(17 % 5)  # 2 (17 ÷ 5 = 3 remainder 2)

# Useful for:
# - Checking even/odd: number % 2 == 0 (even) or 1 (odd)
# - Cycling through values: index % length
```

### Order of Operations (PEMDAS)
Python follows mathematical order of operations:
1. **P**arentheses `()`
2. **E**xponents `**`
3. **M**ultiplication/Division `*`, `/`, `//`, `%`
4. **A**ddition/Subtraction `+`, `-`

```python
result = 2 + 3 * 4      # 14 (not 20) - multiplication first
result = (2 + 3) * 4    # 20 - parentheses first
```

## 📝 Common Use Cases

### Incrementing/Decrementing
```python
counter = 0
counter += 1  # Increment by 1
counter -= 1  # Decrement by 1
```

### Doubling/Halving
```python
value = 100
value *= 2  # Double (value = 200)
value /= 2  # Halve (value = 100.0)
```

### Finding Remainders
```python
# Check if divisible
if number % 5 == 0:
    print("Divisible by 5")
```

## 🚀 Try It Yourself
1. Create a program that calculates compound interest
2. Build a tip calculator (meal cost + tip percentage)
3. Make a BMI calculator (weight / height²)
4. Create a program that finds the max, min, and average of 5 numbers

## 🔗 Next Chapter
Continue to [Chapter 7: If Statements](../7-if/) to learn about conditional logic!
