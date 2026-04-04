# Chapter 29: Rock Paper Scissors Game

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/29-rock-paper-scissors-game/29-rock-paper-scissors-game.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/29-rock-paper-scissors-game/29-rock-paper-scissors-game.ipynb)


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigondaTR/python-bro-code/blob/main/29-rock-paper-scissors-game/29-rock-paper-scissors-game.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/PavanMudigondaTR/python-bro-code/main/29-rock-paper-scissors-game/29-rock-paper-scissors-game.ipynb)

# ✊✋✌️ Rock Paper Scissors Game

## 📺 Video Tutorial

**ROCK PAPER SCISSORS game in Python 🗿** (13:38)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/fn68QNcatfo)

## What You'll Learn

In this chapter, you'll build the classic Rock Paper Scissors game, demonstrating how to use random computer opponents, implement game logic with nested conditionals, validate input with membership operators, and create replay functionality with game loops.

## Learning Objectives

- Implement classic game rules with conditional logic
- Use random.choice() for computer opponent decision-making
- Apply membership operators (in, not in) for input validation
- Create game loops with replay functionality
- Structure nested if-elif statements for complex logic
- Design clear user interaction patterns

## Concept Explanation

### What is Rock Paper Scissors?

Rock Paper Scissors is a simple hand game played between two players. Each player simultaneously forms one of three shapes:
- **Rock** (fist) - beats scissors
- **Paper** (flat hand) - beats rock
- **Scissors** (two fingers) - beats paper

### Game Rules

The win conditions follow a circular logic:

```
Rock crushes Scissors → Rock wins
Scissors cuts Paper → Scissors wins
Paper covers Rock → Paper wins
Same choice → Tie
```

This creates a balanced game where each choice has one win and one loss condition.

### Program Structure

#### 1. **Data Storage**
Use a tuple to store valid options:

```python
options = ("rock", "paper", "scissors")
```

Tuples are perfect because:
- Game options never change (immutable)
- Memory efficient
- Signals these are constants

#### 2. **Random Computer Choice**
```python
import random
computer = random.choice(options)
```

This gives the computer a fair, random selection each game.

#### 3. **Input Validation with Membership**
The **membership operator** checks if a value exists in a sequence:

```python
player = input("Choose: ").lower()
while player not in options:
    player = input("Invalid! Choose rock, paper, or scissors: ").lower()
```

This prevents invalid input before processing game logic.

#### 4. **Nested Conditional Logic**
The game logic requires checking multiple conditions:

```python
if player == computer:
    print("Tie!")
elif player == "rock":
    if computer == "scissors":
        print("You win!")
    else:  # computer == "paper"
        print("You lose!")
# ... more conditions
```

### Game Flow

1. **Setup** - Define valid options, initialize player choice
2. **Computer Selection** - Randomly choose from options
3. **Game Loop** - While user wants to play:
   - **Input Loop** - Get and validate player choice
   - **Comparison** - Check for tie first, then evaluate each player choice
   - **Display Result** - Show outcome with explanation
   - **Replay** - Ask if player wants another round
4. **Exit** - End game when player declines

### Membership Operators

Python provides two membership operators:

```python
# 'in' operator
if "rock" in options:
    print("Found!")

# 'not in' operator  
if player not in options:
    print("Invalid choice!")
```

These are cleaner than multiple comparisons:

```python
# Without membership operator (verbose)
if player == "rock" or player == "paper" or player == "scissors":
    # valid
    
# With membership operator (clean)
if player in options:
    # valid
```

### Decision Tree Structure

The complete game logic as a decision tree:

```
Is player == computer?
├─ Yes → Tie
└─ No → Check player choice
    ├─ Rock?
    │   ├─ vs Paper → Lose
    │   └─ vs Scissors → Win
    ├─ Paper?
    │   ├─ vs Scissors → Lose
    │   └─ vs Rock → Win
    └─ Scissors?
        ├─ vs Rock → Lose
        └─ vs Paper → Win
```

## Examples

### Example 1: Basic Membership Operators
```python
# Using 'in' operator
fruits = ("apple", "banana", "cherry")

if "apple" in fruits:
    print("Found!")  # Executes

if "orange" in fruits:
    print("Found!")  # Doesn't execute

# Using 'not in' operator
if "orange" not in fruits:
    print("Not found!")  # Executes

# With user input
choice = input("Enter a fruit: ").lower()
if choice in fruits:
    print(f"{choice} is available")
else:
    print(f"{choice} is not available")
```

### Example 2: Simple Rock Paper Scissors
```python
import random

options = ("rock", "paper", "scissors")

player = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(options)

print(f"You chose: {player}")
print(f"Computer chose: {computer}")

if player == computer:
    print("Tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "rock" and computer == "paper":
    print("You lose!")
```

### Example 3: Input Validation Loop
```python
options = ("rock", "paper", "scissors")
player = None

# Keep asking until valid input
while player not in options:
    player = input("rock, paper, or scissors: ").lower()
    
    if player not in options:
        print("Invalid! Try again.")

print(f"You chose: {player}")
```

