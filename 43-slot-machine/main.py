# Python Slot Machine
# user has balance
# user can bet amount

import random

# Spin the slot machine (pick 3 random symbols)
def spin_row():
    # symbols are cherry, lemon, orange, watermelon, star, bell, seven
    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '🔔', '7️⃣']
    # choose 3 symbols randomly and return as a list
    return [random.choice(symbols) for _ in range(3)]

# Decide how much the player wins
def calculate_payout(row, bet):
    # All three match
    if row[0] == row[1] == row[2]:
        # Jackpot if all sevens
        if row[0] == '7️⃣':
            return bet * 10   # Jackpot # award 10 times the bet
        else:
            return bet * 5       # Three of a kind # award 5 times the bet
    # Any two match
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        return bet * 2       # Two of a kind # award 2 times the bet
    # No match # no winnings
    return 0

def main():
    # Initial balance for the player
    balance = 100
    print("🎰 Welcome to the Python Slot Machine!")
    print(f"Starting balance: ${balance}")

    # Game loop - continues until player quits or runs out of money
    while balance > 0:
        print(f"\nYour balance: ${balance}")
        bet = input("Enter bet amount (0 to quit): ")

        # Check if input is a number
        if not bet.isdigit():
            print("Please enter a number.")
            continue

        bet = int(bet)

        # Quit if bet is 0
        if bet == 0:
            print("Thanks for playing! Goodbye.")
            break

        # Check if bet is valid
        # Bet cannot be more than balance or negative
        if bet > balance or bet < 0:
            print("Invalid bet amount.")
            continue

        # Deduct bet from balance
        balance -= bet

        # Spin the machine and display result
        row = spin_row()
        print("Spinning...")
        # Display the row
        print(" | ".join(row))

        # Calculate winnings
        payout = calculate_payout(row, bet)
        # Update balance and display result
        if payout > 0:
            balance += payout
            print(f"🎉 You won ${payout}!")
        else:
            print("No win this time.")

    # Game over message
    print("\nGame over! Final balance:", balance)

if __name__ == "__main__":
    main()

