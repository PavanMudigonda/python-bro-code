# 🎯 If __name__ == "__main__"

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/42-if-name-main/42-if-name-main.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/42-if-name-main/42-if-name-main.ipynb)


## 📺 Video Tutorial

**if __name__ == '__main__' for Python beginners 📥** (6:05)

## What You'll Learn

In this chapter, you'll master the `if __name__ == "__main__"` pattern - a fundamental Python idiom that allows you to write code that can be both run as a standalone script and imported as a reusable module. You'll learn how Python's special `__name__` variable works, why this pattern is essential for professional Python development, and how to structure your code for maximum reusability.

## Learning Objectives

- Understand how Python's `__name__` variable works in different execution contexts
- Distinguish between running a file directly vs importing it as a module
- Implement the `if __name__ == "__main__"` pattern correctly
- Create Python files that function as both scripts and importable modules
- Organize code for reusability and maintainability
- Follow professional Python module development best practices

## Concept Explanation

### What is `__name__`?

`__name__` is a special built-in variable in Python that Python automatically sets for every module. Its value depends on how the Python file is being used:

- **When run directly**: `__name__ = "__main__"`
- **When imported**: `__name__ = module name` (the filename without .py)

```python
# Example: my_module.py
print(f"__name__ = {__name__}")

# When run directly:      python my_module.py
# Output: __name__ = __main__

# When imported:          import my_module
# Output: __name__ = my_module
```

### The Problem This Pattern Solves

Without the `if __name__ == "__main__"` pattern, all code in a module executes when imported:

```python
# calculator.py (BAD EXAMPLE)
def add(a, b):
    return a + b

# This runs EVERY TIME the module is imported!
print("Running calculator...")
result = add(5, 3)
print(f"Result: {result}")
```

```python
# app.py
import calculator  # This prints "Running calculator..." and "Result: 8"
                   # Even though we just wanted to use the add() function!
```

### The Solution

The `if __name__ == "__main__"` pattern solves this by separating reusable functions from script execution code:

```python
# calculator.py (GOOD EXAMPLE)
def add(a, b):
    return a + b

def main():
    """This only runs when file is executed directly."""
    print("Running calculator...")
    result = add(5, 3)
    print(f"Result: {result}")

if __name__ == "__main__":
    # This block only executes when running the file directly
    # NOT when importing as a module
    main()
```

```python
# app.py
import calculator  # Nothing prints - clean import!
result = calculator.add(10, 5)  # Just use the function
```

### How It Works

```python
# my_script.py
print("1. This ALWAYS runs (both direct execution and import)")

def my_function():
    return "I'm reusable!"

if __name__ == "__main__":
    print("2. This ONLY runs when executing directly")
    print("   (NOT when imported as a module)")
    result = my_function()
    print(result)

print("3. This ALWAYS runs (both direct execution and import)")
```

**Execution Results:**

```bash
# Direct execution: python my_script.py
# Output:
# 1. This ALWAYS runs (both direct execution and import)
# 3. This ALWAYS runs (both direct execution and import)
# 2. This ONLY runs when executing directly
#    (NOT when imported as a module)
# I'm reusable!
```

```python
# Importing: import my_script
# Output:
# 1. This ALWAYS runs (both direct execution and import)
# 3. This ALWAYS runs (both direct execution and import)
# (The if __name__ == "__main__" block does NOT run)
```

### Use Cases

#### 1. **Library with Standalone Testing**

```python
# math_utils.py
def factorial(n):
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    """Test the functions when run directly."""
    print("Testing factorial function:")
    for i in range(6):
        print(f"  {i}! = {factorial(i)}")

if __name__ == "__main__":
    main()
```

- **As library**: `from math_utils import factorial` (no output, just import)
- **As script**: `python math_utils.py` (runs tests)

#### 2. **Command-Line Tool That's Also Importable**

```python
# text_processor.py
import sys

def process_text(text):
    """Process and return text."""
    return text.upper().strip()

def main():
    """Command-line interface."""
    if len(sys.argv) < 2:
        print("Usage: python text_processor.py <text>")
        sys.exit(1)
    
    text = " ".join(sys.argv[1:])
    result = process_text(text)
    print(result)

if __name__ == "__main__":
    main()
```

- **As tool**: `python text_processor.py hello world` → `HELLO WORLD`
- **As library**: `from text_processor import process_text`

#### 3. **Module with Examples**

```python
# shapes.py
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

def main():
    """Demonstrate usage examples."""
    print("Circle Examples:")
    circle = Circle(5)
    print(f"  Radius: {circle.radius}")
    print(f"  Area: {circle.area()}")

if __name__ == "__main__":
    main()
```

