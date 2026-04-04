# Chapter 36: Iterables

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/36-iterables/36-iterables.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/36-iterables/36-iterables.ipynb)


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/36-iterables/36-iterables.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/36-iterables/36-iterables.ipynb)

# 🔄 Iterables

## 📺 Video Tutorial

**Learn Python iterables in 6 minutes! 🔂** (6:48)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/VL_g3LjsFqs)

## What You'll Learn

In this chapter, you'll understand iterables - objects that can return their elements one at a time, allowing them to be used in loops. You'll learn what makes something iterable, how iteration works under the hood with `iter()` and `next()`, and how to work with different iterable types including lists, tuples, strings, sets, and dictionaries.

## Learning Objectives

- Understand what makes an object iterable in Python
- Use for loops to iterate over various iterable objects
- Apply `reversed()` to iterate in reverse order
- Recognize the difference between ordered and unordered iterables
- Work with the iteration protocol using `iter()` and `next()`
- Identify which built-in types are iterable and their characteristics

## Concept Explanation

### What is an Iterable?

An **iterable** is any Python object capable of returning its elements one at a time, allowing it to be iterated over in a loop.

```python
# These are all iterables
numbers = [1, 2, 3]        # List
letters = "abc"            # String
coordinates = (5, 10)      # Tuple
unique_nums = {1, 2, 3}    # Set
person = {"name": "Alice"} # Dictionary

# They can all be used in for loops
for item in numbers:
    print(item)
```

**Key Point:** If you can use it in a `for` loop, it's iterable!

### Common Iterable Types

#### 1. **Lists** - Ordered, Mutable, Reversible
```python
fruits = ["apple", "banana", "cherry"]

# Forward iteration
for fruit in fruits:
    print(fruit)  # apple, banana, cherry

# Reverse iteration
for fruit in reversed(fruits):
    print(fruit)  # cherry, banana, apple
```

#### 2. **Tuples** - Ordered, Immutable, Reversible
```python
coordinates = (10, 20, 30)

for coord in coordinates:
    print(coord)  # 10, 20, 30

for coord in reversed(coordinates):
    print(coord)  # 30, 20, 10
```

#### 3. **Strings** - Ordered, Immutable, Reversible
```python
name = "Python"

for char in name:
    print(char)  # P, y, t, h, o, n

for char in reversed(name):
    print(char)  # n, o, h, t, y, P
```

#### 4. **Sets** - Unordered, Mutable, NOT Reversible
```python
numbers = {1, 2, 3, 4, 5}

# Iteration works
for num in numbers:
    print(num)  # Order not guaranteed!

# reversed() doesn't work
# for num in reversed(numbers):  # TypeError!
#     print(num)
```

**Important:** Sets have no defined order, so `reversed()` raises a `TypeError`.

#### 5. **Dictionaries** - Ordered (Python 3.7+), Mutable, Reversible
```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Iterate over keys (default)
for key in person:
    print(key)  # name, age, city

# Iterate over values
for value in person.values():
    print(value)  # Alice, 25, NYC

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Reverse iteration (Python 3.8+)
for key in reversed(person):
    print(key)  # city, age, name
```

### The Iteration Protocol

Under the hood, iteration uses two special methods:

#### 1. **`iter()` - Get Iterator**
Converts an iterable to an iterator:

```python
numbers = [1, 2, 3]
iterator = iter(numbers)  # Create iterator

print(type(numbers))   # <class 'list'>
print(type(iterator))  # <class 'list_iterator'>
```

#### 2. **`next()` - Get Next Element**
Gets the next element from an iterator:

```python
numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # StopIteration exception!
```

**What `for` loops do automatically:**

```python
# When you write:
for item in iterable:
    print(item)

# Python actually does:
iterator = iter(iterable)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```

### Ordered vs Unordered Iterables

**Ordered Iterables** (support `reversed()`):
- Lists
- Tuples
- Strings
- Dictionaries (Python 3.7+)
- Ranges

