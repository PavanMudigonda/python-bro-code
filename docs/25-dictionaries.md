# 📖 Dictionaries

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/25-dictionaries/25-dictionaries.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/25-dictionaries/25-dictionaries.ipynb)


## 📺 Video Tutorial

**Python dictionaries are easy 📙** (9:06)

## What You'll Learn

In this chapter, you'll master Python dictionaries - one of the most powerful and versatile data structures in Python. Dictionaries store data as key-value pairs, enabling fast lookups, flexible data organization, and efficient data manipulation.

## Learning Objectives

- Understand dictionary structure and key-value pair relationships
- Create and initialize dictionaries using various methods
- Access, add, update, and delete dictionary items
- Use dictionary methods (get, update, keys, values, items)
- Iterate through dictionaries effectively
- Apply dictionaries to solve real-world problems

## Concept Explanation

### What is a Dictionary?

A **dictionary** is a collection of key-value pairs where each key is unique and maps to a specific value. Think of it like a real dictionary where words (keys) map to definitions (values), or a phone book where names (keys) map to phone numbers (values).

```python
# Dictionary syntax
student = {
    "name": "Alice",      # key: "name", value: "Alice"
    "age": 20,            # key: "age", value: 20
    "major": "Computer Science"
}
```

### Dictionary Properties

1. **Ordered** (as of Python 3.7+) - maintains insertion order
2. **Mutable** - can be changed after creation
3. **Indexed by keys** - not by numeric positions
4. **No duplicate keys** - each key must be unique
5. **Keys must be immutable** - strings, numbers, tuples (not lists)
6. **Values can be anything** - any data type, including other dictionaries

### Key-Value Pairs

The fundamental unit of a dictionary:

```python
capitals = {
    "USA": "Washington D.C.",    # "USA" → key, "Washington D.C." → value
    "France": "Paris",            # "France" → key, "Paris" → value
    "Japan": "Tokyo"              # "Japan" → key, "Tokyo" → value
}
```

### Creating Dictionaries

Multiple ways to create dictionaries:

```python
# Method 1: Literal syntax
person = {"name": "John", "age": 30}

# Method 2: dict() constructor
person = dict(name="John", age=30)

# Method 3: From list of tuples
person = dict([("name", "John"), ("age", 30)])

# Method 4: Empty dictionary
person = {}  # or dict()
```

### Accessing Values

Use keys to retrieve values:

```python
capitals = {"USA": "Washington D.C.", "France": "Paris"}

# Method 1: Square brackets (raises KeyError if key doesn't exist)
print(capitals["USA"])  # "Washington D.C."

# Method 2: get() method (returns None if key doesn't exist)
print(capitals.get("USA"))        # "Washington D.C."
print(capitals.get("Germany"))    # None
print(capitals.get("Germany", "Not Found"))  # "Not Found"
```

### Modifying Dictionaries

```python
capitals = {"USA": "Washington D.C."}

# Add new key-value pair
capitals["France"] = "Paris"

# Update existing value
capitals["USA"] = "Washington DC"

# Delete key-value pair
del capitals["USA"]

# Using update() method
capitals.update({"Germany": "Berlin", "Italy": "Rome"})
```

### Dictionary Methods

Important methods for working with dictionaries:

- **get(key, default)** - Safely retrieve value
- **keys()** - Returns all keys
- **values()** - Returns all values
- **items()** - Returns key-value pairs as tuples
- **update(dict)** - Merge another dictionary
- **pop(key)** - Remove and return value
- **clear()** - Remove all items
- **copy()** - Create shallow copy

### Why Use Dictionaries?

1. **Fast Lookups** - O(1) average time complexity
2. **Flexible Keys** - Use meaningful names instead of indices
3. **Data Organization** - Group related information
4. **Real-World Modeling** - Maps naturally to many scenarios
5. **Readability** - Self-documenting code with descriptive keys

## Examples

### Example 1: Creating and Accessing Dictionaries
```python
# Create dictionary of capitals
capitals = {
    "USA": "Washington D.C.",
    "China": "Beijing",
    "India": "New Delhi",
    "Canada": "Ottawa",
    "Russia": "Moscow"
}

# Access values using keys
print(capitals["USA"])          # "Washington D.C."
print(capitals.get("Canada"))   # "Ottawa"

# Safe access with default value
print(capitals.get("Germany", "Unknown"))  # "Unknown"
```

