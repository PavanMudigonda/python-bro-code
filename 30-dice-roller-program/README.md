# 🎲 Dice Roller Program


## 📺 Video Tutorial

**Code a dice roller program in 10 minutes! 🎲** (10:24)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/x-Ag2_bJ40Y)


## What You'll Learn

In this chapter, you'll build a sophisticated dice rolling program that generates ASCII art representations of dice faces, demonstrates dictionary usage for structured data, works with tuples for multi-line strings, and implements functions with parameter validation. This project combines visual output with practical programming concepts.

## Learning Objectives

- Create ASCII art using Unicode box-drawing characters
- Store multi-line strings in tuples for structured data
- Use dictionaries to map values to complex data structures
- Implement functions with input validation
- Display multiple dice results side-by-side
- Apply random number generation for realistic simulations

## Concept Explanation

### What is a Dice Roller?

A dice roller program simulates rolling physical dice and displays the results visually using ASCII art. Instead of just showing numbers, it draws the actual dice faces, making it more engaging and realistic.

### ASCII Art for Dice

ASCII art uses characters to create pictures. For dice, we use:
- **Box-drawing characters**: ┌ ─ ┐ │ └ ┘ for borders
- **Bullet character**: ● for dots
- **Spaces** for empty areas

Example of a dice showing 3:
```
┌─────────┐
│  ●      │
│    ●    │
│      ●  │
└─────────┘
```

### Unicode Box-Drawing Characters

These special characters create the dice borders:

```python
# Unicode characters
print("\u25CF")  # ● (bullet/dot)
print("\u250C")  # ┌ (top-left corner)
print("\u2510")  # ┐ (top-right corner)
print("\u2502")  # │ (vertical line)
print("\u2514")  # └ (bottom-left corner)
print("\u2518")  # ┘ (bottom-right corner)
print("\u2500")  # ─ (horizontal line)
```

### Data Structure: Dictionary of Tuples

The program uses a clever data structure:

```python
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    # ... more dice faces
}
```

**Why this structure?**
- **Dictionary**: Fast lookup by dice value (1-6)
- **Tuples**: Each dice face is 5 lines that never change
- **Strings**: Each line is a separate string in the tuple

### Displaying Multiple Dice Side-by-Side

To show multiple dice horizontally:

```python
# For each line (0 through 4)
for line_index in range(5):
    line = ""
    # For each dice result
    for result in results:
        # Add that dice's line
        line += dice_art[result][line_index] + "  "
    print(line)
```

This builds each horizontal line across all dice before moving to the next line.

### Function Design

```python
def roll_dice(num_dice):
    """Roll the specified number of dice"""
    # 1. Validate input
    # 2. Generate random results
    # 3. Display results
    # 4. Calculate and show total
```

Functions make code:
- **Reusable** - call multiple times
- **Organized** - clear purpose
- **Testable** - easy to verify behavior
- **Maintainable** - changes in one place

### Input Validation

Always validate user input:

```python
if num_dice < 1:
    print("Please enter a valid number (1 or more)")
    return  # Exit function early
```

### Program Flow

1. **Setup** - Define dice_art dictionary with all 6 faces
2. **Main Loop** - While user wants to continue:
   - Prompt for number of dice
   - Validate input (numeric, >= 1)
   - Generate random rolls
   - Display ASCII dice art
   - Show individual results and total
   - Ask to roll again
3. **Exit** - Graceful goodbye message

### Why Use Tuples for Dice Art?

```python
# Each dice face is a tuple of 5 strings
dice_face = (
    "┌─────────┐",  # Line 0
    "│  ●   ●  │",  # Line 1
    "│    ●    │",  # Line 2
    "│  ●   ●  │",  # Line 3
    "└─────────┘"   # Line 4
)

# Access specific line
print(dice_face[2])  # Middle line
```

Tuples ensure:
- **Immutable** - dice faces never change
- **Indexed** - easy to access by line number
- **Grouped** - all 5 lines stay together

## Examples

### Example 1: Basic Unicode Characters
```python
# Box drawing characters
print("┌─────────┐")
print("│  Hello  │")
print("└─────────┘")

# Bullet for dice dots
print("●")

# Create simple dice face manually
print("┌─────────┐")
print("│    ●    │")
print("│    ●    │")
print("│    ●    │")
print("└─────────┘")
```

### Example 2: Storing Dice Art in Tuple
```python
# Single dice face as tuple of strings
dice_one = (
    "┌─────────┐",
    "│         │",
    "│    ●    │",
    "│         │",
    "└─────────┘"
)

# Display the dice
for line in dice_one:
    print(line)

# Output:
# ┌─────────┐
# │         │
# │    ●    │
# │         │
# └─────────┘
```