**Unordered Iterables** (don't support `reversed()`):
- Sets
- Frozensets

```python
# Ordered - reversed() works
numbers_list = [1, 2, 3]
for n in reversed(numbers_list):
    print(n)  # 3, 2, 1

# Unordered - reversed() fails
numbers_set = {1, 2, 3}
# for n in reversed(numbers_set):  # TypeError!
#     print(n)
```

### The `reversed()` Function

`reversed()` returns a **reverse iterator** that accesses elements in reverse order:

```python
numbers = [1, 2, 3, 4, 5]

# reversed() returns an iterator
rev = reversed(numbers)
print(type(rev))  # <class 'list_reverseiterator'>

# Use in for loop
for num in reversed(numbers):
    print(num)  # 5, 4, 3, 2, 1

# Convert to list
reversed_list = list(reversed(numbers))
print(reversed_list)  # [5, 4, 3, 2, 1]
```

**Alternative: Slicing**

For sequences, you can also use slicing:

```python
numbers = [1, 2, 3, 4, 5]

# Using reversed()
for num in reversed(numbers):
    print(num)

# Using slicing [::-1]
for num in numbers[::-1]:
    print(num)

# Both produce same output
```

**Difference:**
- `reversed()` - Returns an iterator (memory efficient)
- `[::-1]` - Creates a new reversed copy (uses more memory)

### Practical Iteration Patterns

#### 1. **Enumerate - Get Index and Value**
```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start from custom index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: apple
# 2: banana
# 3: cherry
```

#### 2. **Zip - Iterate Multiple Iterables**
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")
# Alice, 25, NYC
# Bob, 30, LA
# Charlie, 35, Chicago
```

#### 3. **Break and Continue**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Break - stop early
for num in numbers:
    if num > 5:
        break
    print(num)  # 1, 2, 3, 4, 5

# Continue - skip some
for num in numbers:
    if num % 2 == 0:  # Skip even numbers
        continue
    print(num)  # 1, 3, 5, 7, 9
```

### Checking if Something is Iterable

```python
from collections.abc import Iterable

# Check if object is iterable
print(isinstance([1, 2, 3], Iterable))    # True
print(isinstance("hello", Iterable))      # True
print(isinstance(123, Iterable))          # False
print(isinstance({"a": 1}, Iterable))     # True
```

## Examples

### Example 1: Iterating Over Different Types
```python
# List iteration
print("List iteration:")
numbers = [10, 20, 30, 40]
for num in numbers:
    print(num, end=" ")  # 10 20 30 40
print()

# String iteration
print("String iteration:")
word = "Python"
for char in word:
    print(char, end=" ")  # P y t h o n
print()

# Tuple iteration
print("Tuple iteration:")
colors = ("red", "green", "blue")
for color in colors:
    print(color, end=" ")  # red green blue
print()

# Set iteration (order not guaranteed)
print("Set iteration:")
unique = {1, 2, 3, 4, 5}
for num in unique:
    print(num, end=" ")  # Could be any order
print()
```

### Example 2: Reverse Iteration
```python
# List
numbers = [1, 2, 3, 4, 5]
print("Forward:", end=" ")
for num in numbers:
    print(num, end=" ")  # 1 2 3 4 5
print()

print("Backward:", end=" ")
for num in reversed(numbers):
    print(num, end=" ")  # 5 4 3 2 1
print()

# String
name = "Alice"
print("Forward:", name)  # Alice
print("Backward:", "".join(reversed(name)))  # ecilA

# Tuple
coordinates = (10, 20, 30)
print("Forward:", coordinates)  # (10, 20, 30)
print("Backward:", tuple(reversed(coordinates)))  # (30, 20, 10)
```

### Example 3: Dictionary Iteration
```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "major": "Computer Science"
}

print("Iterate over keys:")
for key in student:
    print(key, end=" ")  # name age grade major
print()

print("\nIterate over values:")
for value in student.values():
    print(value, end=" ")  # Alice 20 A Computer Science
print()

print("\nIterate over items:")
for key, value in student.items():
    print(f"{key}: {value}")
# name: Alice
# age: 20
# grade: A
# major: Computer Science

print("\nReverse iteration:")
for key in reversed(student):
    print(f"{key}: {student[key]}")
# major: Computer Science
# grade: A
# age: 20
# name: Alice
```

### Example 4: Using iter() and next()
```python
fruits = ["apple", "banana", "cherry"]

# Create iterator
fruit_iterator = iter(fruits)

# Manual iteration with next()
print(next(fruit_iterator))  # apple
print(next(fruit_iterator))  # banana
print(next(fruit_iterator))  # cherry

# This would raise StopIteration
# print(next(fruit_iterator))  # Error!

# Safe next() with default value
print(next(fruit_iterator, "No more fruits"))  # No more fruits
```

### Example 5: Enumerate with Index
```python
shopping_list = ["milk", "eggs", "bread", "butter"]

print("Shopping List:")
print("-" * 30)

# Get both index and item
for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")

# Output:
# Shopping List:
# ------------------------------
# 1. milk
# 2. eggs
# 3. bread
# 4. butter
```

### Example 6: Zipping Multiple Lists
```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999, 25, 75]
quantities = [5, 20, 15]

print("Inventory Report:")
print("-" * 50)
print(f"{'Product':<15} {'Price':<10} {'Quantity':<10} {'Total'}")
print("-" * 50)

for product, price, quantity in zip(products, prices, quantities):
    total = price * quantity
    print(f"{product:<15} ${price:<9} {quantity:<10} ${total}")

# Output:
# Inventory Report:
# --------------------------------------------------
# Product         Price      Quantity   Total
# --------------------------------------------------
# Laptop          $999       5          $4995
# Mouse           $25        20         $500
# Keyboard        $75        15         $1125
```

### Example 7: Processing Lines from String
```python
text = """Python is awesome
It's easy to learn
Great for beginners
Powerful for experts"""

print("Lines with line numbers:")
for line_num, line in enumerate(text.split('\n'), start=1):
    print(f"Line {line_num}: {line}")

# Output:
# Lines with line numbers:
# Line 1: Python is awesome
# Line 2: It's easy to learn
# Line 3: Great for beginners
# Line 4: Powerful for experts

print("\nReversed lines:")
for line in reversed(text.split('\n')):
    print(line)

# Output:
# Reversed lines:
# Powerful for experts
# Great for beginners
# It's easy to learn
# Python is awesome
```

## Practice Exercises

### Beginner Level

1. **Count Elements**: Create a program that counts how many items are in different iterables (list, tuple, string).

2. **Sum Calculator**: Write a function that sums all numbers in any iterable using a for loop.

3. **Character Finder**: Create a program that iterates through a string and counts vowels.

4. **Reverse Printer**: Write a function that prints any iterable in reverse (handle both ordered and unordered).

5. **First and Last**: Create a function that returns the first and last elements of any iterable.

### Intermediate Level

6. **Even/Odd Separator**: Write a function that iterates through a list and separates even and odd numbers into two lists.

7. **Dictionary Reverser**: Create a function that reverses the order of key-value pairs in a dictionary.

8. **Sliding Window**: Implement a function that iterates through a list with a sliding window of size n.

9. **Iterator Class**: Create a custom iterator class that iterates through a range with a custom step.

10. **Palindrome Checker**: Use iteration to check if a string or list is a palindrome.

### Advanced Level

11. **Custom Range**: Implement your own range() function using the iterator protocol.

12. **Infinite Iterator**: Create an infinite iterator that cycles through a list indefinitely.

13. **Grouped Iterator**: Build an iterator that yields items in groups of n (like batching).

14. **Filter Iterator**: Create a custom iterator that filters elements based on a condition during iteration.

15. **Parallel Iteration**: Implement a function that iterates through multiple iterables in parallel and yields tuples.

## Common Mistakes to Avoid

### Mistake 1: Trying to Reverse Unordered Iterables

**Wrong:**
```python
numbers_set = {1, 2, 3, 4, 5}

# TypeError: 'set' object is not reversible
for num in reversed(numbers_set):
    print(num)
```

**Correct:**
```python
numbers_set = {1, 2, 3, 4, 5}

# Convert to list first
for num in reversed(list(numbers_set)):
    print(num)

# Or just iterate normally (sets have no order anyway)
for num in numbers_set:
    print(num)
```

**Why:** Sets are unordered, so reversing doesn't make sense. Convert to list first if you need order.

### Mistake 2: Modifying List While Iterating

**Wrong:**
```python
numbers = [1, 2, 3, 4, 5]

# Dangerous - modifying while iterating
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Can skip elements!

print(numbers)  # May not remove all even numbers
```

**Correct:**
```python
numbers = [1, 2, 3, 4, 5]

# Create new list
numbers = [num for num in numbers if num % 2 != 0]

# Or iterate over copy
for num in numbers[:]:  # [:] creates copy
    if num % 2 == 0:
        numbers.remove(num)
```

**Why:** Modifying a list while iterating can cause skipped elements or errors. Use list comprehension or iterate over a copy.

### Mistake 3: Exhausting Iterators

**Wrong:**
```python
numbers = [1, 2, 3, 4, 5]
num_iterator = iter(numbers)

# Use iterator
total = sum(num_iterator)
print(total)  # 15

# Try to use again
count = len(list(num_iterator))  # Returns 0!
print(count)  # 0 - iterator is exhausted!
```

**Correct:**
```python
numbers = [1, 2, 3, 4, 5]

# Use original iterable multiple times
total = sum(numbers)
count = len(numbers)

# Or create new iterator each time
num_iterator1 = iter(numbers)
total = sum(num_iterator1)

num_iterator2 = iter(numbers)
count = len(list(num_iterator2))
```

**Why:** Iterators can only be used once. Once exhausted, they don't reset. Use the original iterable or create new iterators.

### Mistake 4: Assuming Dictionary Order in Old Python

**Wrong:**
```python
# In Python < 3.7, dictionary order is not guaranteed
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Don't rely on order in Python < 3.7
first_key = list(person.keys())[0]  # Might not be "name"!
```

**Correct:**
```python
# For Python 3.7+ - order is guaranteed
person = {"name": "Alice", "age": 25, "city": "NYC"}
first_key = list(person.keys())[0]  # "name"

# Or use OrderedDict for older Python versions
from collections import OrderedDict
person = OrderedDict([("name", "Alice"), ("age", 25)])
```

**Why:** Dictionaries maintain insertion order only in Python 3.7+. For older versions, use OrderedDict.

## Real-World Applications

### 1. **File Processing**
Reading and processing files line by line:

```python
with open('data.txt', 'r') as file:
    for line in file:  # File objects are iterable
        process_line(line.strip())
```

### 2. **Database Results**
Processing database query results:

```python
cursor.execute("SELECT * FROM users")
for row in cursor:  # Cursor is iterable
    print(row['name'], row['email'])
```

### 3. **Web Scraping**
Iterating through HTML elements:

```python
for element in soup.find_all('div', class_='product'):
    title = element.find('h2').text
    price = element.find('span', class_='price').text
```

### 4. **Data Analysis**
Processing data frames and series:

```python
for index, row in dataframe.iterrows():
    process_row(row)

for value in series:
    analyze_value(value)
```

## Challenge Projects

### 1. **Custom Iterator Class**
Build a custom iterator for a playlist.

**Requirements:**
- Iterate through songs forward and backward
- Support shuffle mode
- Repeat/loop functionality
- Skip functionality
- Track current position

### 2. **Batch Processor**
Create a batch iterator that processes items in chunks.

**Requirements:**
- Accept any iterable
- Yield items in batches of specified size
- Handle remainder items
- Support overlap between batches
- Memory efficient for large datasets

### 3. **Sliding Window Iterator**
Implement a sliding window over an iterable.

**Requirements:**
- Window size parameter
- Step size parameter
- Yield windows as tuples
- Handle edge cases (window > iterable size)
- Support for infinite iterables

### 4. **Chain Iterator**
Build an iterator that chains multiple iterables.

**Requirements:**
- Accept variable number of iterables
- Iterate seamlessly across all
- Support different iterable types
- Lazy evaluation (don't load all at once)
- Track which iterable is currently active

### 5. **File Reader with Iteration**
Create a custom file reader with advanced iteration.

**Requirements:**
- Iterate by lines, words, or characters
- Reverse iteration support
- Skip blank lines option
- Filter lines by pattern
- Buffered reading for large files
- Context manager support

---

## Navigation

- **Previous:** [34. Args and Kwargs](34-args-kwargs.md)
- **Next:** [36. Membership Operators](36-membership-operators.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Lists store multiple items in a single variable
2. Use loops to repeat actions
3. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
