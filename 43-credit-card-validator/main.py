# Credit Card Validator using Luhn Algorithm

def validate_card(card_number):
    """
    Validate credit card number using Luhn algorithm
    Returns: (is_valid, message, card_type)
    """
    # Remove spaces and hyphens
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check if all characters are digits
    if not card_number.isdigit():
        return False, "Card number must contain only digits", None
    
    # Check length
    if len(card_number) < 13 or len(card_number) > 19:
        return False, "Card number must be between 13 and 19 digits", None
    
    # Identify card type
    card_type = get_card_type(card_number)
    
    # Luhn Algorithm
    # Step 1: Remove last digit (check digit)
    check_digit = int(card_number[-1])
    
    # Step 2: Convert remaining digits to list of integers
    digits = [int(d) for d in card_number[:-1]]
    
    # Step 3: Reverse the digits
    digits.reverse()
    
    # Step 4: Double every second digit
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        # If doubled digit is greater than 9, subtract 9
        if digits[i] > 9:
            digits[i] -= 9
    
    # Step 5: Sum all digits
    total = sum(digits)
    
    # Step 6: Add the check digit
    total += check_digit
    
    # Step 7: Check if divisible by 10
    if total % 10 == 0:
        return True, "Valid card number", card_type
    else:
        return False, "Invalid card number (failed Luhn check)", card_type


def get_card_type(card_number):
    """Identify the card type based on the first digits"""
    if card_number.startswith('4'):
        return "Visa"
    elif card_number.startswith(('51', '52', '53', '54', '55')):
        return "Mastercard"
    elif card_number.startswith(('34', '37')):
        return "American Express"
    elif card_number.startswith('6'):
        return "Discover"
    else:
        return "Unknown"


def mask_card_number(card_number):
    """Mask card number for display (show first 4 and last 4 digits)"""
    card_number = card_number.replace(" ", "").replace("-", "")
    if len(card_number) >= 8:
        return f"{card_number[:4]} {'*' * (len(card_number) - 8)} {card_number[-4:]}"
    return card_number


# Main program
print("💳 Credit Card Validator")
print("=" * 50)
print("Using Luhn Algorithm (Mod 10)\n")

while True:
    card = input("Enter card number (or 'quit' to exit): ").strip()
    
    if card.lower() == 'quit':
        print("\nThank you for using Credit Card Validator!")
        break
    
    if not card:
        print("❌ Please enter a card number\n")
        continue
    
    # Validate the card
    is_valid, message, card_type = validate_card(card)
    
    # Display results
    print("\n" + "=" * 50)
    print(f"Card Number: {mask_card_number(card)}")
    
    if card_type:
        print(f"Card Type:   {card_type}")
    
    if is_valid:
        print(f"Status:      ✅ {message}")
    else:
        print(f"Status:      ❌ {message}")
    
    print("=" * 50 + "\n")


# Test with some example numbers (for educational purposes only)
# Valid test numbers:
# Visa: 4532015112830366
# Mastercard: 5425233430109903
# American Express: 374245455400126
# Discover: 6011000991300009
