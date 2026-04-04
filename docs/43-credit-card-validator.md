# Chapter 43: Credit Card Validator

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/43-credit-card-validator/43-credit-card-validator.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/43-credit-card-validator/43-credit-card-validator.ipynb)


## 📺 Video Tutorial

**Credit card validator in Python 💳** (8:49)

## 📚 What You'll Learn
Implement the Luhn algorithm to validate credit card numbers - a real-world application of mathematical algorithms!

## 🎯 Learning Objectives
- Understand the Luhn algorithm (mod 10 algorithm)
- Convert strings to lists of integers
- Implement mathematical validation logic
- Reverse and manipulate lists
- Create practical validation tools

## 📖 Concept Explanation

### The Luhn Algorithm

The Luhn algorithm (also called mod 10 algorithm) is used to validate credit card numbers, IMEI numbers, and other identification numbers.

#### How It Works:
1. Remove the last digit (check digit)
2. Reverse the remaining digits
3. Double every second digit
4. If doubled digit > 9, subtract 9
5. Sum all digits
6. Add the check digit
7. If total % 10 == 0, the number is valid

### Example:
Credit card: `4532015112830366`

1. Check digit: 6
2. Remaining: 453201511283036
3. Reversed: 630382115102354
4. Double every 2nd: 6,6,0,6,8,4,1,2,5,2,0,4,3,10,5,8
5. Subtract 9 if > 9: 6,6,0,6,8,4,1,2,5,2,0,4,3,1,5,8
6. Sum: 61
7. Add check digit: 61 + 6 = 67
8. 67 % 10 = 7 ≠ 0, so invalid (this is just an example)

## 💡 Examples

### Basic Validator
```python
def validate_card(card_number):
    # Remove spaces and convert to string
    card_number = card_number.replace(" ", "")
    
    # Check if all characters are digits
    if not card_number.isdigit():
        return False
    
    # Remove last digit (check digit)
    check_digit = int(card_number[-1])
    digits = [int(d) for d in card_number[:-1]]
    
    # Reverse the digits
    digits.reverse()
    
    # Double every second digit
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    # Sum all digits
    total = sum(digits) + check_digit
    
    # Check if divisible by 10
    return total % 10 == 0

# Test
card = "4532015112830366"
if validate_card(card):
    print("✅ Valid card number")
else:
    print("❌ Invalid card number")
```

### Interactive Validator
```python
def validate_card(card_number):
    # Remove spaces and hyphens
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Validation checks
    if not card_number.isdigit():
        return False, "Card number must contain only digits"
    
    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Card number must be between 13 and 19 digits"
    
    # Luhn algorithm
    check_digit = int(card_number[-1])
    digits = [int(d) for d in card_number[:-1]]
    digits.reverse()
    
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    total = sum(digits) + check_digit
    
    if total % 10 == 0:
        return True, "Valid card number"
    else:
        return False, "Invalid card number"

# Main program
print("💳 Credit Card Validator")
print("-" * 30)
card = input("Enter card number: ")

is_valid, message = validate_card(card)

if is_valid:
    print(f"✅ {message}")
else:
    print(f"❌ {message}")
```

### With Card Type Detection
```python
def get_card_type(card_number):
    """Identify the card type based on the first digits"""
    if card_number.startswith('4'):
        return "Visa"
    elif card_number.startswith('5'):
        return "Mastercard"
    elif card_number.startswith('37'):
        return "American Express"
    elif card_number.startswith('6'):
        return "Discover"
    else:
        return "Unknown"

def validate_card(card_number):
    # Remove spaces and hyphens
    card_number = card_number.replace(" ", "").replace("-", "")
    
    if not card_number.isdigit():
        return False, "Invalid format", None
    
    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Invalid length", None
    
    # Luhn algorithm
    check_digit = int(card_number[-1])
    digits = [int(d) for d in card_number[:-1]]
    digits.reverse()
    
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    total = sum(digits) + check_digit
    card_type = get_card_type(card_number)
    
    if total % 10 == 0:
        return True, "Valid", card_type
    else:
        return False, "Invalid checksum", card_type

# Test
print("💳 Credit Card Validator")
print("-" * 40)
card = input("Enter card number: ")

is_valid, message, card_type = validate_card(card)

if is_valid:
    print(f"✅ Valid {card_type} card")
else:
    print(f"❌ {message}")
    if card_type != "Unknown":
        print(f"   Appears to be {card_type} format")
```

## ✍️ Practice Exercises

### Exercise 1: Basic Validator
Implement a simple Luhn algorithm validator that:
1. Takes a card number as input
2. Validates using Luhn algorithm
3. Prints valid or invalid

### Exercise 2: Format Checker
Add validation for:
- Only digits (or spaces/hyphens)
- Correct length (13-19 digits)
- No letters or special characters

### Exercise 3: Batch Validator
Create a program that validates multiple cards from a file:
```python
cards = [
    "4532015112830366",
    "6011514433546201",
    "371449635398431",
    "0000000000000000"
]

for card in cards:
    is_valid, message, card_type = validate_card(card)
    status = "✅" if is_valid else "❌"
    print(f"{status} {card}: {card_type} - {message}")
```

## 🔍 Common Mistakes

### 1. Not Reversing Before Doubling
```python
# ❌ Wrong - doubles wrong digits
for i in range(1, len(digits), 2):
    digits[i] *= 2

# ✅ Correct - reverse first
digits.reverse()
for i in range(1, len(digits), 2):
    digits[i] *= 2
```

### 2. Forgetting to Subtract 9
```python
# ❌ Wrong - doesn't handle > 9
digits[i] *= 2

# ✅ Correct
digits[i] *= 2
if digits[i] > 9:
    digits[i] -= 9
```

### 3. Including Check Digit in Sum Before Adding
```python
# ❌ Wrong - check digit doubled
digits = [int(d) for d in card_number]

# ✅ Correct - exclude check digit
check_digit = int(card_number[-1])
digits = [int(d) for d in card_number[:-1]]
```

## 🎮 Real-World Applications

1. **E-commerce**: Validate cards before processing
2. **Payment Gateways**: Pre-validation before API calls
3. **Form Validation**: Client-side card number checking
4. **Testing**: Generate valid test card numbers
5. **Security**: Quick check before expensive validation

## 🚀 Challenge Projects

### Challenge 1: Card Generator
Create valid test card numbers using the Luhn algorithm:
```python
def generate_card(prefix, length):
    # Generate random digits
    # Calculate check digit using Luhn
    # Return valid card number
    pass
```

### Challenge 2: Masked Display
Show card number with masking:
- Input: 4532015112830366
- Output: 4532 **** **** 0366

### Challenge 3: Expiry Date Validator
Extend to validate:
- Card number (Luhn)
- Expiry date (MM/YY format, not expired)
- CVV (3-4 digits)

## 📝 Key Takeaways

- Luhn algorithm validates identification numbers
- Reverse digits before doubling
- Double every second digit (after reversing)
- Subtract 9 if doubled digit > 9
- Sum must be divisible by 10
- Always validate format before applying algorithm
- Card type can be identified from first digits

## 🎓 Key Takeaways from Video

1. Lists store multiple items in a single variable
2. Use loops to repeat actions
3. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter

Continue to [Chapter 44: Banking Program](42-banking-program.md) to build a complete banking application!

---

**Security Note:** This validates the format only. Real validation requires checking with the card issuer. Never store card numbers in plain text!