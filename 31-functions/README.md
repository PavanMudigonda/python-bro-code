# 🔧 Functions


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/vsLBErLWBhA)


## What You'll Learn

In this chapter, you'll master Python functions - reusable blocks of code that perform specific tasks. You'll learn how to define functions with parameters, call them with arguments, use return values, and understand why functions are essential for writing organized, maintainable, and DRY (Don't Repeat Yourself) code.

## Learning Objectives

- Define functions using the `def` keyword and proper syntax
- Understand parameters vs arguments and how data flows into functions
- Use return statements to send data back from functions
- Apply the `if __name__ == "__main__"` pattern for script execution
- Create modular, reusable code with well-named functions
- Organize complex programs by breaking them into smaller function-based units

## Concept Explanation

### What are Functions?

Functions are reusable blocks of code that perform a specific task. Think of them as mini-programs within your program. Instead of writing the same code multiple times, you write it once in a function and call it whenever needed.

**Why Use Functions?**

```python
# Without functions - repetitive code
print("Happy Birthday Sarah!")
print("You are 20 years old!")
print()

print("Happy Birthday Mike!")
print("You are 25 years old!")
print()

print("Happy Birthday Lisa!")
print("You are 30 years old!")
print()

# With functions - DRY (Don't Repeat Yourself)
def happy_birthday(name, age):
    print(f"Happy Birthday {name}!")
    print(f"You are {age} years old!")
    print()

happy_birthday("Sarah", 20)
happy_birthday("Mike", 25)
happy_birthday("Lisa", 30)
```

The function version is cleaner, easier to maintain, and if you need to change the message format, you only update it in one place.

### Function Anatomy

A function has several key parts:

```python
def function_name(parameter1, parameter2):  # Definition line
    """Docstring - describes what function does"""
    # Function body - indented code block
    result = parameter1 + parameter2
    return result  # Return value (optional)
```

1. **`def` keyword** - Tells Python you're defining a function
2. **Function name** - Should be descriptive (use snake_case)
3. **Parameters** - Variables that receive values (in parentheses)
4. **Colon `:` ** - Marks end of definition line
5. **Docstring** - Optional documentation string (recommended!)
6. **Function body** - Indented code that runs when function is called
7. **`return` statement** - Sends a value back to caller (optional)

### Parameters vs Arguments

**Parameters** are variables in the function definition:

```python
def greet(name, greeting):  # name and greeting are PARAMETERS
    print(f"{greeting}, {name}!")
```

**Arguments** are the actual values you pass when calling:

```python
greet("Alice", "Hello")  # "Alice" and "Hello" are ARGUMENTS
```

Think of parameters as placeholders, and arguments as the actual data.

### Return Values

Functions can send data back using `return`:

```python
def add(a, b):
    return a + b  # Send sum back to caller

result = add(5, 3)  # result = 8
print(result)
```

Without `return`, functions implicitly return `None`:

```python
def greet(name):
    print(f"Hello {name}")  # No return statement

result = greet("Bob")  # Prints "Hello Bob"
print(result)  # Prints "None"
```

### The `if __name__ == "__main__"` Pattern

This special pattern prevents code from running when your file is imported as a module:

```python
def my_function():
    print("Function called")

# This code only runs if script is executed directly
if __name__ == "__main__":
    my_function()
```

**How it works:**
- `__name__` is a special variable Python sets automatically
- When script runs directly: `__name__ == "__main__"`
- When script is imported: `__name__ == "module_name"`

This lets you write reusable modules that can be both imported and executed.

### Function Design Best Practices

#### 1. **Single Responsibility**
Each function should do one thing well:

```python
# Bad - does too much
def process_user(name, email, age):
    # validate email
    # save to database
    # send welcome email
    # update analytics
    pass

# Good - single responsibility
def validate_email(email):
    return "@" in email

def save_user(name, email, age):
    # save to database
    pass

def send_welcome_email(email):
    # send email
    pass
```

#### 2. **Descriptive Names**
Function names should describe what they do:

```python
# Bad
def calc(x, y):
    return x * y

# Good
def calculate_area(width, height):
    return width * height
```

#### 3. **Keep Functions Small**
Aim for functions that fit on one screen (typically 10-20 lines).

#### 4. **Use Docstrings**
Document what your function does:

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index.
    
    Parameters:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
    
    Returns:
        float: BMI value
    """
    return weight_kg / (height_m ** 2)
```

### Variable Scope in Functions

Variables defined inside functions are **local** - they only exist within that function:

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Prints 10
print(x)  # Error! x doesn't exist outside function
```

## Examples

### Example 1: Simple Function (No Parameters, No Return)
```python
def greet():
    """Display a simple greeting."""
    print("Hello!")
    print("Welcome to Python functions")

# Call the function
greet()
# Output:
# Hello!
# Welcome to Python functions
```

### Example 2: Function with Parameters
```python
def greet_person(name, time_of_day):
    """
    Greet a person based on time of day.
    
    Parameters:
        name (str): Person's name
        time_of_day (str): morning, afternoon, or evening
    """
    print(f"Good {time_of_day}, {name}!")

greet_person("Alice", "morning")   # Good morning, Alice!
greet_person("Bob", "afternoon")   # Good afternoon, Bob!
greet_person("Charlie", "evening") # Good evening, Charlie!
```

### Example 3: Function with Return Value
```python
def calculate_area(length, width):
    """
    Calculate area of a rectangle.
    
    Parameters:
        length (float): Length of rectangle
        width (float): Width of rectangle
    
    Returns:
        float: Area of rectangle
    """
    area = length * width
    return area

# Use returned value
room_area = calculate_area(5, 4)
print(f"Room area: {room_area} sq meters")  # Room area: 20 sq meters

# Can use directly in expressions
total_area = calculate_area(5, 4) + calculate_area(3, 3)
print(f"Total area: {total_area}")  # Total area: 29
```

### Example 4: Function with Multiple Return Values
```python
def get_statistics(numbers):
    """
    Calculate statistics for a list of numbers.
    
    Parameters:
        numbers (list): List of numbers
    
    Returns:
        tuple: (minimum, maximum, average)
    """
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    
    return minimum, maximum, average  # Returns tuple

# Unpack returned values
scores = [85, 92, 78, 90, 88]
min_score, max_score, avg_score = get_statistics(scores)

print(f"Min: {min_score}")   # Min: 78
print(f"Max: {max_score}")   # Max: 92
print(f"Avg: {avg_score}")   # Avg: 86.6
```

### Example 5: Temperature Converter
```python
def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Parameters:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Test conversions
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")  # 25°C = 77.0°F

temp_f = 98.6
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.1f}°C")  # 98.6°F = 37.0°C
```

### Example 6: Input Validation Function
```python
def get_positive_number(prompt):
    """
    Get a positive number from user.
    
    Parameters:
        prompt (str): Message to display to user
    
    Returns:
        float: Valid positive number
    """
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Use the function
age = get_positive_number("Enter your age: ")
weight = get_positive_number("Enter your weight (kg): ")
height = get_positive_number("Enter your height (m): ")

bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.1f}")
```

### Example 7: Complete Program with Main Function
```python
def display_menu():
    """Display calculator menu."""
    print("\n===== CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=" * 22)

def add(a, b):
    """Return sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return product of two numbers."""
    return a * b

def divide(a, b):
    """Return quotient of two numbers."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_numbers():
    """Get two numbers from user."""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def main():
    """Main calculator program."""
    while True:
        display_menu()
        choice = input("\nEnter choice (1-5): ")
        
        if choice == "5":
            print("Thank you for using the calculator!")
            break
        
        if choice in ["1", "2", "3", "4"]:
            num1, num2 = get_numbers()
            
            if choice == "1":
                result = add(num1, num2)
                operation = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = "*"
            elif choice == "4":
                result = divide(num1, num2)
                operation = "/"
            
            print(f"\n{num1} {operation} {num2} = {result}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

## Practice Exercises

### Beginner Level

1. **Simple Greeting**: Write a function `say_hello()` that prints "Hello, World!" when called.

2. **Name Printer**: Create a function `print_name(name)` that takes a name parameter and prints "Your name is [name]".

3. **Square Calculator**: Write a function `square(number)` that returns the square of a number.

4. **Age Calculator**: Create `calculate_age(birth_year, current_year)` that returns the person's age.

5. **Even or Odd**: Write a function `is_even(number)` that returns `True` if the number is even, `False` otherwise.

### Intermediate Level

6. **Grade Calculator**: Create a function that takes a score (0-100) and returns the letter grade (A, B, C, D, F).

7. **Password Validator**: Write a function that checks if a password is at least 8 characters and contains both letters and numbers.

8. **List Reverser**: Create a function that takes a list and returns it reversed (without using built-in `reversed()` or slicing).

9. **Prime Checker**: Write a function `is_prime(n)` that returns whether a number is prime.

10. **String Counter**: Create a function that counts how many times a specific character appears in a string.

### Advanced Level

11. **Fibonacci Generator**: Write a function that generates the first n Fibonacci numbers and returns them as a list.

12. **Anagram Checker**: Create a function that determines if two strings are anagrams of each other.

13. **Matrix Transposer**: Write a function that transposes a 2D list (matrix) - swap rows and columns.

14. **Recursive Factorial**: Implement factorial calculation using recursion.

15. **Function Decorator**: Create a function that measures and prints the execution time of another function.

## Common Mistakes to Avoid

### Mistake 1: Forgetting to Return a Value

**Wrong:**
```python
def add(a, b):
    sum_value = a + b
    # Forgot to return!

result = add(5, 3)
print(result)  # Prints None
```

**Correct:**
```python
def add(a, b):
    sum_value = a + b
    return sum_value  # Or: return a + b

result = add(5, 3)
print(result)  # Prints 8
```

**Why:** Without `return`, the function returns `None` by default. You must explicitly return a value if you want to use it.

### Mistake 2: Confusing Parameters and Arguments

**Wrong:**
```python
def greet(name):
    print(f"Hello {name}")

# Using wrong variable name
greet(person)  # NameError: person is not defined
```

**Correct:**
```python
def greet(name):
    print(f"Hello {name}")

person = "Alice"
greet(person)  # Pass the variable as argument
# or
greet("Alice")  # Pass value directly
```

**Why:** Parameters are placeholders in the function definition. Arguments are the actual values you pass when calling.

### Mistake 3: Incorrect Indentation

**Wrong:**
```python
def calculate_sum(a, b):
total = a + b  # Not indented!
return total

# IndentationError
```

**Correct:**
```python
def calculate_sum(a, b):
    total = a + b  # Properly indented
    return total
```

**Why:** Function body must be indented (4 spaces is standard). Python uses indentation to define code blocks.

### Mistake 4: Modifying Global Variables Without Declaring

**Wrong:**
```python
count = 0

def increment():
    count = count + 1  # UnboundLocalError!

increment()
```

**Correct:**
```python
count = 0

def increment():
    global count  # Declare we're using global variable
    count = count + 1

increment()
print(count)  # 1

# OR BETTER - use return instead:
def increment(value):
    return value + 1

count = increment(count)
```

**Why:** Python treats `count` as a local variable if you assign to it, causing an error. Better to avoid global variables and use parameters/returns instead.

## Real-World Applications

### 1. **Web Development**
Functions are fundamental in web frameworks like Django and Flask. Routes are functions that handle HTTP requests:

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # Show user profile page
    return render_template('profile.html', user=username)
```

### 2. **Data Science**
Data processing pipelines use functions to clean, transform, and analyze data:

```python
def clean_data(dataframe):
    # Remove nulls, fix formatting, normalize
    return cleaned_df

def calculate_statistics(dataframe):
    # Compute mean, median, std dev
    return stats_dict
```

### 3. **Automation Scripts**
Functions organize automation tasks into reusable components:

```python
def backup_files(source_dir, backup_dir):
    # Copy files from source to backup
    pass

def send_email_notification(status):
    # Send email about backup status
    pass
```

### 4. **Game Development**
Game logic is built from functions for movement, collision detection, scoring:

```python
def check_collision(player, enemies):
    # Detect if player hit enemy
    return collision_detected

def update_score(points):
    # Add points to player score
    return new_score
```

## Challenge Projects

### 1. **Unit Converter Library**
Create a module with conversion functions for various units.

**Requirements:**
- Temperature (C, F, K)
- Length (meters, feet, miles, km)
- Weight (kg, pounds, ounces)
- Time (seconds, minutes, hours, days)
- Each conversion as a separate function
- Main menu to select conversion type

### 2. **Math Library**
Build your own math library with common functions.

**Requirements:**
- factorial(n)
- power(base, exponent) - without using `**`
- gcd(a, b) - greatest common divisor
- lcm(a, b) - least common multiple
- is_perfect_square(n)
- nth_root(number, n)
- All functions properly documented

### 3. **String Utilities Module**
Collection of useful string manipulation functions.

**Requirements:**
- reverse_string(s)
- is_palindrome(s)
- count_vowels(s)
- count_words(s)
- title_case(s) - capitalize first letter of each word
- remove_duplicates(s) - remove duplicate characters
- Test suite for each function

### 4. **Statistics Calculator**
Statistical analysis functions for data lists.

**Requirements:**
- mean(data)
- median(data)
- mode(data)
- variance(data)
- standard_deviation(data)
- quartiles(data) - return Q1, Q2, Q3
- Handle edge cases (empty lists, etc.)

### 5. **Banking System with Functions**
Organize banking program into well-structured functions.

**Requirements:**
- create_account(name, initial_balance)
- deposit(account, amount)
- withdraw(account, amount)
- transfer(from_account, to_account, amount)
- display_account(account)
- calculate_interest(account, rate)
- transaction_history(account)
- Input validation functions

---

## Navigation

- **Previous:** [30. Dice Roller Program](../30-dice-roller-program/README.md)
- **Next:** [32. Default Arguments](../32-default-arguments/README.md)
- **[Back to Main README](../README.md)**
