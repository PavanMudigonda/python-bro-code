# ============================================
# CHAPTER 24: QUIZ GAME
# ============================================
# A simple quiz game that demonstrates:
# - Using tuples for storing immutable data
# - Parallel data structures (questions, options, answers)
# - zip() function to iterate over multiple sequences
# - User input validation and scoring
# - List to track user guesses
#
# Key Concepts:
# - Tuples are immutable - perfect for quiz data that shouldn't change
# - zip() allows iterating over multiple iterables simultaneously
# - Parallel data structures keep related data organized
# - Score tracking and percentage calculation

# =============================================
# DATA STRUCTURES SETUP
# =============================================
# Store questions in a tuple (immutable collection)
# Tuples are ideal for data that shouldn't be modified during program execution
questions = ("How many elements are in periodic table?", 
             "Which animal lays the largest eggs?", 
             "What is the most abundant gas in earth's atmosphere?", 
             "How many bones are in human body?",
             "Which planet in the solar system is the hottest"
)

# Store multiple choice options as a tuple of tuples
# Each inner tuple contains the 4 options for one question
# This creates a parallel structure with the questions tuple
options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

# Correct answers stored in a tuple (immutable)
# Matches the order of questions tuple
answers = ("C", "D", "A", "A", "B")

# List to store user's guesses (mutable - we'll add to it)
guesses = []

# Initialize score counter
score = 0

# Track which question we're on
question_num = 0

# =============================================
# QUIZ LOOP - Iterate through all questions
# =============================================
# zip() combines questions and options tuples for parallel iteration
# This allows us to get matching question and its options in each loop
for question, option in zip(questions, options):
    print("--------------------")
    print(question)  # Display the current question
    
    # Display all multiple choice options for this question
    for opt in option:
        print(opt)  # Print each option (A, B, C, D)
    
    # Get user's answer
    guess = input("Enter your guess: ")
    
    # Store the guess in our list for later review
    guesses.append(guess)
    
    # Check if answer is correct (convert to uppercase for comparison)
    if guess.upper() == answers[question_num]:
        score += 1  # Increment score for correct answer
    
    # Move to next question
    question_num += 1

# =============================================
# DISPLAY FINAL SCORE
# =============================================
# Show score as fraction (e.g., "3/5")
# len(questions) gives total number of questions
print(f"Your score is {score}/{len(questions)}")

