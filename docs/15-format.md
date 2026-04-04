# Chapter 15: Format

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/15-format/15-format.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/15-format/15-format.ipynb)


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/15-format/15-format.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/15-format/15-format.ipynb)

# Chapter 15: Format Specifiers

## 📺 Video Tutorial

**Learn Python format specifiers in 5 minutes! 💬** (5:32)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/FrvBwdAU2dQ)

## 📚 What You'll Learn
Master advanced string formatting to display numbers, prices, and data professionally!

## 🎯 Learning Objectives
- Use format specifiers with f-strings
- Control decimal places and rounding
- Align text and numbers
- Format currencies and percentages

## 📖 Concept Explanation

Format specifiers control how values are displayed in f-strings using the syntax `{value:specifier}`.

### Common Format Specifiers

| Specifier | Description | Example | Output |
|-----------|-------------|---------|--------|
| `:.2f` | 2 decimal places | `{3.14159:.2f}` | `3.14` |
| `:10` | Width of 10 | `{42:10}` | `        42` |
| `:>10` | Right align | `{42:>10}` | `        42` |
| `:<10` | Left align | `{42:<10}` | `42        ` |
| `:^10` | Center align | `{42:^10}` | `    42    ` |
| `:05` | Zero padding | `{42:05}` | `00042` |
| `:,` | Thousands separator | `{1000:,}` | `1,000` |
| `:+` | Show sign | `{42:+}` | `+42` |
| `:%` | Percentage | `{0.75:%}` | `75.000000%` |
| `:.1%` | Percentage (1 decimal) | `{0.756:.1%}` | `75.6%` |

## 💡 Examples

### Decimal Places
```python
pi = 3.14159265
print(f"{pi:.2f}")    # 3.14
print(f"{pi:.4f}")    # 3.1416
print(f"{pi:.0f}")    # 3
```

### Alignment and Width
```python
name = "Python"
price = 19.99

print(f"{name:>10}")  # "    Python" (right aligned)
print(f"{name:<10}")  # "Python    " (left aligned)
print(f"{name:^10}")  # "  Python  " (centered)
print(f"{price:>10.2f}")  # "     19.99"
```

### Thousands Separator
```python
population = 7800000000
print(f"{population:,}")  # 7,800,000,000

price = 1234.56
print(f"${price:,.2f}")   # $1,234.56
```

### Zero Padding
```python
number = 42
print(f"{number:05}")  # 00042
print(f"{number:03}")  # 042

# Useful for IDs
user_id = 7
print(f"USER-{user_id:04}")  # USER-0007
```

## ✍️ Practice Exercises

1. Format price to 2 decimals with dollar sign
2. Create aligned table of names and scores
3. Format phone number with zero padding
4. Display large numbers with comma separators
5. Show percentages with 1 decimal place
6. Create formatted invoice

## 🎮 Real-World Examples

### Price List
```python
items = [
    ("Apple", 0.99),
    ("Banana", 0.59),
    ("Orange", 1.29)
]

print("ITEM       | PRICE")
print("-" * 20)
for item, price in items:
    print(f"{item:<10} | ${price:>5.2f}")

# Output:
# ITEM       | PRICE
# --------------------
# Apple      | $ 0.99
# Banana     | $ 0.59
# Orange     | $ 1.29
```

### Financial Report
```python
revenue = 1234567.89
expenses = 987654.32
profit = revenue - expenses

print("FINANCIAL REPORT")
print("=" * 30)
print(f"Revenue:  ${revenue:>12,.2f}")
print(f"Expenses: ${expenses:>12,.2f}")
print(f"Profit:   ${profit:>12,.2f}")

# Output:
# FINANCIAL REPORT
# ==============================
# Revenue:  $ 1,234,567.89
# Expenses: $   987,654.32
# Profit:   $   246,913.57
```

### Progress Display
```python
completed = 75
total = 100
percentage = completed / total

print(f"Progress: {percentage:.1%}")  # Progress: 75.0%
print(f"Completed: {completed}/{total}")
print(f"[{'=' * completed}{' ' * (total-completed)}] {percentage:.0%}")
# [===========================================================================                         ] 75%
```

### Student Grades
```python
students = [
    ("Alice", 95.5),
    ("Bob", 87.3),
    ("Charlie", 92.8)
]

print(f"{'Name':<10} | {'Grade':>5} | {'Letter'}")
print("-" * 30)
for name, grade in students:
    letter = "A" if grade >= 90 else "B" if grade >= 80 else "C"
    print(f"{name:<10} | {grade:>5.1f} | {letter}")

# Output:
# Name       | Grade | Letter
# ------------------------------
# Alice      |  95.5 | A
# Bob        |  87.3 | B
# Charlie    |  92.8 | A
```

## 📝 Advanced Formatting

### Scientific Notation
```python
big_number = 1000000
print(f"{big_number:e}")   # 1.000000e+06
print(f"{big_number:.2e}") # 1.00e+06
```

### Binary, Octal, Hex
```python
number = 255
print(f"{number:b}")   # 11111111 (binary)
print(f"{number:o}")   # 377 (octal)
print(f"{number:x}")   # ff (hexadecimal lowercase)
print(f"{number:X}")   # FF (hexadecimal uppercase)
```

### Custom Separators
```python
number = 1234567
print(f"{number:_}")     # 1_234_567
print(f"{number:,}")     # 1,234,567
```

## 🚀 Challenge Projects

1. **Receipt Generator**: Create formatted receipts with items and prices
2. **Grade Report Card**: Display student names, scores, and letter grades aligned
3. **Financial Dashboard**: Show revenue, expenses, profit with proper formatting
4. **Time Display**: Format seconds into HH:MM:SS with zero padding
5. **Product Catalog**: Create aligned product catalog with prices

## 🎓 Key Takeaways from Video

1. Strings are text data enclosed in quotes
2. Follow along with the video for hands-on practice
3. Experiment with the code examples to deepen understanding

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter
Continue to [Chapter 16: While Loops](16-while.md) to learn about repetition and iteration!

