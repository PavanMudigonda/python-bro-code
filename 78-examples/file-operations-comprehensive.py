# Comprehensive file operations

import os

# Writing to files
def write_examples():
    # Write mode - overwrites file
    with open('sample.txt', 'w') as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        f.writelines(["Line 3\n", "Line 4\n"])
    
    # Append mode - adds to end
    with open('sample.txt', 'a') as f:
        f.write("Line 5 (appended)\n")

# Reading from files
def read_examples():
    # Read entire file
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print("Entire file:", content)
    except FileNotFoundError:
        print("File not found")
        return
    
    # Read line by line
    with open('sample.txt', 'r') as f:
        for line in f:
            print("Line:", line.strip())
    
    # Read all lines into list
    with open('sample.txt', 'r') as f:
        lines = f.readlines()
        print("All lines:", lines)
    
    # Read specific number of characters
    with open('sample.txt', 'r') as f:
        chunk = f.read(10)
        print("First 10 chars:", chunk)

# File operations
def file_operations():
    # Check if file exists
    if os.path.exists('sample.txt'):
        print("File exists")
        
        # Get file size
        size = os.path.getsize('sample.txt')
        print(f"File size: {size} bytes")
        
        # Get file info
        print(f"Is file: {os.path.isfile('sample.txt')}")
        print(f"Is directory: {os.path.isdir('sample.txt')}")
    
    # Rename file
    if os.path.exists('sample.txt'):
        os.rename('sample.txt', 'renamed.txt')
        print("File renamed")
        
        # Delete file
        os.remove('renamed.txt')
        print("File deleted")

# Working with directories
def directory_operations():
    # Create directory
    if not os.path.exists('test_dir'):
        os.mkdir('test_dir')
        print("Directory created")
    
    # List files in directory
    files = os.listdir('.')
    print("Files in current directory:", files[:5])  # First 5
    
    # Get current working directory
    cwd = os.getcwd()
    print("Current directory:", cwd)
    
    # Remove directory
    if os.path.exists('test_dir'):
        os.rmdir('test_dir')
        print("Directory removed")

# Binary file operations
def binary_file_example():
    # Write binary data
    data = bytes([120, 3, 255, 0, 100])
    with open('binary.dat', 'wb') as f:
        f.write(data)
    
    # Read binary data
    with open('binary.dat', 'rb') as f:
        content = f.read()
        print("Binary content:", content)
    
    # Clean up
    if os.path.exists('binary.dat'):
        os.remove('binary.dat')

# CSV file handling (without csv module)
def simple_csv_example():
    # Writing CSV
    with open('data.csv', 'w') as f:
        f.write("Name,Age,City\n")
        f.write("Alice,25,NYC\n")
        f.write("Bob,30,LA\n")
        f.write("Charlie,35,Chicago\n")
    
    # Reading CSV
    with open('data.csv', 'r') as f:
        for i, line in enumerate(f):
            parts = line.strip().split(',')
            if i == 0:
                print("Headers:", parts)
            else:
                print(f"Row {i}:", parts)
    
    # Clean up
    if os.path.exists('data.csv'):
        os.remove('data.csv')

# Run examples
if __name__ == "__main__":
    write_examples()
    read_examples()
    # file_operations()  # Uncomment to test
    # binary_file_example()  # Uncomment to test
    # simple_csv_example()  # Uncomment to test
