# 🎯 Number Guessing Game

## What You'll Learn

In this chapter, you'll build an interactive number guessing game that combines random number generation, input validation, conditional logic, and user feedback. This classic programming project teaches important concepts about game loops, user interaction, and program flow control.

## Learning Objectives

- Combine random module with game logic
- Implement input validation using isdigit() method
- Create game loops with boolean control flags
- Provide contextual feedback based on user input
- Track and display game statistics (attempts)
- Design engaging user experiences with hints

## Concept Explanation

### What is a Number Guessing Game?

A number guessing game generates a random secret number within a range, and the player tries to guess it. After each guess, the program provides feedback ("too high", "too low") until the player guesses correctly. This simple game demonstrates core programming concepts used in more complex interactive applications.

### Game Loop Pattern

The game uses a **while loop with a control flag** - a common pattern in game development:

```python
is_running = True  # Control flag

while is_running:
    # Game logic
    # ...
    if win_condition:
        is_running = False  # Exit loop
```

This pattern provides clear control over when the game starts and stops.

### Key Components

#### 1. **Random Number Generation**
```python
import random
answer = random.randint(1, 100)  # Secret number
```

#### 2. **Input Validation**
```python
guess = input("Enter guess: ")
if guess.isdigit():  # Checks if string contains only digits
    guess = int(guess)  # Safe to convert
else:
    print("Invalid input!")
```

#### 3. **Range Validation**
```python
if guess < lowest_num or guess > highest_num:
    print("Out of range!")
```

#### 4. **Comparison Logic**
```python
if guess < answer:
    print("Too low!")
elif guess > answer:
    print("Too high!")
else:
    print("Correct!")
```

#### 5. **Attempt Tracking**
```python
guesses = 0
# ...
guesses += 1  # Increment on each guess
```

### Input Validation with isdigit()

The **isdigit()** method is crucial for preventing crashes:

```python
"123".isdigit()    # True - all characters are digits
"12.5".isdigit()   # False - contains decimal point
"-10".isdigit()    # False - contains minus sign
"abc".isdigit()    # False - contains letters
"".isdigit()       # False - empty string
```

**Why validate?** Converting non-numeric input to int() raises ValueError:

```python
int("abc")  # ValueError: invalid literal for int()
```

### Program Flow

1. **Setup** - Define range, generate random answer
2. **Initialize** - Set guess counter to 0, running flag to True
3. **Instructions** - Display game rules to player
4. **Game Loop** - While game is running:
   - Get user input
   - Validate input is numeric
   - Validate input is in range
   - Compare with answer
   - Provide feedback
   - Track attempts
   - Check win condition
5. **End Game** - Display final statistics

### Providing Good Feedback

Effective feedback improves user experience:

```python
if guess < answer:
    print("Too low! Try again!")  # Encouraging
elif guess > answer:
    print("Too high! Try again!")  # Clear direction
else:
    print(f"CORRECT! The answer was {answer}")  # Celebration
    print(f"Number of guesses: {guesses}")  # Statistics
```

## Examples

### Example 1: Basic Input Validation
```python
# Validating numeric input
guess = input("Enter a number: ")

if guess.isdigit():
    guess = int(guess)
    print(f"Valid input: {guess}")
else:
    print("Invalid! Please enter a number")

# Testing different inputs:
# "42" → Valid input: 42
# "abc" → Invalid! Please enter a number
# "3.14" → Invalid! Please enter a number
```

### Example 2: Simple Guessing Game
```python
import random

answer = random.randint(1, 10)
guess = int(input("Guess a number between 1-10: "))

if guess == answer:
    print("Correct!")
else:
    print(f"Wrong! The answer was {answer}")
```

### Example 3: With Hints
```python
import random

answer = random.randint(1, 10)
guess = int(input("Guess a number between 1-10: "))

if guess < answer:
    print("Too low!")
elif guess > answer:
    print("Too high!")
else:
    print("Correct!")
```

### Example 4: Tracking Attempts
```python
import random

answer = random.randint(1, 10)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess (1-10): "))
    attempts += 1
    
    if guess == answer:
        print(f"Correct! You won in {attempts} attempts!")
        break
    elif guess < answer:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Game Over! The answer was {answer}")
```

