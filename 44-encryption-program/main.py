# ============================================
# CHAPTER 44: ENCRYPTION PROGRAM
# ============================================
# Substitution Cipher Encryption and Decryption
#
# User Story:
# As a user, I want to encrypt and decrypt messages using a substitution cipher
# so that I can securely communicate without messages being easily read by
# unintended recipients.
#
# How Substitution Cipher Works:
# 1. Create list of all possible characters (alphabet)
# 2. Create shuffled "key" - random arrangement of same characters
# 3. Encryption: Replace each character with its corresponding key character
# 4. Decryption: Reverse the process using the key
#
# Example:
# chars: a b c d e f g h...
# key:   q w e r t y u i...
# "bad" encrypts to "wqr"
#
# Key Concepts:
# - String module for character sets
# - List manipulation and copying
# - Random shuffling
# - Character substitution algorithm
# - Index-based mapping

import random
import string

# =============================================
# BUILD CHARACTER SET
# =============================================
# Combine all possible characters:
# - Space character
# - Punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
# - Digits (0-9)
# - ASCII letters (a-z, A-Z)
chars = "" + " " + string.punctuation + string.digits + string.ascii_letters

# Convert string to list for manipulation
# Lists are mutable, strings are not
chars = list(chars)

# =============================================
# CREATE ENCRYPTION KEY
# =============================================
# Make a copy of chars list (not a reference)
# copy() creates independent list
key = chars.copy()

# Randomly shuffle the key
# This creates the substitution cipher mapping
random.shuffle(key)

# =============================================
# DISPLAY CHARACTER MAPPINGS (For debugging)
# =============================================
# Show original characters and their encrypted equivalents
print(f"chars: {chars}")
print(f"key:   {key}")

# =============================================
# ENCRYPTION PROCESS
# =============================================
# Get message from user
plain_text = input("Enter a message to encrypt: ")

# Initialize empty encrypted message
cipher_text = ""

# =============================================
# ENCRYPT EACH CHARACTER
# =============================================
# For each letter in the original message:
for letter in plain_text:
    # Find position of letter in original character set
    # Example: 'a' might be at index 37 in chars
    index_of_letter = chars.index(letter)
    
    # Replace with character at same position in key
    # Example: chars[37] = 'a', key[37] might be 'q'
    # So 'a' gets encrypted to 'q'
    cipher_text += key[index_of_letter]

# =============================================
# DISPLAY RESULTS
# =============================================
print(f'original message: {plain_text}')
print(f'encrypted message: {cipher_text}')

# =============================================
# HOW TO DECRYPT (not implemented here)
# =============================================
# To decrypt, reverse the process:
# for letter in cipher_text:
#     index_of_letter = key.index(letter)  # Find in key
#     decrypted_text += chars[index_of_letter]  # Use chars at same index

# =============================================
# IMPORTANT NOTES
# =============================================
# 1. Both sender and receiver need the SAME KEY
# 2. Key must be kept secret (not shown to others)
# 3. This is a simple cipher - not cryptographically secure
# 4. For real security, use proven encryption libraries