# ============================================
# CHAPTER 37: LIST COMPREHENSIONS
# ============================================
# List Comprehensions = A concise way to create lists in Python
#                       More compact and easier to read than traditional loops
#                       Syntax: [expression for value in iterable if condition]
#
# Benefits:
# - More concise than traditional for loops
# - Often faster execution
# - More Pythonic and readable
# - Can include conditional logic
#
# General Syntax:
# [expression for item in iterable]
# [expression for item in iterable if condition]
# [expression if condition else other for item in iterable]

# =============================================
# TRADITIONAL LOOP APPROACH (Verbose)
# =============================================
# This is the old way - works but requires more lines
# doubles = []  # Create empty list
# for x in range(1,11):  # Loop through numbers 1-10
#     doubles.append(x * 2)  # Multiply by 2 and add to list
# print(doubles)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# =============================================
# LIST COMPREHENSION SYNTAX
# =============================================
# Syntax: [expression for value in iterable if condition]
# - expression: what to do with each value (e.g., x * 2)
# - for value in iterable: loop through sequence
# - if condition: optional filter (not used here)

# =============================================
# MULTIPLE LIST COMPREHENSION EXAMPLES
# =============================================

# Create list of doubles (multiply by 2)
# [x * 2 for x in range(1,11)] means:
# "For each x from 1 to 10, create x * 2"
doubles = [ x * 2 for x in range(1,11)]

# Create list of triples (multiply by 3)
triples = [ y * 3 for y in range(1,11)]

# Create list of quadruples (multiply by 4)
squares = [ z * 4 for z in range(1,11)]

# Create list of numbers multiplied by 5
pentas  = [ a * 5 for a in range(1,11)]

# =============================================
# DISPLAY RESULTS
# =============================================
print(doubles)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(triples)  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print(squares)  # [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
print(pentas)   # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# =============================================
# ADVANCED LIST COMPREHENSION EXAMPLES
# =============================================
# With condition - only even numbers
# evens = [x for x in range(1,21) if x % 2 == 0]

# With if-else
# labels = ["even" if x % 2 == 0 else "odd" for x in range(1,11)]