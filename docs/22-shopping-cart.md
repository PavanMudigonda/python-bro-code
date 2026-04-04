# Chapter 22: Shopping Cart

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/22-shopping-cart/22-shopping-cart.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/22-shopping-cart/22-shopping-cart.ipynb)


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/22-shopping-cart/22-shopping-cart.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/22-shopping-cart/22-shopping-cart.ipynb)

# 🛒 Shopping Cart Program

## 📺 Video Tutorial

**Python shopping cart program 🛒** (9:12)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/kbyHLU9JqjE)

## What You'll Learn

In this chapter, you'll build a practical shopping cart program that demonstrates how to use parallel lists to store related data, collect user input in a loop, and format output professionally. This project brings together list manipulation, user input validation, and receipt generation.

## Learning Objectives

- Build a complete shopping cart system using parallel lists
- Implement input loops with break conditions
- Store and manipulate related data across multiple lists
- Calculate running totals from list data
- Format professional-looking receipts with string formatting
- Master list indexing and range-based iteration

## Concept Explanation

### What is a Shopping Cart Program?

A shopping cart program simulates a simple point-of-sale system where users can add items with prices, and the program generates a receipt showing all items and the total cost. This is a practical application that combines several fundamental programming concepts.

### Parallel Lists

**Parallel lists** are two or more lists where elements at the same index are related to each other. In our shopping cart:

```python
foods = ["Apple", "Banana", "Cherry"]
prices = [1.50, 0.75, 2.25]
# foods[0] and prices[0] are related
# foods[1] and prices[1] are related
# foods[2] and prices[2] are related
```

The key principle: **corresponding indices represent related data**.

### Key Components

#### 1. **Input Loop with Sentinel Value**
Uses a while loop that continues until user enters a quit signal ('q'):

```python
while True:
    food = input("Enter a food item (or 'q' to quit): ")
    if food.lower() == "q":
        break
    # Process the input
```

#### 2. **Parallel List Management**
Maintains two lists that grow together:

```python
foods.append(food)
prices.append(price)
```

#### 3. **Receipt Generation**
Uses range(len()) pattern to iterate through parallel lists:

```python
for i in range(len(foods)):
    print(f"{foods[i]} ${prices[i]}")
```

#### 4. **String Formatting for Alignment**
Creates professional output with proper spacing:

```python
print(f"{foods[i]:<20} ${prices[i]:>6.2f}")
# :<20  = left-align in 20 characters
# :>6.2f = right-align in 6 chars, 2 decimal places
```

### Why Use Parallel Lists?

While dictionaries might seem more appropriate (and they are for more complex programs), parallel lists teach important concepts:

1. **Index synchronization** - Understanding how to keep related data aligned
2. **List manipulation** - Working with multiple lists simultaneously
3. **Range iteration** - Using indices to access multiple lists
4. **Foundation concepts** - Prepares you for more advanced data structures

### Program Flow

1. **Initialize** empty lists and total variable
2. **Input Loop** - collect items and prices from user
3. **Validation** - check for quit condition
4. **Storage** - append to both lists maintaining parallel structure
5. **Display** - loop through lists to show receipt
6. **Calculate** - accumulate total from prices list

## Examples

### Example 1: Basic Parallel Lists
```python
# Creating parallel lists for shopping cart
foods = []
prices = []

# Adding items
foods.append("Apple")
prices.append(1.50)

foods.append("Banana")
prices.append(0.75)

# Accessing related data
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]}")
# Output:
# Apple: $1.5
# Banana: $0.75
```

### Example 2: Input Loop with Break
```python
# Collecting items until user quits
items = []

while True:
    item = input("Enter item (or 'q' to quit): ")
    if item.lower() == "q":
        break
    items.append(item)
    
print(f"You entered {len(items)} items")
```

### Example 3: Calculating Total
```python
prices = [10.50, 25.00, 15.75, 8.25]

# Method 1: Using a loop
total = 0
for price in prices:
    total += price
print(f"Total: ${total}")  # Total: $59.5

# Method 2: Using sum()
total = sum(prices)
print(f"Total: ${total}")  # Total: $59.5
```

### Example 4: String Formatting for Receipts
```python
# Left-aligned item names, right-aligned prices
items = ["Coffee", "Sandwich", "Cookie"]
prices = [3.50, 8.95, 2.25]

print("=" * 30)
for i in range(len(items)):
    print(f"{items[i]:<20} ${prices[i]:>6.2f}")
print("=" * 30)
# Output:
# ==============================
# Coffee               $  3.50
# Sandwich             $  8.95
# Cookie               $  2.25
# ==============================
```

### Example 5: Input Validation
```python
# Ensuring valid price input
while True:
    try:
        price = float(input("Enter price: $"))
        if price < 0:
            print("Price cannot be negative!")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")
```

### Example 6: Enhanced Receipt with Item Numbers
```python
foods = ["Pizza", "Burger", "Fries"]
prices = [12.99, 8.50, 3.99]

print("   YOUR ORDER")
print("=" * 35)

for i in range(len(foods)):
    # Add 1 to index for human-readable numbering
    print(f"{i + 1}. {foods[i]:<20} ${prices[i]:>6.2f}")
    
print("=" * 35)
# Output:
#    YOUR ORDER
# ===================================
# 1. Pizza                $  12.99
# 2. Burger               $   8.50
# 3. Fries                $   3.99
# ===================================
```

