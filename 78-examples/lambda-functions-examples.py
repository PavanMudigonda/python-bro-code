# Lambda functions - anonymous functions

# Basic lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 7))  # Output: 10

# Lambda with conditional
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(4))  # Output: Even
print(is_even(7))  # Output: Odd

# Sorting with lambda
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
print(students_sorted)  # Sorted by grade

# Lambda in list comprehension
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
