# ============================================
# Chapter 21: Sets
# ============================================
# Collection types in Python:
# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# ============================================
# Creating a set
# ============================================
# Sets use curly braces {}
# Sets automatically remove duplicates
# Items have NO specific order (unordered)
fruits = {"apple", "banana", "cherry", "dragon fruit", "elderberry", "fig", "grape", "honeydew"}

# ============================================
# Viewing set methods (uncomment to try)
# ============================================
# print(dir(fruits))  # Shows all available methods

# ============================================
# Iterating through a set
# ============================================
# Note: Order may vary each time you run the program
print("Original set:")
for fruit in fruits:
    print(fruit)

# ============================================
# .add() - Add single item to set
# ============================================
# If item already exists, set remains unchanged
fruits.add("kiwi")
print("\nAfter adding kiwi:")
print(fruits)

# ============================================
# .remove() - Remove item from set
# ============================================
# Raises KeyError if item doesn't exist
fruits.remove("banana")
print("\nAfter removing banana:")
print(fruits)

# ============================================
# Key Set Characteristics:
# ============================================
# 1. NO duplicates - automatically removes duplicate values
# 2. Unordered - items have no index, order may change
# 3. Mutable - can add/remove items
# 4. Fast membership testing - checking if item exists is very fast
#
# Common Set Methods:
# .add(item)         - Add single item
# .remove(item)      - Remove item (error if not found)
# .discard(item)     - Remove item (no error if not found)
# .clear()           - Remove all items
# .union(set2)       - Combine two sets
# .intersection(set2)- Items in both sets
# .difference(set2)  - Items in first set but not second