### Example 7: Complete Mini Shopping Cart
```python
# Complete shopping cart with all features
cart_items = []
cart_prices = []
total = 0

print("Welcome to Mini Mart!")

while True:
    item = input("\nItem name (or 'done'): ")
    if item.lower() == "done":
        break
        
    try:
        price = float(input(f"Price for {item}: $"))
        cart_items.append(item)
        cart_prices.append(price)
    except ValueError:
        print("Invalid price! Item not added.")

# Display receipt
print("\n" + "=" * 40)
print("           RECEIPT")
print("=" * 40)

for i in range(len(cart_items)):
    print(f"{i+1}. {cart_items[i]:<25} ${cart_prices[i]:>7.2f}")
    total += cart_prices[i]

print("=" * 40)
print(f"{'TOTAL':<27} ${total:>7.2f}")
print("=" * 40)
print("Thank you for shopping!\n")
```

## Practice Exercises

### Beginner Level

1. **Simple Cart**: Create a program that stores 3 items and their prices in parallel lists, then displays them with total.

2. **Fixed Menu**: Create lists of 5 pre-defined items with prices, display them, and let user select by number (1-5).

3. **Item Counter**: Modify the shopping cart to display how many items were added before showing the receipt.

4. **Average Price**: Calculate and display the average price of all items in the cart.

5. **Price Formatter**: Practice string formatting by displaying 10 different prices aligned properly.

### Intermediate Level

6. **Quantity Tracker**: Add a third parallel list to track quantities. Update total calculation to multiply price by quantity.

7. **Remove Item**: Add functionality to remove an item from the cart by name before checkout.

8. **Price Range Filter**: After checkout, display only items within a specified price range.

9. **Most Expensive Item**: Find and display the most expensive item in the cart.

10. **Discount Calculator**: Apply a 10% discount to the total if it exceeds $50.

### Advanced Level

11. **Tax Calculator**: Add sales tax calculation (e.g., 8%) to the final total and display both subtotal and total with tax.

12. **Multiple Carts**: Allow user to create multiple shopping carts (using lists of lists) and compare totals.

13. **Edit Item**: Add functionality to modify an existing item's name or price before checkout.

14. **Receipt Export**: Save the receipt to a text file with timestamp and cart details.

15. **Inventory System**: Start with a predefined inventory (items and stock levels) and decrease stock when items are added to cart. Prevent adding out-of-stock items.

## Common Mistakes to Avoid

### Mistake 1: Forgetting to Convert Price to Float

**Wrong:**
```python
price = input("Enter price: $")
prices.append(price)  # Stored as string!
total += prices[i]    # Error: can't add strings
```

**Correct:**
```python
price = float(input("Enter price: $"))
prices.append(price)  # Stored as float
total += prices[i]    # Works correctly
```

**Why:** Input always returns a string. Must convert to float for mathematical operations.

### Mistake 2: Misaligned Parallel Lists

**Wrong:**
```python
foods.append(food)
if price > 0:  # Conditional append!
    prices.append(price)
# Now lists are different lengths!
```

**Correct:**
```python
if price > 0:
    foods.append(food)
    prices.append(price)
# Both lists grow together
```

**Why:** Parallel lists must maintain the same length with corresponding indices.

### Mistake 3: Incorrect Range Usage

**Wrong:**
```python
for i in range(len(foods) + 1):  # Off by one!
    print(foods[i])  # IndexError on last iteration
```

**Correct:**
```python
for i in range(len(foods)):
    print(foods[i])  # Correct indexing
```

**Why:** Lists are 0-indexed. If len(foods) is 3, valid indices are 0, 1, 2.

### Mistake 4: Not Formatting Decimal Places

**Wrong:**
```python
print(f"Total: ${total}")  # Displays: $10.5
```

**Correct:**
```python
print(f"Total: ${total:.2f}")  # Displays: $10.50
```

**Why:** Money should always display 2 decimal places for professionalism and clarity.

## Real-World Applications

### 1. **E-Commerce Checkout Systems**
Online shopping carts that track items, quantities, and prices before final purchase. Amazon, eBay, and all e-commerce platforms use sophisticated versions of this concept.

### 2. **Restaurant POS Systems**
Point-of-sale terminals in restaurants use similar logic to track orders, items, and prices before generating a bill. The parallel list concept scales to include modifiers, special requests, and table numbers.

### 3. **Expense Tracking Apps**
Personal finance apps track expenses by category and amount, then generate reports and totals. This is essentially a shopping cart for tracking spending.

### 4. **Inventory Management**
Retail stores use parallel data structures to track product names, SKUs, quantities, prices, and locations. When items are sold, these lists are updated together.

## Challenge Projects

### 1. **Multi-User Shopping Cart**
Create a system that supports multiple users, each with their own cart. Use a dictionary where keys are usernames and values are lists of lists (cart data).

**Requirements:**
- User login/registration
- Each user has separate cart
- Display all users' totals at the end
- Find user who spent the most

### 2. **Smart Grocery List**
Build a shopping cart that suggests items based on previous purchases and warns about duplicate entries.

**Requirements:**
- Store purchase history
- Suggest frequently bought items
- Warn if adding duplicate items
- Calculate savings compared to regular price

### 3. **Receipt Generator with Barcode**
Create a detailed receipt system with item codes, taxes, and discounts.

**Requirements:**
- Generate unique item codes
- Calculate multiple tax rates
- Apply discount codes
- Export to formatted text file

### 4. **Budget-Aware Shopping Cart**
Implement a cart that helps users stay within budget by tracking spending in real-time.

**Requirements:**
- Set initial budget
- Show remaining budget after each item
- Warn when approaching budget limit
- Suggest items to remove if over budget

### 5. **Comparison Shopping Tool**
Create a program that compares prices across multiple stores for the same items.

**Requirements:**
- Store prices from 3 different stores
- Calculate total for each store
- Recommend cheapest store
- Calculate savings by shopping at cheapest store

---

## Navigation

- **Previous:** [21. Lists](21-lists.md)
- **Next:** [23. 2D Collections](23-2d-collections.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Lists store multiple items in a single variable
2. Use loops to repeat actions
3. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
