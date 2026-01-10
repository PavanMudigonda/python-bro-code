# ============================================
# CHAPTER 35: ITERABLES
# ============================================
# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop
#
# Common Iterables:
# - Lists: ordered, mutable, can be reversed
# - Tuples: ordered, immutable, can be reversed
# - Sets: unordered, mutable, CANNOT be reversed (no order)
# - Dictionaries: ordered (Python 3.7+), mutable
# - Strings: ordered, immutable, can be reversed
#
# Key Concepts:
# - For loops work with any iterable
# - reversed() creates a reverse iterator
# - Sets don't support reversed() due to lack of order

# =============================================
# EXAMPLES OF DIFFERENT ITERABLES
# =============================================

# List - ordered and reversible
# numbers = ["1","2","3","4","5"]

# Tuple - ordered and reversible (currently active)
numbers = ("1","2","3","4","5")

# Set - unordered, CANNOT be reversed
# numbers = { "1","2","3","4","5" }
# Note: Trying reversed() on a set will raise TypeError

# =============================================
# FORWARD ITERATION
# =============================================
# Standard for loop iterates from first to last element
# for number in numbers:
#     print(number)  # Output: 1, 2, 3, 4, 5

# =============================================
# REVERSE ITERATION
# =============================================
# reversed() returns an iterator that accesses elements in reverse order
# Works with lists, tuples, strings - anything with defined order
for number in reversed(numbers):
    print(number)  # Output: 5, 4, 3, 2, 1

# Other ways to reverse:
# numbers[::-1]  # Slicing - creates reversed copy
# list(reversed(numbers))  # Convert reverse iterator to list
    