### Example 2: Adding and Updating Items
```python
capitals = {"USA": "Washington D.C."}

# Add new items
capitals["France"] = "Paris"
capitals["Japan"] = "Tokyo"

# Update existing item
capitals["USA"] = "Washington DC"  # Updated value

# Add multiple items using update()
capitals.update({
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid"
})

print(capitals)
```

### Example 3: Dictionary Methods
```python
capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

# Get all keys
print(capitals.keys())    # dict_keys(['USA', 'France', 'Japan'])

# Get all values
print(capitals.values())  # dict_values(['Washington D.C.', 'Paris', 'Tokyo'])

# Get all key-value pairs
print(capitals.items())   # dict_items([('USA', 'Washington D.C.'), ...])

# Check if key exists
if "France" in capitals:
    print("France is in the dictionary")

# Number of items
print(len(capitals))  # 3
```

### Example 4: Iterating Through Dictionaries
```python
capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

# Iterate over keys (default)
for country in capitals:
    print(country)

# Iterate over values
for capital in capitals.values():
    print(capital)

# Iterate over key-value pairs
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}")

# Output:
# The capital of USA is Washington D.C.
# The capital of France is Paris
# The capital of Japan is Tokyo
```

### Example 5: Nested Dictionaries
```python
# Dictionary containing dictionaries
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science"
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "major": "Mathematics"
    }
}

# Access nested values
print(students["student1"]["name"])  # "Alice"
print(students["student2"]["major"])  # "Mathematics"

# Iterate through nested dictionary
for student_id, info in students.items():
    print(f"{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

### Example 6: Dictionary Comprehension
```python
# Create dictionary using comprehension
numbers = [1, 2, 3, 4, 5]
squares = {num: num**2 for num in numbers}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter while creating dictionary
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squares)  # {2: 4, 4: 16}

# Convert lists to dictionary
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
print(people)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

### Example 7: Practical Student Grade Book
```python
# Grade book using dictionary
gradebook = {
    "Alice": [85, 92, 88, 95],
    "Bob": [78, 85, 90, 88],
    "Charlie": [92, 88, 85, 91]
}

# Calculate average for each student
print("Student Grade Report:")
print("=" * 40)

for student, grades in gradebook.items():
    average = sum(grades) / len(grades)
    print(f"{student:12} - Average: {average:.2f}")
    
# Find student with highest average
best_student = max(gradebook.items(), 
                   key=lambda x: sum(x[1])/len(x[1]))
print(f"\nTop Student: {best_student[0]}")

# Output:
# Student Grade Report:
# ========================================
# Alice        - Average: 90.00
# Bob          - Average: 85.25
# Charlie      - Average: 89.00
#
# Top Student: Alice
```

## Practice Exercises

### Beginner Level

1. **Create Dictionary**: Create a dictionary with 5 countries and their capitals. Print all countries.

2. **Access Practice**: Create a dictionary of 5 fruits with prices. Access and print the price of "apple".

3. **Add Items**: Start with an empty dictionary. Add 3 items (book titles and authors) one by one.

4. **Update Value**: Create a dictionary of 3 products with prices. Update the price of one product.

5. **Check Existence**: Create a dictionary and check if a specific key exists before accessing it.

### Intermediate Level

6. **Word Counter**: Write a program that counts the frequency of each word in a sentence using a dictionary.

7. **Phone Book**: Create a phone book dictionary with names as keys and phone numbers as values. Implement add, search, and delete functions.

8. **Inventory System**: Create a store inventory with items as keys and quantities as values. Implement functions to add stock, sell items, and check availability.

9. **Grade Calculator**: Store student names and their test scores in a dictionary. Calculate and display each student's average.

10. **Dictionary Merge**: Write a function that merges two dictionaries, keeping values from the second dictionary when keys overlap.

### Advanced Level

11. **Inverted Dictionary**: Write a function that swaps keys and values in a dictionary (values become keys, keys become values).

12. **Nested Data Structure**: Create a dictionary representing a school with multiple classes, each containing multiple students with their information.

13. **Dictionary Sorting**: Sort a dictionary by values (not keys) and display the sorted results.

14. **Frequency Analysis**: Read a text file and create a dictionary showing the frequency of each character.

15. **JSON-like Data**: Create a nested dictionary structure representing a company's employee hierarchy, then write functions to search, add, and remove employees.

## Common Mistakes to Avoid

### Mistake 1: Using Mutable Keys

