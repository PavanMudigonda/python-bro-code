# 🏦 Banking Program

## What You'll Learn

In this chapter, you'll build a complete banking application that demonstrates professional program design. You'll learn how to manage global state, organize code into functions, handle errors gracefully, validate user input, and create an interactive menu-driven interface using Python's match-case statement. This project brings together multiple concepts to create a real-world application.

## Learning Objectives

- Use global variables to manage application state across functions
- Implement error handling with try-except blocks to prevent crashes
- Validate user input for business logic (positive amounts, sufficient funds)
- Create menu-driven programs with match-case statements (Python 3.10+)
- Design modular functions with clear responsibilities
- Build user-friendly interfaces with informative prompts and error messages

## Concept Explanation

### Program Architecture

The banking program demonstrates professional application structure:

```
┌─────────────────────────┐
│   Global State          │
│   (balance variable)    │
└─────────────────────────┘
           ↓
┌─────────────────────────┐
│   Main Program Loop     │
│   (menu system)         │
└─────────────────────────┘
           ↓
┌─────────────────────────┐
│   Action Functions      │
│   (show/deposit/withdraw)│
└─────────────────────────┘
```

### Global Variables

Global variables maintain state across function calls:

```python
# Global variable - accessible by all functions
balance = 0

def show_balance():
    # Read global variable (no 'global' keyword needed)
    print(f"Balance: ${balance}")

def deposit():
    global balance  # Need 'global' keyword to modify
    balance += 100
```

**When to use `global` keyword:**
- **Reading**: Not needed - functions can read global variables directly
- **Modifying**: Required - must declare `global variable_name` before modifying

```python
balance = 1000

def read_balance():
    # No 'global' needed - just reading
    print(balance)  # Works!

def update_balance():
    # 'global' needed - modifying
    global balance
    balance += 100  # Works!

def broken_update():
    # Forgot 'global' keyword
    balance = balance + 100  # UnboundLocalError!
```

### Error Handling with Try-Except

Prevents crashes from invalid input:

```python
try:
    # Code that might raise an exception
    amount = float(input("Enter amount: "))
    
except ValueError:
    # Handle specific error type
    print("Please enter a valid number")
```

**Exception Handling Flow:**
```
User enters: "abc" → float() raises ValueError → except block catches it → Program continues
User enters: "100" → float() succeeds → except block skipped → Program continues
```

### Input Validation

Multiple layers of validation ensure data integrity:

```python
def deposit():
    global balance
    
    try:
        # Layer 1: Type validation (try-except)
        amount = float(input("Enter amount: "))
        
        # Layer 2: Business logic validation (if statement)
        if amount <= 0:
            print("Amount must be positive")
            return
        
        # All validations passed - proceed
        balance += amount
        
    except ValueError:
        print("Invalid input - please enter a number")
```

**Validation Layers:**
1. **Type Validation**: Is input the correct data type? (try-except)
2. **Range Validation**: Is value in acceptable range? (if statements)
3. **Business Logic**: Does operation make sense? (custom validation)

### Match-Case Statements

Modern menu handling (Python 3.10+):

```python
choice = input("Enter choice (1-4): ")

match choice:
    case "1":
        show_balance()
    case "2":
        deposit()
    case "3":
        withdraw()
    case "4":
        print("Goodbye!")
    case _:  # Default case (like 'else')
        print("Invalid choice")
```

**Match-case vs If-elif:**

```python
# Old way (if-elif)
if choice == "1":
    show_balance()
elif choice == "2":
    deposit()
elif choice == "3":
    withdraw()
else:
    print("Invalid")

# New way (match-case) - cleaner!
match choice:
    case "1": show_balance()
    case "2": deposit()
    case "3": withdraw()
    case _: print("Invalid")
```

### Program Flow

```
Start
  ↓
Initialize balance = 0
  ↓
Main Loop:
  ├─ Display Menu
  ├─ Get user choice
  ├─ Match choice:
  │   ├─ "1" → Show Balance
  │   ├─ "2" → Deposit
  │   ├─ "3" → Withdraw
  │   ├─ "4" → Exit
  │   └─ _   → Invalid
  └─ Repeat until exit
```

