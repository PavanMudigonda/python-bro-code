# ============================================
# CHAPTER 36: MEMBERSHIP OPERATORS
# ============================================
# Membership Operators = Used to test whether a value or variable
#                        is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#
# Two Operators:
# 1. in      - Returns True if value is found in sequence
# 2. not in  - Returns True if value is NOT found in sequence
#
# Use Cases:
# - Checking if element exists in collection
# - Validating user input
# - Searching for characters in strings
# - Checking dictionary keys

# =============================================
# SIMPLE WORD GUESSING EXAMPLE
# =============================================

# The word to guess (string is an iterable of characters)
word = "APPLE"

# Get user input
letter = input("Guess a letter in a secret word: ")

# =============================================
# MEMBERSHIP TEST WITH 'in' OPERATOR
# =============================================
# Check if the guessed letter exists in the word
# 'in' operator is case-sensitive!
if letter in word:
    print(f'there is a {letter}')
else:
    print(f'{letter} was not found')

# =============================================
# OTHER MEMBERSHIP OPERATOR EXAMPLES
# =============================================

# Example with lists
# fruits = ["apple", "banana", "orange"]
# if "apple" in fruits:
#     print("Apple found!")

# Example with 'not in'
# if "E" not in word:
#     print("E is not in the word")

# Example with dictionaries (checks keys, not values)
# person = {"name": "John", "age": 25}
# if "name" in person:
#     print("Key 'name' exists")
    