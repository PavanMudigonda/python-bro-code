# ============================================
# Chapter 21: Lists
# ============================================
# Collection = Single variable used to store multiple values
# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# ============================================
# Creating a list
# ============================================
# Lists use square brackets []
# Items are ordered by index (0, 1, 2, ...)
fruits = ["apple", "banana", "cherry", "dragon fruit", "elderberry", "fig", "grape", "honeydew"]

# ============================================
# Useful list functions (uncomment to try)
# ============================================
# dir(fruits)  - shows all available methods
# help(fruits) - displays documentation
# len(fruits)  - returns number of items
# print(len(fruits))

# ============================================
# List Methods
# ============================================

# .append() - Add item to end of list
fruits.append("kiwi")

# Indexing - Access/modify items by position
fruits[0] = "apricot"  # Change first item

# .insert() - Add item at specific position
fruits.insert(1, "blueberry")  # Insert at index 1

# .remove() - Remove specific item
fruits.remove("banana")

# .sort() - Sort list alphabetically
# Note: sort() returns None, it modifies the list in-place
fruits.sort()  # fruits is now sorted

# ============================================
# Iterating through list
# ============================================
print("\nFruits in alphabetical order:")
for fruit in fruits:
    print(fruit)

# ============================================
# Common List Methods:
# ============================================
# .append(item)    - Add to end
# .insert(i, item) - Add at index
# .remove(item)    - Remove first occurrence
# .pop()           - Remove last item
# .pop(i)          - Remove item at index
# .sort()          - Sort ascending
# .reverse()       - Reverse order
# .clear()         - Remove all items
# .count(item)     - Count occurrences
# .index(item)     - Find index of item