# Chapter 4: User Input


## 📺 Video Tutorial

**User input in Python is easy + exercises ⌨️** (9:48)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/nMCOB8KElwo)

## 📚 What You'll Learn
Learn how to make your programs interactive by accepting input from users!

## 🎯 Learning Objectives
- Use the `input()` function to get user data
- Understand that `input()` always returns a string
- Combine `input()` with type casting for numeric inputs
- Create interactive programs that respond to user input

## 📖 Concept Explanation

### The input() Function
The `input()` function is used to get information from the user. It:
1. Displays a message (prompt) to the user
2. Waits for the user to type something
3. Returns what the user typed as a **string**

### Syntax
```python
variable = input("Your prompt message: ")
```

### Important: input() Always Returns a String!
Even if the user types a number, `input()` returns it as text:
```python
age = input("Enter your age: ")  # If user types 25, age = "25" (string)
# To do math, convert it:
age = int(input("Enter your age: "))  # Now age = 25 (integer)
```

## 💡 Examples

### Example 1: Simple Text Input
```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

### Example 2: Numeric Input
```python
# Wrong way (can't do math with strings):
age = input("Enter your age: ")
# next_year = age + 1  # Error!

# Correct way:
age = int(input("Enter your age: "))
next_year = age + 1
print(f"Next year you'll be {next_year}")
```

### Example 3: Multiple Inputs
```python
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))

print(f"Hello {first_name} {last_name}, you are {age} years old!")
```

### Example 4: Float Input
```python
height = float(input("Enter your height in meters: "))
print(f"Your height is {height}m")
```

## ✍️ Practice Exercises
1. Create a program that asks for the user's name and favorite color, then prints them
2. Make a program that asks for two numbers and prints their sum
3. Ask for a user's birth year and calculate their age (assume current year is 2025)
4. Create a mad libs style program that asks for several words and creates a story
5. Ask for temperature in Celsius and convert it to Fahrenheit

## 🔍 Common Mistakes

### Mistake 1: Forgetting Type Conversion
```python
# Wrong:
age = input("Age: ")  # age is "25" (string)
print(age + 1)  # Error! Can't add string and number

# Correct:
age = int(input("Age: "))  # age is 25 (integer)
print(age + 1)  # Works! Prints 26
```

### Mistake 2: Wrong Conversion Type
```python
# If user enters "3.14":
number = int(input("Enter number: "))  # Error! Can't convert "3.14" to int

# Use float() instead:
number = float(input("Enter number: "))  # Works! number = 3.14
```

### Mistake 3: Forgetting the Prompt
```python
name = input()  # Works but user doesn't know what to enter
name = input("Enter your name: ")  # Better! Clear instruction
```

## 📝 Input Patterns

### Pattern 1: Input on Same Line as Conversion
```python
age = int(input("Enter age: "))
```

### Pattern 2: Input Then Convert (easier to debug)
```python
age_str = input("Enter age: ")
age = int(age_str)
```

### Pattern 3: Input with Validation (advanced)
```python
age = input("Enter age: ")
if age.isdigit():  # Check if input is a number
    age = int(age)
    print(f"You are {age} years old")
else:
    print("Please enter a valid number")
```

## 🎮 Interactive Program Example
```python
# Simple greeting program
name = input("What's your name? ")
age = int(input("How old are you? "))
city = input("Where do you live? ")

print(f"\nNice to meet you, {name}!")
print(f"You are {age} years old and live in {city}.")
print("Welcome to Python programming!")
```

## 🚀 Try It Yourself
Create an interactive program that:
1. Asks the user for their name
2. Asks for their favorite number (integer)
3. Asks for their favorite food
4. Creates a personalized message using all the information

## 🔗 Next Chapter
Continue to [Chapter 5: Madlibs Game](../5-madlibs-game/) to create a fun word game using user input!
