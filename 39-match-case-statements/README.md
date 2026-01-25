# 🔀 Match Case Statements


## 📺 Video Tutorial

**Learn Python MATCH-CASE STATEMENTS in 5 minutes! 📆** (5:46)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/L7tT0NZF-Ag)


## What You'll Learn

In this chapter, you'll learn about match-case statements (introduced in Python 3.10) - a powerful alternative to multiple if-elif-else chains. You'll discover how to write cleaner, more readable conditional logic using pattern matching, handle multiple values with the OR operator, and implement sophisticated matching patterns that go beyond simple value comparisons.

## Learning Objectives

- Understand match-case syntax introduced in Python 3.10+
- Replace complex if-elif chains with cleaner match-case statements
- Use the `|` (OR) operator to combine multiple cases
- Implement the wildcard `_` pattern as a default case
- Apply pattern matching to various data types
- Recognize when match-case is more appropriate than if-elif

## Concept Explanation

### What are Match-Case Statements?

Match-case statements (also called "structural pattern matching") provide a cleaner way to handle multiple conditional branches. They're similar to `switch` statements in other programming languages but more powerful.

**Old Way (if-elif-else):**
```python
def day_of_week(day):
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "Invalid day"
```

**New Way (match-case):**
```python
def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:  # Default case (wildcard)
            return "Invalid day"
```

### Basic Syntax

```python
match value:
    case pattern1:
        # code for pattern1
    case pattern2:
        # code for pattern2
    case _:
        # default case (optional)
```

**Key Components:**
- `match` - Keyword to start match statement
- `value` - Expression to match against
- `case` - Keyword for each pattern
- `_` - Wildcard that matches anything (default case)

### The Wildcard Pattern (_)

The underscore `_` acts as a default case that matches anything:

```python
match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:  # Catches everything else
        print("Unknown status")
```

### Combining Cases with | (OR)

Use `|` to match multiple values in one case:

```python
match day:
    case "Saturday" | "Sunday":
        print("Weekend!")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Invalid day")
```

This is much cleaner than:
```python
if day in ["Saturday", "Sunday"]:
    print("Weekend!")
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Weekday")
```

### When to Use Match-Case

**Use match-case when:**
1. You have many (3+) conditions on the same value
2. Checking discrete values (not ranges)
3. Want cleaner, more readable code
4. Using Python 3.10+

**Use if-elif when:**
1. Range comparisons (`if x > 10`)
2. Multiple different conditions
3. Need to support Python < 3.10
4. Only 1-2 conditions

### Match-Case vs If-Elif

```python
# Range check - use if-elif
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"

# Discrete values - use match-case
match command:
    case "start":
        start_game()
    case "stop":
        stop_game()
    case "pause":
        pause_game()
```

### Advanced Pattern Matching

**Match with Conditions (Guards):**
```python
match value:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case _:
        print("Zero")
```

**Match Sequences:**
```python
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

**Match Types:**
```python
match value:
    case int():
        print("It's an integer")
    case str():
        print("It's a string")
    case list():
        print("It's a list")
    case _:
        print("Unknown type")
```

## Examples

### Example 1: HTTP Status Codes
```python
def get_status_message(status_code):
    """Return message for HTTP status code."""
    match status_code:
        case 200:
            return "OK - Success"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"

print(get_status_message(200))  # OK - Success
print(get_status_message(404))  # Not Found
print(get_status_message(999))  # Unknown Status Code
```

### Example 2: Weekend/Weekday Checker
```python
def is_weekend(day):
    """
    Check if a day is a weekend.
    
    Parameters:
        day (str): Name of the day
    
    Returns:
        bool: True if weekend, False if weekday
    """
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False  # Invalid day

print(is_weekend("Saturday"))   # True
print(is_weekend("Monday"))     # False
print(is_weekend("Sunday"))     # True
print(is_weekend("InvalidDay")) # False
```

### Example 3: Calculator
```python
def calculate(num1, num2, operation):
    """
    Perform calculation based on operation.
    
    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation (+, -, *, /, **, %)
    
    Returns:
        float or str: Result or error message
    """
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        case "**":
            return num1 ** num2
        case "%":
            return num1 % num2
        case _:
            return "Error: Unknown operation"

