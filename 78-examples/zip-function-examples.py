# Zip function - combines multiple iterables

# Basic zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Zip with three lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]
info = list(zip(names, ages, cities))
print(info)

# Unzipping
paired = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*paired)
print("Numbers:", numbers)  # (1, 2, 3)
print("Letters:", letters)  # ('a', 'b', 'c')

# Zip with different lengths (stops at shortest)
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
result = list(zip(list1, list2))
print(result)  # [(1, 'a'), (2, 'b'), (3, 'c')]

# Creating dictionary from two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}

# Parallel iteration
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
