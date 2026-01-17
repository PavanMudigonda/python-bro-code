# Chapter 7: If-Elif-Else Statements


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/yUrYouDQZL8)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/yUrYouDQZL8)

## 📚 What You'll Learn
Make your programs smart with conditional logic! Learn how to make decisions based on different conditions.

## 🎯 Learning Objectives
- Understand if, elif, and else statements
- Use comparison operators (==, !=, >, <, >=, <=)
- Create programs that make decisions
- Chain multiple conditions together
- Understand the flow of conditional execution

## 📖 Concept Explanation

### What are Conditional Statements?
Conditional statements let your program make decisions and execute different code based on whether conditions are True or False.

### Syntax

#### Basic If Statement
```python
if condition:
    # This code runs if condition is True
    print("Condition is true!")
```

#### If-Else Statement
```python
if condition:
    # Runs if condition is True
else:
    # Runs if condition is False
```

#### If-Elif-Else Chain
```python
if condition1:
    # Runs if condition1 is True
elif condition2:
    # Runs if condition1 is False and condition2 is True
elif condition3:
    # Runs if condition1 and condition2 are False, and condition3 is True
else:
    # Runs if all conditions above are False
```

### Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

### Important: Indentation Matters!
```python
if age >= 18:
    print("Adult")      # Indented - part of if block
    print("Can vote")   # Indented - part of if block
print("Program ends")   # Not indented - always runs
```

## 💡 Examples

### Example 1: Simple If-Else
```python
temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's nice weather!")
```

### Example 2: Multiple Conditions (Elif)
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### Example 3: User Authentication
```python
password = input("Enter password: ")

if password == "secret123":
    print("Access granted!")
else:
    print("Access denied!")
```

### Example 4: Even or Odd
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

## ✍️ Practice Exercises

### Exercise 1: Voting Eligibility
```python
# Ask for age and determine if person can vote (18+)
age = int(input("Enter your age: "))
# Add if-else logic
```

### Exercise 2: Grade Calculator
```python
# Ask for a test score (0-100) and print the letter grade
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
```

### Exercise 3: Temperature Advisory
```python
# Ask for temperature and give advice:
# > 30: "It's hot! Stay hydrated"
# 20-30: "Nice weather!"
# 10-19: "A bit cool, bring a jacket"
# < 10: "It's cold! Bundle up!"
```

### Exercise 4: Login System
```python
# Ask for username and password
# Correct: username = "admin", password = "pass123"
# Print "Login successful" or "Invalid credentials"
```

### Exercise 5: Movie Rating System
```python
# Ask for age and determine what movies they can watch
# G: All ages
# PG: 7+
# PG-13: 13+
# R: 17+
```

## 🔍 Common Mistakes

### Mistake 1: Using = Instead of ==
```python
# Wrong:
if age = 18:  # Error! This is assignment, not comparison
    print("18!")

# Correct:
if age == 18:  # This is comparison
    print("18!")
```

### Mistake 2: Forgetting the Colon
```python
# Wrong:
if age > 18  # Error! Missing colon
    print("Adult")

# Correct:
if age > 18:  # Colon is required
    print("Adult")
```

### Mistake 3: Incorrect Indentation
```python
# Wrong:
if age > 18:
print("Adult")  # Error! Not indented

# Correct:
if age > 18:
    print("Adult")  # Indented with 4 spaces or 1 tab
```

### Mistake 4: Unreachable Conditions
```python
# Wrong order:
if age > 0:
    print("Positive age")
elif age > 18:  # This will never execute!
    print("Adult")

# Correct order (specific conditions first):
if age > 18:
    print("Adult")
elif age > 0:
    print("Positive age")
```

## 📝 Logical Operators

You can combine conditions using logical operators:

### AND - Both conditions must be True
```python
if age >= 18 and age < 65:
    print("Working age")
```

### OR - At least one condition must be True
```python
if age < 13 or age > 65:
    print("Reduced ticket price")
```

### NOT - Reverses the condition
```python
if not is_raining:
    print("Go outside!")
```

## 🎮 Real-World Examples

### Example: ATM Withdrawal
```python
balance = 1000
withdrawal = int(input("Amount to withdraw: "))

if withdrawal <= 0:
    print("Invalid amount")
elif withdrawal > balance:
    print("Insufficient funds")
else:
    balance -= withdrawal
    print(f"Withdrawal successful. New balance: ${balance}")
```

### Example: Discount Calculator
```python
total = float(input("Enter purchase total: "))

if total >= 100:
    discount = total * 0.20  # 20% off
    print("20% discount applied!")
elif total >= 50:
    discount = total * 0.10  # 10% off
    print("10% discount applied!")
else:
    discount = 0
    print("No discount")

final_price = total - discount
print(f"Final price: ${final_price:.2f}")
```

## 🚀 Try It Yourself
1. Create a number guessing game that checks if user's guess is too high, too low, or correct
2. Make a BMI calculator that categorizes the result (underweight, normal, overweight, obese)
3. Build a simple quiz with multiple choice questions
4. Create a parking fee calculator based on hours parked

## 📊 Flow Control
Remember: In an if-elif-else chain:
- Only **ONE** block will execute
- Python checks conditions from **top to bottom**
- Once a True condition is found, it executes that block and **skips the rest**
- The `else` block is **optional** and runs if all conditions are False

## 🔗 Next Chapter
Continue to [Chapter 8: Calculator](../8-calculator/) to build a functional calculator program!
