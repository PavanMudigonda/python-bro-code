# ============================================
# CHAPTER 42: BANKING PROGRAM
# ============================================
# A complete banking application demonstrating:
# - Global variables for state management
# - Function organization and modularity
# - Exception handling (try-except)
# - Input validation
# - Match-case statements (Python 3.10+)
# - Menu-driven program design
#
# Key Concepts:
# - Global keyword to modify global variables
# - Error handling prevents crashes
# - User-friendly interface with clear prompts
# - Business logic validation (non-negative amounts, sufficient funds)

# =============================================
# GLOBAL STATE VARIABLE
# =============================================
# Global variable to track account balance across all functions
# Must use 'global' keyword inside functions to modify it
balance = 0  # Starting balance of $0

# =============================================
# FUNCTION: SHOW BALANCE
# =============================================
def show_balance():
    """
    Display current account balance.
    Reads global balance variable (no modification).
    """
    print(f"Your current balance is: {balance}")

# =============================================
# FUNCTION: DEPOSIT
# =============================================
def deposit():
    """
    Add money to account balance.
    Uses global keyword to modify balance variable.
    Includes validation and error handling.
    """
    global balance  # Declare we'll modify the global balance
    
    # =============================================
    # TRY-EXCEPT BLOCK FOR ERROR HANDLING
    # =============================================
    try:
        # Get deposit amount from user
        amount_to_deposit = float(input("Enter amount to deposit: "))
        
        # =============================================
        # VALIDATION: Positive Amount Only
        # =============================================
        if amount_to_deposit <= 0:
            print("Entered amount is not valid. Enter a positive amount.")
            return  # Exit function early
        
        # Update balance (modify global variable)
        balance += amount_to_deposit
        print(f"Deposit successful! Your balance is now: {balance}")
        
    # =============================================
    # CATCH INVALID INPUT (non-numeric)
    # =============================================
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# =============================================
# FUNCTION: WITHDRAW
# =============================================
def withdraw():
    """
    Remove money from account balance.
    Includes validation for positive amounts and sufficient funds.
    """
    global balance  # Declare we'll modify the global balance
    
    try:
        # Get withdrawal amount from user
        amount_to_withdraw = float(input("Enter amount to withdraw: "))
        
        # =============================================
        # VALIDATION 1: Positive Amount Only
        # =============================================
        if amount_to_withdraw <= 0:
            print("Entered amount is not valid. Enter a positive amount.")
            return
        
        # =============================================
        # VALIDATION 2: Sufficient Funds Check
        # =============================================
        if amount_to_withdraw > balance:
            print("You don't have sufficient funds to make this withdrawal.")
            return
        
        # Update balance (deduct withdrawal)
        balance -= amount_to_withdraw
        print(f"Withdrawal successful! Your balance is now: {balance}")
        
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# =============================================
# MAIN PROGRAM LOOP
# =============================================
def main():
    """
    Main program loop - displays menu and processes user choices.
    Uses match-case for clean menu handling.
    """
    is_running = True  # Control flag for main loop
    
    while is_running:
        # =============================================
        # DISPLAY MENU
        # =============================================
        print("\nWelcome to XYZ Bank")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        # Get user choice and remove whitespace
        choice = input("Enter your choice (1 - 4): ").strip()
        
        # =============================================
        # PROCESS MENU CHOICE WITH MATCH-CASE
        # =============================================
        match choice:
            case "1":
                show_balance()
            case "2":
                deposit()
            case "3":
                withdraw()
            case "4":
                print("Thank you for banking with us!")
                is_running = False  # Exit loop
            case _:  # Default case (anything else)
                print("Invalid choice. Please enter 1 - 4.")

# =============================================
# PROGRAM ENTRY POINT
# =============================================
# Only run main() if this file is executed directly
# Not if it's imported as a module
if __name__ == "__main__":
    main()
