# *args and **kwargs - variable arguments

# *args - variable positional arguments
def sum_all(*args):
    """Sum any number of arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(10, 20))  # 30

# **kwargs - variable keyword arguments
def print_info(**kwargs):
    """Print key-value pairs"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
print()

# Combining regular args, *args, and **kwargs
def full_function(required, *args, default=10, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

full_function(1, 2, 3, 4, default=20, name="Bob", age=30)
print()

# Unpacking lists and dictionaries
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print("Sum using unpacking:", add_three(*numbers))  # 6

# Unpacking dictionary
def greet(name, age, city):
    print(f"Hello {name}, {age} years old from {city}")

person = {"name": "Alice", "age": 25, "city": "NYC"}
greet(**person)

# Combining lists using unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print("Combined lists:", combined)  # [1, 2, 3, 4, 5, 6]

# Combining dictionaries using unpacking
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined_dict = {**dict1, **dict2}
print("Combined dicts:", combined_dict)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Flexible function accepting both
def flexible_func(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

flexible_func(1, 2, 3, name="Alice", age=25)
