# 📝 List Comprehensions

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/38-list-comprehensions/38-list-comprehensions.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/38-list-comprehensions/38-list-comprehensions.ipynb)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/YlY2g2xrl6Q)

**Learn Python LIST COMPREHENSIONS in 10 minutes! 📃** (10:22)

## What You'll Learn

In this chapter, you'll master list comprehensions - a powerful Python feature that allows you to create lists in a single, readable line of code. You'll learn how to transform data, filter elements, use conditional logic, and write more Pythonic, efficient code that replaces traditional for loops with elegant one-liners.

## Learning Objectives

- Create lists using comprehension syntax instead of traditional loops
- Transform elements with expressions in list comprehensions
- Filter elements using conditional statements (`if`)
- Use if-else conditions within comprehensions
- Apply list comprehensions to various data types
- Recognize when to use comprehensions vs traditional loops

## Concept Explanation

### What are List Comprehensions?

List comprehensions provide a concise way to create lists. They're more compact and often faster than traditional for loops.

**Traditional For Loop:**
```python
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)  # [1, 4, 9, 16, 25]
```

**List Comprehension:**
```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

### Basic Syntax

```python
[expression for item in iterable]
```

- **expression**: What to do with each item (e.g., `x * 2`)
- **item**: Variable representing current element
- **iterable**: Sequence to iterate over (list, range, string, etc.)

**Examples:**
```python
# Double all numbers
doubles = [x * 2 for x in range(1, 6)]  # [2, 4, 6, 8, 10]

# Convert to uppercase
words = ["hello", "world"]
upper = [word.upper() for word in words]  # ['HELLO', 'WORLD']

# Get lengths
names = ["Alice", "Bob", "Charlie"]
lengths = [len(name) for name in names]  # [5, 3, 7]
```

### With Filtering (if condition)

Add an `if` clause to filter elements:

```python
[expression for item in iterable if condition]
```

**Examples:**
```python
# Only even numbers
numbers = range(1, 11)
evens = [x for x in numbers if x % 2 == 0]  # [2, 4, 6, 8, 10]

# Only positive numbers
values = [-5, -2, 0, 3, 7, -1, 9]
positives = [x for x in values if x > 0]  # [3, 7, 9]

# Only long words
words = ["cat", "elephant", "dog", "butterfly"]
long_words = [w for w in words if len(w) > 5]  # ['elephant', 'butterfly']
```

### With If-Else (Conditional Expression)

Use if-else to choose between two expressions:

```python
[expression_if_true if condition else expression_if_false for item in iterable]
```

**Examples:**
```python
# "even" or "odd"
numbers = range(1, 6)
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
# ['odd', 'even', 'odd', 'even', 'odd']

# Convert negatives to 0
values = [-2, 5, -8, 3, -1, 7]
non_negative = [x if x >= 0 else 0 for x in values]
# [0, 5, 0, 3, 0, 7]

# Grade pass/fail
scores = [85, 92, 67, 78, 95]
results = ["Pass" if s >= 70 else "Fail" for s in scores]
# ['Pass', 'Pass', 'Fail', 'Pass', 'Pass']
```

### Why Use List Comprehensions?

#### 1. **More Concise**
```python
# Traditional: 4 lines
squares = []
for x in range(5):
    squares.append(x ** 2)

# Comprehension: 1 line
squares = [x ** 2 for x in range(5)]
```

#### 2. **More Readable**
Once you're familiar with the syntax, comprehensions are easier to read:
```python
# Clear intent: "create list of squares from 0 to 4"
squares = [x ** 2 for x in range(5)]
```

#### 3. **Faster**
List comprehensions are optimized in Python and run faster than equivalent loops.

#### 4. **More Pythonic**
They're the idiomatic Python way to create lists.

### Common Patterns

#### 1. **Transformation**
```python
# Multiply all by 10
numbers = [1, 2, 3, 4, 5]
times_ten = [n * 10 for n in numbers]  # [10, 20, 30, 40, 50]
```

#### 2. **Extraction**
```python
# Extract first letter
words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]  # ['a', 'b', 'c']
```

#### 3. **Filtering**
```python
# Only strings longer than 3 characters
words = ["a", "hello", "hi", "world"]
long = [w for w in words if len(w) > 3]  # ['hello', 'world']
```

#### 4. **Combining**
```python
# Square evens, keep odds as-is
numbers = [1, 2, 3, 4, 5]
result = [x**2 if x % 2 == 0 else x for x in numbers]
# [1, 4, 3, 16, 5]
```

### Nested List Comprehensions

You can nest comprehensions for complex operations:

```python
# Create 2D grid
grid = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]
```

### When NOT to Use List Comprehensions

**Avoid when:**
1. Logic is too complex (reduces readability)
2. You need to perform actions with side effects
3. You don't need the resulting list

```python
# Too complex - use traditional loop
result = [x*2 if x > 0 else abs(x)*3 if x < -5 else 0 for x in numbers]