### Example 4: Complete Game Logic
```python
import random

options = ("rock", "paper", "scissors")
player = input("Choose: ").lower()
computer = random.choice(options)

print(f"\nYou: {player}")
print(f"Computer: {computer}\n")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Rock crushes scissors - You win! 🎉")
    else:  # paper
        print("Paper covers rock - You lose! 😢")
elif player == "paper":
    if computer == "rock":
        print("Paper covers rock - You win! 🎉")
    else:  # scissors
        print("Scissors cuts paper - You lose! 😢")
elif player == "scissors":
    if computer == "paper":
        print("Scissors cuts paper - You win! 🎉")
    else:  # rock
        print("Rock crushes scissors - You lose! 😢")
```

### Example 5: With Replay Functionality
```python
import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(options)
    
    # Input validation
    while player not in options:
        player = input("rock, paper, scissors: ").lower()
    
    # Game logic
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
    
    # Replay
    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        playing = False

print("Thanks for playing!")
```

### Example 6: With Score Tracking
```python
import random

options = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0
playing = True

print("=== ROCK PAPER SCISSORS ===")
print("First to 3 wins!\n")

while playing:
    player = None
    
    # Input validation
    while player not in options:
        player = input("Your choice: ").lower()
    
    computer = random.choice(options)
    print(f"Computer chose: {computer}")
    
    # Determine winner
    if player == computer:
        print("Tie! No points.\n")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round! 🎉\n")
        player_score += 1
    else:
        print("Computer wins this round! 😢\n")
        computer_score += 1
    
    # Display score
    print(f"Score - You: {player_score}, Computer: {computer_score}")
    
    # Check for winner
    if player_score == 3:
        print("\n🏆 YOU WIN THE GAME! 🏆")
        playing = False
    elif computer_score == 3:
        print("\n💻 COMPUTER WINS THE GAME! 💻")
        playing = False
    
    print("-" * 30)
```

### Example 7: Full Featured Version
```python
import random

def get_player_choice(options):
    """Get and validate player input"""
    player = None
    while player not in options:
        player = input("\n🎮 rock, paper, or scissors: ").lower()
        if player not in options:
            print("❌ Invalid choice! Try again.")
    return player

def determine_winner(player, computer):
    """Determine game outcome"""
    if player == computer:
        return "tie"
    
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if win_conditions[player] == computer:
        return "player"
    else:
        return "computer"

def display_result(player, computer, winner):
    """Display game result with explanation"""
    actions = {
        ("rock", "scissors"): "Rock crushes scissors",
        ("scissors", "paper"): "Scissors cuts paper",
        ("paper", "rock"): "Paper covers rock",
        ("scissors", "rock"): "Rock crushes scissors",
        ("paper", "scissors"): "Scissors cuts paper",
        ("rock", "paper"): "Paper covers rock"
    }
    
    print(f"\n{'='*40}")
    print(f"You chose: {player.upper()}")
    print(f"Computer chose: {computer.upper()}")
    print(f"{'='*40}")
    
    if winner == "tie":
        print("🤝 It's a TIE!")
    else:
        action = actions.get((player, computer)) or actions.get((computer, player))
        if winner == "player":
            print(f"✅ {action}")
            print("🎉 YOU WIN!")
        else:
            print(f"❌ {action}")
            print("😢 YOU LOSE!")

def main():
    """Main game function"""
    options = ("rock", "paper", "scissors")
    player_wins = 0
    computer_wins = 0
    ties = 0
    
    print("\n" + "="*40)
    print("    ROCK PAPER SCISSORS GAME")
    print("="*40)
    
    playing = True
    
    while playing:
        # Get choices
        player = get_player_choice(options)
        computer = random.choice(options)
        
        # Determine winner
        winner = determine_winner(player, computer)
        
        # Update statistics
        if winner == "player":
            player_wins += 1
        elif winner == "computer":
            computer_wins += 1
        else:
            ties += 1
        
        # Display result
        display_result(player, computer, winner)
        
        # Show statistics
        print(f"\n📊 Statistics:")
        print(f"   Wins: {player_wins} | Losses: {computer_wins} | Ties: {ties}")
        
        # Play again?
        print("\n" + "-"*40)
        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            playing = False
    
    # Final summary
    print("\n" + "="*40)
    print("         GAME OVER")
    print("="*40)
    print(f"Final Score:")
    print(f"  You: {player_wins} wins")
    print(f"  Computer: {computer_wins} wins")
    print(f"  Ties: {ties}")
    
    if player_wins > computer_wins:
        print("\n🏆 YOU ARE THE CHAMPION! 🏆")
    elif computer_wins > player_wins:
        print("\n💻 COMPUTER IS THE CHAMPION! 💻")
    else:
        print("\n🤝 IT'S A DRAW! 🤝")
    
    print("\nThanks for playing! 👋\n")

if __name__ == "__main__":
    main()
```

## Practice Exercises

### Beginner Level

1. **Fixed Choices**: Create a game where both player and computer choices are hardcoded. Determine winner.