### Function Design Principles

Each function has a single, clear responsibility:

```python
def show_balance():
    """Single responsibility: Display balance"""
    print(f"Balance: ${balance}")

def deposit():
    """Single responsibility: Add money"""
    global balance
    try:
        amount = float(input("Enter deposit: "))
        if amount <= 0:
            print("Must be positive")
            return
        balance += amount
    except ValueError:
        print("Invalid input")

def withdraw():
    """Single responsibility: Remove money"""
    global balance
    try:
        amount = float(input("Enter withdrawal: "))
        if amount <= 0:
            print("Must be positive")
            return
        if amount > balance:
            print("Insufficient funds")
            return
        balance -= amount
    except ValueError:
        print("Invalid input")
```

### Business Logic Validation

Banking operations require specific business rules:

**Deposit Rules:**
1. Amount must be numeric (type validation)
2. Amount must be positive (business rule)

**Withdrawal Rules:**
1. Amount must be numeric (type validation)
2. Amount must be positive (business rule)
3. Amount must not exceed balance (business rule)

```python
def withdraw():
    global balance
    
    try:
        amount = float(input("Enter amount: "))
        
        # Business Rule 1: Positive amounts only
        if amount <= 0:
            print("Amount must be positive")
            return
        
        # Business Rule 2: Sufficient funds check
        if amount > balance:
            print("Insufficient funds")
            return
        
        # All rules passed - execute transaction
        balance -= amount
        print(f"Withdrawal successful! Balance: ${balance}")
        
    except ValueError:
        print("Invalid input")
```

### User Experience Considerations

**Clear Prompts:**
```python
# Bad: Confusing
amount = float(input("$: "))

# Good: Clear
amount = float(input("Enter amount to deposit: "))
```

**Informative Feedback:**
```python
# Bad: Silent failure
if amount <= 0:
    return

# Good: Explain what happened
if amount <= 0:
    print("Entered amount is not valid. Enter a positive amount.")
    return
```

**Consistent Formatting:**
```python
# Use consistent currency formatting
print(f"Balance: ${balance:.2f}")  # Always 2 decimal places
```

## Examples

### Example 1: Basic Banking Program (Complete)

```python
# Banking Program - Complete Implementation

balance = 0  # Global variable for account balance

def show_balance():
    """Display current account balance."""
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    """Add money to account with validation."""
    global balance
    
    try:
        amount = float(input("Enter amount to deposit: $"))
        
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        balance += amount
        print(f"Deposit successful! New balance: ${balance:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter a number.")

def withdraw():
    """Remove money from account with validation."""
    global balance
    
    try:
        amount = float(input("Enter amount to withdraw: $"))
        
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        if amount > balance:
            print("Insufficient funds.")
            return
        
        balance -= amount
        print(f"Withdrawal successful! New balance: ${balance:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main program loop with menu."""
    is_running = True
    
    while is_running:
        print("\n" + "="*30)
        print("     SIMPLE BANK")
        print("="*30)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        match choice:
            case "1":
                show_balance()
            case "2":
                deposit()
            case "3":
                withdraw()
            case "4":
                print("\nThank you for banking with us!")
                is_running = False
            case _:
                print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
```

### Example 2: Banking with Transaction History

```python
# Banking with transaction history tracking

balance = 0
transactions = []  # List to store transaction history

def show_balance():
    """Display current balance."""
    print(f"\nCurrent Balance: ${balance:.2f}")

def deposit():
    """Deposit money and record transaction."""
    global balance
    
    try:
        amount = float(input("Enter deposit amount: $"))
        
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        balance += amount
        transactions.append(f"Deposit: +${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
        
    except ValueError:
        print("Invalid input.")

def withdraw():
    """Withdraw money and record transaction."""
    global balance
    
    try:
        amount = float(input("Enter withdrawal amount: $"))
        
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        if amount > balance:
            print(f"Insufficient funds. Available: ${balance:.2f}")
            return
        
        balance -= amount
        transactions.append(f"Withdrawal: -${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
        
    except ValueError:
        print("Invalid input.")

def show_history():
    """Display transaction history."""
    if not transactions:
        print("\nNo transactions yet.")
        return
    
    print("\nTransaction History:")
    print("-" * 30)
    for i, transaction in enumerate(transactions, 1):
        print(f"{i}. {transaction}")

def main():
    """Main program with transaction history."""
    while True:
        print("\n" + "="*30)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("\nChoice: ").strip()
        
        match choice:
            case "1": show_balance()
            case "2": deposit()
            case "3": withdraw()
            case "4": show_history()
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
```

