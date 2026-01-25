# Chapter 13: String Methods


## 📺 Video Tutorial

**String methods in Python are easy! 〰️** (12:14)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/tb6EYiHtcXU)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/7pXf1DUuaIo)

## 📚 What You'll Learn
Master Python's powerful string manipulation methods to transform and analyze text!

## 🎯 Learning Objectives
- Use common string methods (.upper(), .lower(), .title(), etc.)
- Find and replace substrings
- Validate string content
- Combine multiple string operations

## 📖 Concept Explanation

Strings in Python come with many built-in methods for manipulation. Methods are functions that belong to an object (in this case, strings).

### Common String Methods

| Method | Description | Example |
|--------|-------------|---------|
| `.upper()` | Convert to uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | Convert to lowercase | `"HELLO".lower()` → `"hello"` |
| `.title()` | Capitalize first letter of each word | `"hello world".title()` → `"Hello World"` |
| `.capitalize()` | Capitalize first letter only | `"hello world".capitalize()` → `"Hello world"` |
| `.find()` | Find substring index | `"hello".find("e")` → `1` |
| `.replace()` | Replace substring | `"hello".replace("l", "L")` → `"heLLo"` |
| `.isdigit()` | Check if all digits | `"123".isdigit()` → `True` |
| `.isalpha()` | Check if all letters | `"abc".isalpha()` → `True"` |
| `.strip()` | Remove whitespace | `"  hi  ".strip()` → `"hi"` |
| `.split()` | Split into list | `"a,b,c".split(",")` → `['a','b','c']` |

## 💡 Examples

### Example 1: Case Conversion
```python
name = "john DOE"
print(name.upper())      # JOHN DOE
print(name.lower())      # john doe
print(name.title())      # John Doe
print(name.capitalize()) # John doe
```

### Example 2: Finding Substrings
```python
text = "Python Programming"
print(text.find("Pro"))      # 7 (index where "Pro" starts)
print(text.find("Java"))     # -1 (not found)
print("Pro" in text)         # True (membership check)
```

### Example 3: Replacing Text
```python
phone = "123-456-7890"
clean = phone.replace("-", "")
print(clean)  # 1234567890

message = "Hello World"
new_msg = message.replace("World", "Python")
print(new_msg)  # Hello Python
```

### Example 4: Validation
```python
user_input = "12345"
if user_input.isdigit():
    number = int(user_input)
    print(f"Valid number: {number}")
else:
    print("Please enter only digits")
```

## ✍️ Practice Exercises

1. Create a program that converts usernames to lowercase
2. Clean phone numbers by removing spaces and dashes
3. Validate email format (contains @ and .)
4. Count how many times a letter appears in a word
5. Create a function that capitalizes names properly
6. Build a simple text processor that removes extra spaces

## 📝 More Useful Methods

### `.count(substring)`
```python
text = "hello world"
print(text.count("l"))  # 3
```

### `.startswith()` and `.endswith()`
```python
filename = "document.pdf"
print(filename.endswith(".pdf"))  # True
print(filename.startswith("doc")) # True
```

### `.strip()`, `.lstrip()`, `.rstrip()`
```python
text = "   hello   "
print(text.strip())   # "hello" (both sides)
print(text.lstrip())  # "hello   " (left side)
print(text.rstrip())  # "   hello" (right side)
```

### `.split()` and `.join()`
```python
# Split string into list
sentence = "Python is awesome"
words = sentence.split()  # ['Python', 'is', 'awesome']

# Join list into string
joined = " ".join(words)  # "Python is awesome"
csv = ",".join(words)     # "Python,is,awesome"
```

## 🎮 Real-World Examples

### Email Validator
```python
email = input("Enter email: ")
if "@" in email and "." in email:
    domain = email.split("@")[1]
    print(f"Domain: {domain}")
else:
    print("Invalid email format")
```

### Username Formatter
```python
username = input("Username: ")
username = username.strip().lower().replace(" ", "_")
print(f"Formatted username: {username}")
```

### Password Strength Checker
```python
password = input("Enter password: ")
has_digit = any(c.isdigit() for c in password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)

if len(password) >= 8 and has_digit and has_upper and has_lower:
    print("Strong password!")
else:
    print("Weak password")
```

## 🚀 Challenge Projects

1. **Text Analyzer**: Count words, letters, vowels, consonants
2. **Name Formatter**: Handle various name formats (JOHN DOE, john doe, etc.)
3. **Censorship Filter**: Replace bad words with asterisks
4. **Acronym Generator**: Create acronyms from phrases (e.g., "For Your Information" → "FYI")
5. **Text Reverser**: Reverse words and sentences in different ways

## 🔗 Next Chapter
Continue to [Chapter 14: Indexing](../14-index/) to learn how to access individual characters!
