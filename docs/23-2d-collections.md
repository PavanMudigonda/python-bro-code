# 📊 2D Collections (Nested Lists & Matrices)

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/23-2d-collections/23-2d-collections.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/23-2d-collections/23-2d-collections.ipynb)


## 📺 Video Tutorial

**Python 2D collections are easy! ⬜** (5:55)

## What You'll Learn

In this chapter, you'll explore two-dimensional (2D) data structures using nested lists to create matrices, tables, and grids. You'll learn how to organize data in rows and columns, access elements using double indexing, and iterate through multi-dimensional data structures effectively.

## Learning Objectives

- Create and manipulate 2D lists (lists containing other lists)
- Access elements using row and column indices [row][col]
- Iterate through nested structures using nested loops
- Understand the relationship between 1D and 2D data structures
- Modify elements in multi-dimensional collections
- Apply 2D lists to practical problems like grids and tables

## Concept Explanation

### What are 2D Collections?

A **2D collection** (or 2D list) is a list that contains other lists as its elements. Think of it like a spreadsheet with rows and columns, a game board, or a table of data.

```python
# A simple 2D list (3 rows, 3 columns)
grid = [
    [1, 2, 3],    # Row 0
    [4, 5, 6],    # Row 1
    [7, 8, 9]     # Row 2
]
```

### Visualizing 2D Lists

```
Index:     [0] [1] [2]
         ┌───┬───┬───┐
    [0]  │ 1 │ 2 │ 3 │
         ├───┼───┼───┤
    [1]  │ 4 │ 5 │ 6 │
         ├───┼───┼───┤
    [2]  │ 7 │ 8 │ 9 │
         └───┴───┴───┘
```

### Double Indexing

To access an element in a 2D list, use **double bracket notation**:

```python
grid[row][column]
```

- **First bracket** selects the row (which list)
- **Second bracket** selects the column (which element in that list)

```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

grid[0][1]  # Row 0, Column 1 → 2
grid[1][0]  # Row 1, Column 0 → 4
grid[2][2]  # Row 2, Column 2 → 9
```

### Creating 2D Lists

There are several ways to create 2D lists:

#### Method 1: Direct Definition
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

#### Method 2: From Existing Lists
```python
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "lettuce", "onion"]
meats = ["beef", "chicken", "pork"]

# Combine into 2D list
groceries = [fruits, vegetables, meats]
```

#### Method 3: Using List Comprehension
```python
# Create 3x3 grid filled with zeros
grid = [[0 for _ in range(3)] for _ in range(3)]
```

### Nested Iteration

To process all elements in a 2D list, use **nested loops**:

```python
groceries = [
    ["apple", "banana", "cherry"],
    ["carrot", "lettuce", "onion"],
    ["beef", "chicken", "pork"]
]

# Outer loop: iterate through rows
for collection in groceries:
    # Inner loop: iterate through items in each row
    for food in collection:
        print(food)
```

### Common 2D List Patterns

1. **Grid/Matrix** - Equal-sized rows and columns
2. **Table** - Data organized in rows with named columns
3. **Jagged Array** - Rows of different lengths
4. **Game Board** - Chess, Tic-Tac-Toe, etc.

## Examples

### Example 1: Creating and Accessing 2D Lists
```python
# Create a 2D list from separate lists
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "lettuce", "onion"]
meats = ["beef", "chicken", "pork"]

groceries = [fruits, vegetables, meats]

# Access specific elements
print(groceries[0][1])  # "banana"
print(groceries[1][0])  # "carrot"
print(groceries[2][2])  # "pork"
print(groceries[1][1])  # "lettuce"
```

### Example 2: Modifying 2D List Elements
```python
groceries = [
    ["apple", "banana", "cherry"],
    ["carrot", "lettuce", "onion"],
    ["beef", "chicken", "pork"]
]

# Change banana to blueberry
groceries[0][1] = "blueberry"

print(groceries[0])  # ['apple', 'blueberry', 'cherry']
```