- **As library**: Import and use `Circle` class
- **As demo**: Run to see usage examples

### Best Practices

#### 1. **Always Use a main() Function**

```python
# GOOD - Organized and clear
def helper_function():
    pass

def main():
    # Script logic here
    helper_function()

if __name__ == "__main__":
    main()
```

```python
# BAD - Messy script logic
def helper_function():
    pass

if __name__ == "__main__":
    # Too much logic here
    x = 5
    y = 10
    result = helper_function()
    print(result)
    # ... more code ...
```

#### 2. **Keep Module-Level Code Minimal**

```python
# GOOD - Only imports and definitions at module level
import math

def calculate(x):
    return math.sqrt(x)

if __name__ == "__main__":
    print(calculate(16))
```

```python
# BAD - Side effects at module level
import math

print("Module loading...")  # Runs on every import!
GLOBAL_VALUE = calculate_something()  # Side effect!

def calculate(x):
    return math.sqrt(x)
```

#### 3. **Write Importable Functions**

Design functions to be reusable:

```python
# GOOD - Pure, reusable functions
def add(a, b):
    return a + b

def main():
    result = add(5, 3)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

```python
# BAD - Function has side effects
def add(a, b):
    result = a + b
    print(f"Result: {result}")  # Side effect - always prints!
    return result
```

### Common Patterns

#### Testing Pattern
```python
def my_function(x):
    return x * 2

if __name__ == "__main__":
    # Quick tests
    assert my_function(5) == 10
    assert my_function(0) == 0
    print("All tests passed!")
```

#### CLI Pattern
```python
import argparse

def process(data):
    return data.upper()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data")
    args = parser.parse_args()
    
    result = process(args.data)
    print(result)

if __name__ == "__main__":
    main()
```

#### Demo Pattern
```python
class MyClass:
    def __init__(self, value):
        self.value = value

if __name__ == "__main__":
    # Show usage examples
    print("Example 1:")
    obj1 = MyClass(10)
    print(f"  Value: {obj1.value}")
    
    print("\nExample 2:")
    obj2 = MyClass(20)
    print(f"  Value: {obj2.value}")
