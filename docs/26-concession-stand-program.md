# 🍿 Concession Stand Program

## 📺 Video Tutorial

**Python concession stand program 🍿** (10:46)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/PbkIzW_70EI)

## What You'll Learn

In this chapter, you'll build a practical concession stand ordering system that demonstrates real-world application of dictionaries. You'll learn to create interactive menu systems, manage shopping carts, calculate totals, and format professional output using dictionary data structures.

## Learning Objectives

- Apply dictionaries to solve practical business problems
- Create menu systems with item-price mappings
- Implement shopping cart functionality using lists and dictionaries
- Validate user input against dictionary keys
- Calculate totals from dictionary values
- Format output for professional presentation

## Concept Explanation

### What is a Concession Stand Program?

A concession stand program simulates a food ordering system like those found at movie theaters, sports stadiums, or cafeterias. Users can view a menu, select items, and receive a total price. This project demonstrates how dictionaries excel at storing structured data with meaningful keys.

### Why Dictionaries for Menus?

Dictionaries are perfect for menus because:

1. **Natural Mapping** - Items naturally map to prices
2. **Easy Lookup** - Check if item exists and get price in one operation
3. **Readable Code** - `menu["pizza"]` is clearer than `menu[0]`
4. **Easy Updates** - Add, remove, or change prices easily
5. **Validation** - Built-in membership testing with `in` operator

```python
# Dictionary is perfect for this
menu = {"pizza": 3.00, "hotdog": 2.50, "popcorn": 4.00}

# vs parallel lists (confusing and error-prone)
items = ["pizza", "hotdog", "popcorn"]
prices = [3.00, 2.50, 4.00]
```

### Program Components

#### 1. **Menu Dictionary**
The core data structure storing items and prices:

```python
menu = {
    "pizza": "3.0",      # Item name (key) → Price (value)
    "nachos": "4.5",
    "popcorn": "6.0"
}
```

#### 2. **Shopping Cart**
A list to accumulate user selections:

```python
cart = []  # Stores item names selected by user
cart.append("pizza")
cart.append("popcorn")
```

#### 3. **Input Validation**
Check if user's selection exists in menu:

```python
food = input("Select item: ").lower()
if menu.get(food) is not None:  # Item exists
    cart.append(food)
else:
    print("Item not available")
```

#### 4. **Total Calculation**
Sum up prices from cart items:

```python
total = 0
for item in cart:
    total += float(menu.get(item))
```

### Key Patterns

#### Dictionary Iteration
```python
# Loop through both keys and values
for item, price in menu.items():
    print(f"{item}: ${price}")
```

#### Safe Key Access
```python
# get() returns None if key doesn't exist
price = menu.get("pizza")  # Safe

# vs direct access (raises KeyError if missing)
# price = menu["pizza"]  # Unsafe
```

#### String to Float Conversion
```python
# Prices stored as strings in dictionary
menu = {"pizza": "3.00"}

# Convert when calculating
total = float(menu.get("pizza"))  # "3.00" → 3.0
```

### Program Flow

1. **Display Menu** - Show all items and prices
2. **Input Loop** - Collect user selections
3. **Validation** - Check if item exists in menu
4. **Storage** - Add valid items to cart
5. **Exit Condition** - User enters 'q' to quit
6. **Calculation** - Sum prices of cart items
7. **Display** - Show cart and total

### String Formatting for Menus

Professional menu display using f-strings:

```python
for item, price in menu.items():
    print(f"{item:10}: ${float(price):.2f}")
    # item:10 - left align in 10 characters
    # :.2f - 2 decimal places for price
```

## Examples

### Example 1: Basic Menu Dictionary
```python
# Create menu with items and prices
menu = {
    "burger": 5.99,
    "fries": 2.99,
    "soda": 1.99,
    "shake": 3.99
}

# Display menu
print("--- MENU ---")
for item, price in menu.items():
    print(f"{item.title()}: ${price:.2f}")

# Output:
# --- MENU ---
# Burger: $5.99
# Fries: $2.99
# Soda: $1.99
# Shake: $3.99
```

### Example 2: Adding Items to Cart
```python
menu = {"pizza": 3.00, "hotdog": 2.50, "soda": 1.50}
cart = []

# Simulate user selections
selections = ["pizza", "soda", "pizza"]

for selection in selections:
    if selection in menu:
        cart.append(selection)
        print(f"Added {selection} to cart")
    else:
        print(f"{selection} not available")

print(f"Cart: {cart}")
# Output:
# Added pizza to cart
# Added soda to cart
# Added pizza to cart
# Cart: ['pizza', 'soda', 'pizza']
```