### Example 3: Dictionary of Dice Faces
```python
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
        "└─────────┘")
}

# Display dice showing 1
for line in dice_art[1]:
    print(line)

# Display dice showing 2
for line in dice_art[2]:
    print(line)
```

### Example 4: Rolling Random Dice
```python
import random

dice_art = {
    1: ("┌─────────┐", "│         │", "│    ●    │", 
        "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │",
        "│      ●  │", "└─────────┘"),
    # ... add more
}

# Roll random die
roll = random.randint(1, 6)
print(f"You rolled: {roll}\n")

for line in dice_art[roll]:
    print(line)
```

### Example 5: Displaying Multiple Dice Side-by-Side
```python
import random

dice_art = {
    1: ("┌─────────┐", "│         │", "│    ●    │", 
        "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │",
        "│      ●  │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●      │", "│    ●    │",
        "│      ●  │", "└─────────┘")
}

# Roll 3 dice
results = [random.randint(1, 3) for _ in range(3)]
print(f"Results: {results}\n")

# Display side by side
for line_idx in range(5):
    line = ""
    for result in results:
        line += dice_art[result][line_idx] + "  "
    print(line)

# Example output (rolling 2, 1, 3):
# ┌─────────┐  ┌─────────┐  ┌─────────┐
# │  ●      │  │         │  │  ●      │
# │         │  │    ●    │  │    ●    │
# │      ●  │  │         │  │      ●  │
# └─────────┘  └─────────┘  └─────────┘
```

### Example 6: Simple Dice Roller Function
```python
import random

def roll_dice(num_dice=1):
    """Roll specified number of dice and return results"""
    if num_dice < 1:
        print("Must roll at least 1 die!")
        return []
    
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6))
    
    return results

# Roll 2 dice
results = roll_dice(2)
print(f"You rolled: {results}")
print(f"Total: {sum(results)}")

# Roll 5 dice
results = roll_dice(5)
print(f"You rolled: {results}")
print(f"Total: {sum(results)}")
```

### Example 7: Complete Dice Roller (Simplified)
```python
import random

# Complete dice art dictionary
dice_art = {
    1: ("┌─────────┐", "│         │", "│    ●    │", 
        "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │",
        "│      ●  │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●      │", "│    ●    │",
        "│      ●  │", "└─────────┘"),
    4: ("┌─────────┐", "│  ●   ●  │", "│         │",
        "│  ●   ●  │", "└─────────┘"),
    5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │",
        "│  ●   ●  │", "└─────────┘"),
    6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │",
        "│  ●   ●  │", "└─────────┘")
}

def roll_dice(num_dice):
    """Roll dice and display results"""
    if num_dice < 1:
        print("❌ Please enter at least 1 die")
        return
    
    # Generate rolls
    results = [random.randint(1, 6) for _ in range(num_dice)]
    
    # Display header
    print("\n" + "="*50)
    print(f"🎲 Rolling {num_dice} dice...")
    print("="*50 + "\n")
    
    # Display dice art side by side
    for line_idx in range(5):
        line = ""
        for result in results:
            line += dice_art[result][line_idx] + "  "
        print(line)
    
    # Display results
    print("\n" + "="*50)
    print(f"Results: {results}")
    print(f"Total: {sum(results)}")
    print("="*50 + "\n")

# Main program
print("🎲 Welcome to Dice Roller! 🎲\n")

while True:
    try:
        num = input("How many dice? (or 'q' to quit): ").strip()
        
        if num.lower() == 'q':
            print("Thanks for playing! 👋")
            break
        
        num = int(num)
        roll_dice(num)
        
    except ValueError:
        print("❌ Please enter a valid number!\n")
```

## Practice Exercises

### Beginner Level

1. **Single Die Display**: Create a program that displays one random dice face using ASCII art.

2. **All Faces**: Display all 6 dice faces (1 through 6) one after another.

3. **Two Dice**: Roll two dice and display them side-by-side with their total.

4. **Input Practice**: Ask user for a number and display that specific dice face (1-6).

5. **Sum Calculator**: Roll 3 dice, display the results as numbers (not art yet), and show the total.

### Intermediate Level

6. **Dice Statistics**: Roll a die 100 times and show how many times each number (1-6) appeared.

7. **Yahtzee Checker**: Roll 5 dice and check if you got Yahtzee (all same number).

8. **Doubles Detector**: Roll 2 dice repeatedly until you get doubles (both same).

9. **Target Sum**: Keep rolling 2 dice until their sum equals a target number (e.g., 7).

10. **Custom Dice**: Create 8-sided or 10-sided dice with appropriate ASCII art.

### Advanced Level

11. **Dice Game (Pig)**: Implement the dice game "Pig" where players accumulate points but risk losing them.

12. **Probability Visualizer**: Roll 2 dice 1000 times and create a histogram showing sum distribution.

13. **Colored Dice**: Use ANSI color codes to display dice in different colors.

