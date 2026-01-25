# Chapter 21: Sets 🎲

## 📺 Video Tutorial

**Python lists, sets, and tuples explained 🍍** (13:04)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/gOMW_n2-2Mw)

## What You'll Learn
Master Python sets, an unordered collection type that automatically handles unique values and provides powerful mathematical set operations.

## Learning Objectives
By the end of this chapter, you will:
- Understand what sets are and when to use them
- Create and manipulate sets using methods
- Leverage automatic duplicate removal
- Apply set operations (union, intersection, difference)
- Choose between lists, sets, and tuples appropriately
- Optimize code using set membership testing

## Concept Explanation

### What is a Set?
A **set** is an unordered collection of unique items. Think of it like a bag of items where:
- No duplicates allowed
- No specific order (can't access by index)
- Items are immutable (but you can add/remove from set)
- Very fast membership testing

### Collection Types Comparison
| Type | Symbol | Ordered | Changeable | Duplicates | Speed |
|------|--------|---------|------------|------------|-------|
| List | `[]` | ✅ Yes | ✅ Yes | ✅ Yes | Medium |
| Set | `{}` | ❌ No | ✅ Yes* | ❌ No | Fast |
| Tuple | `()` | ✅ Yes | ❌ No | ✅ Yes | Fastest |

*Can add/remove items, but items themselves must be immutable

### Set Syntax
```python
# Creating sets
empty_set = set()  # Must use set(), not {}
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14}  # Different types OK
```

### Why Use Sets?
1. **Remove duplicates** automatically
2. **Fast membership testing** (`in` operator)
3. **Mathematical operations** (union, intersection)
4. **Unique collections** (tags, categories, IDs)

## Examples

### Example 1: Creating Sets
```python
# Basic set creation
colors = {"red", "green", "blue"}

# From list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3])
print(numbers)  # {1, 2, 3}

# Empty set (careful!)
wrong = {}  # This is a dictionary!
correct = set()  # This is an empty set
```

### Example 2: Automatic Duplicate Removal
```python
# Duplicates automatically removed
fruits = {"apple", "banana", "apple", "cherry"}
print(fruits)  # {'apple', 'banana', 'cherry'}

# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)
print(unique)  # {1, 2, 3, 4}
```

### Example 3: Adding and Removing
```python
fruits = {"apple", "banana"}

# Add single item
fruits.add("cherry")  # {'apple', 'banana', 'cherry'}

# Try to add duplicate (no effect)
fruits.add("apple")  # Still {'apple', 'banana', 'cherry'}

# Remove item
fruits.remove("banana")  # {'apple', 'cherry'}

# Safe remove (doesn't error if missing)
fruits.discard("orange")  # No error even though orange not in set
```

### Example 4: Set Operations
```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (all items from both)
print(set_a | set_b)  # {1, 2, 3, 4, 5, 6}

# Intersection (items in both)
print(set_a & set_b)  # {3, 4}

# Difference (in A but not B)
print(set_a - set_b)  # {1, 2}

# Symmetric difference (in either, not both)
print(set_a ^ set_b)  # {1, 2, 5, 6}
```

### Example 5: Membership Testing
```python
# Fast membership check
valid_users = {"alice", "bob", "charlie"}

user = "alice"
if user in valid_users:
    print(f"Welcome, {user}!")  # Fast lookup!
```

### Example 6: Iterating Sets
```python
fruits = {"apple", "banana", "cherry"}

# Order may vary each run!
for fruit in fruits:
    print(fruit)
```

### Example 7: Set Comprehension
```python
# Create set of squares
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Filter vowels from string
text = "hello world"
vowels = {char for char in text if char in "aeiou"}
print(vowels)  # {'o', 'e'}
```

## Practice Exercises

### Beginner
1. **Create Set**: Make a set of your 5 favorite foods
2. **Remove Duplicates**: Convert list `[1,1,2,2,3,3]` to unique values
3. **Add Items**: Start with empty set, add 5 numbers
4. **Membership Test**: Check if "python" is in set of languages
5. **Count Unique**: Count unique letters in "mississippi"

### Intermediate
6. **Common Items**: Find common elements in two sets of numbers
7. **Unique Words**: Find all unique words in a sentence
8. **Set Difference**: Find items in set A but not in set B
9. **Symmetric Diff**: Find items in either set but not both
10. **Update Set**: Use update() to add multiple items at once

### Advanced
11. **Tag System**: Build a tagging system with set operations
12. **Duplicate Finder**: Find duplicate items across multiple lists
13. **Set Math**: Implement set operations manually without operators
14. **Frozen Sets**: Create immutable sets and understand use cases
15. **Optimize Search**: Replace list membership with set for performance

## Common Mistakes to Avoid

### ❌ Mistake 1: Empty Set Syntax
```python
# WRONG: Creates dictionary, not set!
empty = {}
print(type(empty))  # <class 'dict'>

# CORRECT: Use set() function
empty = set()
print(type(empty))  # <class 'set'>
```

### ❌ Mistake 2: Expecting Order
```python
# WRONG: Assuming sets maintain order
numbers = {5, 2, 8, 1, 9}
print(numbers)  # Order not guaranteed!

# CORRECT: Use list if order matters
numbers = [5, 2, 8, 1, 9]
```

### ❌ Mistake 3: Trying to Index
```python
fruits = {"apple", "banana", "cherry"}
# WRONG: Sets don't support indexing
# print(fruits[0])  # TypeError!

# CORRECT: Convert to list if needed
fruits_list = list(fruits)
print(fruits_list[0])
```

### ❌ Mistake 4: Mutable Items in Set
```python
# WRONG: Lists are mutable, can't be in sets
# my_set = {[1, 2], [3, 4]}  # TypeError!

# CORRECT: Use tuples (immutable)
my_set = {(1, 2), (3, 4)}  # Works!
```

## Real-World Applications

### 1. Remove Duplicate Emails
```python
# Email list with duplicates
emails = ["user@example.com", "admin@site.com", "user@example.com"]

# Get unique emails
unique_emails = set(emails)
print(f"Unique subscribers: {len(unique_emails)}")
```

### 2. Tag System
```python
post1_tags = {"python", "programming", "tutorial"}
post2_tags = {"python", "web", "flask"}

# Find common tags
common = post1_tags & post2_tags
print(f"Common tags: {common}")  # {'python'}
```

### 3. Permissions System
```python
user_permissions = {"read", "write"}
required_permissions = {"read", "write", "delete"}

# Check if user has all required permissions
if required_permissions.issubset(user_permissions):
    print("Access granted")
else:
    missing = required_permissions - user_permissions
    print(f"Missing permissions: {missing}")
```

### 4. Data Validation
```python
valid_statuses = {"pending", "approved", "rejected"}

def validate_status(status):
    return status.lower() in valid_statuses

print(validate_status("APPROVED"))  # True (fast lookup!)
```

## Challenge Projects

### Project 1: Student Enrollment System
Create a system that:
- Tracks students enrolled in courses using sets
- Finds students in multiple courses
- Identifies courses unique to each semester
- Calculates total unique students

### Project 2: Social Network Friend Finder
Build an app that:
- Stores friends as sets for each user
- Finds mutual friends (intersection)
- Suggests friends (friends of friends)
- Identifies exclusive friends

### Project 3: Inventory Deduplicator
Develop a program that:
- Removes duplicate SKUs from inventory
- Finds items in warehouse A but not B
- Merges inventory from multiple sources
- Reports unique vs duplicate items

### Project 4: Word Analyzer
Create a tool that:
- Finds unique words in documents
- Compares vocabulary between texts
- Identifies unique words per author
- Builds word frequency analysis

### Project 5: Access Control System
Build a permissions manager:
- Define role-based permissions as sets
- Check user access levels
- Combine permissions from multiple roles
- Audit permission differences

## Navigation
- [← Previous: Chapter 21 - Lists](../21-lists/)
- [→ Next: Chapter 22 - Shopping Cart Program](../22-shopping-cart/)
- [↑ Back to Main](../../README.md)

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Use loops to repeat actions
3. Follow along with the video for hands-on practice

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