### Example 3: Calculating Total
```python
menu = {"pizza": 3.00, "hotdog": 2.50, "soda": 1.50}
cart = ["pizza", "soda", "pizza"]

total = 0
print("\n--- YOUR ORDER ---")
for item in cart:
    price = menu[item]
    print(f"{item.title()}: ${price:.2f}")
    total += price

print(f"\nTotal: ${total:.2f}")

# Output:
# --- YOUR ORDER ---
# Pizza: $3.00
# Soda: $1.50
# Pizza: $3.00
#
# Total: $7.50
```

### Example 4: Input Validation
```python
menu = {"pizza": 3.00, "burger": 5.00}

# Get user input
item = input("Enter item: ").lower()

# Validate using 'in' operator
if item in menu:
    print(f"{item} costs ${menu[item]:.2f}")
else:
    print(f"Sorry, {item} is not on the menu")

# Safe access using get()
price = menu.get(item)
if price is not None:
    print(f"Price: ${price:.2f}")
else:
    print("Item not found")
```

### Example 5: Formatted Menu Display
```python
menu = {
    "pizza": 3.0,
    "nachos": 4.5,
    "popcorn": 6.0,
    "fries": 2.5,
    "chips": 1.0
}

print("=" * 30)
print("      CONCESSION STAND")
print("=" * 30)

for item, price in menu.items():
    # Left-align item in 15 chars, right-align price
    print(f"{item.capitalize():15} ${price:>5.2f}")

print("=" * 30)

# Output:
# ==============================
#       CONCESSION STAND
# ==============================
# Pizza           $ 3.00
# Nachos          $ 4.50
# Popcorn         $ 6.00
# Fries           $ 2.50
# Chips           $ 1.00
# ==============================
```

### Example 6: Complete Simple Version
```python
# Menu setup
menu = {
    "popcorn": 5.00,
    "candy": 2.50,
    "soda": 3.00,
    "pretzel": 4.00
}

cart = []
total = 0

# Display menu
print("\n--- SNACK BAR MENU ---")
for item, price in menu.items():
    print(f"{item.title():12} ${price:.2f}")

print("\nEnter items (or 'done' to checkout):")

# Collect orders
while True:
    choice = input("> ").lower()
    
    if choice == "done":
        break
    
    if choice in menu:
        cart.append(choice)
        print(f"Added {choice}")
    else:
        print("Item not available")

# Calculate and display total
if cart:
    print("\n--- YOUR ORDER ---")
    for item in cart:
        print(f"{item.title():12} ${menu[item]:.2f}")
        total += menu[item]
    
    print("-" * 20)
    print(f"{'Total:':12} ${total:.2f}")
else:
    print("No items ordered")
```

### Example 7: Enhanced with Quantity Tracking
```python
menu = {"pizza": 3.00, "hotdog": 2.50, "soda": 1.50}

# Use dictionary to track quantities
cart = {}  # {item: quantity}

print("--- MENU ---")
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

while True:
    item = input("\nItem (or 'q' to quit): ").lower()
    
    if item == 'q':
        break
    
    if item in menu:
        # Increment quantity or set to 1
        cart[item] = cart.get(item, 0) + 1
        print(f"Added {item} (qty: {cart[item]})")
    else:
        print("Not available")

# Display receipt with quantities
print("\n--- RECEIPT ---")
total = 0

for item, qty in cart.items():
    price = menu[item]
    subtotal = price * qty
    total += subtotal
    print(f"{item} x{qty:2} @ ${price:.2f} = ${subtotal:.2f}")

print(f"\nTotal: ${total:.2f}")
```

## Practice Exercises

### Beginner Level

1. **Fixed Order**: Create a menu dictionary and a pre-defined cart. Calculate and display the total.

2. **Single Item**: Let user order one item from the menu. Display the price and thank them.

3. **Menu Display**: Practice formatting by displaying a menu with 5 items in a professional format.

4. **Price Check**: Let user enter an item name and display its price if it exists.

5. **Item Count**: After building a cart, display how many items were ordered.

### Intermediate Level

6. **Quantity Support**: Modify the program to ask for quantity when adding items. Calculate total correctly.

7. **Remove Items**: Add functionality to remove items from cart before checkout.

8. **Category Menus**: Create separate menus for "Food" and "Drinks". Let user choose category first.

9. **Discount System**: Apply 10% discount if total exceeds $20.

10. **Most Expensive Item**: After checkout, display which item in the cart was most expensive.

### Advanced Level

11. **Tax Calculation**: Add sales tax calculation (configurable rate) to the final total. Show subtotal, tax, and grand total.

12. **Special Offers**: Implement "Buy 2 Get 1 Free" promotions for specific items.

