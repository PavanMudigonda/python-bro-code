# ============================================
# Chapter 12: Conditional Expressions (Ternary Operator)
# ============================================
# Conditional Expression = A one-line shortcut for if-else statements
# Syntax: value_if_true if condition else value_if_false
# Also called: ternary operator or inline if

# Sample variables for demonstrations
num = 5
a = 6
b = 7
age = 13
temperature = 22
user_role = 'admin'

# ============================================
# Example 1: Simple Positive/Negative Check
# ============================================
# Traditional if-else would be:
# if num > 0:
#     print("positive")
# else:
#     print("non-positive")

# Ternary version (one line):
print("positive" if num > 0 else "non-positive")

# ============================================
# Example 2: Even or Odd Check
# ============================================
# Assign result based on condition
result = 'EVEN' if num % 2 == 0 else 'ODD'
print(result)

# ============================================
# Example 3: Finding Maximum Number
# ============================================
# Returns a if a > b, otherwise returns b
max_num = a if a > b else b
print(f'maximum number: {max_num}')

# ============================================
# Example 4: Finding Minimum Number
# ============================================
# Returns a if a < b, otherwise returns b
min_num = a if a < b else b
print(f'minimum number: {min_num}')

# ============================================
# Example 5: Access Level Based on Role
# ============================================
# Assign different access based on user role
access_level = 'Full Access' if user_role == 'admin' else 'Limited Access'
print(f'Access Level: {access_level}')

# ============================================
# When to use Conditional Expressions:
# ============================================
# ✓ Simple conditions with single-line results
# ✓ Variable assignments based on conditions
# ✓ When you want concise, readable code
# ✗ Complex conditions (use regular if-else instead)