import random

options = ("rock", "paper", "scissors" )
player = None
computer = random.choice(options)

running = True

while running:
    while player not in options:
        player = input("rock, paper, scissors: ").lower()
        if player == computer:
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
                
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
                
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer) if computer == "" else ""
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.") if computer == "" else ""
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        running = False
    player = None
    computer = random.choice(options)
