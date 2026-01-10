# ============================================
# Chapter 3: Type Casting
# ============================================
# Type casting = Converting a value from one data type to another
# Common type casting functions: str(), int(), float(), bool()

# Create variables with different data types
name: str = "Pavan"
age: int = 25
is_student: bool = False
gpa: float = 3.5

# The type() function returns the data type of a variable
print(type(name))        # Output: <class 'str'>
print(type(age))         # Output: <class 'int'>
print(type(is_student))  # Output: <class 'bool'>
print(type(gpa))         # Output: <class 'float'>

# ============================================
# Converting int to float
# ============================================
# float() converts an integer to a floating-point number
age = float(age)  # age is now 25.0 (a float)
print(age)

# ============================================
# Converting float to int
# ============================================
# int() converts a float to an integer (removes decimal part)
# Note: This truncates (cuts off) the decimal, doesn't round
print(int(gpa))  # Output: 3 (not 4, even though 3.5 is closer to 4)

# ============================================
# Common Type Casting Examples
# ============================================
# String to int (useful for user input)
# age_str = "25"
# age_int = int(age_str)  # Converts "25" to 25

# String to float
# price_str = "19.99"
# price_float = float(price_str)  # Converts "19.99" to 19.99

# Number to string (useful for concatenation)
# age = 25
# message = "I am " + str(age) + " years old"  # str(age) converts 25 to "25"