# 🔐 Encryption Program

## 📺 Video Tutorial

**Encryption program in Python 🔐** (9:47)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/vsLBErLWBhA)

## What You'll Learn

In this chapter, you'll build a substitution cipher encryption program that demonstrates cryptographic concepts, string manipulation, character substitution algorithms, and the use of Python's string module. You'll learn how to create encryption keys, map characters between original and encrypted forms, and implement both encryption and decryption processes.

## Learning Objectives

- Understand substitution cipher encryption principles
- Use Python's `string` module for character sets (punctuation, digits, letters)
- Create and manipulate character mapping systems
- Implement character-by-character substitution algorithms
- Use `random.shuffle()` to generate encryption keys
- Build reversible encryption/decryption systems

## Concept Explanation

### What is a Substitution Cipher?

A substitution cipher replaces each character with another character according to a fixed mapping:

```
Original:  a b c d e f g h i j k...
Key:       q w e r t y u i o p a...

"hello" → "itaad" (h→i, e→t, l→a, l→a, o→d)
```

### How It Works

**Encryption Process:**
1. Create list of all possible characters
2. Create shuffled copy as the "key"
3. For each character in message:
   - Find its position in original list
   - Replace with character at same position in key
4. Return encrypted message

**Decryption Process:**
1. For each character in encrypted message:
   - Find its position in key list
   - Replace with character at same position in original list
2. Return decrypted message

### String Module

Python's `string` module provides useful character sets:

```python
import string

string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits        # '0123456789'
string.punctuation   # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

**Building Complete Character Set:**
```python
chars = " " + string.punctuation + string.digits + string.ascii_letters
# Now chars contains: space, all punctuation, all digits, all letters
```

### List vs String Mutability

```python
# Strings are immutable (can't change)
text = "hello"
# text[0] = 'H'  # Error!

# Lists are mutable (can change)
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']
chars[0] = 'H'         # Works! → ['H', 'e', 'l', 'l', 'o']
```

**Why convert to list?**
```python
# Need to shuffle characters for encryption key
chars = list("abcde")
random.shuffle(chars)  # Works! Shuffles the list

# Can't shuffle a string
text = "abcde"
# random.shuffle(text)  # Error! Strings are immutable
```

### Creating the Encryption Key

```python
import random
import string

# Step 1: Build character set
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)  # Convert to list for shuffling

# Step 2: Create key (shuffled copy)
key = chars.copy()   # Make independent copy
random.shuffle(key)  # Shuffle the key

# Now chars and key have same characters but different order
```

**Why use `.copy()`?**
```python
# Without copy - both variables point to same list
chars = [1, 2, 3]
key = chars           # Same list!
random.shuffle(key)   # Shuffles both!

# With copy - independent lists
chars = [1, 2, 3]
key = chars.copy()    # Separate list
random.shuffle(key)   # Only shuffles key
```

### Character Substitution Algorithm

```python
plain_text = "hello"
cipher_text = ""

for letter in plain_text:
    # Find position in original characters
    index = chars.index(letter)
    
    # Replace with character at same position in key
    cipher_text += key[index]
```

**Step-by-step example:**
```
chars = ['a', 'b', 'c', 'd', 'e', ...]
key   = ['q', 'w', 'e', 'r', 't', ...]

Encrypting "bad":
1. 'b' → index 1 in chars → key[1] = 'w'
2. 'a' → index 0 in chars → key[0] = 'q'
3. 'd' → index 3 in chars → key[3] = 'r'

Result: "wqr"
```

### Index Method

```python
my_list = ['a', 'b', 'c', 'd', 'e']

my_list.index('a')  # 0
my_list.index('c')  # 2
my_list.index('e')  # 4
# my_list.index('z')  # ValueError: 'z' is not in list
```

### Security Considerations

**Substitution Cipher Weaknesses:**
1. **Frequency Analysis**: Common letters (E, T, A) appear frequently
2. **Pattern Recognition**: Word patterns remain visible
3. **Known Plaintext**: If any part is known, key can be deduced

**Why it's weak:**
```
Original: "the cat sat on the mat"
Encrypted: "xio esx wsx da xio msx"
           ↓
Pattern "xio" appears 3 times = probably "the"
Can deduce: x=t, i=h, o=e
```

## Examples

### Example 1: Basic Encryption Program

```python
import random
import string

# Build character set
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Create encryption key
key = chars.copy()
random.shuffle(key)

# Encrypt
plain_text = input("Enter message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original: {plain_text}")
print(f"Encrypted: {cipher_text}")
```

### Example 2: Encryption with Decryption

```python
import random
import string

# Setup
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

