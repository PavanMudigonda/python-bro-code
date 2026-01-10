# ============================================
# Chapter 4: User Input
# ============================================
# The input() function allows programs to receive data from the user
# It always returns a string, so type casting is often needed

# Example 1: Getting string input
# input() displays a prompt and waits for the user to type something
name = input("what is your name? ")

# Example 2: Getting numeric input
# We use int() to convert the string input to an integer
age = int(input("what is your age? "))

# Example 3: Using the input in output
# F-strings make it easy to display the user's input
print(f'Hello {name}!')
print(f'You are {age} years old.')

# ============================================
# How input() works:
# ============================================
# 1. Displays the prompt message to the user
# 2. Waits for the user to type something and press Enter
# 3. Returns whatever the user typed as a STRING
# 4. If you need a number, use int() or float() to convert it