# ============================================
# CHAPTER 39: MODULES
# ============================================
# main.py - Main program file that imports and uses a custom module
#
# Module = A file containing Python code you want to include in your program
#          Use 'import' to include a module (built-in or your own)
#
# Benefits of Modules:
# - Code organization - break up large programs into manageable files
# - Reusability - use same code in multiple programs
# - Namespace separation - avoid name conflicts
# - Easier maintenance - update code in one place
#
# Types of Modules:
# - Built-in modules (math, random, datetime, etc.)
# - Third-party modules (requests, numpy, pandas, etc.)
# - Your own custom modules (like example.py)
#
# Import Syntax:
# - import module_name          (import entire module)
# - from module_name import x   (import specific item)
# - import module_name as alias (import with alias)

# =============================================
# IMPORT CUSTOM MODULE
# =============================================
# Import our custom 'example' module (example.py must be in same directory)
# This makes all functions and variables from example.py available
import example

# =============================================
# ACCESS MODULE VARIABLES
# =============================================
# Access the 'pi' variable from the example module
# Use module_name.variable_name syntax
result = example.pi
print(result)  # Output: 3.14159...

# =============================================
# CALL MODULE FUNCTIONS
# =============================================
# Use module_name.function_name() to call functions

# Calculate square using example.square() function
square_value = example.square(3)
print(f"square value: {square_value}")  # Output: 9

# Calculate cube using example.cube() function
cube_value = example.cube(3)
print(f"cube value: {cube_value}")  # Output: 27

# Calculate circumference using example.circumference() function
circumference_value = example.circumference(3)
print(f"circumference value: {circumference_value}")  # Output: 18.84...

# Calculate area using example.area() function
area_value = example.area(4)
print(f"area value: {area_value}")  # Output: 50.26...

# =============================================
# ALTERNATIVE IMPORT METHODS
# =============================================
# Import specific items only:
# from example import pi, square, cube
# square_value = square(3)  # No need for example. prefix

# Import with alias:
# import example as ex
# result = ex.pi  # Use alias instead of full name

# Import everything (not recommended):
# from example import *
# square_value = square(3)  # Direct access, but can cause naming conflicts