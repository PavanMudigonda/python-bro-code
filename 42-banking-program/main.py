# Python Banking Program

balance = 0  # global balance

def show_balance():
    print(f"Your current balance is: {balance}")

def deposit():
    global balance
    try:
        amount_to_deposit = float(input("Enter amount to deposit: "))
        if amount_to_deposit <= 0:
            print("Entered amount is not valid. Enter a positive amount.")
            return
        balance += amount_to_deposit
        print(f"Deposit successful! Your balance is now: {balance}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def withdraw():
    global balance
    try:
        amount_to_withdraw = float(input("Enter amount to withdraw: "))
        if amount_to_withdraw <= 0:
            print("Entered amount is not valid. Enter a positive amount.")
            return
        if amount_to_withdraw > balance:
            print("You don't have sufficient funds to make this withdrawal.")
            return
        balance -= amount_to_withdraw
        print(f"Withdrawal successful! Your balance is now: {balance}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def main():
    is_running = True
    while is_running:
        print("\nWelcome to XYZ Bank")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1 - 4): ").strip()
        match choice:
            case "1":
                show_balance()
            case "2":
                deposit()
            case "3":
                withdraw()
            case "4":
                print("Thank you for banking with us!")
                is_running = False
            case _:
                print("Invalid choice. Please enter 1 - 4.")

if __name__ == "__main__":
    main()
