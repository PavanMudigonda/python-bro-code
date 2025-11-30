import random

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


def roll_dice(number_of_dice_to_roll):
    """ Enter Number of dices to throw between 1 and 6 and calculate score"""
    print(f"you asked me to roll,{number_of_dice_to_roll}")
    
    results = []
    
    for i in range (int(number_of_dice_to_roll)):
        results.append(random.randint(1,6))
    print(f'results: {results}')
    sum_of_results = sum(results)
    print(f"sum: {sum_of_results}")

    # print the dices 
    

    for result in results:
        for line_index in range(5):            
            print(dice_art[result][line_index])

def main():
    while True:
        try:
            num_of_dice = input("Enter number of dice you would like to throw !! ( 'q' or 'quit' to exit game): " ).strip()
            
            if num_of_dice.lower() == 'q' or num_of_dice == 'quit':
                print("thanks for playing")
                break
            elif int(num_of_dice) < 6 and int(num_of_dice) > 1:
                roll_dice(num_of_dice)
            else:
                "provide a valid input..enter 1 to 6 to roll dice or q to quit"
        except ValueError:
            print(f"value error")

if __name__ == "__main__":
    main()