def encrypt(message):
    """Encrypt a message using the key."""
    cipher = ""
    for letter in message:
        index = chars.index(letter)
        cipher += key[index]
    return cipher

def decrypt(cipher):
    """Decrypt a message using the key."""
    message = ""
    for letter in cipher:
        index = key.index(letter)  # Find in key instead
        message += chars[index]    # Use chars instead
    return message

# Test
message = input("Enter message: ")
encrypted = encrypt(message)
decrypted = decrypt(encrypted)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

### Example 3: Save/Load Encryption Key

```python
import random
import string
import json

def generate_key():
    """Generate new random encryption key."""
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    return chars, key

def save_key(chars, key, filename="key.json"):
    """Save key to file."""
    data = {'chars': chars, 'key': key}
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Key saved to {filename}")

def load_key(filename="key.json"):
    """Load key from file."""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['chars'], data['key']

def encrypt(message, chars, key):
    """Encrypt message."""
    cipher = ""
    for letter in message:
        index = chars.index(letter)
        cipher += key[index]
    return cipher

def decrypt(cipher, chars, key):
    """Decrypt message."""
    message = ""
    for letter in cipher:
        index = key.index(letter)
        message += chars[index]
    return message

# Main program
print("1. Generate new key")
print("2. Load existing key")
choice = input("Choice: ")

if choice == "1":
    chars, key = generate_key()
    save_key(chars, key)
else:
    try:
        chars, key = load_key()
        print("Key loaded successfully")
    except FileNotFoundError:
        print("No key file found. Generating new key...")
        chars, key = generate_key()
        save_key(chars, key)

# Encrypt/Decrypt
message = input("\nEnter message: ")
encrypted = encrypt(message, chars, key)
print(f"Encrypted: {encrypted}")

decrypted = decrypt(encrypted, chars, key)
print(f"Decrypted: {decrypted}")
```

### Example 4: Caesar Cipher (Shift-Based)

```python
def caesar_encrypt(text, shift):
    """Encrypt using Caesar cipher (shift each letter)."""
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            
            # Shift character
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted)
        else:
            result += char  # Keep non-letters unchanged
    
    return result

def caesar_decrypt(text, shift):
    """Decrypt Caesar cipher."""
    return caesar_encrypt(text, -shift)  # Decrypt = shift backwards

# Test
message = input("Enter message: ")
shift = int(input("Enter shift amount: "))

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

### Example 5: Interactive Encryption Program

```python
import random
import string

class EncryptionTool:
    def __init__(self):
        chars = " " + string.punctuation + string.digits + string.ascii_letters
        self.chars = list(chars)
        self.key = self.chars.copy()
        random.shuffle(self.key)
    
    def encrypt(self, message):
        """Encrypt a message."""
        result = ""
        for char in message:
            try:
                index = self.chars.index(char)
                result += self.key[index]
            except ValueError:
                result += char  # Keep unknown characters
        return result
    
    def decrypt(self, cipher):
        """Decrypt a message."""
        result = ""
        for char in cipher:
            try:
                index = self.key.index(char)
                result += self.chars[index]
            except ValueError:
                result += char
        return result
    
    def show_key(self):
        """Display encryption key mapping."""
        print("\nEncryption Key Mapping:")
        print("Original → Encrypted")
        print("-" * 30)
        for i, char in enumerate(self.chars[:20]):  # Show first 20
            print(f"'{char}' → '{self.key[i]}'")
        print("...")

