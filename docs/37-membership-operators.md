# ✅ Membership Operators

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/37-membership-operators/37-membership-operators.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/37-membership-operators/37-membership-operators.ipynb)


## 📺 Video Tutorial

**Learn Python MEMBERSHIP OPERATORS in 8 minutes! 🔎** (8:23)

## What You'll Learn

In this chapter, you'll master Python's membership operators - `in` and `not in`. These operators test whether a value exists in a sequence like strings, lists, tuples, sets, or dictionaries. You'll learn how to validate input, search for elements, check dictionary keys, and write cleaner conditional logic.

## Learning Objectives

- Use the `in` operator to test for membership in sequences
- Use the `not in` operator to test for absence of membership
- Apply membership operators to strings, lists, tuples, sets, and dictionaries
- Validate user input efficiently with membership checks
- Write cleaner conditionals using membership operators
- Understand performance characteristics of membership tests across different data types

## Concept Explanation

### What are Membership Operators?

Membership operators test whether a value is found in a sequence (string, list, tuple, set, or dictionary).

**Two Operators:**
1. **`in`** - Returns `True` if value is found in sequence
2. **`not in`** - Returns `True` if value is NOT found in sequence

```python
# in operator
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # True
print("orange" in fruits)  # False

# not in operator
print("orange" not in fruits)  # True
print("apple" not in fruits)   # False
```

### Membership Operators with Different Types

#### 1. **Lists**
```python
numbers = [1, 2, 3, 4, 5]

print(3 in numbers)      # True
print(10 in numbers)     # False
print(10 not in numbers) # True
```

#### 2. **Tuples**
```python
colors = ("red", "green", "blue")

print("red" in colors)    # True
print("yellow" in colors) # False
```

#### 3. **Strings**
```python
message = "Hello World"

print("H" in message)     # True (case-sensitive!)
print("h" in message)     # False
print("World" in message) # True (can check substrings)
print("world" in message) # False (case-sensitive)
```

#### 4. **Sets**
```python
unique_nums = {1, 2, 3, 4, 5}

print(3 in unique_nums)  # True
print(10 in unique_nums) # False
```

#### 5. **Dictionaries (Checks Keys by Default)**
```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

print("name" in person)    # True (checks keys)
print("Alice" in person)   # False (doesn't check values by default)

# Check values explicitly
print("Alice" in person.values())  # True

# Check key-value pairs
print(("name", "Alice") in person.items())  # True
```

### Why Use Membership Operators?

#### 1. **Input Validation**
```python
valid_options = ("rock", "paper", "scissors")
choice = input("Choose: ").lower()

if choice in valid_options:
    print("Valid choice!")
else:
    print("Invalid! Try again.")
```

#### 2. **Cleaner Code**
```python
# Without membership operator (verbose)
if x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
    print("Found!")

# With membership operator (clean)
if x in [1, 2, 3, 4, 5]:
    print("Found!")
```

#### 3. **Search Operations**
```python
# Check if email is blacklisted
blacklist = ["spam@example.com", "fake@example.com"]

if user_email in blacklist:
    print("Access denied!")
```

#### 4. **Character/Substring Checking**
```python
password = "MyPassword123"

if "@" not in password:
    print("Password must contain @")
```

### Performance Considerations

Different data structures have different lookup speeds:

**Fast (O(1) - Constant Time):**
- Sets: `{1, 2, 3}`
- Dictionaries: `{"key": "value"}`

```python
# Very fast for large datasets
large_set = set(range(1000000))
print(999999 in large_set)  # Instant!
```

**Slow (O(n) - Linear Time):**
- Lists: `[1, 2, 3]`
- Tuples: `(1, 2, 3)`
- Strings: `"abc"`

```python
# Slower for large datasets
large_list = list(range(1000000))
print(999999 in large_list)  # Must scan through all elements
```

**Best Practice:** Use sets for membership testing with large datasets!

## Examples

