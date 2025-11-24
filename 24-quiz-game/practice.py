
questions = (
    "How many elements are in periodic table?", 
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

for question, answer, option in zip(questions, answers, options):
    print("-------")    
    print(f"Q{question_num + 1}: {question}")
    print("------------------------------------")
    for x in option:
        print(x)
    
    # Validate input
    while True:
        user_selected_option = input("Please select an answer (A/B/C/D): ").upper()
        if user_selected_option in ["A", "B", "C", "D"]:
            break
        print("Invalid choice. Please enter A, B, C, or D.")
    
    print(f"You selected: {user_selected_option}")
    guesses.append(user_selected_option)
    
    if answer == user_selected_option:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {answer}")
    
    question_num += 1

print("#####################################")
print("Your answers:", guesses)
print("Correct answers:", answers)
print(f"Your score is {score}/{len(questions)}")
