# ============================================
# Chapter 14: String Indexing and Slicing
# ============================================
# Indexing = Accessing elements of a sequence using [] (indexing operator)
# Slicing Syntax: [start : end : step]
# - start: beginning index (inclusive)
# - end: ending index (exclusive)
# - step: interval between indices

credit_card = '4111-1234-5678-1234'

# ============================================
# Single Character Indexing
# ============================================
# Index starts at 0 for the first character
print("First character [0]:", credit_card[0])    # Output: '4'
print("Third character [2]:", credit_card[2])    # Output: '1'

# ============================================
# Slicing - Extract Substring
# ============================================
# [start:end] - from start up to (but not including) end
print("First 4 chars [0:4]:", credit_card[0:4])  # Output: '4111'
print("Characters 5-9 [5:9]:", credit_card[5:9])  # Output: '1234'

# ============================================
# Omitting start or end
# ============================================
# [start:] - from start to the end
print("From index 5 onward [5:]:", credit_card[5:])  # Output: '1234-5678-1234'

# [:end] - from beginning to end (not shown but same as [0:end])
# [:4] would give '4111'

# ============================================
# Negative Indexing
# ============================================
# -1 is the last character, -2 is second to last, etc.
print("Last character [-1]:", credit_card[-1])  # Output: '4'

# ============================================
# Step Parameter
# ============================================
# [::step] - every nth character
print("Every 3rd character [::3]:", credit_card[::3])  # Output: '413-6-2'

# ============================================
# Reverse a String
# ============================================
# [::-1] - step of -1 reverses the string
print("Reversed [::-1]:", credit_card[::-1])  # Output: '4321-8765-4321-1114'

# ============================================
# Indexing Cheat Sheet:
# ============================================
# s[i]      → character at index i
# s[start:end] → substring from start to end-1
# s[start:]    → substring from start to end of string
# s[:end]      → substring from beginning to end-1
# s[:]         → entire string (copy)
# s[-1]        → last character
# s[::step]    → every step-th character
# s[::-1]      → reversed string