def main():
    encryptor = EncryptionTool()
    
    while True:
        print("\n" + "="*40)
        print("ENCRYPTION TOOL")
        print("="*40)
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Show key mapping")
        print("4. Generate new key")
        print("5. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == "1":
            message = input("Enter message to encrypt: ")
            encrypted = encryptor.encrypt(message)
            print(f"Encrypted: {encrypted}")
        
        elif choice == "2":
            cipher = input("Enter message to decrypt: ")
            decrypted = encryptor.decrypt(cipher)
            print(f"Decrypted: {decrypted}")
        
        elif choice == "3":
            encryptor.show_key()
        
        elif choice == "4":
            encryptor = EncryptionTool()
            print("New key generated!")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
```

### Example 6: Vigenère Cipher

```python
def vigenere_encrypt(text, keyword):
    """Encrypt using Vigenère cipher."""
    result = ""
    keyword = keyword.upper()
    keyword_index = 0
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            
            # Get shift amount from keyword
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            
            # Encrypt character
            encrypted = (ord(char) - start + shift) % 26
            result += chr(start + encrypted)
            
            keyword_index += 1
        else:
            result += char
    
    return result

def vigenere_decrypt(text, keyword):
    """Decrypt Vigenère cipher."""
    result = ""
    keyword = keyword.upper()
    keyword_index = 0
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            
            # Get shift amount from keyword
            shift = ord(keyword[keyword_index % len(keyword)]) - ord('A')
            
            # Decrypt character
            decrypted = (ord(char) - start - shift) % 26
            result += chr(start + decrypted)
            
            keyword_index += 1
        else:
            result += char
    
    return result

# Test
message = input("Enter message: ")
keyword = input("Enter keyword: ")

encrypted = vigenere_encrypt(message, keyword)
decrypted = vigenere_decrypt(encrypted, keyword)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

### Example 7: File Encryption

```python
import random
import string
import os

def generate_key():
    """Generate encryption key."""
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    return chars, key

def encrypt_file(input_file, output_file, chars, key):
    """Encrypt entire file."""
    try:
        with open(input_file, 'r') as f:
            content = f.read()
        
        encrypted = ""
        for char in content:
            try:
                index = chars.index(char)
                encrypted += key[index]
            except ValueError:
                encrypted += char
        
        with open(output_file, 'w') as f:
            f.write(encrypted)
        
        print(f"File encrypted: {output_file}")
        return True
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        return False

def decrypt_file(input_file, output_file, chars, key):
    """Decrypt entire file."""
    try:
        with open(input_file, 'r') as f:
            content = f.read()
        
        decrypted = ""
        for char in content:
            try:
                index = key.index(char)
                decrypted += chars[index]
            except ValueError:
                decrypted += char
        
        with open(output_file, 'w') as f:
            f.write(decrypted)
        
        print(f"File decrypted: {output_file}")
        return True
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        return False

# Main program
chars, key = generate_key()

print("FILE ENCRYPTION TOOL")
print("1. Encrypt file")
print("2. Decrypt file")

choice = input("Choice: ")

if choice == "1":
    input_file = input("Input file: ")
    output_file = input("Output file: ")
    encrypt_file(input_file, output_file, chars, key)

elif choice == "2":
    input_file = input("Input file: ")
    output_file = input("Output file: ")
    decrypt_file(input_file, output_file, chars, key)
```

## Practice Exercises

### Beginner Exercises

1. **Simple Letter Shifter**
   - Shift each letter by 3 positions (A→D, B→E, etc.)
   - Handle wrapping (Z→C)
   - Keep spaces and punctuation unchanged

2. **Character Swapper**
   - Swap pairs of characters: ab→ba, cd→dc
   - Handle odd-length strings
   - Reverse to decrypt

3. **Vowel Encryptor**
   - Replace vowels with numbers (a→1, e→2, i→3, o→4, u→5)
   - Keep consonants unchanged
   - Write decrypt function

4. **Reverse Cipher**
   - Reverse the entire message
   - Reverse each word individually
   - Combine both methods

5. **Morse Code**
   - Create dictionary mapping letters to morse code
   - Encrypt text to morse code
   - Decrypt morse code to text

### Intermediate Exercises

1. **Complete Substitution Cipher**
   - Implement full encryption/decryption
   - Save and load keys from files
   - Handle unknown characters gracefully
   - Add brute-force key testing

2. **ROT13 Cipher**
   - Implement ROT13 (shift by 13)
   - Handle uppercase and lowercase
   - Preserve non-alphabetic characters
   - Show that encrypt = decrypt for ROT13

3. **Polyalphabetic Cipher**
   - Use multiple substitution alphabets
   - Rotate between alphabets
   - Stronger than simple substitution
   - Implement decryption

4. **Transposition Cipher**
   - Rearrange character positions
   - Use columnar transposition
   - Handle padding for incomplete columns
   - Write reversal algorithm

5. **Password-Protected Encryption**
   - Generate key from password
   - Use password to seed random generator
   - Decrypt only with correct password
   - Add password strength checking

### Advanced Exercises

1. **Multi-Layer Encryption**
   - Apply multiple encryption methods
   - Substitution + Transposition + Caesar
   - Decrypt in reverse order
   - Compare security vs single method

2. **Frequency Analysis Breaker**
   - Analyze encrypted text letter frequencies
   - Compare to expected English frequencies
   - Suggest possible substitutions
   - Attempt automatic decryption

3. **Stream Cipher Implementation**
   - Generate keystream from seed
   - XOR each character with keystream
   - Implement synchronization
   - Handle stream re-synchronization

4. **File Encryption System**
   - Encrypt/decrypt files of any size
   - Support multiple encryption methods
   - Compress before encrypting
   - Add integrity checking (checksums)

5. **Secure Messaging System**
   - Encrypt messages between users
   - Key exchange system
   - Message authentication
   - Replay attack prevention
   - Message expiration

## Common Mistakes to Avoid

### Mistake 1: Not Using .copy() for Key

❌ **Wrong:**
```python
chars = list("abcdef")
key = chars  # Same list, not a copy!
random.shuffle(key)
# Now both chars and key are shuffled!
```

✅ **Correct:**
```python
chars = list("abcdef")
key = chars.copy()  # Independent copy
random.shuffle(key)
# Only key is shuffled, chars unchanged
```

**Why:** Without `.copy()`, both variables point to the same list. Shuffling one shuffles both.

### Mistake 2: Reversing Encryption and Decryption Logic

❌ **Wrong:**
```python
def decrypt(cipher):
    result = ""
    for char in cipher:
        index = chars.index(char)  # Wrong! Using chars
        result += key[index]       # Should use key.index()
    return result
```

✅ **Correct:**
```python
def decrypt(cipher):
    result = ""
    for char in cipher:
        index = key.index(char)    # Find in key
        result += chars[index]     # Get from chars
    return result
```

**Why:** Decryption is the reverse of encryption. Find position in key, get character from chars.

### Mistake 3: Not Handling Unknown Characters

❌ **Wrong:**
```python
for char in message:
    index = chars.index(char)  # Crashes if char not in chars!
    cipher += key[index]
```

✅ **Correct:**
```python
for char in message:
    try:
        index = chars.index(char)
        cipher += key[index]
    except ValueError:
        cipher += char  # Keep character unchanged
```

**Why:** Messages might contain characters not in your character set. Handle them gracefully.

### Mistake 4: Forgetting random.seed() for Reproducible Keys

❌ **Wrong:**
```python
# Key is different every time - can't decrypt later!
key = chars.copy()
random.shuffle(key)
```

✅ **Correct:**
```python
# Use seed for reproducible key
password = "secret123"
random.seed(password)
key = chars.copy()
random.shuffle(key)
# Same seed always produces same key
```

**Why:** Without saving the key or using a seed, you can't decrypt messages later.

## Real-World Applications

### 1. **Data Security**

Encryption protects sensitive information:

**Examples:**
- Password storage (with hashing)
- File encryption
- Database encryption
- Communication encryption
- Secure backups

**Modern Equivalents:**
- AES (Advanced Encryption Standard)
- RSA (Public-key cryptography)
- SHA (Secure Hash Algorithm)

### 2. **Secure Communication**

Messaging and data transfer:

**Examples:**
- HTTPS web traffic
- Email encryption (PGP)
- Messaging apps (Signal, WhatsApp)
- VPN services
- Secure file transfer

### 3. **Authentication Systems**

Verifying identity:

**Examples:**
- Password authentication
- Digital signatures
- Two-factor authentication
- API key encryption
- Token-based auth

### 4. **Educational Tools**

Teaching cryptography concepts:

**Examples:**
- Cryptography courses
- Security awareness training
- Historical cipher demonstrations
- Puzzle and game design
- STEM education

## Challenge Projects

### 1. **Complete Encryption Suite**

Build multi-method encryption system:

**Requirements:**
- 5+ encryption methods
- Key management system
- File and text encryption
- Password-based key derivation
- Encryption strength comparison
- Brute-force resistance testing
- GUI or menu interface

### 2. **Secure Messaging Application**

Create encrypted chat system:

**Requirements:**
- User registration
- Key exchange protocol
- Message encryption/decryption
- Message history
- Forward secrecy
- Message expiration
- Read receipts
- File attachments

### 3. **Cryptanalysis Tool**

Build cipher-breaking application:

**Requirements:**
- Frequency analysis
- Pattern recognition
- Dictionary attacks
- Brute force testing
- Key suggestions
- Success probability calculator
- Multiple cipher support

### 4. **Password Manager**

Create encrypted password storage:

**Requirements:**
- Master password
- Encrypted password storage
- Password generator
- Category organization
- Search functionality
- Auto-fill simulation
- Password strength meter
- Backup/restore

### 5. **Digital Signature System**

Implement signature verification:

**Requirements:**
- Document signing
- Signature verification
- Public/private key simulation
- Timestamp integration
- Chain of custody
- Tamper detection
- Certificate management

---

## Navigation

← [Previous: 43 - Slot Machine](../43-slot-machine/README.md) | [Next: 45 - Hangman Game](../45-hangman-game/README.md) →

[↑ Back to Main README](../README.md)

## 🎓 Key Takeaways from Video

1. Import modules to use external code
2. Follow along with the video for hands-on practice
3. Experiment with the code examples to deepen understanding

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