### Example 3: Multi-Account Banking

```python
# Banking system with multiple accounts

accounts = {}  # Dictionary: {account_number: balance}

def create_account():
    """Create a new bank account."""
    account_num = input("Enter account number: ").strip()
    
    if account_num in accounts:
        print("Account already exists!")
        return
    
    try:
        initial = float(input("Initial deposit: $"))
        if initial < 0:
            print("Cannot open account with negative balance.")
            return
        
        accounts[account_num] = initial
        print(f"Account {account_num} created with ${initial:.2f}")
        
    except ValueError:
        print("Invalid amount.")

def show_balance():
    """Show balance for specific account."""
    account_num = input("Enter account number: ").strip()
    
    if account_num not in accounts:
        print("Account not found.")
        return
    
    print(f"Account {account_num} balance: ${accounts[account_num]:.2f}")

def deposit():
    """Deposit to specific account."""
    account_num = input("Enter account number: ").strip()
    
    if account_num not in accounts:
        print("Account not found.")
        return
    
    try:
        amount = float(input("Deposit amount: $"))
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        accounts[account_num] += amount
        print(f"Deposited ${amount:.2f}. New balance: ${accounts[account_num]:.2f}")
        
    except ValueError:
        print("Invalid amount.")

def transfer():
    """Transfer money between accounts."""
    from_acc = input("From account: ").strip()
    to_acc = input("To account: ").strip()
    
    if from_acc not in accounts or to_acc not in accounts:
        print("One or both accounts not found.")
        return
    
    try:
        amount = float(input("Transfer amount: $"))
        
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        if accounts[from_acc] < amount:
            print("Insufficient funds.")
            return
        
        accounts[from_acc] -= amount
        accounts[to_acc] += amount
        print(f"Transferred ${amount:.2f} from {from_acc} to {to_acc}")
        
    except ValueError:
        print("Invalid amount.")

def main():
    """Main program for multi-account banking."""
    while True:
        print("\n" + "="*30)
        print("MULTI-ACCOUNT BANK")
        print("="*30)
        print("1. Create Account")
        print("2. Show Balance")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Exit")
        
        choice = input("\nChoice: ").strip()
        
        match choice:
            case "1": create_account()
            case "2": show_balance()
            case "3": deposit()
            case "4": transfer()
            case "5":
                print("Thank you!")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
```

### Example 4: Banking with Interest

```python
# Banking program with interest calculations

balance = 0.0
interest_rate = 0.02  # 2% annual interest

def show_balance():
    """Display current balance."""
    print(f"Current Balance: ${balance:.2f}")
    print(f"Interest Rate: {interest_rate * 100}%")

def deposit():
    """Deposit money."""
    global balance
    
    try:
        amount = float(input("Deposit amount: $"))
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        balance += amount
        print(f"Deposited ${amount:.2f}")
        
    except ValueError:
        print("Invalid input.")

def withdraw():
    """Withdraw money."""
    global balance
    
    try:
        amount = float(input("Withdrawal amount: $"))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > balance:
            print("Insufficient funds.")
            return
        
        balance -= amount
        print(f"Withdrew ${amount:.2f}")
        
    except ValueError:
        print("Invalid input.")

def apply_interest():
    """Apply interest to current balance."""
    global balance
    
    interest = balance * interest_rate
    balance += interest
    print(f"Interest applied: ${interest:.2f}")
    print(f"New balance: ${balance:.2f}")

def set_interest_rate():
    """Change interest rate."""
    global interest_rate
    
    try:
        rate = float(input("Enter new interest rate (e.g., 0.02 for 2%): "))
        if rate < 0 or rate > 1:
            print("Rate must be between 0 and 1.")
            return
        
        interest_rate = rate
        print(f"Interest rate set to {interest_rate * 100}%")
        
    except ValueError:
        print("Invalid input.")

def main():
    """Main program with interest."""
    while True:
        print("\n" + "="*30)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Apply Interest")
        print("5. Set Interest Rate")
        print("6. Exit")
        
        choice = input("\nChoice: ").strip()
        
        match choice:
            case "1": show_balance()
            case "2": deposit()
            case "3": withdraw()
            case "4": apply_interest()
            case "5": set_interest_rate()
            case "6":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
```