**Wrong:**
```python
# Lists are mutable and cannot be used as keys
inventory = {
    ["apple", "red"]: 10,  # TypeError!
    ["banana", "yellow"]: 5
}
```

**Correct:**
```python
# Use tuples (immutable) as keys
inventory = {
    ("apple", "red"): 10,
    ("banana", "yellow"): 5
}
```

**Why:** Dictionary keys must be immutable (hashable). Use tuples, strings, or numbers as keys.

### Mistake 2: KeyError When Accessing Non-Existent Keys

**Wrong:**
```python
capitals = {"USA": "Washington D.C."}
print(capitals["Germany"])  # KeyError!
```

**Correct:**
```python
capitals = {"USA": "Washington D.C."}
# Method 1: Use get() with default value
print(capitals.get("Germany", "Not found"))  # "Not found"

# Method 2: Check before accessing
if "Germany" in capitals:
    print(capitals["Germany"])
else:
    print("Not found")
```

**Why:** Accessing non-existent keys with square brackets raises KeyError. Use get() for safe access.

### Mistake 3: Modifying Dictionary During Iteration

**Wrong:**
```python
grades = {"Alice": 85, "Bob": 70, "Charlie": 90}
for student in grades:
    if grades[student] < 75:
        del grades[student]  # RuntimeError!
```

**Correct:**
```python
grades = {"Alice": 85, "Bob": 70, "Charlie": 90}
# Create list of keys to delete
to_delete = [student for student, grade in grades.items() if grade < 75]
for student in to_delete:
    del grades[student]

# Or use dictionary comprehension to create new dict
grades = {s: g for s, g in grades.items() if g >= 75}
```

**Why:** Cannot modify dictionary size while iterating. Create a separate list or new dictionary.

### Mistake 4: Confusing Keys and Values

**Wrong:**
```python
capitals = {"USA": "Washington D.C.", "France": "Paris"}
# Trying to find country by capital
country = capitals["Paris"]  # KeyError!
```

**Correct:**
```python
capitals = {"USA": "Washington D.C.", "France": "Paris"}
# Find key by value
country = [k for k, v in capitals.items() if v == "Paris"][0]
print(country)  # "France"

# Or create reverse dictionary
reverse = {v: k for k, v in capitals.items()}
print(reverse["Paris"])  # "France"
```

**Why:** Dictionary lookup works by key, not value. To find by value, iterate through items.

## Real-World Applications

### 1. **Configuration Management**
Software applications use dictionaries to store configuration settings, user preferences, and environment variables. JSON and YAML files are parsed into dictionaries.

### 2. **Caching and Memoization**
Web applications and databases use dictionary-like structures (hash maps) for caching frequently accessed data, reducing query times from milliseconds to microseconds.

### 3. **Data Analysis and Counting**
Analytics tools use dictionaries to count occurrences (word frequency, event types, user actions) and group data by categories for analysis.

### 4. **Database Records**
ORMs (Object-Relational Mappers) represent database rows as dictionaries, making it easy to access fields by column names rather than indices.

## Challenge Projects

### 1. **Contact Management System**
Build a complete contact manager with search, add, edit, and delete functions.

**Requirements:**
- Store contacts with multiple fields (name, phone, email, address)
- Search by any field
- Edit existing contacts
- Delete contacts with confirmation
- Save/load from file

### 2. **Language Translator**
Create a simple dictionary-based translator between two languages.

**Requirements:**
- Store word translations in dictionary
- Translate sentences word by word
- Handle words not in dictionary
- Add new words to dictionary
- Support reverse translation

### 3. **Inventory Management System**
Build a product inventory tracker for a small store.

**Requirements:**
- Track products with name, quantity, price, category
- Add new products or update existing
- Sell items (decrease quantity)
- Alert when stock is low
- Generate inventory reports

### 4. **Student Management System**
Create a comprehensive student information system.

**Requirements:**
- Store student info (ID, name, courses, grades)
- Calculate GPA for each student
- Find students by course
- Generate transcripts
- Sort students by GPA

### 5. **Website Analytics Tracker**
Simulate a basic analytics system for tracking website visits.

**Requirements:**
- Track page views by URL
- Count unique visitors
- Record visit timestamps
- Calculate average time between visits
- Generate top 10 most visited pages

---

## Navigation

- **Previous:** [24. Quiz Game](24-quiz-game.md)
- **Next:** [26. Concession Stand Program](26-concession-stand-program.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Dictionaries store data in key-value pairs
2. Use loops to repeat actions
3. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*