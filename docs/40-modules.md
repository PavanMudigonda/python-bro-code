# 📦 Modules

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/40-modules/40-modules.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/40-modules/40-modules.ipynb)


## 📺 Video Tutorial

**What are Python modules? 📨** (7:57)

## What You'll Learn

In this chapter, you'll learn about Python modules - files containing Python code that you can import and reuse in other programs. You'll discover how to import built-in modules, create your own custom modules, use different import styles, and organize your code into reusable, maintainable components that promote the DRY (Don't Repeat Yourself) principle.

## Learning Objectives

- Understand what modules are and why they're important
- Import and use built-in Python modules
- Create your own custom modules
- Use different import syntaxes (`import`, `from...import`, `as`)
- Understand the `__name__` variable and `if __name__ == "__main__"` pattern
- Organize code into reusable modules for better project structure

## Concept Explanation

### What is a Module?

A **module** is simply a file containing Python code (functions, variables, classes) that you can import and use in other programs.

**Why Use Modules?**
1. **Code Reusability** - Write once, use many times
2. **Organization** - Break large programs into smaller, manageable files
3. **Namespace Separation** - Avoid naming conflicts
4. **Maintainability** - Update code in one place

**Types of Modules:**
- **Built-in modules** - Included with Python (math, random, datetime)
- **Third-party modules** - Installed via pip (requests, numpy, pandas)
- **Custom modules** - Your own Python files

### Basic Import Syntax

#### 1. **Import Entire Module**
```python
import math

result = math.sqrt(16)
print(result)  # 4.0
```

#### 2. **Import Specific Items**
```python
from math import sqrt, pi

print(sqrt(16))  # 4.0
print(pi)        # 3.14159...
```

#### 3. **Import with Alias**
```python
import math as m

print(m.sqrt(16))  # 4.0
```

#### 4. **Import Everything** (Not Recommended!)
```python
from math import *

print(sqrt(16))  # 4.0 - no prefix needed
# Problem: Can cause naming conflicts!
```

### Creating Custom Modules

Any Python file can be a module. Just save your code in a `.py` file and import it!

**example.py** (Your custom module):
```python
# example.py - Custom module

pi = 3.14159

def square(x):
    """Return the square of x."""
    return x ** 2

def cube(x):
    """Return the cube of x."""
    return x ** 3

def circumference(radius):
    """Calculate circumference of a circle."""
    return 2 * pi * radius

def area(radius):
    """Calculate area of a circle."""
    return pi * (radius ** 2)
```

**main.py** (Using the custom module):
```python
# main.py
import example

# Access module variables
print(example.pi)  # 3.14159

# Call module functions
print(example.square(5))           # 25
print(example.cube(3))             # 27
print(example.circumference(10))   # 62.8318
print(example.area(5))             # 78.53975
```

### The __name__ Variable

Every Python module has a special variable called `__name__`:
- When module is **run directly**: `__name__ == "__main__"`
- When module is **imported**: `__name__ == "module_name"`

This allows you to write code that only runs when the file is executed directly:

**example.py**:
```python
# example.py
def greet(name):
    print(f"Hello, {name}!")

# This only runs when example.py is executed directly
if __name__ == "__main__":
    print("Running example.py directly")
    greet("Alice")
```

**main.py**:
```python
# main.py
import example

# The if __name__ block in example.py doesn't run
example.greet("Bob")  # Only this executes
```

### Import Styles Comparison

```python
# Style 1: Import module
import math
print(math.sqrt(16))  # Must use math. prefix

# Style 2: Import specific items
from math import sqrt
print(sqrt(16))  # No prefix needed

# Style 3: Import with alias
import math as m
print(m.sqrt(16))  # Use alias prefix

# Style 4: Import all (avoid!)
from math import *
print(sqrt(16))  # No prefix, but can cause conflicts
```

### Common Built-in Modules

#### **math** - Mathematical functions
```python
import math

print(math.sqrt(25))     # 5.0
print(math.pi)           # 3.14159...
print(math.ceil(4.3))    # 5
print(math.floor(4.7))   # 4
```

#### **random** - Random number generation
```python
import random

print(random.randint(1, 10))        # Random int 1-10
print(random.choice(['a', 'b', 'c']))  # Random choice
print(random.random())              # Random float 0-1
```

#### **datetime** - Date and time
```python
import datetime

now = datetime.datetime.now()
print(now)  # Current date and time
```

#### **os** - Operating system functions
```python
import os

print(os.getcwd())  # Current working directory
print(os.listdir())  # List files in directory
```

### Module Search Path

Python looks for modules in this order:
1. Current directory
2. PYTHONPATH environment variable
3. Installation-dependent directories

```python
import sys
print(sys.path)  # Shows module search paths
```

## Examples

### Example 1: Using math Module
```python
import math

# Square root
print(f"Square root of 16: {math.sqrt(16)}")  # 4.0

# Power
print(f"2 to the power of 3: {math.pow(2, 3)}")  # 8.0

# Constants
print(f"Pi: {math.pi}")  # 3.14159...
print(f"Euler's number: {math.e}")  # 2.71828...

# Trigonometry
print(f"Sin(90°): {math.sin(math.radians(90))}")  # 1.0
print(f"Cos(0°): {math.cos(math.radians(0))}")    # 1.0

# Rounding
print(f"Ceiling of 4.3: {math.ceil(4.3)}")   # 5
print(f"Floor of 4.7: {math.floor(4.7)}")    # 4
```

### Example 2: Using random Module
```python
import random

# Random integer in range
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# Random choice from list
colors = ["red", "blue", "green", "yellow"]
chosen_color = random.choice(colors)
print(f"Chosen color: {chosen_color}")

# Random float 0-1
random_float = random.random()
print(f"Random float: {random_float}")

# Shuffle a list
cards = ["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
print(f"Shuffled cards: {cards}")

# Random sample (multiple choices)
lottery_numbers = random.sample(range(1, 50), 6)
print(f"Lottery numbers: {lottery_numbers}")
```

### Example 3: Creating Custom Module
```python
# calculator.py
"""
A simple calculator module.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Test code (only runs when executed directly)
if __name__ == "__main__":
    print("Testing calculator module...")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")

# main.py
import calculator

print(calculator.add(15, 7))       # 22
print(calculator.multiply(4, 8))   # 32
print(calculator.divide(20, 4))    # 5.0
```

### Example 4: Different Import Styles
```python
# Style 1: Import entire module
import random
print(random.randint(1, 10))

# Style 2: Import specific function
from random import choice
colors = ["red", "blue", "green"]
print(choice(colors))

# Style 3: Import with alias
import random as r
print(r.random())

# Style 4: Import multiple items
from math import sqrt, pi, e
print(sqrt(16))
print(pi)
print(e)
```

### Example 5: Using datetime Module
```python
import datetime

# Current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")

# Create specific date
birthday = datetime.datetime(1990, 5, 15)
print(f"Birthday: {birthday}")

# Date arithmetic
days_alive = now - birthday
print(f"Days alive: {days_alive.days}")

# Format date
formatted = now.strftime("%B %d, %Y")
print(f"Formatted: {formatted}")  # Example: January 10, 2026
```

### Example 6: Custom Geometry Module
```python
# geometry.py
"""Geometry calculations module."""

import math

def circle_area(radius):
    """Calculate area of a circle."""
    return math.pi * (radius ** 2)

def circle_circumference(radius):
    """Calculate circumference of a circle."""
    return 2 * math.pi * radius

def rectangle_area(length, width):
    """Calculate area of a rectangle."""
    return length * width

def rectangle_perimeter(length, width):
    """Calculate perimeter of a rectangle."""
    return 2 * (length + width)

def triangle_area(base, height):
    """Calculate area of a triangle."""
    return 0.5 * base * height

# Test the module
if __name__ == "__main__":
    print("=== Geometry Module Tests ===")
    print(f"Circle (r=5) area: {circle_area(5):.2f}")
    print(f"Rectangle (4x6) area: {rectangle_area(4, 6)}")
    print(f"Triangle (b=8, h=5) area: {triangle_area(8, 5)}")

# main.py
import geometry

print(geometry.circle_area(10))         # 314.159...
print(geometry.rectangle_area(5, 8))    # 40
print(geometry.triangle_area(10, 6))    # 30.0
```

### Example 7: Using os Module
```python
import os

# Current working directory
print(f"Current directory: {os.getcwd()}")

# List files in directory
print(f"Files in current directory: {os.listdir()}")

# Check if file exists
if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File not found")

# Get file size
if os.path.exists("example.txt"):
    size = os.path.getsize("example.txt")
    print(f"File size: {size} bytes")

# Create directory
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
    print("Directory created")
```

## Practice Exercises

### Beginner Level

1. **Import and Use**: Import the `math` module and use 5 different functions from it.

2. **Random Generator**: Create a program that uses `random` module to simulate dice rolls.

3. **Date Display**: Use `datetime` to display current date in different formats.

4. **Simple Module**: Create a module with 3 functions for temperature conversions.

5. **Import Styles**: Practice all four import styles with the `random` module.

### Intermediate Level

6. **String Utils Module**: Create a module with string manipulation functions (reverse, capitalize, count_vowels).

7. **Math Library**: Build a comprehensive math module with functions for factorial, GCD, LCM, isPrime.

8. **File Utils**: Create a module for file operations (read, write, append, delete).

9. **Data Validator**: Build a validation module for emails, phone numbers, URLs.

10. **Game Module**: Create a module for game utilities (score tracking, player management).

### Advanced Level

11. **Package Structure**: Create a package with multiple related modules organized in folders.

12. **Module with Classes**: Build a module containing classes for a bank account system.

13. **Configuration Module**: Create a module for loading and saving application configurations.

14. **Database Module**: Build a module that abstracts database operations.

15. **API Client Module**: Create a reusable module for making API requests with error handling.

## Common Mistakes to Avoid

### Mistake 1: Circular Imports

**Wrong:**
```python
# module_a.py
import module_b

def func_a():
    module_b.func_b()

# module_b.py
import module_a  # Circular import!

def func_b():
    module_a.func_a()
```

**Correct:**
```python
# Restructure to avoid circular dependencies
# Or import inside function if necessary
```

**Why:** Circular imports cause errors. Restructure your code to avoid them.

### Mistake 2: Using `from module import *`

**Wrong:**
```python
from math import *
from random import *

# Name conflicts possible!
# Which module does choice() come from?
```

**Correct:**
```python
import math
import random

# Clear which module each function comes from
math.sqrt(16)
random.choice(['a', 'b'])
```

**Why:** `import *` can cause naming conflicts and makes code less readable.

### Mistake 3: Module Naming Conflicts

**Wrong:**
```python
# Don't name your file math.py - conflicts with built-in!
# math.py (your file)
def my_function():
    pass

# main.py
import math  # Imports YOUR math.py, not built-in!
```

**Correct:**
```python
# Use descriptive, unique names
# my_math_utils.py
def my_function():
    pass
```

**Why:** Avoid naming your modules the same as built-in modules.

### Mistake 4: Forgetting `__name__` Check

**Wrong:**
```python
# module.py
def useful_function():
    return "Result"

# Test code runs even when imported!
print("Testing...")
useful_function()
```

**Correct:**
```python
# module.py
def useful_function():
    return "Result"

# Only runs when executed directly
if __name__ == "__main__":
    print("Testing...")
    useful_function()
```

**Why:** Without `if __name__ == "__main__"`, test code runs every time module is imported.

## Real-World Applications

### 1. **Web Development**
```python
from flask import Flask, request, jsonify
from database import db_connect, db_query
from auth import check_authentication
```

### 2. **Data Science**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
```

### 3. **Automation**
```python
import os
import shutil
from datetime import datetime
from email_utils import send_email
```

### 4. **Testing**
```python
import unittest
from my_module import function_to_test
```

## Challenge Projects

### 1. **Utility Library**
Create a comprehensive utility module collection.

**Requirements:**
- String utilities module
- File operations module
- Date/time helpers module
- Data validators module
- Math utilities module
- Proper documentation

### 2. **Game Framework**
Build a reusable game framework as modules.

**Requirements:**
- Player management module
- Scoring system module
- Inventory module
- Combat system module
- Save/load module
- Example game using framework

### 3. **Data Processing Pipeline**
Create modules for data processing.

**Requirements:**
- Data loading module
- Data cleaning module
- Data transformation module
- Data validation module
- Data export module
- Pipeline orchestrator

### 4. **CLI Tool Framework**
Build a framework for CLI tools.

**Requirements:**
- Command parser module
- Configuration module
- Logging module
- Error handling module
- Help system module
- Example CLI tool

### 5. **Web Scraper Framework**
Create a modular web scraping framework.

**Requirements:**
- Request handler module
- HTML parser module
- Data extractor module
- Storage module
- Error handling module
- Rate limiting module

---

## Navigation

- **Previous:** [38. Match Case Statements](38-match-case-statements.md)
- **Next:** [40. Scope Resolution](40-scope-resolution.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Lists store multiple items in a single variable
2. Define functions using the def keyword
3. Import modules to use external code

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
