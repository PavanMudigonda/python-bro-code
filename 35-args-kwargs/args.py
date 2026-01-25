# ============================================
# CHAPTER 34: *ARGS (Arbitrary Arguments)
# ============================================
# *args = Allows you to pass multiple non-keyword arguments
# **kwargs = Allows you to pass multiple keyword arguments
#          * = unpacking operator
#
# Argument Order (IMPORTANT):
# 1. Positional arguments
# 2. Default arguments
# 3. Keyword arguments
# 4. ARBITRARY arguments (*args, **kwargs)
#
# Key Concepts:
# - *args collects extra positional arguments into a tuple
# - Useful when you don't know how many arguments will be passed
# - The name 'args' is convention, * is what matters
# - args becomes a tuple inside the function

# =============================================
# TRADITIONAL FUNCTION (Limited Arguments)
# =============================================
# This function only accepts exactly 2 arguments
# def add(a, b):
#     return a + b
# Problem: Can't add 3, 4, or more numbers!

# =============================================
# FUNCTION WITH *ARGS (Unlimited Arguments)
# =============================================
def add(*args):
    """
    Add any number of values together.
    
    Parameters:
        *args: Variable number of numeric arguments
    
    Returns:
        Sum of all arguments
    """
    # Method 1: Using a loop
    total = 0
    for arg in args:  # args is a tuple of all passed values
        total += arg
    
    # Method 2: Using built-in sum() function
    # More Pythonic and concise
    return sum(args)

# =============================================
# UNDERSTANDING *ARGS TYPE
# =============================================
# Uncomment to see that args is a tuple
# def add(*args):
#     print(type(args))  # Output: <class 'tuple'>
#     for arg in args:
#         total += arg
#     return total

# =============================================
# CALLING FUNCTION WITH VARIABLE ARGUMENTS
# =============================================
# Can pass any number of arguments!
print(add(1, 2))  # Output: 3
# print(add(1, 2, 3))  # Output: 6
# print(add(1, 2, 3, 4, 5))  # Output: 15
# print(add(10, 20, 30, 40, 50, 60))  # Output: 210