### Example 5: Banking with File Persistence

```python
# Banking with saving/loading from file

import json

balance = 0.0
SAVE_FILE = "bank_data.json"

def load_data():
    """Load balance from file."""
    global balance
    
    try:
        with open(SAVE_FILE, 'r') as f:
            data = json.load(f)
            balance = data.get('balance', 0.0)
        print(f"Loaded balance: ${balance:.2f}")
    except FileNotFoundError:
        print("No saved data found. Starting with $0.")
    except json.JSONDecodeError:
        print("Error reading save file. Starting with $0.")

def save_data():
    """Save balance to file."""
    try:
        with open(SAVE_FILE, 'w') as f:
            json.dump({'balance': balance}, f)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def show_balance():
    """Display balance."""
    print(f"Current Balance: ${balance:.2f}")

def deposit():
    """Deposit money."""
    global balance
    
    try:
        amount = float(input("Deposit: $"))
        if amount <= 0:
            print("Must be positive.")
            return
        
        balance += amount
        save_data()  # Auto-save after transaction
        print(f"Deposited ${amount:.2f}")
        
    except ValueError:
        print("Invalid input.")

def withdraw():
    """Withdraw money."""
    global balance
    
    try:
        amount = float(input("Withdraw: $"))
        if amount <= 0:
            print("Must be positive.")
            return
        if amount > balance:
            print("Insufficient funds.")
            return
        
        balance -= amount
        save_data()  # Auto-save after transaction
        print(f"Withdrew ${amount:.2f}")
        
    except ValueError:
        print("Invalid input.")

def main():
    """Main program with persistence."""
    load_data()  # Load saved data on startup
    
    while True:
        print("\n" + "="*30)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("\nChoice: ").strip()
        
        match choice:
            case "1": show_balance()
            case "2": deposit()
            case "3": withdraw()
            case "4":
                save_data()
                print("Goodbye!")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
```

### Example 6: Banking with Limits

```python
# Banking with withdrawal limits and fees

balance = 0.0
daily_limit = 500.0
daily_withdrawn = 0.0
withdrawal_fee = 2.0

def show_balance():
    """Display balance and limits."""
    print(f"Balance: ${balance:.2f}")
    print(f"Daily limit: ${daily_limit:.2f}")
    print(f"Withdrawn today: ${daily_withdrawn:.2f}")
    print(f"Remaining: ${daily_limit - daily_withdrawn:.2f}")

def deposit():
    """Deposit money."""
    global balance
    
    try:
        amount = float(input("Deposit: $"))
        if amount <= 0:
            print("Must be positive.")
            return
        
        balance += amount
        print(f"Deposited ${amount:.2f}")
        
    except ValueError:
        print("Invalid input.")

def withdraw():
    """Withdraw with limits and fees."""
    global balance, daily_withdrawn
    
    try:
        amount = float(input("Withdraw: $"))
        
        if amount <= 0:
            print("Must be positive.")
            return
        
        # Check daily limit
        if daily_withdrawn + amount > daily_limit:
            remaining = daily_limit - daily_withdrawn
            print(f"Daily limit exceeded. Remaining: ${remaining:.2f}")
            return
        
        # Calculate total with fee
        total = amount + withdrawal_fee
        
        if total > balance:
            print(f"Insufficient funds (amount + ${withdrawal_fee:.2f} fee).")
            return
        
        balance -= total
        daily_withdrawn += amount
        print(f"Withdrew ${amount:.2f} (fee: ${withdrawal_fee:.2f})")
        print(f"New balance: ${balance:.2f}")
        
    except ValueError:
        print("Invalid input.")

def reset_daily_limit():
    """Reset daily withdrawal counter."""
    global daily_withdrawn
    daily_withdrawn = 0.0
    print("Daily limit reset.")

def main():
    """Main program with limits."""
    while True:
        print("\n" + "="*30)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Reset Daily Limit")
        print("5. Exit")
        
        choice = input("\nChoice: ").strip()
        
        match choice:
            case "1": show_balance()
            case "2": deposit()
            case "3": withdraw()
            case "4": reset_daily_limit()
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
```

