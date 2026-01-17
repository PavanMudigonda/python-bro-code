# Exception handling - try, except, else, finally

# Basic try-except
def divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid type for division!")

divide(10, 2)   # Result: 5.0
divide(10, 0)   # Error: Cannot divide by zero!
divide(10, "2") # Error: Invalid type for division!

# Multiple exceptions
def safe_conversion(value):
    try:
        num = int(value)
        return num
    except (ValueError, TypeError) as e:
        print(f"Conversion error: {e}")
        return None

print(safe_conversion("42"))    # 42
print(safe_conversion("abc"))   # Conversion error: ...
print(safe_conversion(None))    # Conversion error: ...

# Try-except-else-finally
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        content = None
    except PermissionError:
        print(f"Permission denied for '{filename}'")
        content = None
    else:
        print("File read successfully!")
    finally:
        try:
            file.close()
            print("File closed")
        except:
            pass
    return content

# Raising exceptions
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems invalid")
    return True

try:
    validate_age(25)
    print("Age is valid")
except (TypeError, ValueError) as e:
    print(f"Validation error: {e}")

# Custom exceptions
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Insufficient funds: Balance ${balance}, Requested ${amount}"
        super().__init__(message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Error: {e}")

# Re-raising exceptions
def process_data(data):
    try:
        result = data / 10
    except Exception as e:
        print(f"Logging error: {e}")
        raise  # Re-raise the same exception
    return result

try:
    process_data("invalid")
except TypeError:
    print("Caught re-raised exception")