# Better with traditional loop:
result = []
for x in numbers:
    if x > 0:
        result.append(x * 2)
    elif x < -5:
        result.append(abs(x) * 3)
    else:
        result.append(0)
```

## Examples

### Example 1: Basic Transformations
```python
# Squares
squares = [x**2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Cubes
cubes = [x**3 for x in range(1, 6)]
print(cubes)  # [1, 8, 27, 64, 125]

# Multiply by 5
numbers = range(1, 11)
times_five = [n * 5 for n in numbers]
print(times_five)  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

### Example 2: String Manipulation
```python
fruits = ["apple", "banana", "cherry", "date"]

# Uppercase
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # ['APPLE', 'BANANA', 'CHERRY', 'DATE']

# First letter
initials = [fruit[0] for fruit in fruits]
print(initials)  # ['a', 'b', 'c', 'd']

# Add prefix
prefixed = [f"I like {fruit}" for fruit in fruits]
print(prefixed)  # ['I like apple', 'I like banana', ...]
```

### Example 3: Filtering
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Only evens
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Only odds
odds = [n for n in numbers if n % 2 != 0]
print(odds)  # [1, 3, 5, 7, 9]

# Greater than 5
greater_five = [n for n in numbers if n > 5]
print(greater_five)  # [6, 7, 8, 9, 10]
```

### Example 4: Conditional Expressions
```python
numbers = range(1, 11)

# Even/Odd labels
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(labels)  # ['Odd', 'Even', 'Odd', 'Even', ...]

# Pass/Fail
scores = [45, 78, 92, 65, 88, 55]
results = ["Pass" if s >= 60 else "Fail" for s in scores]
print(results)  # ['Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Fail']

# Positive/Negative/Zero
values = [-5, 0, 3, -2, 7, 0, -1]
signs = ["Positive" if v > 0 else "Negative" if v < 0 else "Zero" for v in values]
print(signs)  # ['Negative', 'Zero', 'Positive', ...]
```

### Example 5: Working with Strings
```python
sentence = "Hello World Python Programming"
words = sentence.split()

# Word lengths
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6, 11]

# Long words only (> 5 chars)
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['Python', 'Programming']

# Lowercase
lower_words = [word.lower() for word in words]
print(lower_words)  # ['hello', 'world', 'python', 'programming']

# First 3 letters
short = [word[:3] for word in words]
print(short)  # ['Hel', 'Wor', 'Pyt', 'Pro']
```

### Example 6: Temperature Conversion
```python
celsius = [0, 10, 20, 25, 30, 37, 100]

# Convert to Fahrenheit
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 77.0, 86.0, 98.6, 212.0]

# Format as strings with units
temp_strings = [f"{c}°C = {(c * 9/5) + 32}°F" for c in celsius]
for temp in temp_strings:
    print(temp)
# 0°C = 32.0°F
# 10°C = 50.0°F
# ...
```

### Example 7: Data Processing
```python
# Student data
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

# Extract names
names = [student["name"] for student in students]
print(names)  # ['Alice', 'Bob', 'Charlie', 'David']

# Extract scores
scores = [student["score"] for student in students]
print(scores)  # [85, 92, 78, 95]

# Get high scorers (score >= 90)
high_scorers = [s["name"] for s in students if s["score"] >= 90]
print(high_scorers)  # ['Bob', 'David']

