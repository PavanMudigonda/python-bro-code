import os.path
import sys

# Example 1: Check if file exists
if os.path.isfile('test.txt'):
    print('The file exists')

# Example 2: Remove file if it exists
if os.path.isfile('test.txt'):
    os.remove('test.txt')

# Example 3: Read file from command line argument
# Usage: python nintyone.py myfile.txt
if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as input_file:
        print(input_file.read())
