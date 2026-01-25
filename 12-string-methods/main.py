# ============================================
# Chapter 13: String Methods
# ============================================
# Strings have many built-in methods for manipulation and analysis

# Get user's name
name = input("Enter your name: ")

# ============================================
# String Concatenation
# ============================================
# Combining strings using the + operator
print("Hello, " + name + "!")

# ============================================
# len() - Get string length
# ============================================
# Returns the number of characters in a string
length = len(name)
print("Your name has " + str(length) + " characters.")

# ============================================
# .upper() - Convert to uppercase
# ============================================
result = name.upper()
print("Your name in uppercase: " + result)

# ============================================
# .lower() - Convert to lowercase
# ============================================
result = name.lower()
print("Your name in lowercase: " + result)

# ============================================
# .title() - Convert to title case
# ============================================
# First letter of each word is capitalized
result = name.title()
print("Your name in titlecase: " + result)

# ============================================
# .find() - Find substring position
# ============================================
# Returns the index of first occurrence, or -1 if not found
find_p = name.find("P")
print("The position of the letter 'P': " + str(find_p))

# ============================================
# .capitalize() - Capitalize first letter only
# ============================================
name = name.capitalize()

# ============================================
# .isdigit() and .isnumeric() - Check if string contains only digits
# ============================================
result = name.isdigit()   # Returns True if all characters are digits
result = name.isnumeric() # Similar to isdigit() but handles more number types
print("Is your name a number? " + str(result))

# ============================================
# .replace() - Replace substring with another
# ============================================
phone_number = input("What is your phone number? ")
# Remove dashes from phone number
phone_number = phone_number.replace('-', "")
print("Phone without dashes: " + phone_number)

# ============================================
# help() - Get documentation for a class/function
# ============================================
# Uncomment the line below to see all string methods:
# print(help(str))