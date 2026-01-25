# ============================================
# Chapter 9: Weight Converter Program
# ============================================
# This program converts weight between pounds (lbs) and kilograms (kg)

# ============================================
# Conversion Formula:
# ============================================
# 1 kg = 1000 grams
# 1 lb = 453.6 grams
# Therefore: 1 kg = 1000/453.6 lbs (approximately 2.20462 lbs)

# ============================================
# Method 1: Simple Conversion (Commented Out)
# ============================================
# weight = float(input("Enter your weight: "))
# unit = input("(L)bs or (K)g: ")

# if unit.upper() == "L":
#     # Convert pounds to kilograms
#     weight_kg = weight * 0.45  # Simplified: 1 lb ≈ 0.45 kg
#     print(f"You are {weight_kg} kilos")
# elif unit.upper() == "K":
#     # Convert kilograms to pounds
#     weight_lbs = weight / 0.45  # Simplified: 1 kg ≈ 2.2 lbs
#     print(f"You are {weight_lbs} pounds")
# else:
#     print(f'Invalid unit: {unit}')

# ============================================
# Method 2: More Accurate Conversion
# ============================================

# Step 1: Get weight value from user
weight = float(input("Enter your weight: "))

# Step 2: Get unit (Lbs or Kgs)
unit = str(input("Enter L for Lbs and K for Kgs: "))

# Step 3: Calculate conversion factor
# 1 kg = 1000 grams, 1 lb = 453.6 grams
# So: kg_to_lb_factor = 1000 / 453.6 = 2.20462
kg_to_lb_factor = 1000 / 453.6

print(f"kg_to_lb_factor: {kg_to_lb_factor}")

# Step 4: Convert based on user's unit choice
if unit.upper() == "L":
    # User entered weight in Pounds, convert to Kilograms
    weight = float(weight / kg_to_lb_factor)
    unit = "Kgs"
    print(f"Your weight in Kgs: {weight:.2f}")
elif unit.upper() == "K":
    # User entered weight in Kilograms, convert to Pounds
    weight = float(weight * kg_to_lb_factor)
    unit = "Lbs"
    print(f"Your weight in Lbs: {weight:.2f}")
else:
    # Invalid unit entered
    print("You have entered invalid unit for weight")

# ============================================
# How this program works:
# ============================================
# 1. User enters their weight as a number
# 2. User specifies unit: L for Pounds or K for Kilograms
# 3. Program calculates conversion factor (2.20462)
# 4. Program converts to the opposite unit
# 5. Displays the converted weight
#
# Note: .upper() converts input to uppercase, so 'l' and 'L' both work