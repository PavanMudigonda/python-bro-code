# Generators and yield keyword

# Basic generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

# Generator in for loop
for num in count_up_to(5):
    print(num, end=' ')  # 1 2 3 4 5
print()

# Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Fibonacci:", list(fibonacci(10)))

# Generator expression (like list comprehension)
squares = (x ** 2 for x in range(10))
print("First square:", next(squares))  # 0
print("Second square:", next(squares))  # 1

# Memory efficient file reader
def read_large_file(file_path):
    """Generator for reading large files line by line"""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        yield "File not found"

# Infinite generator
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# Use with break to avoid infinite loop
gen = infinite_sequence()
for _ in range(5):
    print(next(gen), end=' ')  # 0 1 2 3 4
print()
