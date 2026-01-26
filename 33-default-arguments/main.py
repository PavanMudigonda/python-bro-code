# ============================================
# CHAPTER 32: DEFAULT ARGUMENTS
# ============================================
# Default arguments = A default value for certain parameters
#                     The default is used when that argument is omitted
#                     Makes functions more flexible and reduces required arguments
#
# Argument Order (IMPORTANT):
# 1. Positional arguments (required)
# 2. DEFAULT arguments (optional with default values)
# 3. Keyword arguments (named)
# 4. Arbitrary arguments (*args, **kwargs)
#
# Key Rules:
# - Default arguments MUST be placed AFTER positional arguments
# - Example: def func(pos1, pos2, default1=5, default2="hello")
# - Cannot have positional argument after a default argument

# =============================================
# FUNCTION WITH DEFAULT ARGUMENTS
# =============================================
# price is a required positional argument
# tax_rate and discount are optional default arguments
def net_price(price, tax_rate=0.08, discount=0):
    """
    Calculate the net price of an item after tax and discount.
    
    Parameters:
        price (float): Base price of item (REQUIRED)
        tax_rate (float): Tax rate as decimal (DEFAULT: 0.08 = 8%)
        discount (float): Discount amount in dollars (DEFAULT: 0)
    
    Returns:
        float: Final price after tax and discount
    """
    # Calculate: base price + tax - discount
    final_price = price + (price * tax_rate) - discount
    return final_price

# =============================================
# CALLING FUNCTIONS WITH DEFAULT ARGUMENTS
# =============================================

# Example 1: Use default tax_rate (0.08) and discount (0)
# print(net_price(500))  # Result: 500 + 40 - 0 = 540

# Example 2: Override tax_rate, use default discount
# Provide custom tax rate of 10% (0.1)
print(net_price(500, 0.1))  # Result: 500 + 50 - 0 = 550

# Example 3: Override both defaults
# print(net_price(500, 0.08, 50))  # Result: 500 + 40 - 50 = 490