print(calculate(10, 5, "+"))   # 15
print(calculate(10, 5, "*"))   # 50
print(calculate(10, 0, "/"))   # Error: Division by zero
print(calculate(10, 5, "^"))   # Error: Unknown operation
```

### Example 4: Traffic Light System
```python
def traffic_light_action(color):
    """
    Return action for traffic light color.
    
    Parameters:
        color (str): Traffic light color
    
    Returns:
        str: Action to take
    """
    match color.lower():
        case "red":
            return "STOP"
        case "yellow" | "amber":
            return "SLOW DOWN"
        case "green":
            return "GO"
        case _:
            return "INVALID COLOR"

print(traffic_light_action("Red"))     # STOP
print(traffic_light_action("Green"))   # GO
print(traffic_light_action("Yellow"))  # SLOW DOWN
print(traffic_light_action("Amber"))   # SLOW DOWN
print(traffic_light_action("Blue"))    # INVALID COLOR
```

### Example 5: Grade Letter System
```python
def number_to_letter_grade(score):
    """
    Convert numeric score to letter grade.
    
    Parameters:
        score (int): Score out of 100
    
    Returns:
        str: Letter grade
    """
    match score:
        case s if s >= 90:
            return "A"
        case s if s >= 80:
            return "B"
        case s if s >= 70:
            return "C"
        case s if s >= 60:
            return "D"
        case s if s >= 0:
            return "F"
        case _:
            return "Invalid Score"

print(number_to_letter_grade(95))  # A
print(number_to_letter_grade(82))  # B
print(number_to_letter_grade(65))  # D
print(number_to_letter_grade(-5))  # Invalid Score
```

### Example 6: Menu System
```python
def process_menu_choice(choice):
    """
    Process user menu selection.
    
    Parameters:
        choice (int): Menu option number
    """
    match choice:
        case 1:
            print("Opening new file...")
            return "open"
        case 2:
            print("Saving file...")
            return "save"
        case 3:
            print("Printing document...")
            return "print"
        case 4:
            print("Closing application...")
            return "exit"
        case _:
            print("Invalid option! Please choose 1-4")
            return "invalid"

print("=== FILE MENU ===")
print("1. Open")
print("2. Save")
print("3. Print")
print("4. Exit")

result = process_menu_choice(2)  # Saving file...
result = process_menu_choice(5)  # Invalid option! Please choose 1-4
```

### Example 7: Game Command Parser
```python
def parse_game_command(command):
    """
    Parse and execute game commands.
    
    Parameters:
        command (str): User command
    """
    match command.lower():
        case "north" | "n":
            print("You move north.")
        case "south" | "s":
            print("You move south.")
        case "east" | "e":
            print("You move east.")
        case "west" | "w":
            print("You move west.")
        case "look" | "l":
            print("You look around.")
        case "inventory" | "i":
            print("You check your inventory.")
        case "help" | "h" | "?":
            print("Available commands: north, south, east, west, look, inventory, quit")
        case "quit" | "q" | "exit":
            print("Thanks for playing!")
        case _:
            print("Unknown command. Type 'help' for available commands.")

parse_game_command("north")      # You move north.
parse_game_command("n")          # You move north.
parse_game_command("inventory")  # You check your inventory.
parse_game_command("invalid")    # Unknown command...
```

## Practice Exercises

### Beginner Level

1. **Month Name**: Create a function that converts month number (1-12) to name using match-case.

2. **Rock Paper Scissors**: Implement game logic using match-case for winner determination.

3. **Temperature Unit**: Convert temperatures using match-case for unit selection (C, F, K).

4. **Card Rank**: Map playing card numbers (1-13) to ranks (Ace, 2-10, Jack, Queen, King).

5. **Planet Position**: Return planet name based on position from sun (1-8).

### Intermediate Level

6. **BMI Calculator**: Use match-case to categorize BMI values into underweight, normal, overweight, obese.

7. **File Extension Handler**: Determine file type based on extension using match-case.

8. **HTTP Method Router**: Route HTTP methods (GET, POST, PUT, DELETE) to appropriate handlers.

9. **Chess Piece Mover**: Validate chess moves based on piece type using match-case.

10. **Currency Converter**: Convert between currencies using match-case for currency selection.

### Advanced Level

11. **State Machine**: Implement a finite state machine using match-case for transitions.

12. **Expression Evaluator**: Build a calculator that parses expressions using pattern matching.

13. **JSON Type Handler**: Handle different JSON data types with pattern matching.

14. **Command Line Parser**: Parse command-line arguments using advanced pattern matching.

15. **Protocol Handler**: Route different network protocols to handlers using match-case.

## Common Mistakes to Avoid

### Mistake 1: Using Match-Case in Python < 3.10

**Wrong:**
```python
# SyntaxError in Python 3.9 and earlier
match value:
    case 1:
        print("One")
