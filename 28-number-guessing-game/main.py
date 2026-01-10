# ============================================
# CHAPTER 28: NUMBER GUESSING GAME
# ============================================
# An interactive game demonstrating:
# - Random number generation
# - Input validation and error handling
# - While loop with conditional logic
# - Tracking attempts/guesses
# - User feedback and hints
#
# Key Concepts:
# - isdigit() method validates numeric input
# - Range validation ensures sensible guesses
# - Conditional feedback guides the player
# - Loop control with boolean flag

# Import random module for generating the secret number
import random

# =============================================
# GAME SETUP - Define range and generate answer
# =============================================
# Define the valid range for guessing
lowest_num = 1
highest_num = 100

# Generate random secret number within the range
# randint is inclusive on both ends
answer = random.randint(lowest_num, highest_num)

# Track how many guesses the player makes
guesses = 0

# Control flag for the game loop
# When False, the loop ends and game stops
is_running = True

# =============================================
# GAME START - Display instructions
# =============================================
print("Python Number Guessing Game")
print(f'select a number between {lowest_num} and {highest_num}')

# =============================================
# GAME LOOP - Main game logic
# =============================================
while is_running:
    # Get player's guess as string input
    guess = input("enter your guess")
    
    # =============================================
    # INPUT VALIDATION
    # =============================================
    # isdigit() returns True if string contains only digits
    # This prevents crashes from non-numeric input like "abc"
    if guess.isdigit():
        # Convert validated string to integer
        guess = int(guess)
        
        # Increment guess counter
        guesses += 1
        
        # =============================================
        # RANGE VALIDATION
        # =============================================
        # Check if guess is within valid range
        if guess < lowest_num or guess > highest_num:
            print(f'select a number between {lowest_num} and {highest_num}')
            
        # =============================================
        # COMPARISON AND FEEDBACK
        # =============================================
        # Too low - give hint
        elif guess < answer:
            print("Too low ! Try again!")
            
        # Too high - give hint
        elif guess > answer:
            print("Too high ! Try again!")   
            
        # =============================================
        # CORRECT GUESS - Win condition
        # =============================================
        else:
            print(f"CORRECT! The answer was {answer}")  
            print(f'Number of guesses: {guesses}')
            is_running = False  # End the game loop
            
    # =============================================
    # INVALID INPUT - Not a number
    # =============================================
    else:
        print(f'select a number between {lowest_num} and {highest_num}') 