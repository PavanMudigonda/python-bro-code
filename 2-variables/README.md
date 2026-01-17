# Chapter 2: Variables and Data Types


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/7IoQ5BGkTJo)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/7IoQ5BGkTJo)

## � Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-Chapter_2-red?style=for-the-badge&logo=youtube)](https://youtu.be/dvJ6J2H5KjQ)

## �📚 What You'll Learn
Variables are fundamental in programming - they let you store and manipulate data in your programs!

## 🎯 Learning Objectives
- Understand what variables are and how to create them
- Learn about Python's basic data types (str, int, float, bool)
- Practice using f-strings to format output
- Combine variables with conditional statements

## 📖 Concept Explanation

### What are Variables?
Variables are named containers that store data values. Think of them as labeled boxes where you can put different types of information.

```python
name = "Alice"  # name is the variable, "Alice" is the value
age = 25        # age stores the number 25
```

### Python's Basic Data Types

#### 1. **String (str)** - Text Data
```python
name: str = "John"
message: str = "Hello, World!"
```
- Strings hold text
- Must be enclosed in quotes (single or double)

#### 2. **Integer (int)** - Whole Numbers
```python
age: int = 20
quantity: int = 100
```
- Integers are whole numbers (no decimals)
- Can be positive or negative

#### 3. **Float (float)** - Decimal Numbers
```python
price: float = 19.99
pi: float = 3.14159
```
- Floats are numbers with decimal points
- Used for precise calculations

#### 4. **Boolean (bool)** - True or False
```python
is_student: bool = True
is_available: bool = False
```
- Booleans can only be `True` or `False`
- Used for logic and conditions

### Type Annotations
The `: type` syntax is called a type hint:
```python
name: str = "Alice"  # Explicitly states this is a string
```
Type hints are optional but make code more readable!

### F-Strings (Formatted Strings)
F-strings let you embed variables directly in strings:
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
# Output: My name is Alice and I am 25 years old
```

## 💡 Examples

### Creating Variables
```python
# String variable
favorite_food: str = "Pizza"

# Integer variable
student_count: int = 30

# Float variable
temperature: float = 72.5

# Boolean variable
is_raining: bool = False
```

### Using Variables
```python
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"
print(full_name)  # Output: John Doe
```

## ✍️ Practice Exercises
1. Create variables for your name, age, height (in meters), and whether you like programming
2. Print all these variables using f-strings
3. Create a variable called `temperature` and use it in an if-else statement to check if it's hot (> 30) or cold
4. Create variables for a product (name, price, quantity) and calculate the total cost

## 🔍 Common Mistakes
- **Forgetting quotes around strings**: `name = Alice` ❌ should be `name = "Alice"` ✅
- **Using spaces in variable names**: `first name = "John"` ❌ should be `first_name = "John"` ✅
- **Starting variable names with numbers**: `1st_name` ❌ should be `first_name` ✅

## 📝 Variable Naming Rules
- Can contain letters, numbers, and underscores
- Must start with a letter or underscore
- Case-sensitive (`age` and `Age` are different)
- Use snake_case for multi-word variables: `first_name`, `student_count`

## 🚀 Try It Yourself
Modify `main.py` to create variables about yourself and print them in creative ways!

## 🔗 Next Chapter
Continue to [Chapter 3: Type Casting](../3-type-casting/) to learn how to convert between data types!
