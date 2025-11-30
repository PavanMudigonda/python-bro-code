
# *args  = allows you to pass multiple non-keyword arguments
# **kwargs = allows you to pass multiple keyword arguments
# * and ** are unpacking operators
# Argument types:
# 1. positional
# 2. default
# 3. keyword
# 4. arbitrary

def print_address(**kwargs):
    print(type(kwargs))  # kwargs is a dict
    for key, value in kwargs.items():  # use .items() to get key-value pairs
        print(f'{key}: {value}')

print_address(street="Front Street", city="Toronto", state="Ontario", zip="M5V3A4")


