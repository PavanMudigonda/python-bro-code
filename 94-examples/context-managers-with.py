# Context managers and 'with' statement

# File handling with context manager
# The file is automatically closed after the block
def write_and_read_file():
    # Writing to file
    with open('example.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write("Using context managers\n")
    # File is automatically closed here
    
    # Reading from file
    try:
        with open('example.txt', 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        print("File not found")

write_and_read_file()

# Multiple context managers
try:
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        content = infile.read()
        outfile.write(content.upper())
except FileNotFoundError:
    print("Input file not found")

# Custom context manager using class
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        return False

# Using custom context manager
try:
    with ManagedFile('test.txt', 'w') as f:
        f.write("Custom context manager example\n")
except Exception as e:
    print(f"Error: {e}")

# Context manager using contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Acquiring resource")
    resource = "Resource"
    try:
        yield resource
    finally:
        print("Releasing resource")

# Using the custom context manager
with managed_resource() as res:
    print(f"Using {res}")
