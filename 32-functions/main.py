# ============================================
# CHAPTER 31: FUNCTIONS
# ============================================
# Functions are reusable blocks of code that perform specific tasks
# Benefits:
# - Code reusability - write once, use many times
# - Organization - break complex problems into smaller pieces
# - Maintainability - update logic in one place
# - Readability - clear function names make code self-documenting
#
# Key Concepts:
# - def keyword defines a function
# - Parameters allow input to functions
# - Functions can be called multiple times with different arguments
# - if __name__ == "__main__" ensures code runs only when executed directly

# =============================================
# FUNCTION DEFINITION
# =============================================
# Define a function that takes name and age as parameters
# Parameters are variables that receive values when function is called
def happy_birthday(name, age):
    """
    Print a birthday message with personalized name and age.
    
    Parameters:
        name (str): Person's name
        age (int): Person's age
    """
    print(f"happy birthday, {name}!")
    print(f"you are {age} years old!")
    print("happy birthday !")

# =============================================
# MAIN FUNCTION
# =============================================
# It's good practice to have a main() function as the program entry point
# This function orchestrates the program flow
def main(name, age):
    """
    Main function that calls the happy_birthday function.
    
    Parameters:
        name (str): Person's name
        age (int): Person's age
    """
    # Call the happy_birthday function with arguments
    happy_birthday(name, age)

# =============================================
# PROGRAM ENTRY POINT
# =============================================
# This special if statement checks if script is run directly (not imported)
# __name__ is a special variable that equals "__main__" when script runs directly
# This pattern prevents code from running when module is imported elsewhere
if __name__ == "__main__":
    # Call main function with arguments "Joe" and 21
    # Arguments are the actual values passed to function parameters
    main("Joe", 21)
    
    