### Example 5: Complete Simple Version
```python
import random

# Setup
answer = random.randint(1, 50)
guesses = 0
won = False

print("=== NUMBER GUESSING GAME ===")
print("I'm thinking of a number between 1 and 50")

# Game loop
while not won:
    guess_str = input("\nYour guess: ")
    
    # Validate input
    if not guess_str.isdigit():
        print("Please enter a valid number!")
        continue
    
    guess = int(guess_str)
    guesses += 1
    
    # Compare
    if guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(f"\n🎉 Correct! The answer was {answer}")
        print(f"You guessed it in {guesses} attempts!")
        won = True
```

### Example 6: With Difficulty Levels
```python
import random

print("Choose difficulty:")
print("1. Easy (1-10)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    max_num = 10
    difficulty = "Easy"
elif choice == "2":
    max_num = 50
    difficulty = "Medium"
else:
    max_num = 100
    difficulty = "Hard"

answer = random.randint(1, max_num)
guesses = 0

print(f"\n{difficulty} mode: Guess a number between 1 and {max_num}")

while True:
    guess_str = input("Guess: ")
    
    if not guess_str.isdigit():
        print("Invalid input!")
        continue
    
    guess = int(guess_str)
    guesses += 1
    
    if guess == answer:
        print(f"Correct in {guesses} guesses!")
        break
    elif guess < answer:
        print("Higher!")
    else:
        print("Lower!")
```

### Example 7: Full Featured Version
```python
import random

def play_game():
    """Main game function"""
    # Setup
    lowest = 1
    highest = 100
    answer = random.randint(lowest, highest)
    guesses = 0
    is_running = True
    
    # Instructions
    print("\n" + "="*50)
    print("       NUMBER GUESSING GAME")
    print("="*50)
    print(f"Guess a number between {lowest} and {highest}")
    print("="*50 + "\n")
    
    # Game loop
    while is_running:
        guess_str = input("Enter your guess (or 'quit' to exit): ")
        
        # Check for quit
        if guess_str.lower() == 'quit':
            print(f"Game ended. The answer was {answer}")
            return
        
        # Validate numeric
        if not guess_str.isdigit():
            print(f"⚠ Please enter a number between {lowest} and {highest}")
            continue
        
        guess = int(guess_str)
        guesses += 1
        
        # Validate range
        if guess < lowest or guess > highest:
            print(f"⚠ Number must be between {lowest} and {highest}")
            continue
        
        # Compare and give feedback
        if guess < answer:
            distance = answer - guess
            if distance > 20:
                print("❄ Too low! Way off!")
            else:
                print("📉 Too low! Getting closer!")
                
        elif guess > answer:
            distance = guess - answer
            if distance > 20:
                print("🔥 Too high! Way off!")
            else:
                print("📈 Too high! Getting closer!")
        else:
            # Win condition
            print("\n" + "="*50)
            print(f"🎉 CORRECT! The answer was {answer}")
            print(f"🏆 You guessed it in {guesses} attempts!")
            print("="*50 + "\n")
            is_running = False
            
            # Performance rating
            if guesses <= 5:
                print("⭐⭐⭐ Excellent!")
            elif guesses <= 10:
                print("⭐⭐ Good job!")
            else:
                print("⭐ You won!")

# Main program
if __name__ == "__main__":
    while True:
        play_game()
        
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye! 👋")
            break
```

## Practice Exercises

### Beginner Level

1. **Fixed Range**: Create a guessing game with numbers 1-20. No input validation needed yet.

2. **Attempt Limit**: Modify the game to allow only 5 guesses. Display "Game Over" if limit reached.

3. **Higher/Lower Only**: Create a simple version that only says "Higher" or "Lower" without "Too".

4. **Win Message**: Add a special congratulations message when the player wins.

5. **Display Range**: Always show the valid range in the prompt: "Guess (1-100): ".

### Intermediate Level

6. **Guess History**: Store all guesses in a list and display them when the game ends.

7. **Hint System**: After 5 wrong guesses, give a hint (e.g., "The number is even").

8. **Score System**: Award points based on how many guesses it took. Fewer guesses = more points.

9. **Multiple Rounds**: Play 5 rounds and track total score across all rounds.

10. **Binary Search Helper**: Show if the player is guessing efficiently (like binary search) or randomly.

### Advanced Level

11. **Adaptive Range**: After each guess, display the narrowed range (e.g., "Try between 50-100").

12. **Multiplayer Mode**: Two players take turns guessing. First to guess correctly wins.

