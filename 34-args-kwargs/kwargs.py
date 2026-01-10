# ============================================
# CHAPTER 34: **KWARGS (Keyword Arguments)
# ============================================
# *args  = Allows you to pass multiple non-keyword arguments (as tuple)
# **kwargs = Allows you to pass multiple keyword arguments (as dictionary)
# * and ** are unpacking operators
#
# Argument Types in Order:
# 1. Positional arguments
# 2. Default arguments
# 3. Keyword arguments
# 4. Arbitrary arguments (*args, **kwargs)
#
# Key Concepts:
# - **kwargs collects keyword arguments into a dictionary
# - Useful for functions that accept many optional named parameters
# - The name 'kwargs' is convention, ** is what matters
# - kwargs becomes a dict inside the function (key-value pairs)
# - Perfect for configuration, settings, or flexible parameters

# =============================================
# FUNCTION WITH **KWARGS
# =============================================
def print_address(**kwargs):
    """
    Print address information with flexible named parameters.
    
    Parameters:
        **kwargs: Variable number of keyword arguments
                  Can include street, city, state, zip, country, etc.
    """
    # Show that kwargs is a dictionary
    print(type(kwargs))  # Output: <class 'dict'>
    
    # Iterate through all key-value pairs
    # .items() returns tuples of (key, value)
    for key, value in kwargs.items():
        print(f'{key}: {value}')

# =============================================
# CALLING FUNCTION WITH KEYWORD ARGUMENTS
# =============================================
# Can pass any number of named arguments!
# Order doesn't matter with keyword arguments
print_address(street="Front Street", 
              city="Toronto", 
              state="Ontario", 
              zip="M5V3A4")

# Output:
# <class 'dict'>
# street: Front Street
# city: Toronto
# state: Ontario
# zip: M5V3A4

# =============================================
# FLEXIBILITY OF **KWARGS
# =============================================
# Can include different fields in different calls
# print_address(name="John Doe", street="Main St", city="NYC")
# print_address(company="Tech Corp", address="123 Tech Blvd", country="USA")


