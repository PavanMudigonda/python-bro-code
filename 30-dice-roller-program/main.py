import random

# unicode chars for dice faces

# print("\u25CF \u250C \u2510 \u2502 \u2514 \u2518")

# ● ┌ - ┐ │ └ ┘

# 🎲 Dice Roller Program

# ASCII art for dice faces

# lets build a dictionary to hold the dice art

# dictionary is a combination of key:value pairs in a curly braces {}

# The value is a tuple of 5 strings in matrix form  representing each line of the dice

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

def roll_dice(num_dice):
    """Roll the specified number of dice and display the results"""
    
    # If user enters less than 1 dice, prompt for valid input
    
    if num_dice < 1:
        print("Please enter a valid number of dice (1 or more)")
        return
    
    # construct a list to hold the results of each dice roll
    results = []
    
    # for each dice to be rolled, generate a random number between 1 and 6
    # image this as rolling 6  physical dice on a table
    
    for _ in range(num_dice):
        results.append(random.randint(1, 6))
    
    
    # Display dice art
    print("\n" + "="*50)
    print(f"Rolling {num_dice} dice...")
    print("="*50 + "\n")
    
    # Display all dice side by side
    for line_index in range(5):
        line = ""
        for result in results:
            line += dice_art[result][line_index] + "  "
        print(line)
    
    # Display results and total
    
    print("\n" + "="*50)
    print(f"Results: {results}")
    print(f"Total: {sum(results)}")
    print("="*50 + "\n")

def main():
    print("🎲 Welcome to the Dice Roller Program! 🎲\n")
    
    while True:
        try:
            num_dice = input("How many dice would you like to roll? (or 'q' to quit): ").strip()
            
            if num_dice.lower() == 'q':
                print("Thanks for playing! Goodbye! 👋")
                break
            
            num_dice = int(num_dice)
            roll_dice(num_dice)
            
        except ValueError:
            print("Please enter a valid number or 'q' to quit\n")

if __name__ == "__main__":
    main()