### Example 1: Word Guessing Game
```python
word = "PYTHON"
letter = input("Guess a letter: ").upper()

if letter in word:
    print(f"✓ Yes! '{letter}' is in the word")
else:
    print(f"✗ No, '{letter}' is not in the word")

# Example runs:
# Guess a letter: P
# ✓ Yes! 'P' is in the word

# Guess a letter: Z  
# ✗ No, 'Z' is not in the word
```

### Example 2: Student Checker
```python
students = ["Alice", "Bob", "Charlie", "David"]
name = input("Enter student name: ")

if name in students:
    print(f"{name} is enrolled")
else:
    print(f"{name} is not enrolled")

if name not in students:
    print("Would you like to enroll?")
```

### Example 3: Email Validator
```python
email = input("Enter email: ")

# Check required characters
if "@" in email and "." in email:
    # Check domain
    if "gmail.com" in email or "yahoo.com" in email or "outlook.com" in email:
        print("Email looks valid!")
    else:
        print("Unknown email provider")
else:
    print("Invalid email format")

# Example:
# Enter email: user@gmail.com
# Email looks valid!
```

### Example 4: Menu Selection
```python
menu = {
    "1": "View Profile",
    "2": "Edit Settings",
    "3": "Logout",
    "4": "Help"
}

choice = input("Select option (1-4): ")

if choice in menu:
    print(f"You selected: {menu[choice]}")
else:
    print("Invalid option! Please choose 1-4")
```

### Example 5: Grade Validator
```python
valid_grades = ['A', 'B', 'C', 'D', 'F']
grade = input("Enter grade: ").upper()

if grade in valid_grades:
    print(f"Grade {grade} recorded")
    
    # Additional checks
    if grade in ['A', 'B']:
        print("Excellent work!")
    elif grade in ['C', 'D']:
        print("Need improvement")
    else:
        print("Failed")
else:
    print("Invalid grade! Use A, B, C, D, or F")
```

### Example 6: Vowel Counter
```python
text = input("Enter text: ")
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"Vowels found: {vowel_count}")

# Example:
# Enter text: Hello World
# Vowels found: 3
```

### Example 7: Access Control System
```python
# User database
admins = {"alice", "bob"}
moderators = {"charlie", "david"}
regular_users = {"eve", "frank", "grace"}

username = input("Enter username: ").lower()

if username in admins:
    print("Access Level: Administrator")
    print("Full access granted!")
elif username in moderators:
    print("Access Level: Moderator")
    print("Limited admin access")
elif username in regular_users:
    print("Access Level: User")
    print("Standard access")
else:
    print("Unknown user - Access denied")
```

## Practice Exercises

### Beginner Level

1. **Fruit Checker**: Create a program that checks if a fruit is in your shopping list.

2. **Number Validator**: Write a program that validates if input is in range 1-10 using membership operators.

