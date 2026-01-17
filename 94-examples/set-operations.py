# Set operations and methods

# Creating sets
fruits = {"apple", "banana", "cherry"}
colors = set(["red", "green", "blue"])
print("Fruits:", fruits)
print("Colors:", colors)

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union - all unique elements
union = set1 | set2
print("Union:", union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection - common elements
intersection = set1 & set2
print("Intersection:", intersection)  # {4, 5}

# Difference - in first but not second
difference = set1 - set2
print("Difference (set1 - set2):", difference)  # {1, 2, 3}

# Symmetric difference - in either but not both
sym_diff = set1 ^ set2
print("Symmetric difference:", sym_diff)  # {1, 2, 3, 6, 7, 8}

# Set methods
numbers = {1, 2, 3}
numbers.add(4)
print("After add:", numbers)  # {1, 2, 3, 4}

numbers.update([5, 6, 7])
print("After update:", numbers)  # {1, 2, 3, 4, 5, 6, 7}

numbers.remove(7)  # Raises KeyError if not found
print("After remove:", numbers)

numbers.discard(100)  # Does not raise error if not found
print("After discard:", numbers)

# Subset and superset
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print("Is set_a subset of set_b?", set_a.issubset(set_b))  # True
print("Is set_b superset of set_a?", set_b.issuperset(set_a))  # True

# Disjoint sets (no common elements)
set_x = {1, 2, 3}
set_y = {4, 5, 6}
print("Are sets disjoint?", set_x.isdisjoint(set_y))  # True

# Remove duplicates from list
numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = list(set(numbers_list))
print("Unique numbers:", unique_numbers)