```

## Examples

### Example 1: Basic Calculator Module

```python
# calculator.py
"""A simple calculator module that can be imported or run directly."""

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
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    """Interactive calculator when run directly."""
    print("Simple Calculator")
    print("-" * 20)
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    print(f"\n{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    
    try:
        print(f"{a} / {b} = {divide(a, b)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

**Usage:**
```python
# As module:
from calculator import add, multiply
result = add(5, 3)  # 8

# As script:
# python calculator.py
# (runs interactive calculator)
```

### Example 2: String Utilities Library

```python
# string_utils.py
"""String manipulation utilities."""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    """Check if text is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def main():
    """Demonstrate string utilities."""
    test_strings = ["Hello", "racecar", "Python Programming", "A man a plan a canal Panama"]
    
    for text in test_strings:
        print(f"\nText: '{text}'")
        print(f"  Reversed: {reverse_string(text)}")
        print(f"  Vowels: {count_vowels(text)}")
        print(f"  Palindrome: {is_palindrome(text)}")

if __name__ == "__main__":
    main()
```

### Example 3: Temperature Converter

```python
# temp_converter.py
"""Temperature conversion utilities."""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def main():
    """Interactive temperature converter."""
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    
    choice = input("\nChoose conversion (1-4): ")
    temp = float(input("Enter temperature: "))
    
    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    elif choice == "3":
        result = celsius_to_kelvin(temp)
        print(f"{temp}°C = {result:.2f}K")
    elif choice == "4":
        result = kelvin_to_celsius(temp)
        print(f"{temp}K = {result:.2f}°C")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
```

### Example 4: File Statistics Module

```python
# file_stats.py
"""Analyze text file statistics."""

import os

def count_lines(filename):
    """Count lines in a file."""
    with open(filename, 'r') as f:
        return len(f.readlines())

def count_words(filename):
    """Count words in a file."""
    with open(filename, 'r') as f:
        return sum(len(line.split()) for line in f)

def count_characters(filename):
    """Count characters in a file."""
    with open(filename, 'r') as f:
        return sum(len(line) for line in f)

def analyze_file(filename):
    """Get complete file statistics."""
    return {
        'filename': filename,
        'size_bytes': os.path.getsize(filename),
        'lines': count_lines(filename),
        'words': count_words(filename),
        'characters': count_characters(filename)
    }

def main():
    """Analyze a file specified by user."""
    filename = input("Enter filename to analyze: ")
    
    try:
        stats = analyze_file(filename)
        print(f"\nFile Statistics for '{stats['filename']}':")
        print(f"  Size: {stats['size_bytes']} bytes")
        print(f"  Lines: {stats['lines']}")
        print(f"  Words: {stats['words']}")
        print(f"  Characters: {stats['characters']}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Example 5: Data Validator

```python
# validators.py
"""Input validation functions."""

import re

def is_valid_email(email):
    """Check if email address is valid."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone):
    """Check if phone number is valid (US format)."""
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

def is_strong_password(password):
    """Check if password is strong (8+ chars, upper, lower, digit)."""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

def main():
    """Test validators with user input."""
    print("Input Validator Demo\n")
    
    email = input("Enter email: ")
    print(f"Valid email: {is_valid_email(email)}")
    
    phone = input("Enter phone (XXX-XXX-XXXX): ")
    print(f"Valid phone: {is_valid_phone(phone)}")
    
    password = input("Enter password: ")
    print(f"Strong password: {is_strong_password(password)}")

if __name__ == "__main__":
    main()
```

### Example 6: Math Operations Library

```python
# math_ops.py
"""Advanced math operations."""

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Generate first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    """Demonstrate math operations."""
    print("Factorial Examples:")
    for i in range(6):
        print(f"  {i}! = {factorial(i)}")
    
    print("\nFibonacci Sequence (first 10):")
    print(f"  {fibonacci(10)}")
    
    print("\nPrime Numbers (1-20):")
    primes = [n for n in range(1, 21) if is_prime(n)]
    print(f"  {primes}")

if __name__ == "__main__":
    main()
```

### Example 7: Configuration Manager

```python
# config.py
"""Application configuration manager."""

import json
import os

DEFAULT_CONFIG = {
    'app_name': 'MyApp',
    'version': '1.0.0',
    'debug': False,
    'max_connections': 100
}

def load_config(filename='config.json'):
    """Load configuration from JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()

def save_config(config, filename='config.json'):
    """Save configuration to JSON file."""
    with open(filename, 'w') as f:
        json.dump(config, f, indent=2)

def get_setting(key, default=None):
    """Get a specific configuration setting."""
    config = load_config()
    return config.get(key, default)

def main():
    """Interactive configuration manager."""
    print("Configuration Manager")
    print("1. View configuration")
    print("2. Update configuration")
    print("3. Reset to defaults")
    
    choice = input("\nChoose option (1-3): ")
    
    if choice == "1":
        config = load_config()
        print("\nCurrent Configuration:")
        for key, value in config.items():
            print(f"  {key}: {value}")
    
    elif choice == "2":
        config = load_config()
        key = input("Enter setting name: ")
        value = input("Enter new value: ")
        config[key] = value
        save_config(config)
        print("Configuration updated!")
    
    elif choice == "3":
        save_config(DEFAULT_CONFIG)
        print("Configuration reset to defaults!")

if __name__ == "__main__":
    main()
```

## Practice Exercises

### Beginner Exercises

1. **Module Checker**
   - Create a Python file that prints "Running as script" when executed directly
   - Prints "Imported as module" when imported
   - Test both scenarios

2. **Simple Greeter Module**
   - Write a module with a `greet(name)` function
   - When run directly, prompt for a name and call greet()
   - When imported, just provide the function

3. **List Helper**
   - Create functions: `find_max(lst)`, `find_min(lst)`, `find_average(lst)`
   - When run directly, demonstrate with sample lists
   - Make functions importable

4. **Number Checker**
   - Write functions: `is_even(n)`, `is_odd(n)`
   - Include a main() that tests numbers 1-10
   - Use the `if __name__ == "__main__"` pattern

5. **Text Formatter**
   - Create functions: `to_uppercase(text)`, `to_lowercase(text)`, `capitalize_words(text)`
   - When run directly, provide a demo
   - When imported, provide the functions

### Intermediate Exercises

1. **Unit Converter Module**
   - Create multiple conversion functions (km to miles, kg to lbs, etc.)
   - When run directly, provide an interactive menu
   - When imported, expose all conversion functions
   - Include proper error handling

2. **Data Processor**
   - Write a module that processes CSV data
   - Provide functions for reading, filtering, and analyzing data
   - Include a main() that demonstrates usage with sample data
   - Handle file not found errors

3. **Password Generator**
   - Create `generate_password(length, include_symbols, include_numbers)` function
   - When run directly, prompt user for preferences
   - When imported, use as a library
   - Add validation for parameters

4. **Shopping List Manager**
   - Functions: `add_item()`, `remove_item()`, `show_list()`, `save_list()`, `load_list()`
   - Interactive menu when run directly
   - Importable functions for use in other programs
   - Persist data to a JSON file

5. **Grade Calculator**
   - Functions for calculating: average, letter grade, GPA
   - When run directly, analyze a sample gradebook
   - When imported, provide calculation functions
   - Include input validation

### Advanced Exercises

1. **Database Utility Module**
   - Create a SQLite wrapper with functions for CRUD operations
   - Provide both a CLI interface and importable functions
   - Include connection pooling and error handling
   - Support both script execution and library usage

2. **API Client Library**
   - Build a reusable API client module
   - When imported, provide API interaction functions
   - When run directly, demonstrate API usage with examples
   - Include authentication, error handling, and rate limiting

3. **Log Analyzer**
   - Parse log files and extract statistics
   - Provide functions for different analysis types
   - Interactive mode for direct execution
   - Library mode for integration with other tools
   - Support multiple log formats

4. **Task Scheduler**
   - Create a task scheduling and management system
   - CLI interface when run directly
   - Importable task management functions
   - Persist tasks to database
   - Support recurring tasks

5. **Plugin System**
   - Design a module that can load and execute plugins
   - Each plugin is a separate Python file
   - Main script discovers and runs plugins
   - Plugins can be imported individually
   - Include plugin validation and error handling

## Common Mistakes to Avoid

### Mistake 1: Putting Script Logic at Module Level

❌ **Wrong:**
```python
# bad_module.py
import sys

def helper_function():
    return "data"

# Script logic at module level - runs on import!
print("Starting program...")
data = helper_function()
result = process(data)
print(f"Result: {result}")
```

✅ **Correct:**
```python
# good_module.py
import sys

def helper_function():
    return "data"

def main():
    """Script logic in main() - only runs when executed directly."""
    print("Starting program...")
    data = helper_function()
    result = process(data)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

**Why:** Code at module level executes every time the file is imported, causing unwanted side effects and making the module unusable as a library.

### Mistake 2: Forgetting the if Statement

❌ **Wrong:**
```python
# module.py
def my_function():
    return "result"

def main():
    print(my_function())

# Calling main() without checking __name__
main()  # This ALWAYS runs, even when imported!
```

✅ **Correct:**
```python
# module.py
def my_function():
    return "result"

def main():
    print(my_function())

# Only call main() when run directly
if __name__ == "__main__":
    main()
```

**Why:** Without the `if` check, `main()` executes on import, defeating the purpose of the pattern.

### Mistake 3: Using Wrong Comparison

❌ **Wrong:**
```python
# Wrong comparison operators
if __name__ = "__main__":  # SyntaxError: assignment, not comparison
    main()

if __name__ is "__main__":  # Works sometimes, but wrong
    main()
```

✅ **Correct:**
```python
# Correct comparison
if __name__ == "__main__":  # Use == for string comparison
    main()
```

**Why:** Use `==` for string comparison, not `=` (assignment) or `is` (identity). While `is` might work, it's not guaranteed and considered bad practice.

### Mistake 4: Making Functions Depend on Direct Execution

❌ **Wrong:**
```python
# bad_design.py
def process_data():
    """This function assumes it's being run directly."""
    # Getting input directly - makes function unusable when imported
    data = input("Enter data: ")
    result = data.upper()
    print(f"Result: {result}")  # Side effect - always prints
    return result

if __name__ == "__main__":
    process_data()
```

✅ **Correct:**
```python
# good_design.py
def process_data(data):
    """Pure function - accepts input as parameter."""
    return data.upper()

def main():
    """Handle I/O in main(), keep functions pure."""
    data = input("Enter data: ")
    result = process_data(data)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```

**Why:** Functions should be pure and reusable. Handle user interaction in `main()`, not in the functions themselves. This makes functions usable when imported.

## Real-World Applications

### 1. **Python Packages and Libraries**

Professional Python libraries use this pattern extensively:

```python
# requests library example
# Can be used as:
import requests
response = requests.get('https://api.github.com')

# Or run directly for demos/tests:
# python -m requests.demo
```

**Use Cases:**
- Creating pip-installable packages
- Building internal company libraries
- Developing open-source projects
- Sharing code between projects

### 2. **Command-Line Tools**

Tools that work both as CLI utilities and importable libraries:

```python
# aws_cli_tools.py
def upload_file(filename, bucket):
    """Upload file to S3."""
    # Implementation
    pass

def main():
    """AWS CLI interface."""
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('bucket')
    args = parser.parse_args()
    
    upload_file(args.filename, args.bucket)

if __name__ == "__main__":
    main()

# Usage:
# CLI: python aws_cli_tools.py file.txt my-bucket
# Library: from aws_cli_tools import upload_file
```

**Use Cases:**
- DevOps automation scripts
- Data processing pipelines
- System administration tools
- Build and deployment scripts

### 3. **Testing and Development**

Include test code that runs only during development:

```python
# database.py
class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string
    
    def connect(self):
        # Database connection logic
        pass

def main():
    """Development and testing code."""
    # Quick tests during development
    db = Database("localhost:5432")
    db.connect()
    print("Connection test successful!")

if __name__ == "__main__":
    main()

# Production: from database import Database
# Development: python database.py (runs tests)
```

**Use Cases:**
- Unit testing during development
- Quick function verification
- Integration testing
- Debugging and troubleshooting

### 4. **Data Science and Analytics**

Jupyter notebooks and analysis scripts that are also reusable:

```python
# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    """Load and preprocess data."""
    return pd.read_csv(filename)

def analyze_sales(df):
    """Perform sales analysis."""
    return df.groupby('region')['sales'].sum()

def main():
    """Run complete analysis."""
    df = load_data('sales.csv')
    results = analyze_sales(df)
    results.plot(kind='bar')
    plt.savefig('sales_report.png')
    print("Analysis complete!")

if __name__ == "__main__":
    main()

# Interactive: python data_analysis.py
# Notebook: from data_analysis import load_data, analyze_sales
```

**Use Cases:**
- Automated reporting
- Data pipeline components
- Reusable analysis functions
- Machine learning utilities

## Challenge Projects

### 1. **Multi-Tool Utility Suite**

Create a comprehensive utility module with various tools:

**Requirements:**
- Implement 10+ utility functions (file operations, string manipulation, math, etc.)
- CLI menu system when run directly
- Each function fully importable and documented
- Include unit tests in the main() function
- Support both interactive and batch modes
- Configuration file support

**Skills Applied:**
- Module organization
- CLI design
- Function documentation
- Error handling
- Configuration management

### 2. **Personal Finance Manager**

Build a finance tracking system:

**Requirements:**
- Functions for adding expenses, income, generating reports
- Interactive mode: menu-driven interface
- Library mode: functions for use in other applications
- Data persistence (JSON/SQLite)
- Export to CSV functionality
- Budget tracking and alerts
- Visual reports (matplotlib) in direct execution mode

**Skills Applied:**
- Data persistence
- User interface design
- Mathematical calculations
- Report generation
- Module design patterns

### 3. **Web Scraper Framework**

Create a reusable web scraping library:

**Requirements:**
- Generic scraping functions (fetch page, parse HTML, extract data)
- Site-specific scrapers as examples in main()
- Configurable via parameters when imported
- Demo mode showing multiple scraping examples
- Rate limiting and error handling
- Cache support
- Export to multiple formats (JSON, CSV)

**Skills Applied:**
- HTTP requests
- HTML parsing
- Error handling
- Caching strategies
- Data export

### 4. **Code Generator Tool**

Build a code generation utility:

**Requirements:**
- Functions to generate boilerplate code (classes, functions, modules)
- Templates for common patterns
- CLI for interactive code generation
- Importable for integration with other tools
- Support multiple programming languages
- Customizable templates
- File writing with safety checks (no overwrite without confirmation)

**Skills Applied:**
- String templating
- File I/O
- Code organization
- Template design
- User interaction

### 5. **API Testing Framework**

Develop an API testing and documentation tool:

**Requirements:**
- Functions for making API requests and validating responses
- When run directly: execute test suites and generate reports
- When imported: provide testing utilities
- Support for multiple HTTP methods
- Authentication handling
- Response validation
- Performance testing
- Report generation (HTML/JSON)
- Mock server for testing

**Skills Applied:**
- HTTP requests
- JSON handling
- Test automation
- Report generation
- Documentation
- Performance monitoring

---

## Navigation

← [Previous: 40 - Scope Resolution](40-scope-resolution.md) | [Next: 42 - Banking Program](42-banking-program.md) →

[↑ Back to Main README](../README.md)

## 🎓 Key Takeaways from Video

1. Strings are text data enclosed in quotes
2. Define functions using the def keyword
3. Import modules to use external code

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
