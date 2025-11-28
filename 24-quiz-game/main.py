# python quiz game.
# use a tuple for questions
# use another tuple for options
# use another tuple for storing actual answers
# use list for guesses

questions = ("How many elements are in periodic table?", 
             "Which animal lays the largest eggs?", 
             "What is the most abundant gas in earth's atmosphere?", 
             "How many bones are in human body?",
             "Which planet in the solar system is the hottest"
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question, option in zip(questions, options):
    print("--------------------")
    print(question)
    for opt in option:
        print(opt)
    guess = input("Enter your guess: ")
    guesses.append(guess)
    if guess.upper() == answers[question_num]:
        score += 1
    question_num += 1

print(f"Your score is {score}/{len(questions)}")