### Example 3: Nested Loops for 2D Lists
```python
groceries = [
    ["apple", "banana", "cherry"],
    ["carrot", "lettuce", "onion"],
    ["beef", "chicken", "pork"]
]

# Print each item with category
categories = ["Fruits", "Vegetables", "Meats"]

for i in range(len(groceries)):
    print(f"\n{categories[i]}:")
    for item in groceries[i]:
        print(f"  - {item}")

# Output:
# Fruits:
#   - apple
#   - banana
#   - cherry
# Vegetables:
#   - carrot
#   - lettuce
#   - onion
# Meats:
#   - beef
#   - chicken
#   - pork
```

### Example 4: Number Pad Example
```python
# Representing a phone keypad
num_pad = (
    (7, 8, 9),
    (4, 5, 6),
    (1, 2, 3),
    ("*", 0, "#")
)

# Display the keypad
for row in num_pad:
    for button in row:
        print(button, end=" ")
    print()  # New line after each row

# Output:
# 7 8 9 
# 4 5 6 
# 1 2 3 
# * 0 # 
```

### Example 5: Tic-Tac-Toe Board
```python
# Create empty tic-tac-toe board
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Place some moves
board[0][0] = "X"
board[1][1] = "O"
board[2][2] = "X"

# Display board
for row in board:
    print(" ".join(row))

# Output:
# X - -
# - O -
# - - X
```

### Example 6: Matrix Operations
```python
# Create a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calculate sum of all elements
total = 0
for row in matrix:
    for num in row:
        total += num

print(f"Sum of all elements: {total}")  # 45

# Find maximum value
max_val = matrix[0][0]
for row in matrix:
    for num in row:
        if num > max_val:
            max_val = num

print(f"Maximum value: {max_val}")  # 9
```

### Example 7: Student Grades Table
```python
# Student grades: [name, math, science, english]
students = [
    ["Alice", 85, 92, 88],
    ["Bob", 78, 85, 90],
    ["Charlie", 92, 88, 85]
]

# Display formatted table
print(f"{'Name':<10} {'Math':<6} {'Science':<8} {'English':<8} {'Average':<8}")
print("=" * 50)

for student in students:
    name = student[0]
    grades = student[1:]
    average = sum(grades) / len(grades)
    print(f"{name:<10} {grades[0]:<6} {grades[1]:<8} {grades[2]:<8} {average:<8.2f}")

# Output:
# Name       Math   Science  English  Average 
# ==================================================
# Alice      85     92       88       88.33   
# Bob        78     85       90       84.33   
# Charlie    92     88       85       88.33   
```

## Practice Exercises

### Beginner Level

1. **Create and Display**: Create a 2D list with 3 rows and 4 columns of your favorite numbers. Print each row on a separate line.

2. **Access Practice**: Create a 2D list representing a 3x3 grid. Access and print the elements at positions [0][0], [1][1], and [2][2] (the diagonal).

3. **Modify Elements**: Create a 2D list of colors. Change the element at position [1][1] and print the entire modified list.

4. **Count Elements**: Create a 2D list and count the total number of elements across all rows.

5. **Row Sums**: Create a 2D list of numbers. Calculate and print the sum of each row.

### Intermediate Level

6. **Transpose Matrix**: Write a program to transpose a 3x3 matrix (swap rows and columns).

7. **Checkerboard Pattern**: Create an 8x8 2D list representing a checkerboard with alternating "B" and "W" for black and white squares.

8. **Find Element**: Search for a specific value in a 2D list and return its row and column indices.

9. **Border Elements**: Print only the border elements of a 2D matrix (first/last row and first/last column).

10. **Row and Column Averages**: Calculate the average of each row and each column in a 2D list of numbers.

### Advanced Level

11. **Spiral Print**: Print elements of a 2D matrix in spiral order (clockwise from outside to inside).

12. **Rotate Matrix**: Rotate a square matrix 90 degrees clockwise.

13. **Saddle Point**: Find a saddle point in a matrix (element that is minimum in its row and maximum in its column).

14. **Pascal's Triangle**: Generate the first n rows of Pascal's Triangle using a 2D list.

15. **Matrix Multiplication**: Implement matrix multiplication for two compatible 2D matrices.

## Common Mistakes to Avoid

### Mistake 1: Shallow Copy Creating References

