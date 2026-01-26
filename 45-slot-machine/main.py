# ============================================
# CHAPTER 43: SLOT MACHINE PROGRAM
# ============================================
# A complete slot machine game demonstrating:
# - List comprehensions for concise code
# - Random symbol generation
# - Conditional payout logic
# - Game loop with balance tracking
# - Input validation and error handling
# - User-friendly emoji interface
#
# User Story:
# As a user, I want to play a slot machine game where I can bet money from my balance.
# I want to spin the machine and either win or lose money based on the outcome.
# The slot machine has three symbols:
# - All three match: Big win (jackpot for 7s)
# - Two match: Small win
# - None match: Lose bet
# The game continues until I quit or run out of money.
#
# Key Concepts:
# - List comprehensions with random.choice()
# - Conditional logic for payout calculation
# - Balance management and betting validation
# - Emoji symbols for visual appeal

import random

# =============================================
# FUNCTION: SPIN THE SLOT MACHINE
# =============================================
def spin_row():
    """
    Generate a random slot machine result.
    
    Returns:
        list: Three random symbols from available symbols
    """
    # Available symbols with emoji representation
    # Cherry, lemon, orange, watermelon, star, bell, seven
    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '🔔', '7️⃣']
    
    # Use list comprehension to pick 3 random symbols
    # [expression for _ in range(3)] creates list of 3 items
    # random.choice() picks one random item from symbols
    return [random.choice(symbols) for _ in range(3)]

# =============================================
# FUNCTION: CALCULATE PAYOUT
# =============================================
def calculate_payout(row, bet):
    """
    Determine winnings based on matching symbols.
    
    Parameters:
        row (list): The three symbols from the spin
        bet (int): Amount the player bet
    
    Returns:
        int: Winnings amount (0 if no win)
    """
    # =============================================
    # CHECK 1: All Three Symbols Match
    # =============================================
    if row[0] == row[1] == row[2]:
        # Special jackpot for three 7s
        if row[0] == '7️⃣':
            return bet * 10   # Jackpot! 10x bet
        else:
            return bet * 5    # Three of a kind: 5x bet
    
    # =============================================
    # CHECK 2: Any Two Symbols Match
    # =============================================
    # Check all possible pairs: (0,1), (1,2), (0,2)
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        return bet * 2       # Two of a kind: 2x bet
    
    # =============================================
    # NO MATCH - Player Loses
    # =============================================
    return 0  # No winnings

# =============================================
# MAIN GAME FUNCTION
# =============================================
def main():
    """
    Main game loop - handles betting, spinning, and balance management.
    """
    # =============================================
    # GAME INITIALIZATION
    # =============================================
    balance = 100  # Starting balance for player
    print("🎰 Welcome to the Python Slot Machine!")
    print(f"Starting balance: ${balance}")

    # =============================================
    # GAME LOOP - Continues while player has money
    # =============================================
    while balance > 0:
        print(f"\nYour balance: ${balance}")
        bet = input("Enter bet amount (0 to quit): ")

        # =============================================
        # INPUT VALIDATION: Check if input is numeric
        # =============================================
        if not bet.isdigit():
            print("Please enter a number.")
            continue  # Skip rest of loop, ask again

        bet = int(bet)

        # =============================================
        # QUIT CONDITION: Bet of 0 exits game
        # =============================================
        if bet == 0:
            print("Thanks for playing! Goodbye.")
            break  # Exit game loop

        # =============================================
        # BET VALIDATION: Check if bet is valid
        # =============================================
        # Bet cannot be more than balance or negative
        if bet > balance or bet < 0:
            print("Invalid bet amount.")
            continue

        # =============================================
        # PLACE BET: Deduct from balance
        # =============================================
        balance -= bet

        # =============================================
        # SPIN THE MACHINE
        # =============================================
        row = spin_row()  # Get three random symbols
        print("Spinning...")
        
        # Display the result with | separator
        print(" | ".join(row))

        # =============================================
        # CALCULATE AND AWARD WINNINGS
        # =============================================
        payout = calculate_payout(row, bet)
        
        # Update balance and display result
        if payout > 0:
            balance += payout  # Add winnings to balance
            print(f"🎉 You won ${payout}!")
        else:
            print("No win this time.")  # Player lost the bet

    # =============================================
    # GAME OVER - Show final balance
    # =============================================
    print("\nGame over! Final balance:", balance)

# =============================================
# PROGRAM ENTRY POINT
# =============================================
if __name__ == "__main__":
    main()

