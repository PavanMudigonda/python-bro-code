# ============================================
# CHAPTER 33: KEYWORD ARGUMENTS
# ============================================
# Keyword arguments = Arguments preceded by an identifier (name=value)
#                     Benefits:
#                     - Order doesn't matter
#                     - More readable and self-documenting
#                     - Less error-prone than positional arguments
#                     - Can skip optional arguments selectively
#
# Argument Types (in order):
# 1. Positional arguments (order matters)
# 2. Default arguments (optional with defaults)
# 3. KEYWORD arguments (name=value)
# 4. Arbitrary arguments (*args, **kwargs)
#
# Key Advantages:
# - Explicit parameter names make code clearer
# - Can mix positional and keyword arguments
# - Must provide keyword args after positional args

# =============================================
# FUNCTION WITH MULTIPLE PARAMETERS
# =============================================
def hello(greeting, title, first, last):
    """
    Print a formatted greeting with title and full name.
    
    Parameters:
        greeting (str): Greeting word (e.g., "Hello", "Hi")
        title (str): Title (e.g., "Mr", "Ms", "Dr")
        first (str): First name
        last (str): Last name
    """
    print(f"{greeting} {title} {first} {last}")

# =============================================
# CALLING WITH DIFFERENT ARGUMENT STYLES
# =============================================

# Example 1: All positional arguments (order matters!)
# Must provide arguments in exact order: greeting, title, first, last
# hello("Hello", "Mr", "Spongebob", "Squarepants")
# Output: Hello Mr Spongebob Squarepants

# Example 2: Mix of positional and keyword arguments
# First two are positional (greeting, title)
# Last two use keyword arguments (order doesn't matter!)
hello("Hello", "Mr", first="Spongebob", last="Squarepants")
# Output: Hello Mr Spongebob Squarepants

# Example 3: All keyword arguments (completely flexible order)
# hello(last="Squarepants", first="Spongebob", greeting="Hi", title="Mr")
# Output: Hi Mr Spongebob Squarepants

# Example 4: Why keyword arguments are better for readability
# hello(greeting="Good morning", title="Dr", first="Jane", last="Smith")
# Much clearer what each argument represents!


