# ============================================
# Chapter 22: Shopping Cart Program
# ============================================
# This program creates a shopping cart where users can add items
# and prices, then displays a receipt with total

# ============================================
# Initialize empty lists for foods and prices
# ============================================
foods: list = []   # List to store food item names
prices: list = []  # List to store corresponding prices
total = 0          # Variable to track total cost

# ============================================
# Input loop - collect items from user
# ============================================
while True:
    # Get food item from user
    food = input("Enter a food item (or 'q' to quit): ")
    
    # Check if user wants to quit
    if food.lower() == "q" or food.lower() == "quit":
        break  # Exit the loop
    
    # Get price for the food item
    price = float(input(f"Enter the price for {food}: $"))
    
    # Add food and price to respective lists
    # Lists maintain parallel structure (same index = related items)
    foods.append(food)
    prices.append(price)

# ============================================
# Display receipt
# ============================================
print("\n" + "="*35)
print("   Pavan's Food Emporium")
print("="*35)

# ============================================
# Loop through items and calculate total
# ============================================
# range(len(foods)) creates indices: 0, 1, 2, ...
for i in range(len(foods)):
    # Display item number, name, and price
    print(f"{i + 1}. {foods[i]:<20} ${prices[i]:>6.2f}")
    # Add price to running total
    total += prices[i]

# ============================================
# Display total
# ============================================
print("="*35)
print(f"{'Total:':<21} ${total:>6.2f}")
print("="*35)
print("\nThank you for shopping!\n")

# ============================================
# Key Concepts:
# ============================================
# - Parallel lists: foods[i] and prices[i] are related
# - len() returns number of items in list
# - range(len(list)) generates indices for iteration
# - String formatting: {:<20} left-align, {:>6.2f} right-align with 2 decimals