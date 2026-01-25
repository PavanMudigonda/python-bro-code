# Chapter 19: Nested Loops

## 📺 Video Tutorial

**Nested loops in Python are easy ➿** (6:12)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/APWy6Pc83gE)

## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/Watch-BroCode_Python_Master_Class-red?style=for-the-badge&logo=youtube)](https://youtu.be/KseiSR0MCTI)

## 📚 What You'll Learn
Master nested loops - loops within loops - to create patterns, process 2D data, and solve complex iteration problems!

## 🎯 Learning Objectives
- Understand nested loop structure
- Create patterns using nested loops
- Process 2D data structures (grids, tables)
- Use nested loops with multiple sequences
- Combine nested loops with conditionals
- Optimize nested loop performance

## 📖 Concept Explanation

### What are Nested Loops?
A nested loop is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

### Syntax
```python
for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        # code executes for each combination
```

### How It Works
```python
for i in range(3):      # Outer loop: 3 iterations
    for j in range(2):  # Inner loop: 2 iterations
        print(f"({i}, {j})")

# Output:
# (0, 0) (0, 1)  <- i=0, j=0 and j=1
# (1, 0) (1, 1)  <- i=1, j=0 and j=1
# (2, 0) (2, 1)  <- i=2, j=0 and j=1
```

### Total Iterations
Total iterations = Outer iterations × Inner iterations
- If outer runs 3 times and inner runs 4 times = 12 total iterations

## 💡 Examples

### Example 1: Basic Nested Loop
```python
for i in range(3):
    for j in range(4):
        print(f"i={i}, j={j}")

# Executes 3 × 4 = 12 times
```

### Example 2: Rectangle Pattern
```python
rows = 4
cols = 6

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()  # New line after each row

# Output:
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * *
```

### Example 3: Multiplication Table
```python
print("Multiplication Table (1-10)\n")

# Header
print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()
print("-" * 44)

# Table
for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
```

### Example 4: Right Triangle Pattern
```python
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
```

### Example 5: Number Pyramid
```python
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")
    
    # Print numbers
    for j in range(i):
        print(i, end=" ")
    
    print()

# Output:
#         1 
#       2 2 
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5
```

### Example 6: Checkerboard Pattern
```python
size = 8

for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

# Creates checkerboard pattern
```

### Example 7: 2D List Iteration
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate through rows and columns
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Alternative with indices
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
```

### Example 8: Finding Pairs
```python
numbers = [1, 2, 3, 4]

print("All pairs:")
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        print(f"({numbers[i]}, {numbers[j]})")

# Output:
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)
```

### Example 9: Sum of 2D List
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0
for row in matrix:
    for num in matrix:
        total += num

print(f"Sum: {total}")  # 45
```

### Example 10: Diamond Pattern
```python
n = 5

# Upper half
for i in range(n):
    # Spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Stars
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# Lower half
for i in range(n - 2, -1, -1):
    # Spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Stars
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
```

## 🔍 Common Mistakes

### Mistake 1: Confusing Loop Variables
```python
# Wrong - using same variable
for i in range(3):
    for i in range(2):  # Overwrites outer i!
        print(i)

# Correct - different variables
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

### Mistake 2: Wrong Indentation
```python
# Wrong
for i in range(3):
    for j in range(2):
        print(f"({i},{j})")
print()  # Outside both loops!

# Correct
for i in range(3):
    for j in range(2):
        print(f"({i},{j})", end=" ")
    print()  # After inner loop
```

### Mistake 3: Inefficient Nested Loops
```python
# Inefficient - O(n²)
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    for j in numbers:
        if i == j:
            print(i)

# Better - O(n)
for num in numbers:
    print(num)
```

### Mistake 4: Modifying List While Iterating
```python
# Dangerous!
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for num in row:
        row.remove(num)  # Don't do this!

# Safe approach
matrix = [[1, 2], [3, 4]]
new_matrix = [[num for num in row if num > 2] 
              for row in matrix]
```

## ✍️ Practice Exercises

### Easy
1. Print a 5×5 grid of asterisks
2. Create a square of numbers (1-5 in each row)
3. Make a right triangle of stars (1-10 rows)
4. Print a times table (1-5)
5. Create a simple checkerboard (4×4)

### Medium
6. Build a number pyramid (centered)
7. Create an inverted triangle
8. Make a hollow square pattern
9. Print Pascal's triangle
10. Generate a multiplication grid with labels

### Hard
11. Create a diamond pattern (variable size)
12. Build an hourglass shape
13. Make a spiral number pattern
14. Create ASCII art alphabet letters
15. Generate a maze pattern

## 🎮 Real-World Applications

### Application 1: Seating Chart
```python
def create_seating_chart():
    rows = 5
    seats_per_row = 8
    
    print("=== Movie Theater Seating ===\n")
    print("   ", end="")
    
    # Column headers
    for seat in range(1, seats_per_row + 1):
        print(f"{seat:3}", end="")
    print("\n")
    
    # Rows
    row_labels = ['A', 'B', 'C', 'D', 'E']
    for i in range(rows):
        print(f"{row_labels[i]}  ", end="")
        for j in range(seats_per_row):
            print("[ ]", end="")
        print()