13. **Combo Meals**: Create combo deals (e.g., "burger + fries + soda = $7.99"). Detect when user orders combo components.

14. **Receipt Export**: Generate a formatted text file receipt with timestamp and order details.

15. **Inventory Management**: Add stock levels to menu. Prevent ordering out-of-stock items and update stock after each purchase.

## Common Mistakes to Avoid

### Mistake 1: Not Converting String Prices to Float

**Wrong:**
```python
menu = {"pizza": "3.00"}  # String price
total = 0
total += menu["pizza"]  # TypeError: can only concatenate str!
```

**Correct:**
```python
menu = {"pizza": "3.00"}  # String price
total = 0
total += float(menu["pizza"])  # Convert to float first
# Or store as float initially
menu = {"pizza": 3.00}
```

**Why:** String prices must be converted to numbers for mathematical operations.

### Mistake 2: Case Sensitivity Issues

**Wrong:**
```python
menu = {"Pizza": 3.00, "Burger": 5.00}
choice = input("Item: ")  # User enters "pizza"
if choice in menu:  # "pizza" != "Pizza"
    print("Found")  # Won't execute
```

**Correct:**
```python
menu = {"pizza": 3.00, "burger": 5.00}  # Lowercase keys
choice = input("Item: ").lower()  # Convert input to lowercase
if choice in menu:
    print("Found")
```

**Why:** Dictionary keys are case-sensitive. Normalize both keys and input to lowercase.

### Mistake 3: Using Direct Access Instead of get()

**Wrong:**
```python
menu = {"pizza": 3.00}
item = "burger"
price = menu[item]  # KeyError: 'burger'
```

**Correct:**
```python
menu = {"pizza": 3.00}
item = "burger"
price = menu.get(item)  # Returns None, no error

# Or check first
if item in menu:
    price = menu[item]
```

**Why:** Direct bracket access raises KeyError for non-existent keys. Use get() for safe access.

### Mistake 4: Forgetting to Format Currency

**Wrong:**
```python
total = 10.5
print(f"Total: ${total}")  # $10.5 (missing zero)
```

**Correct:**
```python
total = 10.5
print(f"Total: ${total:.2f}")  # $10.50 (always 2 decimals)
```

**Why:** Currency should always display exactly 2 decimal places for professionalism.

## Real-World Applications

### 1. **Point of Sale (POS) Systems**
Retail stores, restaurants, and cafeterias use POS systems that map products to prices, track orders, apply discounts, and calculate totals - exactly like this concession stand program.

### 2. **E-Commerce Shopping Carts**
Online shopping platforms like Amazon use sophisticated versions of cart systems that track items, quantities, prices, apply promotions, and calculate shipping and tax.

### 3. **Food Delivery Apps**
Apps like Uber Eats, DoorDash, and GrubHub use menu dictionaries to display restaurant items, manage carts, calculate subtotals, and process orders.

### 4. **Vending Machines**
Modern vending machines use similar logic to display products with codes, validate selections, calculate change, and track inventory levels.

## Challenge Projects

### 1. **Full Restaurant Ordering System**
Create a comprehensive restaurant order system with multiple menus and features.

**Requirements:**
- Multiple menu categories (appetizers, entrees, desserts, drinks)
- Quantity and size options (small/medium/large)
- Special instructions for items
- Calculate tax and optional tip
- Generate itemized receipt

### 2. **Movie Theater Concession Stand**
Build a realistic movie theater snack bar system.

**Requirements:**
- Combo deals (popcorn + soda = discount)
- Size upgrades (small/medium/large)
- Loyalty points system
- Track inventory levels
- Generate sales reports

### 3. **Coffee Shop POS System**
Create a coffee shop ordering system with customizations.

**Requirements:**
- Base drinks with customization options (milk type, size, extras)
- Add-ons with additional charges (shot of espresso, whipped cream)
- Save favorite orders
- Calculate totals with tax
- Receipt printing with order number

### 4. **Food Truck Menu Manager**
Build a system for a food truck with daily menu changes.

**Requirements:**
- Load menu from file (allow daily updates)
- Mark items as "sold out"
- Track sales by item
- Calculate daily revenue
- Generate top-selling items report

### 5. **Campus Cafeteria System**
Create a meal plan system for university dining halls.

**Requirements:**
- Student meal plan accounts (prepaid balance)
- Deduct from balance when ordering
- Different pricing for students vs guests
- Nutritional information display
- Weekly spending reports

---

## Navigation

- **Previous:** [25. Dictionaries](25-dictionaries.md)
- **Next:** [27. Random Numbers](27-random-numbers.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Dictionaries store data in key-value pairs
2. Use loops to repeat actions
3. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
