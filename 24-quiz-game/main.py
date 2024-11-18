questions = ("how many elements are in periodic table?", 
             "which animal lays the largest eggs?", 
             "what is the most abundant gas in earth's atmosphere?", 
             "how many bones are in human body?",
             "which planet in the solar system is the hottest"
)

options = (
    ("A. 118", "B. 108", "C. 128", "D. 98"),
    ("A. ostrich", "B. whale", "C. elephant", "D. giraffe"),
    ("A. oxygen", "B. nitrogen", "C. carbon dioxide", "D. argon"),
    ("A. 206", "B. 208", "C. 210", "D. 212"),
    ("A. mercury", "B. venus", "C. earth", "D. mars")
)

answers = ("A", "A", "B", "A", "B")
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

