# ============================================
# CHAPTER 40: SCOPE RESOLUTION
# ============================================
# Variable Scope = Where a variable is visible and accessible
# Scope Resolution = The order in which Python looks for a variable
#
# LEGB Rule (order Python searches for variables):
# 1. L - Local:     Variables inside current function
# 2. E - Enclosing: Variables in enclosing functions (nested functions)
# 3. G - Global:    Variables at module level (top of file)
# 4. B - Built-in:  Python's built-in names (print, len, etc.)
#
# Key Concepts:
# - Local variables only exist inside their function
# - Each function has its own local scope
# - Variables are searched from innermost to outermost scope
# - Local variables shadow (hide) outer variables with same name
# - Use 'global' keyword to modify global variables from functions

# =============================================
# EXAMPLE: INDEPENDENT LOCAL SCOPES
# =============================================

def func1():
    """
    Function with its own local variable x.
    This x only exists inside func1.
    """
    x = 10  # Local scope - only visible inside func1
    print("Inside func1, x =", x)  # Output: 10

def func2():
    """
    Function with its own local variable x.
    This is a different x than in func1!
    """
    x = 20  # Local scope - only visible inside func2
    # This x is completely separate from func1's x
    print("Inside func2, x =", x)  # Output: 20

# =============================================
# FUNCTION CALLS
# =============================================
func1()  # Output: Inside func1, x = 10
func2()  # Output: Inside func2, x = 20

# Note: Each function has its own x variable
# They don't interfere with each other

# =============================================
# ADDITIONAL SCOPE EXAMPLES
# =============================================

# Global variable example:
# x = 100  # Global scope - accessible everywhere
# def func3():
#     print("Inside func3, x =", x)  # Accesses global x
# func3()  # Output: 100

# Modifying global variable:
# x = 100
# def func4():
#     global x  # Declare we want to use global x
#     x = 200   # Modifies the global x
# func4()
# print(x)  # Output: 200

# Enclosing scope example:
# def outer():
#     x = 10  # Enclosing scope for inner()
#     def inner():
#         print(x)  # Accesses x from enclosing scope
#     inner()
# outer()  # Output: 10