# ============================================
# CHAPTER 27: RANDOM NUMBERS
# ============================================
# The random module provides functions for generating random values
# Essential for:
# - Games (dice, cards, choices)
# - Simulations
# - Random sampling
# - Testing with random data
#
# Key Functions:
# - randint(a, b): Random integer between a and b (inclusive)
# - random(): Random float between 0.0 and 1.0
# - choice(sequence): Random element from a non-empty sequence
# - shuffle(sequence): Shuffle sequence in place

# Import the random module for random number generation
import random

# =============================================
# RANDOM INTEGER - randint()
# =============================================
# Generate random integer in a range (inclusive of both endpoints)
# low = 1
# high = 100
# number = random.randint(low, high)  # Returns integer from 1 to 100

# =============================================
# RANDOM FLOAT - random()
# =============================================
# Generate random float between 0.0 and 1.0 (1.0 not included)
# Useful for probabilities, percentages, etc.
# number = random.random()  # Returns float like 0.7854329

# print(number)

# =============================================
# RANDOM CHOICE - choice()
# =============================================
# Select one random element from a sequence (list, tuple, string)
# Perfect for games like Rock Paper Scissors
options = ["rock", "paper", "scissors"]

# Randomly select one option from the list
option = random.choice(options)
print(option)  # Could print "rock", "paper", or "scissors"

# =============================================
# SHUFFLE - shuffle()
# =============================================
# Randomly reorder elements in a list (modifies the list in place)
# Perfect for shuffling cards, randomizing quiz questions, etc.
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

# Shuffle the cards list randomly
random.shuffle(cards)
print(cards)  # Cards now in random order like ['5', 'K', '2', 'A', ...]