# substitution cipher encryption and decryption program
# write the entire user story for this program
# As a user, I want to be able to encrypt and decrypt messages using a substitution cipher
# So that I can securely communicate with others without my messages being easily read by unintended recipients

import random, string

chars = "" + " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key:   {key}")

# ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index_of_letter = chars.index(letter)
    cipher_text += key[index_of_letter]

print(f'original message: {plain_text}')
print(f'encryption message: {cipher_text}')