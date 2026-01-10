# ============================================
# CHAPTER 26: CONCESSION STAND PROGRAM
# ============================================
# A practical program demonstrating:
# - Dictionary usage for menu items and prices
# - Shopping cart implementation with list
# - User input validation and menu navigation
# - Price formatting and total calculation
#
# Key Concepts:
# - Dictionaries for key-value storage (item: price)
# - Lists for collecting user selections
# - String formatting for aligned output
# - Input validation and error handling

# =============================================
# MENU SETUP
# =============================================
# Dictionary stores menu items (keys) and prices (values)
# Prices stored as strings but converted to float for calculations
menu = {"pizza": "3.0",
        "nachos": "4.5",
        "popcorn": "6.0",
        "fries": "2.50",
        "chips": "1.00",
        "pretzel": "3.00",
        "soda": "3.00",
        "lemonade": "4.25",                                
        }

# =============================================
# INITIALIZE SHOPPING CART AND TOTAL
# =============================================
# List to store items selected by user
cart = []

# Running total of all items in cart
total = 0

# =============================================
# DISPLAY MENU
# =============================================
print("----------MENU-------------")

# items() returns both keys and values from dictionary
# String formatting: {key:10} left-aligns item name in 10 characters
# {float(value):.2f} converts to float and formats to 2 decimal places
for key,value in menu.items():
    print(f'{key:10}: ${float(value):.2f}')
    
print("---------------------------")

# =============================================
# ORDER LOOP - Get user selections
# =============================================
while True:
    # Get user input and convert to lowercase for comparison
    food = input("Select an item to buy (q to quit):  ".lower())
    
    # Check if user wants to quit
    if food == "q":
        break
    # Validate that item exists in menu
    # get() returns None if key doesn't exist
    elif menu.get(food) is not None:
        cart.append(food)  # Add valid item to cart

# Display all items in cart
print(cart)

# =============================================
# CALCULATE TOTAL AND DISPLAY RECEIPT
# =============================================
# Loop through cart items to calculate total
for food in cart:
    # Add price of each item to running total
    total += float(menu.get(food))
    
    # Print item name with space (no newline)
    print(food, end=" ")

print()  # Print newline after all items

# Display final total with 2 decimal places
print(f'total: {total}')