14. **3D Dice Animation**: Create an animation effect that simulates dice tumbling before showing result.

15. **Dice RPG Battle System**: Create a turn-based battle system using different dice types (d4, d6, d8, d12, d20).

## Common Mistakes to Avoid

### Mistake 1: Incorrect Line Indexing

**Wrong:**
```python
# Only 3 lines (missing top and bottom)
dice_face = (
    "│  ●   ●  │",
    "│    ●    │",
    "│  ●   ●  │"
)

for line_idx in range(5):  # Trying to access 5 lines!
    print(dice_face[line_idx])  # IndexError!
```

**Correct:**
```python
# All 5 lines included
dice_face = (
    "┌─────────┐",  # Line 0
    "│  ●   ●  │",  # Line 1
    "│    ●    │",  # Line 2
    "│  ●   ●  │",  # Line 3
    "└─────────┘"   # Line 4
)

for line_idx in range(5):
    print(dice_face[line_idx])
```

**Why:** Each dice face must have exactly 5 lines for proper display.

### Mistake 2: Not Adding Spacing Between Dice

**Wrong:**
```python
for line_idx in range(5):
    line = ""
    for result in results:
        line += dice_art[result][line_idx]  # No space!
    print(line)

# Output: dice are squished together
# ┌─────────┐┌─────────┐┌─────────┐
```

**Correct:**
```python
for line_idx in range(5):
    line = ""
    for result in results:
        line += dice_art[result][line_idx] + "  "  # Add spacing
    print(line)

# Output: dice are properly spaced
# ┌─────────┐  ┌─────────┐  ┌─────────┐
```

**Why:** Need spacing between dice for readability.

### Mistake 3: Using List Instead of Tuple

**Wrong:**
```python
dice_art = {
    1: ["┌─────────┐", "│    ●    │", "└─────────┘"]  # List!
}
# Works but semantically wrong - dice faces shouldn't change
```

**Correct:**
```python
dice_art = {
    1: ("┌─────────┐", "│    ●    │", "└─────────┘")  # Tuple!
}
# Better - signals immutability
```

**Why:** Tuples better represent immutable data that won't change.

### Mistake 4: Not Validating Number of Dice

**Wrong:**
```python
def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    # If num_dice is 0 or negative, creates empty or invalid list!
```

**Correct:**
```python
def roll_dice(num_dice):
    if num_dice < 1:
        print("Must roll at least 1 die!")
        return
    results = [random.randint(1, 6) for _ in range(num_dice)]
```

**Why:** Always validate input to prevent invalid states.

## Real-World Applications

### 1. **Tabletop RPG Helpers**
Digital dice rollers for Dungeons & Dragons and other RPGs support complex dice notation (3d6+2, 1d20, etc.), track critical hits, and maintain roll history.

### 2. **Board Game Apps**
Digital versions of board games like Monopoly, Backgammon, and Yahtzee use dice rollers with visual representations to simulate physical gameplay.

### 3. **Probability Education**
Educational software uses dice simulations to teach statistics, probability distributions, and the law of large numbers through interactive experiments.

### 4. **Random Number Visualization**
Data visualization tools use dice-like visual representations to make random number generation more intuitive and engaging for users.

## Challenge Projects

### 1. **Yahtzee Game**
Implement the complete Yahtzee game with scoring.

**Requirements:**
- Roll 5 dice per turn
- Allow selecting dice to keep and re-rolling others (up to 3 rolls)
- Score categories (three of a kind, full house, etc.)
- Track scorecard
- Multi-player support

### 2. **Farkle Dice Game**
Create the popular dice game Farkle.

**Requirements:**
- Roll 6 dice
- Score combinations (straights, triples, etc.)
- Risk management (keep scoring dice or re-roll)
- Banking points vs going bust
- Multi-player turns

### 3. **Dice Probability Simulator**
Educational tool for teaching probability.

**Requirements:**
- Roll any number of dice thousands of times
- Display results in histogram
- Show theoretical vs actual probabilities
- Calculate expected value
- Support different dice types (d4, d6, d8, d12, d20)

### 4. **Animated Dice Roller**
Create dice with rolling animation.

**Requirements:**
- Show dice "tumbling" with changing faces
- Sound effects for rolling
- Physics-based final position
- Multiple dice with individual animations
- Slow-motion replay option

### 5. **RPG Combat Simulator**
Full combat system using various dice types.

**Requirements:**
- Characters with stats and HP
- Attack rolls (d20 + modifiers)
- Damage rolls (various dice types)
- Critical hits and fumbles
- Status effects
- Turn-based combat log

---

## Navigation

- **Previous:** [29. Rock Paper Scissors Game](../29-rock-paper-scissors-game/README.md)
- **Next:** [31. Functions](../31-functions/README.md)
- **[Back to Main README](../README.md)**
