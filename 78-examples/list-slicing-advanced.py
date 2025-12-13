# Advanced list slicing techniques

# Basic slicing: list[start:end:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get first 5 elements
print("First 5:", numbers[:5])  # [0, 1, 2, 3, 4]

# Get last 5 elements
print("Last 5:", numbers[-5:])  # [5, 6, 7, 8, 9]

# Get middle elements
print("Middle:", numbers[3:7])  # [3, 4, 5, 6]

# Reverse a list
print("Reversed:", numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Every second element
print("Every 2nd:", numbers[::2])  # [0, 2, 4, 6, 8]

# Every third element starting from index 1
print("Every 3rd from 1:", numbers[1::3])  # [1, 4, 7]

# Reverse every second element
print("Reverse every 2nd:", numbers[::-2])  # [9, 7, 5, 3, 1]

# String slicing
text = "Python Programming"
print("First word:", text[:6])  # Python
print("Last word:", text[7:])  # Programming
print("Reverse text:", text[::-1])  # gnimmargorP nohtyP

# Slice assignment
numbers = [0, 1, 2, 3, 4, 5]
numbers[2:4] = [10, 20, 30]
print("After slice assignment:", numbers)  # [0, 1, 10, 20, 30, 4, 5]

# Delete elements using slice
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]  # Delete every second element
print("After deletion:", numbers)  # [1, 3, 5, 7, 9]

# Copy a list using slicing
original = [1, 2, 3, 4, 5]
copy = original[:]
copy[0] = 100
print("Original:", original)  # [1, 2, 3, 4, 5]
print("Copy:", copy)  # [100, 2, 3, 4, 5]

# Palindrome check using slicing
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print("Is 'racecar' palindrome?", is_palindrome("racecar"))  # True
print("Is 'hello' palindrome?", is_palindrome("hello"))  # False
print("Is 'A man a plan a canal Panama' palindrome?", 
      is_palindrome("A man a plan a canal Panama"))  # True
