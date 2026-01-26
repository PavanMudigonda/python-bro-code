# ============================================
# Chapter 7: If-Elif-Else Statements
# ============================================
# Conditional statements allow your program to make decisions
# based on different conditions

# Get user's age
age = int(input("Enter your age: "))

# ============================================
# If-Elif-Else Chain
# ============================================
# Python evaluates conditions from top to bottom
# Once a condition is True, it executes that block and skips the rest

# Check if age is 100 or greater
if age >= 100:
    print("You are too old to sign up.")
# Check if age is 0 or less (invalid age)
elif age <= 0:
    print("You are not born yet.")
# Check if age is exactly 17
elif age == 17:
    print("You are 17 years old, you can sign up next year.")
# Check if age is 18 or greater
elif age >= 18:
    print("You are now signed up")
# If none of the above conditions are true (age is 1-16)
else:
    print("You are a minor therefore not eligible to sign up.")

# ============================================
# Comparison Operators:
# ============================================
# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)