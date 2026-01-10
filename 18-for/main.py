# ============================================
# Chapter 18: For Loops
# ============================================
# For loops execute a block of code a fixed number of times
# You can iterate over ranges, strings, lists, and other sequences

# ============================================
# Example 1: Basic range() loop
# ============================================
# range(start, stop) generates numbers from start to stop-1
print("Counting 1 to 9:")
for x in range(1, 10):
    print(x)
print("Done!\n")

# ============================================
# Example 2: Reversed range
# ============================================
# reversed() iterates through the range in reverse order
print("Countdown from 10 to 1:")
for x in reversed(range(1, 11)):
    print(x)
print("Blastoff!\n")

# ============================================
# Example 3: Range with step
# ============================================
# range(start, stop, step) - step determines the increment
print("Odd numbers 1 to 9:")
for x in range(1, 11, 2):  # step of 2 skips even numbers
    print(x)
print("Done!\n")

# ============================================
# Example 4: Iterating over a string
# ============================================
# For loops can iterate over each character in a string
print("Each character in credit card:")
credit_card = '1234-5678-9012-3456'
for x in credit_card:
    print(x, end=' ')  # end=' ' prints on same line
print("\n")

# ============================================
# Example 5: Using continue statement
# ============================================
# continue skips the current iteration and moves to the next
print("Numbers 1-10, skipping 5:")
for x in range(1, 11):
    if x == 5:
        continue  # Skip 5, move to next iteration
    print(x)
print("Done!")

# ============================================
# For Loop Components:
# ============================================
# range(stop)           → 0 to stop-1
# range(start, stop)    → start to stop-1
# range(start, stop, step) → start to stop-1 with increment
# reversed(range(...)) → iterate in reverse
# continue             → skip current iteration
# break                → exit loop early
    