3. **Password Character Check**: Check if a password contains required characters (@, #, $, etc.).

4. **Color Validator**: Create a list of valid colors and check user input against it.

5. **Banned Words**: Check if a message contains banned words from a list.

### Intermediate Level

6. **Username Availability**: Check if a username is already taken from a list of existing users.

7. **Multiple Criteria**: Create a validator that checks if input meets multiple membership criteria.

8. **Dictionary Permission System**: Use dictionary keys to check user permissions.

9. **Substring Search**: Find all occurrences where a substring appears in a text.

10. **Whitelist/Blacklist**: Implement both whitelist (allowed) and blacklist (blocked) checks.

### Advanced Level

11. **Smart Search**: Build a case-insensitive search that handles partial matches using membership operators.

12. **Set Operations**: Use membership with set operations (union, intersection) for complex validation.

13. **Nested Membership**: Check membership in nested data structures (lists of dicts, etc.).

14. **Performance Comparison**: Compare membership testing performance between lists and sets with large datasets.

15. **Custom Membership**: Create a class that implements `__contains__` to support custom membership logic.

## Common Mistakes to Avoid

### Mistake 1: Case Sensitivity in Strings

**Wrong:**
```python
word = "Python"
if "python" in word:  # False - case mismatch!
    print("Found")
```

**Correct:**
```python
word = "Python"
if "python" in word.lower():  # True - convert to lowercase
    print("Found")
```

**Why:** String membership is case-sensitive. Always normalize case for comparison.

### Mistake 2: Checking Values in Dictionary (Wrong Way)

**Wrong:**
```python
person = {"name": "Alice", "age": 25}
if "Alice" in person:  # False - checks keys, not values!
    print("Found")
```

**Correct:**
```python
person = {"name": "Alice", "age": 25}
if "Alice" in person.values():  # True - checks values
    print("Found")
```

**Why:** `in` checks dictionary keys by default. Use `.values()` to check values.

### Mistake 3: Inefficient Membership Testing with Lists

**Wrong:**
```python
# Slow for large lists - O(n) lookup
large_list = list(range(1000000))
for i in range(1000):
    if i in large_list:  # Scans entire list each time!
        print("Found")
```

**Correct:**
```python
# Fast with sets - O(1) lookup
large_set = set(range(1000000))
for i in range(1000):
    if i in large_set:  # Instant lookup!
        print("Found")
```

**Why:** Lists have O(n) lookup time. Sets have O(1). Use sets for large membership tests.

### Mistake 4: Using 'in' with Numbers Incorrectly

**Wrong:**
```python
# Checking if digit is in a number (wrong approach)
number = 12345
if 3 in number:  # TypeError: argument of type 'int' is not iterable
    print("Found")
```

**Correct:**
```python
# Convert to string first
number = 12345
if "3" in str(number):  # True
    print("Found")

# Or use math operations
if 3 in [int(d) for d in str(number)]:
    print("Found")
```

**Why:** `in` works with iterables. Convert numbers to strings to check digits.

## Real-World Applications

### 1. **Form Validation**
Web forms validate input against allowed values:
```python
ALLOWED_COUNTRIES = ["USA", "Canada", "UK", "Australia"]
if country in ALLOWED_COUNTRIES:
    process_form()
```

### 2. **Access Control**
Security systems check permissions:
```python
if user.role in ["admin", "superuser"]:
    grant_access()
```

### 3. **Content Filtering**
Filter prohibited content:
```python
BANNED_WORDS = ["spam", "abuse", "illegal"]
if any(word in message.lower() for word in BANNED_WORDS):
    reject_message()
```

### 4. **Search Features**
Search functionality checks for matches:
```python
if search_term in product_name.lower():
    display_product()
```

## Challenge Projects

### 1. **Advanced Password Validator**
Build a comprehensive password validation system.

**Requirements:**
- Check for required character types using membership
- Banned words check
- Common password blacklist
- Minimum/maximum length
- Sequential character detection
- Provide specific feedback

### 2. **Spelling Checker**
Create a simple spelling checker.

**Requirements:**
- Load dictionary of valid words
- Check each word in text
- Use set for fast membership testing
- Suggest corrections for misspelled words
- Handle punctuation
- Case-insensitive checking

### 3. **IP Address Blocker**
Build an IP blocking/allowing system.

**Requirements:**
- Whitelist of allowed IPs
- Blacklist of blocked IPs
- IP range support
- Logging of access attempts
- Admin override capabilities
- Performance optimized with sets

### 4. **Smart Content Filter**
Create a content moderation system.

**Requirements:**
- Multiple blacklists (offensive, spam, etc.)
- Context-aware filtering
- Partial match detection
- Whitelist exceptions
- Severity levels
- Detailed reporting

### 5. **Game Inventory System**
Build an inventory checker for a game.

**Requirements:**
- Check item ownership
- Valid item database
- Item categories with membership
- Quest item requirements
- Crafting recipe validation
- Trade restrictions

---

## Navigation

- **Previous:** [35. Iterables](35-iterables.md)
- **Next:** [37. List Comprehensions](37-list-comprehensions.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Use if-elif-else for conditional logic
3. Test your code to ensure it works correctly

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*