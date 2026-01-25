# Chapter 16: While Loops

## 📺 Video Tutorial

**While loops in Python are easy! ♾️** (8:04)

[![Watch on YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/rRTjPnVooxE)

## 📚 What You'll Learn
Execute code repeatedly while a condition is true - essential for creating interactive programs!

## 🎯 Learning Objectives
- Understand while loop syntax
- Create loops with conditions
- Use while loops for user input validation
- Avoid infinite loops
- Use break and continue statements

## 📖 Concept Explanation

### What is a While Loop?
A while loop repeatedly executes code as long as a condition remains True.

### Syntax
```python
while condition:
    # code to execute
    # update condition eventually!
```

### How It Works
1. Check if condition is True
2. If True, execute the code block
3. Go back to step 1
4. If False, exit the loop

## 💡 Examples

### Example 1: Age Verification
```python
age = int(input("Enter your age: "))

while age < 18:
    print("You are a minor")
    age = int(input("Enter your age: "))

print("You are an adult!")
```

### Example 2: Countdown
```python
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blastoff!")
```

### Example 3: Sum Numbers Until Zero
```python
total = 0
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))

print(f"Total: {total}")
```

### Example 4: Password Validator
```python
password = input("Enter password: ")

while len(password) < 8:
    print("Password must be at least 8 characters!")
    password = input("Enter password: ")

print("Password accepted!")
```

## ✍️ Practice Exercises

1. Create a number guessing game
2. Keep asking for positive numbers until user enters negative
3. Validate email format (must contain @)
4. Create a simple menu system
5. Build a countdown timer
6. Make a multiplication drill program

## 📝 Loop Control Statements

### break - Exit Loop Early
```python
count = 0
while True:  # Infinite loop
    count += 1
    if count > 5:
        break  # Exit loop
    print(count)
# Prints: 1, 2, 3, 4, 5
```

### continue - Skip Current Iteration
```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)
# Prints: 1, 3, 5, 7, 9
```

## 🔍 Common Mistakes

### Infinite Loops
```python
# Wrong: Condition never becomes False
count = 1
while count > 0:
    print(count)  # Runs forever!

# Correct: Update condition
count = 5
while count > 0:
    print(count)
    count -= 1  # Eventually becomes 0
```

## 🎮 Real-World Examples

### ATM Machine
```python
balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        print(f"Balance: ${balance}")
    elif choice == "2":
        amount = float(input("Amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds")
    elif choice == "3":
        break
    else:
        print("Invalid choice")
```

## 🚀 Challenge Projects

1. **Login System**: 3 attempts before lockout
2. **Shopping Cart**: Add items until user is done
3. **Grade Calculator**: Keep accepting scores until user enters "done"
4. **Dice Game**: Roll until you get 6
5. **Calculator Loop**: Perform calculations until user quits

## 🎓 Key Takeaways from Video

1. Strings are text data enclosed in quotes
2. Use loops to repeat actions
3. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter
Continue to [Chapter 17: Interest Calculator](../17-interest-calculator/) to build a compound interest calculator!