### Example 7: Banking with PIN Protection

```python
# Banking with PIN authentication

balance = 0.0
pin = "1234"  # In real app, use hashing!
logged_in = False

def login():
    """Authenticate user with PIN."""
    global logged_in
    
    attempts = 3
    
    while attempts > 0:
        entered_pin = input("Enter PIN: ")
        
        if entered_pin == pin:
            logged_in = True
            print("Login successful!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect PIN. {attempts} attempts remaining.")
            else:
                print("Too many failed attempts. Access denied.")
    
    return False

def logout():
    """Logout user."""
    global logged_in
    logged_in = False
    print("Logged out successfully.")

def require_auth(func):
    """Decorator to require authentication."""
    def wrapper():
        if not logged_in:
            print("Please login first.")
            return
        func()
    return wrapper

@require_auth
def show_balance():
    """Display balance (requires auth)."""
    print(f"Balance: ${balance:.2f}")

@require_auth
def deposit():
    """Deposit money (requires auth)."""
    global balance
    
    try:
        amount = float(input("Deposit: $"))
        if amount <= 0:
            print("Must be positive.")
            return
        
        balance += amount
        print(f"Deposited ${amount:.2f}")
        
    except ValueError:
        print("Invalid input.")

@require_auth
def withdraw():
    """Withdraw money (requires auth)."""
    global balance
    
    try:
        amount = float(input("Withdraw: $"))
        if amount <= 0:
            print("Must be positive.")
            return
        if amount > balance:
            print("Insufficient funds.")
            return
        
        balance -= amount
        print(f"Withdrew ${amount:.2f}")
        
    except ValueError:
        print("Invalid input.")

def main():
    """Main program with authentication."""
    while True:
        print("\n" + "="*30)
        print("1. Login")
        print("2. Show Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Logout")
        print("6. Exit")
        
        choice = input("\nChoice: ").strip()
        
        match choice:
            case "1": login()
            case "2": show_balance()
            case "3": deposit()
            case "4": withdraw()
            case "5": logout()
            case "6":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
```

## Practice Exercises

### Beginner Exercises

1. **Simple Counter**
   - Create a global counter variable
   - Functions: increment(), decrement(), show_count(), reset()
   - Menu system with match-case
   - Input validation for increment/decrement amounts

2. **Temperature Manager**
   - Global variable for current temperature
   - Functions: set_temp(), show_temp(), adjust_temp()
   - Validate temperature is reasonable (-50 to 50°C)
   - Display temperature in both Celsius and Fahrenheit

3. **Score Tracker**
   - Global score variable starting at 0
   - Functions: add_points(), subtract_points(), show_score()
   - Prevent negative scores
   - Keep track of high score

4. **To-Do Counter**
   - Global variable for number of tasks
   - Functions: add_task(), complete_task(), show_tasks()
   - Cannot complete more tasks than exist
   - Show completed vs remaining

5. **Basic Calculator**
   - Global result variable
   - Functions: add(), subtract(), multiply(), divide(), clear()
   - Handle division by zero
   - Display running total

### Intermediate Exercises

1. **Enhanced Banking**
   - Add minimum balance requirement ($100)
   - Charge $5 fee for going below minimum
   - Track number of transactions
   - Generate monthly statement

2. **Savings Goal Tracker**
   - Set savings goal amount
   - Track deposits toward goal
   - Show progress percentage
   - Calculate time to reach goal at current rate
   - Prevent withdrawals that break goal progress

