# Chapter 18: For Loops

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/18-for/18-for.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/18-for/18-for.ipynb)


## 📺 Video Tutorial

**Learn Python for loops in 5 minutes! 🔁** (5:47)

## 📚 What You'll Learn
Master the for loop - Python's most elegant way to iterate through sequences and repeat code!

## 🎯 Learning Objectives
- Understand for loop syntax and usage
- Use range() function effectively
- Iterate through strings, lists, and sequences
- Use reversed() and step parameters
- Apply enumerate() for indexed iteration
- Combine loops with conditionals

## 📖 Concept Explanation

### What is a For Loop?
A for loop iterates through a sequence (like a list, string, or range) and executes code for each item.

### Syntax
```python
for variable in sequence:
    # code to execute for each item
```

### How It Works
1. Take first item from sequence
2. Execute the code block
3. Take next item
4. Repeat until no items left

### For Loop vs While Loop
- **For loop**: When you know how many times to repeat
- **While loop**: When you repeat until a condition is false

## 💡 Examples

### Example 1: Basic For Loop
```python
for i in range(5):
    print(i)

# Output: 0, 1, 2, 3, 4
```

### Example 2: Iterating Through a String
```python
name = "Python"

for letter in name:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n
```

### Example 3: Iterating Through a List
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# Output:
# I like apple
# I like banana
# I like cherry
```

### Example 4: Using range() with Different Parameters
```python
# range(stop) - starts at 0
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

print()

# range(start, stop)
for i in range(2, 7):
    print(i, end=" ")  # 2 3 4 5 6

print()

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
```

### Example 5: Countdown with Reversed
```python
# Countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)
print("Blastoff!")

# Alternative using reversed()
for i in reversed(range(1, 11)):
    print(i)
print("Blastoff!")
```

### Example 6: Sum of Numbers
```python
total = 0

for num in range(1, 11):
    total += num

print(f"Sum of 1-10: {total}")  # 55
```

### Example 7: Multiplication Table
```python
number = 7

print(f"Multiplication table for {number}:\n")

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
```

### Example 8: Enumerate for Index and Value
```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start index from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

### Example 9: Iterating Through Dictionary
```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Iterate through keys
for key in student:
    print(f"{key}: {student[key]}")

# Iterate through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

### Example 10: Nested For Loops (Preview)
```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

# Output:
# (0, 0) (0, 1) (0, 2) 
# (1, 0) (1, 1) (1, 2) 
# (2, 0) (2, 1) (2, 2)
```

## 🔍 Common Mistakes

### Mistake 1: Off-by-One Errors
```python
# Wrong: range stops BEFORE the end
for i in range(10):
    print(i)  # Prints 0-9, NOT 0-10

# Correct: Add 1 to include the number
for i in range(11):
    print(i)  # Prints 0-10

# Or use appropriate start/stop
for i in range(1, 11):
    print(i)  # Prints 1-10
```

### Mistake 2: Modifying List While Iterating
```python
# Dangerous!
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Can skip elements!

# Better approach
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
```

### Mistake 3: Using Wrong Variable Name
```python
fruits = ["apple", "banana"]

# Confusing
for fruit in fruits:
    print(fruits)  # Prints whole list twice!

# Clear
for fruit in fruits:
    print(fruit)  # Prints each fruit
```

### Mistake 4: Forgetting range() Around Numbers
```python
# Wrong
for i in 5:  # TypeError!
    print(i)

# Correct
for i in range(5):
    print(i)
```

## ✍️ Practice Exercises

### Easy
1. Print numbers 1-20
2. Print even numbers from 2-20
3. Print your name 10 times
4. Sum numbers from 1-100
5. Print each character in a word

### Medium
6. Create a multiplication table (1-12)
7. Count vowels in a string
8. Find factorial of a number
9. Print Fibonacci sequence (first 10 numbers)
10. Calculate average of a list of numbers

### Hard
11. Print prime numbers up to 50
12. Reverse a string using a loop
13. Find all divisors of a number
14. Create a pattern printer
15. Build a grade calculator for multiple students

## 🎮 Real-World Applications

### Application 1: Grade Calculator
```python
print("=== Grade Calculator ===\n")

num_students = int(input("How many students? "))
total_average = 0

for i in range(1, num_students + 1):
    print(f"\nStudent {i}:")
    grade = float(input("Enter grade: "))
    total_average += grade
    
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"
    
    print(f"Letter grade: {letter}")

class_average = total_average / num_students
print(f"\nClass average: {class_average:.2f}")
```

### Application 2: Shopping Receipt
```python
print("=== Shopping Receipt ===\n")