**Wrong:**
```python
# This creates 3 references to the SAME list!
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)
# Output: [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
# All rows changed!
```

**Correct:**
```python
# Create separate lists for each row
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)
# Output: [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
# Only first row changed
```

**Why:** `[[0] * 3] * 3` repeats the same list object 3 times, not creating independent copies.

### Mistake 2: Confusing Row/Column Order

**Wrong:**
```python
matrix = [[1, 2, 3], [4, 5, 6]]
# Trying to access column 2, row 1
value = matrix[2][1]  # IndexError!
```

**Correct:**
```python
matrix = [[1, 2, 3], [4, 5, 6]]
# Correct: row first, then column
value = matrix[1][2]  # 6
```

**Why:** Always use `matrix[row][column]`, not `matrix[column][row]`.

### Mistake 3: Forgetting to Print Newlines

**Wrong:**
```python
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for num in row:
        print(num, end=" ")
# Output: 1 2 3 4 (all on one line!)
```

**Correct:**
```python
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # Newline after each row
# Output:
# 1 2 
# 3 4 
```

**Why:** Need explicit `print()` after inner loop to move to next line.

### Mistake 4: Incorrect Loop Range for Indices

**Wrong:**
```python
matrix = [[1, 2, 3], [4, 5, 6]]
for i in range(len(matrix)):
    for j in range(len(matrix)):  # Wrong!
        print(matrix[i][j])
# IndexError when j >= 3 (row has only 3 elements)
```

**Correct:**
```python
matrix = [[1, 2, 3], [4, 5, 6]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):  # Correct
        print(matrix[i][j])
```

**Why:** Number of rows may differ from number of columns. Use `len(matrix[i])` for column count.

## Real-World Applications

### 1. **Image Processing**
Digital images are stored as 2D arrays (or 3D for color) where each element represents a pixel's color value. Photo editing software manipulates these matrices to apply filters, adjust brightness, or detect edges.

### 2. **Spreadsheet Applications**
Excel, Google Sheets, and other spreadsheet programs use 2D data structures to store and manipulate cell data. Each cell can be referenced by row and column, just like 2D lists.

### 3. **Game Development**
Board games (Chess, Checkers, Tic-Tac-Toe), tile-based games (Sudoku, Minesweeper), and level maps in video games use 2D grids to represent game state and player positions.

### 4. **Scientific Computing**
Matrices are fundamental in physics simulations, engineering calculations, machine learning (neural network weights), and data analysis. Libraries like NumPy build on 2D array concepts.

## Challenge Projects

### 1. **Conway's Game of Life**
Implement the classic cellular automaton where cells live or die based on their neighbors.

**Requirements:**
- Create a 20x20 grid of cells (0 = dead, 1 = alive)
- Implement the rules for cell birth/death
- Animate multiple generations
- Add patterns like gliders and oscillators

### 2. **Minesweeper Game**
Create a simplified version of Minesweeper with mine placement and number calculation.

**Requirements:**
- Generate random mine positions
- Calculate numbers showing adjacent mines
- Reveal cells when clicked
- Detect win/lose conditions

### 3. **Seat Reservation System**
Build a movie theater seat booking system using a 2D grid.

**Requirements:**
- Display seat availability (O = available, X = booked)
- Allow user to select row and seat
- Prevent double-booking
- Calculate total revenue
- Show most popular rows

### 4. **Image ASCII Art Generator**
Convert a simple 2D number matrix into ASCII art.

**Requirements:**
- Create brightness matrix (0-9 scale)
- Map numbers to ASCII characters
- Display the ASCII art
- Allow loading different patterns

### 5. **Sudoku Solver**
Create a program that validates and solves Sudoku puzzles.

**Requirements:**
- Represent 9x9 Sudoku board as 2D list
- Validate row, column, and 3x3 box constraints
- Implement backtracking algorithm to solve
- Display solution step-by-step

---

## Navigation

- **Previous:** [22. Shopping Cart Program](22-shopping-cart.md)
- **Next:** [24. Quiz Game](24-quiz-game.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Lists store multiple items in a single variable
2. Use loops to repeat actions
3. Follow along with the video for hands-on practice

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
