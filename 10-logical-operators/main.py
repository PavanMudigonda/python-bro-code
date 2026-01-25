# ============================================
# Chapter 11: Logical Operators
# ============================================
# Logical operators combine multiple conditions
# Three main logical operators: and, or, not

# Get temperature from user
temp = float(input("What is the temperature outside? "))

# Set weather condition (you can change this to False to test other conditions)
is_sunny = True

# ============================================
# AND operator - Both conditions must be True
# ============================================
if temp > 20 and is_sunny:
    # True only if temperature > 20 AND it's sunny
    print("Don't forget your sunscreen!")

# ============================================
# AND operator - checking different combination
# ============================================
elif temp <= 20 and is_sunny:
    # True only if temperature <= 20 AND it's sunny
    print("Wear a hat!")

# ============================================
# NOT operator - Reverses the boolean value
# ============================================
elif temp > 20 and not is_sunny:
    # True only if temperature > 20 AND it's NOT sunny (cloudy/rainy)
    print("Take an umbrella!")

# ============================================
# Else - None of the above conditions are true
# ============================================
else:
    # This runs if: temp <= 20 and not sunny
    print("Stay home!")

# ============================================
# Logical Operators Summary:
# ============================================
# and  → Both conditions must be True
# or   → At least one condition must be True
# not  → Reverses the boolean value