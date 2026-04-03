[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/3-type-casting/3-type-casting.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/3-type-casting/3-type-casting.ipynb)

# Chapter 3: Type Casting

## 📺 Video Tutorial

**Learn type casting in 7 minutes! 💱** (7:39)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/Qtq83lAoogM)

## 📚 What You'll Learn
Type casting is the process of converting data from one type to another - essential for working with user input and performing calculations!

## 🎯 Learning Objectives
- Understand what type casting is and why it's needed
- Learn to convert between int, float, str, and bool
- Use the `type()` function to check data types
- Handle common type conversion scenarios

## 📖 Concept Explanation

### What is Type Casting?
Type casting (or type conversion) is the process of converting a variable from one data type to another.

### Why is Type Casting Needed?
- User input is always a string, even if you enter numbers
- Mathematical operations require numeric types
- String concatenation requires all values to be strings
- Different operations work with different types

### Common Type Casting Functions

#### `int()` - Convert to Integer
```python
float_num = 3.14
int_num = int(float_num)  # Result: 3 (decimal is removed)

text = "25"
number = int(text)  # Result: 25 (string becomes integer)
```

#### `float()` - Convert to Float
```python
int_num = 25
float_num = float(int_num)  # Result: 25.0

text = "3.14"
number = float(text)  # Result: 3.14
```

#### `str()` - Convert to String
```python
age = 25
age_text = str(age)  # Result: "25"

price = 19.99
price_text = str(price)  # Result: "19.99"
```

#### `bool()` - Convert to Boolean
```python
number = 1
is_true = bool(number)  # Result: True (any non-zero number is True)

empty_string = ""
is_false = bool(empty_string)  # Result: False (empty strings are False)
```

### The `type()` Function
The `type()` function tells you what data type a variable is:
```python
name = "Alice"
age = 25
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
```

## 💡 Examples

### Example 1: Converting User Input
```python
# input() always returns a string
age_str = input("Enter your age: ")  # If user types "25", age_str = "25"
age_int = int(age_str)  # Convert to integer: 25
print(age_int + 5)  # Now we can do math: 30
```

### Example 2: String Concatenation
```python
age = 25
# This doesn't work: print("I am " + age)  # Error!
print("I am " + str(age))  # Works! Convert age to string first
# Or use f-strings (no conversion needed):
print(f"I am {age}")  # Also works!
```

### Example 3: Float to Int
```python
gpa = 3.7
gpa_int = int(gpa)  # Result: 3 (truncates, doesn't round)
print(gpa_int)
```

## ✍️ Practice Exercises
1. Ask the user for two numbers and add them (remember to convert from string to int)
2. Create a float variable and convert it to int, then to string
3. Ask user for their height in meters (float) and convert it to centimeters (int)
4. Create a program that asks for a price (string) and adds 10% tax, displaying the result

## 🔍 Common Mistakes

### Forgetting to Convert User Input
```python
# Wrong:
age = input("Enter age: ")
print(age + 5)  # Error! Can't add string and number

# Correct:
age = int(input("Enter age: "))
print(age + 5)  # Works!
```

### Trying to Convert Invalid Strings
```python
# This will cause an error:
text = "hello"
number = int(text)  # Error! Can't convert "hello" to int

# Only numeric strings can be converted:
text = "123"
number = int(text)  # Works! Result: 123
```

### Losing Precision
```python
pi = 3.14159
pi_int = int(pi)  # Result: 3 (decimal part is lost forever!)
```

## 📝 Key Points
- `input()` **always** returns a string, even if the user types a number
- `int()` truncates decimals (doesn't round): `int(3.9)` → `3`
- You can't convert non-numeric strings to numbers: `int("hello")` → Error
- Type casting is **permanent** for that variable unless you reassign it

## 🚀 Try It Yourself
Modify `main.py` to create a program that:
1. Asks for a person's name (string)
2. Asks for their age (convert to int)
3. Asks for their height in meters (convert to float)
4. Displays all information with proper types

## 🎓 Key Takeaways from Video

1. Strings are text data enclosed in quotes
2. Follow along with the video for hands-on practice
3. Experiment with the code examples to deepen understanding

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter
Continue to [Chapter 4: User Input](../4-user-input/) to learn how to interact with users!