3. **Budget Manager**
   - Set monthly budget
   - Track spending in categories (food, transport, etc.)
   - Warn when approaching budget limit
   - Generate spending report
   - Reset monthly

4. **Inventory System**
   - Track multiple items (dictionary)
   - Functions: add_item(), remove_item(), update_quantity()
   - Check stock levels
   - Generate low-stock alerts
   - Calculate total inventory value

5. **Student Grade Manager**
   - Store grades for multiple students (nested dictionary)
   - Add/update/delete grades
   - Calculate averages
   - Generate report cards
   - Find class average

### Advanced Exercises

1. **Complete Banking System**
   - Multiple account types (checking, savings, credit)
   - Different interest rates per account
   - Transaction history with timestamps
   - Export statements to CSV
   - Monthly account fees
   - Overdraft protection

2. **Investment Portfolio Manager**
   - Track multiple investments
   - Calculate portfolio value
   - Show gains/losses
   - Rebalancing recommendations
   - Risk assessment
   - Generate performance reports

3. **Store Management System**
   - Inventory tracking
   - Sales processing
   - Customer loyalty points
   - Discount calculations
   - Daily/weekly/monthly reports
   - Low stock auto-alerts

4. **Library Management**
   - Book checkout/return system
   - Fine calculations for late returns
   - Member management
   - Reservation system
   - Generate usage statistics
   - Database persistence

5. **Restaurant Order System**
   - Menu management
   - Order taking
   - Bill calculation with tax and tip
   - Table management
   - Kitchen order queue
   - Daily sales reports

## Common Mistakes to Avoid

### Mistake 1: Forgetting the global Keyword

❌ **Wrong:**
```python
balance = 0

def deposit():
    # Forgot 'global' keyword
    balance = balance + 100  # UnboundLocalError!
    print(f"Balance: {balance}")

deposit()
```

✅ **Correct:**
```python
balance = 0

def deposit():
    global balance  # Declare we're modifying global variable
    balance = balance + 100
    print(f"Balance: {balance}")

deposit()  # Works correctly
```

**Why:** Without `global`, Python treats `balance` as a local variable, but tries to use it before assignment, causing an error.

### Mistake 2: Not Handling Invalid Input

❌ **Wrong:**
```python
def deposit():
    global balance
    # No error handling - crashes on non-numeric input
    amount = float(input("Enter amount: "))
    balance += amount
```

✅ **Correct:**
```python
def deposit():
    global balance
    
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        balance += amount
        print("Deposit successful!")
        
    except ValueError:
        print("Invalid input. Please enter a number.")
```

**Why:** Users can enter anything. Error handling prevents crashes and provides helpful feedback.

### Mistake 3: Missing Business Logic Validation

❌ **Wrong:**
```python
def withdraw():
    global balance
    
    try:
        amount = float(input("Withdraw: $"))
        # No validation - allows negative amounts and overdrafts!
        balance -= amount
        print(f"Withdrew ${amount}")
        
    except ValueError:
        print("Invalid input.")
```

✅ **Correct:**
```python
def withdraw():
    global balance
    
    try:
        amount = float(input("Withdraw: $"))
        
        # Validate positive amount
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        # Validate sufficient funds
        if amount > balance:
            print(f"Insufficient funds. Available: ${balance:.2f}")
            return
        
        balance -= amount
        print(f"Withdrew ${amount:.2f}")
        
    except ValueError:
        print("Invalid input.")
```

**Why:** Type validation alone isn't enough. Business rules (positive amounts, sufficient funds) must be explicitly checked.

### Mistake 4: Poor User Feedback

❌ **Wrong:**
```python
def deposit():
    global balance
    
    try:
        amount = float(input("$"))  # Unclear prompt
        if amount <= 0:
            return  # Silent failure
        balance += amount
        print("OK")  # Vague feedback
        
    except ValueError:
        print("Error")  # Unhelpful error message
```

✅ **Correct:**
```python
def deposit():
    global balance
    
    try:
        amount = float(input("Enter deposit amount: $"))
        
        if amount <= 0:
            print("Amount must be positive. Please try again.")
            return
        
        balance += amount
        print(f"Successfully deposited ${amount:.2f}")
        print(f"New balance: ${balance:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
```