13. **Difficulty Adjustment**: Game adjusts difficulty based on player performance over multiple rounds.

14. **Statistics Tracker**: Save game statistics to a file (average guesses, best score, total games).

15. **AI Opponent**: Create a computer opponent that guesses efficiently using binary search strategy. Race against it!

## Common Mistakes to Avoid

### Mistake 1: Not Validating Input Before Converting

**Wrong:**
```python
guess = int(input("Guess: "))  # Crashes if user enters "abc"
```

**Correct:**
```python
guess_str = input("Guess: ")
if guess_str.isdigit():
    guess = int(guess_str)
else:
    print("Invalid input!")
```

**Why:** int() raises ValueError for non-numeric strings. Always validate first.

### Mistake 2: Using 'is' Instead of '==' for Numbers

**Wrong:**
```python
guess = 5
answer = 5
if guess is answer:  # May not work for larger numbers!
    print("Correct")
```

**Correct:**
```python
guess = 5
answer = 5
if guess == answer:  # Always works
    print("Correct")
```

**Why:** 'is' checks object identity, not value equality. Use '==' for comparing values.

### Mistake 3: Off-by-One Range Error

**Wrong:**
```python
# Checking if 1 <= guess <= 100
if guess < 1 or guess >= 100:  # Wrong! Excludes 100
    print("Out of range")
```

**Correct:**
```python
# Checking if 1 <= guess <= 100
if guess < 1 or guess > 100:  # Correct! Includes 1 and 100
    print("Out of range")
```

**Why:** Be careful with inclusive vs exclusive bounds. For range 1-100, both endpoints are valid.

### Mistake 4: Incrementing Guesses in Wrong Place

**Wrong:**
```python
while running:
    guess = input("Guess: ")
    if not guess.isdigit():
        guesses += 1  # Wrong! Counts invalid input
        continue
    # ...
```

**Correct:**
```python
while running:
    guess = input("Guess: ")
    if not guess.isdigit():
        continue  # Don't count invalid input
    guesses += 1  # Only count valid guesses
    # ...
```

**Why:** Only increment guess counter for valid attempts, not for invalid input.

## Real-World Applications

### 1. **Password Cracking Simulations**
Security researchers use similar logic to demonstrate the difficulty of guessing passwords, showing why longer passwords with more possibilities are more secure.

### 2. **Machine Learning Search Algorithms**
Hyperparameter tuning in ML uses binary search-like strategies to find optimal values, similar to an efficient guessing game strategy.

### 3. **User Onboarding Tutorials**
Games and apps use guessing-game mechanics to teach users how to interact with interfaces, providing immediate feedback on actions.

### 4. **Educational Tools**
Math education software uses number guessing games to teach concepts like number sense, estimation, and strategic thinking.

## Challenge Projects

### 1. **Multi-Level Guessing Game**
Create a game with progressive difficulty levels.

**Requirements:**
- Start at easy level (1-10)
- Upon winning, advance to next level with wider range
- Track level progression
- Bonus points for quick guesses
- High score system

### 2. **Reverse Guessing Game**
Computer tries to guess YOUR number.

**Requirements:**
- You think of a number (don't tell computer)
- Computer makes guesses using binary search
- You respond "higher", "lower", or "correct"
- Computer should guess efficiently
- Detect if user is lying (inconsistent responses)

### 3. **Multiplayer Guessing Competition**
Two players compete to guess first.

**Requirements:**
- Both players see same range
- Take turns guessing
- First to guess correctly wins
- Track wins for each player
- Best of 5 rounds

### 4. **Guessing Game with Powerups**
Add special abilities players can use.

**Requirements:**
- "Hint" powerup (narrow the range)
- "Skip" powerup (new number if stuck)
- "Extra guess" powerup (more attempts)
- Limited uses per game
- Cost/reward system for powerups

### 5. **Pattern Recognition Guessing**
Numbers follow a hidden pattern.

**Requirements:**
- Generate numbers following a pattern (multiples of 7, fibonacci, etc.)
- Players guess the pattern, not just the number
- Award bonus points for identifying pattern
- Increasing difficulty with more complex patterns
- Leaderboard for pattern masters

---

## Navigation

- **Previous:** [27. Random Numbers](../27-random-numbers/README.md)
- **Next:** [29. Rock Paper Scissors Game](../29-rock-paper-scissors-game/README.md)
- **[Back to Main README](../README.md)**