# Create grade labels
grades = [f"{s['name']}: {'A' if s['score'] >= 90 else 'B'}" for s in students]
print(grades)  # ['Alice: B', 'Bob: A', 'Charlie: B', 'David: A']
```

## Practice Exercises

### Beginner Level

1. **Number Doubler**: Create a list of numbers 1-20 doubled.

2. **Name Lengths**: Given a list of names, create a list of their lengths.

3. **Vowel Filter**: Extract only vowels from a string using list comprehension.

4. **Square Odds**: Square all odd numbers from 1-20.

5. **Negative Converter**: Convert all positive numbers to negative.

### Intermediate Level

6. **Prime Filter**: Create a list of prime numbers from 1-100 using comprehension.

7. **Word Filter**: Extract words that start with a vowel from a list.

8. **Nested Lists**: Create a 5x5 multiplication table using list comprehension.

9. **Dictionary Transformation**: Transform a list of dictionaries, extracting specific fields.

10. **Conditional Formatting**: Format numbers differently based on whether they're positive or negative.

### Advanced Level

11. **Flatten Nested Lists**: Flatten a list of lists into a single list using comprehension.

12. **Matrix Operations**: Transpose a 2D matrix using nested list comprehensions.

13. **Complex Filtering**: Combine multiple conditions with AND/OR logic in comprehensions.

14. **String Processing**: Parse CSV-like strings into structured data using comprehensions.

15. **Cartesian Product**: Generate all combinations of two lists using nested comprehensions.

## Common Mistakes to Avoid

### Mistake 1: Too Complex Comprehension

**Wrong:**
```python
# Unreadable - too complex
result = [x*2 if x > 0 else x*3 if x < 0 else 0 for x in nums if x != 5]
```

**Correct:**
```python
# Use traditional loop for complex logic
result = []
for x in nums:
    if x == 5:
        continue
    if x > 0:
        result.append(x * 2)
    elif x < 0:
        result.append(x * 3)
    else:
        result.append(0)
```

**Why:** Comprehensions should be readable. Complex logic is better in traditional loops.

### Mistake 2: Wrong If/Else Position

**Wrong:**
```python
# SyntaxError - if-else in wrong position
evens = [x for x in range(10) if x % 2 == 0 else x + 1]
```

**Correct:**
```python
# If-else goes BEFORE 'for'
result = [x if x % 2 == 0 else x + 1 for x in range(10)]

# If-only (filter) goes at END
evens = [x for x in range(10) if x % 2 == 0]
```

**Why:** Filter `if` goes at end. Conditional expression `if-else` goes before `for`.

### Mistake 3: Modifying Original List

**Wrong:**
```python
numbers = [1, 2, 3, 4, 5]
# This creates a new list, doesn't modify original
[n * 2 for n in numbers]
print(numbers)  # [1, 2, 3, 4, 5] - unchanged!
```

**Correct:**
```python
numbers = [1, 2, 3, 4, 5]
numbers = [n * 2 for n in numbers]  # Assign to variable
print(numbers)  # [2, 4, 6, 8, 10]
```

**Why:** Comprehensions create new lists. Must assign to variable to save result.

### Mistake 4: Unnecessary Comprehension

**Wrong:**
```python
# Don't need list, just iterating
[print(x) for x in range(5)]  # Creates unnecessary list
```

**Correct:**
```python
# Use regular loop for side effects
for x in range(5):
    print(x)
```

**Why:** Use comprehensions to create lists, not for side effects.

## Real-World Applications

### 1. **Data Cleaning**
```python
# Remove empty strings and whitespace
data = ["  hello", "", "world  ", "  ", "python"]
cleaned = [s.strip() for s in data if s.strip()]
```

### 2. **API Response Processing**
```python
# Extract IDs from API response
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
user_ids = [user["id"] for user in users]
```

### 3. **File Processing**
```python
# Read and process file lines
lines = [line.strip() for line in file.readlines() if line.strip()]
```

### 4. **URL Generation**
```python
# Create list of URLs
ids = [1, 2, 3, 4, 5]
urls = [f"https://api.example.com/users/{id}" for id in ids]
```

## Challenge Projects

### 1. **Data Transformer**
Create a program that transforms various data formats using comprehensions.

**Requirements:**
- CSV to dictionary list
- JSON flattening
- Data type conversions
- Filtering and sorting
- Nested comprehensions

### 2. **Text Analyzer**
Build a text analysis tool using comprehensions.

**Requirements:**
- Word frequency counter
- Extract emails/URLs
- Filter profanity
- Statistics (avg word length, etc.)
- Sentence parser

### 3. **Matrix Calculator**
Implement matrix operations with comprehensions.

**Requirements:**
- Matrix addition/subtraction
- Matrix multiplication
- Transpose
- Determinant (2x2, 3x3)
- Row/column operations

### 4. **Game Board Generator**
Create various game boards using comprehensions.

**Requirements:**
- Chess board
- Tic-tac-toe grid
- Sudoku template
- Minesweeper grid
- Custom patterns

### 5. **Report Generator**
Generate formatted reports from raw data.

**Requirements:**
- Table formatting
- Summary statistics
- Grouping and aggregation
- Conditional formatting
- Multi-level headers

---

## Navigation

- **Previous:** [36. Membership Operators](36-membership-operators.md)
- **Next:** [38. Match Case Statements](38-match-case-statements.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Lists store multiple items in a single variable
2. Use loops to repeat actions
3. Follow along with the video for hands-on practice

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*