items = []
prices = []
quantities = []

num_items = int(input("How many items? "))

for i in range(num_items):
    print(f"\nItem {i + 1}:")
    item = input("Item name: ")
    price = float(input("Price: $"))
    qty = int(input("Quantity: "))
    
    items.append(item)
    prices.append(price)
    quantities.append(qty)

print("\n" + "="*40)
print("RECEIPT")
print("="*40)

total = 0
for i in range(num_items):
    subtotal = prices[i] * quantities[i]
    total += subtotal
    print(f"{items[i]:<20} {quantities[i]}× ${prices[i]:.2f} = ${subtotal:.2f}")

print("="*40)
print(f"{'TOTAL:':<20} ${total:.2f}")
print("="*40)
```

### Application 3: Password Generator
```python
import random

print("=== Password Generator ===\n")

length = int(input("Password length: "))
password = ""

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*"

all_chars = lowercase + uppercase + digits + symbols

for i in range(length):
    password += random.choice(all_chars)

print(f"Generated password: {password}")
```

### Application 4: Data Analysis
```python
# Temperature analysis
temperatures = [72, 75, 68, 70, 73, 71, 69, 74, 76, 72]

total = 0
highest = temperatures[0]
lowest = temperatures[0]

for temp in temperatures:
    total += temp
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

average = total / len(temperatures)

print(f"Average temperature: {average:.1f}°F")
print(f"Highest: {highest}°F")
print(f"Lowest: {lowest}°F")
print(f"Range: {highest - lowest}°F")
```

### Application 5: ASCII Art Generator
```python
# Triangle pattern
height = int(input("Enter height: "))

for i in range(1, height + 1):
    print("* " * i)

# Output for height=5:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
```

## 🚀 Challenge Projects

### Challenge 1: Prime Number Finder
Create a program that:
- Finds all prime numbers up to N
- Shows how many primes were found
- Calculates sum of all primes
- Displays them in rows of 10

### Challenge 2: Fibonacci Sequence
Build a program that:
- Generates first N Fibonacci numbers
- Shows the ratio between consecutive numbers
- Calculates sum of even Fibonacci numbers
- Finds Fibonacci numbers under a limit

### Challenge 3: Statistics Calculator
Create a tool that:
- Accepts multiple numbers from user
- Calculates mean, median, mode
- Finds range and standard deviation
- Shows frequency distribution

### Challenge 4: Text Analyzer
Build a program that:
- Counts words, sentences, paragraphs
- Finds most common words
- Calculates average word length
- Identifies longest and shortest words

### Challenge 5: Pattern Creator
Create patterns like:
```
    *
   ***
  *****
 *******
*********
```
- Allow user to choose height
- Create different shapes (diamond, pyramid, etc.)
- Use different characters
- Add colors (using ANSI codes)

## 📚 Range() Function Reference

```python
# Basic usage
range(stop)           # 0 to stop-1
range(start, stop)    # start to stop-1
range(start, stop, step)  # start to stop-1, by step

# Examples
range(5)              # 0, 1, 2, 3, 4
range(2, 8)           # 2, 3, 4, 5, 6, 7
range(0, 10, 2)       # 0, 2, 4, 6, 8
range(10, 0, -1)      # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
range(5, 0, -2)       # 5, 3, 1
```

## 🔄 Loop Control Statements

### Break - Exit Loop Early
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Prints: 0, 1, 2, 3, 4
```

### Continue - Skip Current Iteration
```python
for i in range(6):
    if i == 3:
        continue
    print(i)
# Prints: 0, 1, 2, 4, 5
```

### Else with For Loop
```python
for i in range(5):
    print(i)
else:
    print("Loop completed!")
# Runs if loop wasn't broken
```

## 🎯 Common Patterns

### Count Occurrences
```python
text = "hello world"
count = 0

for char in text:
    if char == 'l':
        count += 1

print(f"'l' appears {count} times")
```

### Build a String
```python
result = ""

for i in range(5):
    result += str(i) + " "

print(result)  # "0 1 2 3 4 "
```

### Find Maximum
```python
numbers = [34, 78, 12, 90, 45]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Maximum: {maximum}")
```

## 💪 Try It Yourself

Modify `main.py` to:
1. Create a countdown timer
2. Build a times table generator
3. Make a number pattern printer
4. Calculate factorial
5. Find all multiples of 3 in a range

## 🎓 Key Takeaways from Video

1. Strings are text data enclosed in quotes
2. Understanding the proper syntax is important
3. Use loops to repeat actions
4. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter
Continue to [Chapter 19: Countdown Timer](19-timer.md) to build a real countdown timer application!