create_seating_chart()
```

### Application 2: Grade Table
```python
students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]
grades = [
    [95, 88, 92],
    [87, 91, 85],
    [92, 95, 89]
]

print("=== Grade Report ===\n")

# Header
print(f"{'Student':<12}", end="")
for subject in subjects:
    print(f"{subject:>10}", end="")
print(f"{'Average':>10}")
print("-" * 55)

# Grades
for i in range(len(students)):
    print(f"{students[i]:<12}", end="")
    
    total = 0
    for j in range(len(subjects)):
        grade = grades[i][j]
        print(f"{grade:>10}", end="")
        total += grade
    
    average = total / len(subjects)
    print(f"{average:>10.1f}")
```

### Application 3: Calendar Generator
```python
def print_calendar(days, start_day):
    print("Su Mo Tu We Th Fr Sa")
    
    # Print leading spaces
    for i in range(start_day):
        print("   ", end="")
    
    # Print days
    day = 1
    current_day = start_day
    
    while day <= days:
        print(f"{day:2} ", end="")
        current_day += 1
        day += 1
        
        if current_day % 7 == 0:
            print()  # New week

print("November 2024")
print_calendar(30, 4)  # 30 days, starts on Thursday
```

### Application 4: Matrix Operations
```python
def matrix_multiply(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])
    
    result = []
    
    for i in range(rows1):
        row = []
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)
    
    return result

# Example
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = matrix_multiply(A, B)

print("Result:")
for row in C:
    print(row)
```

### Application 5: Game Board
```python
def create_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Sample game state
    board[0][0] = "X"
    board[0][2] = "O"
    board[1][1] = "X"
    board[2][1] = "O"
    
    print("=== Tic-Tac-Toe ===\n")
    
    for i in range(3):
        for j in range(3):
            print(f" {board[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("-----------")

create_tic_tac_toe()

# Output:
#  X |   | O 
# -----------
#    | X |   
# -----------
#    | O |   
```

### Application 6: ASCII Art Generator
```python
def draw_box(width, height):
    # Top border
    print("┌" + "─" * (width - 2) + "┐")
    
    # Middle rows
    for i in range(height - 2):
        print("│" + " " * (width - 2) + "│")
    
    # Bottom border
    print("└" + "─" * (width - 2) + "┘")

draw_box(20, 8)
```

## 🚀 Challenge Projects

### Challenge 1: Pattern Generator
Create a program that:
- Displays menu of patterns (triangle, diamond, pyramid, etc.)
- Lets user choose pattern and size
- Generates pattern with characters of choice
- Allows saving pattern to file

### Challenge 2: Sudoku Validator
Build a validator that:
- Checks if 9×9 grid is valid Sudoku
- Validates rows, columns, and 3×3 boxes
- Identifies specific errors
- Suggests possible corrections

### Challenge 3: Conway's Game of Life
Implement the cellular automaton:
- Create initial grid state
- Apply rules for each generation
- Display grid evolution
- Allow pause/step/run modes

### Challenge 4: ASCII Maze Generator
Create a maze generator:
- Generate random maze using nested loops
- Ensure path from start to end exists
- Display walls and open paths
- Add difficulty levels

### Challenge 5: Image ASCII Converter
Build a converter that:
- Reads image pixel data
- Converts to grayscale
- Maps brightness to ASCII characters
- Displays ASCII version using nested loops

## 📊 Performance Considerations

### Time Complexity
```python
# O(n²) - Quadratic
for i in range(n):
    for j in range(n):
        # do something

# O(n³) - Cubic  
for i in range(n):
    for j in range(n):
        for k in range(n):
            # do something
```

### Optimization Tips
```python
# Avoid unnecessary iterations
for i in range(n):
    for j in range(i, n):  # Start from i instead of 0
        # Reduces iterations by half

# Break early when possible
for i in range(n):
    for j in range(n):
        if condition:
            break  # Exit inner loop
```

## 🎯 Common Patterns Reference

### Rectangle
```python
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
```

### Right Triangle
```python
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
```

### Inverted Triangle
```python
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

### Pyramid
```python
for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1))
```

## 💪 Try It Yourself

Modify `task.py` to:
1. Create different triangle patterns
2. Build a multiplication table
3. Generate number spirals
4. Make ASCII art shapes
5. Create a simple text-based game board
6. Build a pattern menu system

## 🎓 Key Takeaways from Video

1. Loops repeat code multiple times
2. Use loops to repeat actions
3. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter
Continue to [Chapter 21: Lists](../21-lists/) to learn about Python's most versatile data structure!