**Why:** Clear prompts and informative feedback create better user experience and help users understand what went wrong.

## Real-World Applications

### 1. **Financial Management Systems**

Banking programs are the foundation of financial software:

**Examples:**
- ATM software interfaces
- Mobile banking apps
- Personal finance managers
- Accounting software
- Cryptocurrency wallets

**Key Features:**
- Transaction processing with validation
- Balance management
- Security and authentication
- Audit trails and logging
- Regulatory compliance checks

### 2. **Point of Sale (POS) Systems**

Retail and restaurant systems use similar patterns:

**Examples:**
- Cash register software
- Restaurant order systems
- E-commerce checkout
- Inventory management
- Sales tracking

**Key Features:**
- Menu-driven interfaces
- Transaction validation
- Inventory updates
- Receipt generation
- Daily sales reports

### 3. **Resource Management**

Track and manage limited resources:

**Examples:**
- Server resource monitoring
- Cloud computing billing
- Energy usage tracking
- Database connection pools
- API rate limiting

**Key Features:**
- Usage tracking
- Limit enforcement
- Quota management
- Alert systems
- Usage analytics

### 4. **Game Development**

Games use similar state management:

**Examples:**
- Player health/mana systems
- Inventory management
- Currency and shops
- Experience and leveling
- Resource gathering games

**Key Features:**
- State persistence
- Transaction validation
- Balance calculations
- Limit enforcement
- Progress tracking

## Challenge Projects

### 1. **Full-Featured Banking Application**

Build a complete banking system with all the features:

**Requirements:**
- Multiple account types (checking, savings, credit card)
- User authentication with PIN
- Transaction history with timestamps
- Interest calculations
- Monthly statements
- Bill pay functionality
- Account transfers
- ATM simulation with daily limits
- Data persistence (JSON or SQLite)
- Error logging

**Skills Applied:**
- Global state management
- Complex validation logic
- File I/O
- Date/time handling
- Report generation

### 2. **Restaurant Management System**

Create a complete restaurant order and management system:

**Requirements:**
- Table management (open/close tables)
- Menu with prices and categories
- Order taking and modification
- Bill calculation (tax, tip, split bill)
- Kitchen display system
- Inventory tracking
- Daily sales reports
- Employee shift tracking
- Reservation system

**Skills Applied:**
- Multi-entity state management
- Complex calculations
- Time-based operations
- Report generation

### 3. **Personal Budget Tracker**

Build a comprehensive budgeting application:

**Requirements:**
- Multiple budget categories
- Income and expense tracking
- Recurring transactions
- Budget vs actual comparison
- Spending alerts and warnings
- Monthly/yearly reports
- Goal setting and tracking
- Data visualization (charts)
- Export to CSV/Excel
- Multi-user support

**Skills Applied:**
- Category management
- Time series data
- Calculations and analytics
- Data export
- User preferences

### 4. **Inventory Management System**

Create a warehouse/store inventory system:

**Requirements:**
- Product database with SKUs
- Stock level tracking
- Purchase orders
- Sales processing
- Low stock alerts
- Supplier management
- Price management
- Stock valuation
- Inventory reports
- Barcode support (simulation)

**Skills Applied:**
- Complex data structures
- Business logic validation
- Reporting
- Alert systems

### 5. **Cryptocurrency Portfolio Manager**

Build a crypto trading and tracking system:

**Requirements:**
- Multiple cryptocurrency support
- Buy/sell transactions
- Portfolio value calculation
- Profit/loss tracking
- Price alerts
- Transaction fees
- Historical data
- Performance analytics
- Risk assessment
- Tax reporting

**Skills Applied:**
- Financial calculations
- Real-time data (simulated)
- Complex reporting
- Multi-currency handling

---

## Navigation

← [Previous: 41 - If Name Main](../41-if-name-main/README.md) | [Next: 43 - Slot Machine](../43-slot-machine/README.md) →

[↑ Back to Main README](../README.md)
