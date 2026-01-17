# Map, Filter, and Reduce functions

from functools import reduce

# MAP - applies function to each item
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)  # [1, 4, 9, 16, 25]

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = list(map(lambda x, y: x + y, list1, list2))
print("Sum:", result)  # [11, 22, 33]

# FILTER - filters items based on condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)  # [2, 4, 6, 8, 10]

# Filter strings
names = ["Alice", "Bob", "Alexander", "Charlie", "Amanda"]
a_names = list(filter(lambda x: x.startswith('A'), names))
print("Names starting with A:", a_names)

# REDUCE - reduces sequence to single value
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum of all:", sum_all)  # 15

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)  # 120

# Find maximum using reduce
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum:", max_num)  # 5
