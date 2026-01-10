# ============================================
# CHAPTER 29: ROCK PAPER SCISSORS GAME
# ============================================
# Classic rock-paper-scissors game demonstrating:
# - Random computer opponent
# - Conditional game logic (nested if-elif)
# - Input validation with membership operators
# - Game loop with replay functionality
#
# Game Rules:
# - Rock smashes scissors (rock wins)
# - Scissors cut paper (scissors wins)
# - Paper covers rock (paper wins)
# - Same choice = tie

# Import random module for computer's choice
import random

# =============================================
# GAME SETUP
# =============================================
# Tuple of valid options (immutable)
options = ("rock", "paper", "scissors" )

# Initialize player choice (None until first input)
player = None

# Computer randomly selects from options
computer = random.choice(options)

# Main game loop control flag
running = True

# =============================================
# MAIN GAME LOOP
# =============================================
while running:
    # =============================================
    # INPUT VALIDATION LOOP
    # =============================================
    # Keep asking until player enters valid option
    # Membership operator: "while player not in options"
    while player not in options:
        # Get input and convert to lowercase for comparison
        player = input("rock, paper, scissors: ").lower()
        
        # =============================================
        # CHECK FOR TIE
        # =============================================
        if player == computer:
            print("Tie!")
            
        # =============================================
        # PLAYER CHOSE ROCK
        # =============================================
        elif player == "rock":
            # Rock vs Paper - computer wins
            if computer == "paper":
                print("You lose!", computer, "covers", player)
            # Rock vs Scissors - player wins
            else:
                print("You win!", player, "smashes", computer)
                
        # =============================================
        # PLAYER CHOSE PAPER
        # =============================================
        elif player == "paper":
            # Paper vs Scissors - computer wins
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
            # Paper vs Rock - player wins
            else:
                print("You win!", player, "covers", computer)
                
        # =============================================
        # PLAYER CHOSE SCISSORS
        # =============================================
        elif player == "scissors":
            # Scissors vs Rock - computer wins
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
            # Scissors vs Paper - player wins
            else:
                print("You win!", player, "cut", computer) if computer == "" else ""
                
        # =============================================
        # INVALID CHOICE (should not reach due to while condition)
        # =============================================
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.") if computer == "" else ""
            
    # =============================================
    # REPLAY LOGIC
    # =============================================
    # Ask if player wants to continue
    play_again = input("Play again? (yes/no): ").lower()
    
    if play_again != "yes":
        running = False  # Exit main loop
        
    # Reset for next round
    player = None  # Clear player choice
    computer = random.choice(options)  # New random choice for computer
