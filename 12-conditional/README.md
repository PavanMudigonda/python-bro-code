# Chapter 12: Conditional Expressions (Ternary Operator)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/tb6EYiHtcXU)


## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/tb6EYiHtcXU)

## 📚 What You'll Learn
Write compact, elegant one-line conditional statements using Python's ternary operator!

## 🎯 Learning Objectives
- Understand the ternary operator syntax
- Convert if-else statements to one-liners
- Know when to use ternary vs traditional if-else
- Write cleaner, more pythonic code

## 📖 Concept Explanation

### What is a Ternary Operator?
A ternary operator (conditional expression) is a compact way to write simple if-else statements in one line.

### Syntax
```python
value_if_true if condition else value_if_false
```

### Traditional vs Ternary
```python
# Traditional if-else
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary operator (one line)
status = "Adult" if age >= 18 else "Minor"
```

## 💡 Examples

### Example 1: Even or Odd
```python
number = 7
result = "EVEN" if number % 2 == 0 else "ODD"
print(result)  # Output: ODD
```

### Example 2: Max of Two Numbers
```python
a, b = 15, 23
maximum = a if a > b else b
print(f"Max: {maximum}")  # Output: Max: 23
```

### Example 3: Pass/Fail
```python
score = 75
result = "PASS" if score >= 60 else "FAIL"
print(result)  # Output: PASS
```

### Example 4: Access Level
```python
user_role = "admin"
access = "Full Access" if user_role == "admin" else "Limited Access"
print(access)  # Output: Full Access
```

## ✍️ Practice Exercises

1. Check if number is positive, negative, or zero
2. Determine if year is leap year (divisible by 4)
3. Assign discount based on purchase amount (>100 = 10%, else 0%)
4. Check if password is strong (length >= 8)
5. Determine shipping: "Free" if total > 50 else "$5.99"
6. Set temperature message: "Cold" if temp < 60 else "Warm"

## 🔍 When to Use

### ✅ Good Use Cases
```python
# Simple value assignment
status = "Open" if is_open else "Closed"

# Function arguments
print("Hello" if is_greeting else "Goodbye")

# List/dict values
data = {"status": "active" if user.is_active else "inactive"}

# Return statements
return True if value > 0 else False
```

### ❌ Avoid Ternary For
```python
# Complex logic (use regular if-else)
result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
# Too hard to read!

# Multiple statements
message = (print("Hello"), user.save(), "Done") if condition else "Skip"
# Not allowed - ternary is for expressions, not statements
```

## 📝 Nested Ternary (Use Sparingly!)
```python
# Can be hard to read
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"

# Better: use regular if-elif-else for multiple conditions
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

## 🎮 Real-World Examples

### Example: Discount Calculator
```python
total = 120
discount = 0.10 if total >= 100 else 0.05 if total >= 50 else 0
savings = total * discount
final = total - savings
print(f"Discount: {discount*100}%, You save: ${savings:.2f}")
```

### Example: User Status Badge
```python
points = 1500
badge = "🥇 Gold" if points >= 1000 else "🥈 Silver" if points >= 500 else "🥉 Bronze"
print(f"Your badge: {badge}")
```

## 🚀 Try It Yourself
1. Create age category checker (Child/Teen/Adult/Senior)
2. Build temperature converter with unit check
3. Make a simple calculator using ternary for operation selection
4. Create BMI category determiner
5. Build a simple voting eligibility checker

## 🔗 Next Chapter
Continue to [Chapter 13: String Methods](../13-string/) to explore string manipulation techniques!
