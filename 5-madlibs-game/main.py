# ============================================
# Chapter 5: Madlibs Game
# ============================================
# Madlibs is a word game where you create a story by filling in blanks
# with random words without knowing the full context
# This is a fun way to practice user input and string formatting!

# ============================================
# Getting words from the user
# ============================================
# We ask the user for different types of words
adjective1 = input("enter an adjective (description): ")
noun1 = input("enter a noun (person, animal, thing): ")
adjective2 = input("enter another adjective (description): ")
verb1 = input("enter a verb ending with 'ing' (current tense): ")
adjective3 = input("enter a third adjective (description): ")

# ============================================
# Creating the story using the user's words
# ============================================
# We use f-strings to insert the user's words into our story
print(f"today i went to a {adjective1} zoo.")
print(f"in an exhibit, i saw {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

# ============================================
# How this works:
# ============================================
# 1. The program asks for different types of words (adjectives, nouns, verbs)
# 2. The user provides words without knowing the full story
# 3. The program inserts those words into a pre-written story template
# 4. The result is usually funny because of the random word combinations!
#
# Example output:
# "today i went to a smelly zoo."
# "in an exhibit, i saw banana"
# "banana was purple and flying"
# "I was confused!"
