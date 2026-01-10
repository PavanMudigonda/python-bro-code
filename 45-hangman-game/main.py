# ============================================
# CHAPTER 45: HANGMAN GAME
# ============================================
# Classic Hangman word-guessing game demonstrating:
# - Dictionary data structure for ASCII art
# - Set data structure for tracking guesses
# - List manipulation for hint display
# - Random word selection
# - Game loop with win/loss conditions
# - Input validation
# - Modular function design
#
# Game Rules:
# 1. Computer selects random word
# 2. Player guesses one letter at a time
# 3. Correct guesses reveal letters in word
# 4. Wrong guesses draw hangman (max 6 wrong guesses)
# 5. Win by guessing all letters before hangman complete
#
# Key Concepts:
# - Dictionary for mapping wrong guesses to ASCII art
# - Set for O(1) lookup of guessed letters
# - enumerate() for index-value iteration
# - String validation with isalpha()

# Import word list from separate module
from words_list import words

import random

# =============================================
# HANGMAN ASCII ART DICTIONARY
# =============================================
# Maps number of wrong guesses (0-6) to hangman drawing stages
# Key: number of wrong guesses
# Value: ASCII art string showing hangman state
hangman_art = {
    0: """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    1: """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    2: """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    3: """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    4: """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    5: """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    6: """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
}

# =============================================
# HELPER FUNCTIONS
# =============================================

def display_man(wrong_guesses):
    """
    Display hangman ASCII art based on wrong guess count.
    
    Parameters:
        wrong_guesses (int): Number of incorrect guesses (0-6)
    """
    print(hangman_art[wrong_guesses])


def display_hint(hint):
    """
    Display current state of word with underscores for unknown letters.
    
    Parameters:
        hint (list): List of letters and underscores (e.g., ['_', 'a', '_', 't'])
    """
    # Join list with spaces: ['_', 'a', 't'] -> "_ a t"
    print(" ".join(hint))


def display_answer(answer):
    """
    Reveal the answer word when game ends.
    
    Parameters:
        answer (str): The secret word
    """
    print("The answer was: " + answer)

# =============================================
# MAIN GAME FUNCTION
# =============================================

def main():
    """
    Main game loop - handles all game logic and user interaction.
    """
    # =============================================
    # GAME INITIALIZATION
    # =============================================
    # Select random word from imported word list
    answer = random.choice(words)
    
    # Create hint list with underscores for each letter
    # Example: "cat" -> ['_', '_', '_']
    hint = ["_"] * len(answer)
    
    # Track wrong guesses
    wrong_guesses = 0
    
    # Use set to store guessed letters (fast lookup)
    # Sets don't allow duplicates
    guessed_letters = set()
    
    # Maximum wrong guesses allowed (one less than art dictionary length)
    max_wrong = len(hangman_art) - 1

    # =============================================
    # MAIN GAME LOOP
    # =============================================
    while True:
        # Display current hangman state
        display_man(wrong_guesses)
        
        # Display current word progress (e.g., "_ a _")
        display_hint(hint)

        # =============================================
        # GET AND VALIDATE USER INPUT
        # =============================================
        guess = input("Enter a letter: ").lower()

        # Validation 1: Must be single letter (not number or multiple chars)
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue  # Skip rest of loop, ask again

        # Validation 2: Check if letter already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add to guessed letters set
        guessed_letters.add(guess)

        # =============================================
        # CHECK IF GUESS IS CORRECT
        # =============================================
        if guess in answer:
            # =============================================
            # CORRECT GUESS - Reveal letters in hint
            # =============================================
            # enumerate() gives both index and letter
            # Example: enumerate("cat") -> (0,'c'), (1,'a'), (2,'t')
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess  # Replace underscore with guessed letter
            
            # =============================================
            # CHECK FOR WIN CONDITION
            # =============================================
            # If no underscores left, all letters guessed
            if "_" not in hint:
                print("🎉 You win! The word was:", answer)
                break  # Exit game loop
        else:
            # =============================================
            # WRONG GUESS - Increment counter
            # =============================================
            wrong_guesses += 1
            
            # =============================================
            # CHECK FOR LOSS CONDITION
            # =============================================
            if wrong_guesses == max_wrong:
                display_man(wrong_guesses)  # Show complete hangman
                print("💀 You lost!")
                display_answer(answer)
                break  # Exit game loop

# =============================================
# PROGRAM ENTRY POINT
# =============================================
if __name__ == "__main__":
    main()