```

**Correct:**
```python
# Use if-elif for older Python versions
if value == 1:
    print("One")
elif value == 2:
    print("Two")
```

**Why:** Match-case only works in Python 3.10+. Check your Python version first.

### Mistake 2: Forgetting the Wildcard Case

**Wrong:**
```python
match color:
    case "red":
        print("Red")
    case "blue":
        print("Blue")
# No default - what if color is "green"?
```

**Correct:**
```python
match color:
    case "red":
        print("Red")
    case "blue":
        print("Blue")
    case _:  # Handles all other cases
        print("Other color")
```

**Why:** Without `_`, unmatched values fall through silently. Always include a default case.

### Mistake 3: Using Range Comparisons

**Wrong:**
```python
# This doesn't work as expected
match score:
    case > 90:  # SyntaxError
        print("A")
```

**Correct:**
```python
# Use if-elif for range comparisons
if score > 90:
    print("A")
elif score > 80:
    print("B")

# Or use guards in match-case
match score:
    case s if s > 90:
        print("A")
    case s if s > 80:
        print("B")
```

**Why:** Match-case is for exact matches. Use if-elif or guards for ranges.

### Mistake 4: Case Fall-Through Assumption

**Wrong:**
```python
# In some languages, cases "fall through"
# Python match-case does NOT fall through!
match value:
    case 1:
        print("One")
        # No break needed - automatically exits
    case 2:
        print("Two")
```

**Correct:**
```python
# Python match-case automatically breaks
# No fall-through behavior
match value:
    case 1:
        print("One")
        # Automatically exits here
    case 2:
        print("Two")  # Only executes if value is 2
```

**Why:** Unlike C/Java switch, Python's match-case doesn't fall through. Each case is isolated.

## Real-World Applications

### 1. **API Route Handlers**
```python
match request.method:
    case "GET":
        return handle_get(request)
    case "POST":
        return handle_post(request)
    case "DELETE":
        return handle_delete(request)
```

### 2. **State Machines**
```python
match current_state:
    case "idle":
        transition_to_running()
    case "running":
        process_data()
    case "error":
        handle_error()
```

### 3. **Event Handlers**
```python
match event.type:
    case "mouse_click":
        handle_click(event)
    case "key_press":
        handle_key(event)
    case "window_close":
        shutdown()
```

### 4. **Command Dispatchers**
```python
match command:
    case "start":
        start_service()
    case "stop":
        stop_service()
    case "restart":
        restart_service()
```

## Challenge Projects

### 1. **Vending Machine**
Build a vending machine simulator with match-case.

**Requirements:**
- Product selection (1-9)
- Payment processing
- Change calculation
- Error handling
- Inventory management

### 2. **Text Adventure Game**
Create a text adventure using match-case for commands.

**Requirements:**
- Movement commands (n, s, e, w)
- Action commands (take, drop, use)
- Multiple room types
- Inventory system
- Win/lose conditions

### 3. **CLI Tool**
Build a command-line tool with match-case routing.

**Requirements:**
- Multiple commands
- Subcommands
- Help system
- Error handling
- Argument parsing

### 4. **State Machine Calculator**
Implement a calculator with state machine logic.

**Requirements:**
- Different states (entering, operation, result)
- Transition logic with match-case
- Error state handling
- Memory functions
- Operation history

### 5. **Protocol Router**
Create a network protocol router.

**Requirements:**
- Different protocols (HTTP, FTP, SSH, etc.)
- Port routing
- Request parsing
- Response handling
- Logging system

---

## Navigation

- **Previous:** [37. List Comprehensions](../37-list-comprehensions/README.md)
- **Next:** [39. Modules](../39-modules/README.md)
- **[Back to Main README](../README.md)**
