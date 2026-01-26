# ============================================
# Chapter 10: Temperature Converter Program
# ============================================
# This program converts temperature between Fahrenheit and Celsius
# In the US, temperature is measured in Fahrenheit (°F)
# In most other countries (including Canada), it's measured in Celsius (°C)

# ============================================
# Conversion Formulas:
# ============================================
# Celsius to Fahrenheit: F = (C × 9/5) + 32
# Fahrenheit to Celsius: C = (F - 32) × 5/9

# Step 1: Ask user for the current unit of their temperature
unit = input("Enter the unit of temperature (F/C): ")

# Step 2: Get the temperature value
temp = float(input("Enter the temperature: "))

# Step 3: Convert based on the unit
if unit == "F" or unit == "f":
    # Convert Fahrenheit to Celsius
    # Formula: (F - 32) * 5/9 = C
    temp = ((temp - 32) * 5.0 / 9.0)
    print(f'The temperature in Celsius is: {temp:.2f} °C')
elif unit == "C" or unit == "c":
    # Convert Celsius to Fahrenheit
    # Formula: (C * 9/5) + 32 = F
    temp = ((temp * 9.0 / 5.0) + 32)
    print(f'The temperature in Fahrenheit is: {temp:.2f} °F')
else:
    # Invalid unit entered
    print(f'Invalid unit: {unit}. Please enter F or C.')

# ============================================
# How this program works:
# ============================================
# 1. User specifies the current unit (F or C)
# 2. User enters the temperature value
# 3. Program determines which conversion to perform
# 4. Applies the appropriate formula
# 5. Displays the converted temperature
#
# Note: We use 5.0 and 9.0 (floats) to ensure decimal division