# ============================================
# CHAPTER 41: IF __NAME__ == "__MAIN__"
# ============================================
# app.py - Main application file demonstrating module import
#
# if __name__ == "__main__" Pattern:
# - Checks if a Python file is being run directly or imported as module
# - __name__ is a special variable:
#   * When run directly: __name__ = "__main__"
#   * When imported: __name__ = module name (e.g., "calculator")
#
# Why Use This Pattern:
# - Allows file to be both executable script AND importable module
# - Prevents code from running when module is imported
# - Enables code reusability
# - Professional Python best practice
#
# Two Ways to Import:
# 1. import module_name          (import entire module)
# 2. from module_name import *   (import everything directly)

# =============================================
# METHOD 1: IMPORT ENTIRE MODULE (Recommended)
# =============================================
# This imports the calculator module as an object
# Access functions using calculator.function_name()
import calculator

# Alternative import (commented out):
# from calculator import *
# This imports all functions directly (can cause naming conflicts)

# =============================================
# DIRECT FUNCTION CALLS
# =============================================
# Call functions using module_name.function_name() syntax
# This clearly shows where the function comes from

print(calculator.add(10, 5))        # ➝ 15
print(calculator.subtract(10, 5))   # ➝ 5
print(calculator.multiply(10, 5))   # ➝ 50
print(calculator.divide(10, 5))     # ➝ 2.0

# =============================================
# USING THE DISPATCHER FUNCTION
# =============================================
# The calculate() function acts as a dispatcher
# It takes an operator symbol and routes to the correct function
result = calculator.calculate('*', 7, 3)
print(result)  # ➝ 21

# =============================================
# KEY CONCEPTS DEMONSTRATED
# =============================================
# 1. Importing modules cleanly
# 2. Using module.function() syntax
# 3. Accessing functions from another file
# 4. Code organization and reusability
# 5. This file runs directly (no if __name__ check needed here)