2. **One Round**: Build a single round game with player input and random computer choice.

3. **Tie Checker**: Write a program that only checks if choices are the same (tie).

4. **Win Condition Only**: Check only if player wins, ignore loss and tie.

5. **Choice Display**: Display both choices before showing the result.

### Intermediate Level

6. **Best of Three**: Play 3 rounds and declare overall winner based on wins.

7. **Win Percentage**: Track total games and display win percentage.

8. **Choice Statistics**: Track how often each choice (rock/paper/scissors) is selected by both players.

9. **Streak Tracker**: Track and display longest winning streak.

10. **Difficulty Levels**: Add "easy" mode (computer chooses randomly) and "hard" mode (computer tries to predict player's pattern).

### Advanced Level

11. **Extended Version**: Add "lizard" and "spock" options (Rock Paper Scissors Lizard Spock variant with 5 choices).

12. **AI Opponent**: Create a computer that learns from player's previous choices and adapts strategy.

13. **Tournament Mode**: Multiple players compete in elimination rounds.

14. **Multiplayer**: Two human players instead of player vs computer.

15. **Statistical Analysis**: After 100 games, show detailed analytics (most common choices, win rates per choice, pattern detection).

## Common Mistakes to Avoid

### Mistake 1: Not Handling Case Sensitivity

**Wrong:**
```python
options = ("rock", "paper", "scissors")
player = input("Choose: ")  # User enters "Rock"
if player in options:  # "Rock" != "rock"
    print("Valid")  # Won't execute
```

**Correct:**
```python
options = ("rock", "paper", "scissors")
player = input("Choose: ").lower()  # Convert to lowercase
if player in options:
    print("Valid")
```

**Why:** User input case varies. Always normalize to lowercase for comparison.

### Mistake 2: Incomplete Win Conditions

**Wrong:**
```python
if player == "rock":
    if computer == "paper":
        print("You lose!")
    # Missing scissors case!
```

**Correct:**
```python
if player == "rock":
    if computer == "paper":
        print("You lose!")
    elif computer == "scissors":
        print("You win!")
    # Now complete
```

**Why:** Must handle all possible computer choices for each player choice.

### Mistake 3: Resetting Computer Choice in Wrong Place

**Wrong:**
```python
computer = random.choice(options)  # Only once!

while True:
    player = input("Choose: ").lower()
    # computer is same every game!
```

**Correct:**
```python
while True:
    computer = random.choice(options)  # New choice each game
    player = input("Choose: ").lower()
```

**Why:** Computer needs a fresh random choice for each round.

### Mistake 4: Not Resetting Player Choice

**Wrong:**
```python
player = None

while running:
    while player not in options:  # First time only!
        player = input("Choose: ")
    # player keeps old value in next iteration
```

**Correct:**
```python
while running:
    player = None  # Reset each round
    while player not in options:
        player = input("Choose: ").lower()
```

**Why:** Player choice must be reset each round to prompt for new input.

## Real-World Applications

### 1. **Game Theory Research**
Rock Paper Scissors is studied in game theory, economics, and psychology to understand strategic decision-making, prediction, and randomness in competitive scenarios.

### 2. **Conflict Resolution**
Used as a simple, fair decision-making tool in casual situations when a random, unbiased choice is needed between two parties.

### 3. **Robot Programming**
Teaching robots to play RPS helps demonstrate basic AI concepts like decision trees, pattern recognition, and strategy adaptation.

### 4. **Tournament Systems**
The game is used in actual competitive tournaments worldwide, demonstrating how simple rules can create complex strategic depth.

## Challenge Projects

### 1. **Rock Paper Scissors Lizard Spock**
Expand to the 5-option variant from "The Big Bang Theory".

**Requirements:**
- Implement all 5 options (rock, paper, scissors, lizard, spock)
- 10 different win conditions
- Display rule explanations
- Track statistics for all options

### 2. **AI That Learns**
Create a computer opponent that improves over time.

**Requirements:**
- Track player's choice history
- Detect patterns (if player chooses rock twice, likely paper next)
- Adapt strategy based on history
- Display AI "confidence level"
- Compare random vs learning AI performance

### 3. **RPS Championship Tournament**
Host a multi-player elimination tournament.

**Requirements:**
- Support 8+ players
- Bracket-style elimination
- Best of 3 per match
- Display tournament bracket
- Crown champion

### 4. **RPS Casino**
Gambling version with betting system.

**Requirements:**
- Starting balance of $100
- Place bets before each round
- Win doubles bet, lose forfeits bet
- Track balance over time
- Bankruptcy detection
- High score leaderboard

### 5. **RPS Battle RPG**
Turn-based battle game using RPS mechanics.

**Requirements:**
- Health points for player and enemy
- RPS determines damage dealt
- Special moves and powerups
- Multiple enemy types
- Boss battles
- Level progression

---

## Navigation

- **Previous:** [28. Number Guessing Game](28-number-guessing-game.md)
- **Next:** [30. Dice Roller Program](30-dice-roller-program.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Import modules to use external code
3. Use loops to repeat actions
4. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
