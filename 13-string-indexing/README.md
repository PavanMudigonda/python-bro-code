[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/13-string-indexing/13-string-indexing.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/13-string-indexing/13-string-indexing.ipynb)

# Chapter 14: String Indexing and Slicing

## 📺 Video Tutorial

**String indexing in Python is easy ✂️** (6:17)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/7pXf1DUuaIo)

## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/6MAufQ6vGtI)

## 📚 What You'll Learn
Access and extract parts of strings using indexing and slicing - essential for text processing!

## 🎯 Learning Objectives
- Understand zero-based indexing
- Use positive and negative indices
- Slice strings with [start:end:step]
- Reverse strings and extract substrings

## 📖 Concept Explanation

### Indexing
Each character in a string has a position (index) starting from 0.

```
String: "PYTHON"
Index:   0 1 2 3 4 5
Negative:-6-5-4-3-2-1
```

### Slicing Syntax
```python
string[start:end:step]
```
- **start**: Beginning index (inclusive)
- **end**: Ending index (exclusive)  
- **step**: Interval between characters

## 💡 Examples

### Single Character Access
```python
word = "Python"
print(word[0])   # P (first character)
print(word[3])   # h (fourth character)
print(word[-1])  # n (last character)
print(word[-2])  # o (second to last)
```

### Slicing Ranges
```python
text = "Programming"
print(text[0:4])   # "Prog" (index 0 to 3)
print(text[3:7])   # "gram" (index 3 to 6)
print(text[:4])    # "Prog" (start to index 3)
print(text[4:])    # "ramming" (index 4 to end)
print(text[:])     # "Programming" (entire string)
```

### Step Parameter
```python
numbers = "0123456789"
print(numbers[::2])   # "02468" (every 2nd char)
print(numbers[1::2])  # "13579" (every 2nd, starting at 1)
print(numbers[::3])   # "0369" (every 3rd char)
```

### Reversing Strings
```python
word = "Python"
print(word[::-1])  # "nohtyP" (reversed)

# Practical use: palindrome checker
word = "racecar"
if word == word[::-1]:
    print("It's a palindrome!")
```

## ✍️ Practice Exercises

1. Extract first 3 characters from a string
2. Get the last 4 characters
3. Extract every other character
4. Reverse a user's name
5. Check if a string is a palindrome
6. Extract domain from email (after @)
7. Get file extension from filename

## 🎮 Real-World Examples

### Credit Card Formatter
```python
card = "1234567812345678"
formatted = f"{card[0:4]}-{card[4:8]}-{card[8:12]}-{card[12:16]}"
print(formatted)  # 1234-5678-1234-5678

# Hide middle digits
hidden = f"{card[0:4]}-****-****-{card[-4:]}"
print(hidden)  # 1234-****-****-5678
```

### Extract Information
```python
date = "2024-01-15"
year = date[0:4]    # "2024"
month = date[5:7]   # "01"
day = date[8:10]    # "15"
print(f"Year: {year}, Month: {month}, Day: {day}")
```

### URL Parser
```python
url = "https://www.example.com/page"
protocol = url[0:5]        # "https"
domain = url[12:23]        # "example.com"
path = url[23:]            # "/page"
```

## 📝 Common Patterns

### First/Last N Characters
```python
text = "Hello World"
first_5 = text[:5]    # "Hello"
last_5 = text[-5:]    # "World"
```

### Remove First/Last N Characters
```python
text = "Hello World"
without_first = text[1:]   # "ello World"
without_last = text[:-1]   # "Hello Worl"
```

### Every Nth Character
```python
text = "ABCDEFGHIJ"
every_2nd = text[::2]  # "ACEGI"
every_3rd = text[::3]  # "ADGJ"
```

## 🚀 Challenge Projects

1. **Social Security Number Formatter**: XXX-XX-XXXX
2. **Phone Number Parser**: Extract area code, prefix, line number
3. **Acronym Maker**: Take first letter of each word
4. **Text Truncator**: Limit text to N characters + "..."
5. **Caesar Cipher**: Shift characters by N positions

## 🔍 Slicing Tricks

### Copy a String
```python
original = "Python"
copy = original[:]  # Creates a copy
```

### Reverse Words
```python
sentence = "Hello World"
words = sentence.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)
print(result)  # "olleH dlroW"
```

### Extract Extension
```python
filename = "document.pdf"
extension = filename[filename.rfind('.')+1:]
print(extension)  # "pdf"
```

## 🎓 Key Takeaways from Video

1. Strings are text data enclosed in quotes
2. Follow along with the video for hands-on practice
3. Experiment with the code examples to deepen understanding

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter
Continue to [Chapter 15: Format Specifiers](../15-format/) to learn advanced string formatting!

