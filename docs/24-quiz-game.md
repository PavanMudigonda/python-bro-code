# 🎯 Quiz Game

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/24-quiz-game/24-quiz-game.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/24-quiz-game/24-quiz-game.ipynb)


## 📺 Video Tutorial

**Create a QUIZ GAME with Python 💯** (14:14)

## What You'll Learn

In this chapter, you'll build an interactive quiz game that demonstrates how to work with tuples for immutable data storage, use the zip() function to iterate over multiple sequences simultaneously, and implement scoring systems with user input validation.

## Learning Objectives

- Use tuples to store immutable quiz data (questions, options, answers)
- Implement parallel data structures with multiple tuples
- Master the zip() function for iterating over multiple sequences
- Build scoring systems with accurate tracking
- Validate user input and handle case-insensitive comparisons
- Create engaging interactive programs with feedback

## Concept Explanation

### What is a Quiz Game?

A quiz game presents questions to users, collects their answers, compares them to correct answers, and provides a score. This project demonstrates proper data organization, user interaction, and score tracking.

### Why Use Tuples for Quiz Data?

**Tuples** are immutable sequences - once created, they cannot be modified. This makes them perfect for quiz data because:

1. **Data Integrity** - Questions and answers shouldn't change during the game
2. **Performance** - Tuples are faster and use less memory than lists
3. **Safety** - Prevents accidental modification of quiz content
4. **Intent** - Signals to other programmers that this data is constant

```python
# Tuple (immutable) - perfect for quiz data
questions = ("What is 2+2?", "What is the capital of France?")

# List (mutable) - for data that needs to change
guesses = []  # Will store user's answers
```

### Parallel Data Structures

The quiz uses three parallel tuples that must stay synchronized:

```python
questions = ("Question 1?", "Question 2?")
options = (
    ("A. Ans1", "B. Ans2", "C. Ans3", "D. Ans4"),
    ("A. Ans1", "B. Ans2", "C. Ans3", "D. Ans4")
)
answers = ("A", "C")

# Index 0: Question 1, its options, and its answer
# Index 1: Question 2, its options, and its answer
```

### The zip() Function

**zip()** is a powerful function that combines multiple iterables into tuples:

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

# zip() pairs them together
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Output:
# Alice: 95
# Bob: 87
# Charlie: 92
```

In our quiz, zip() pairs questions with their options:

```python
for question, option in zip(questions, options):
    print(question)      # Current question
    for opt in option:   # Its four options
        print(opt)
```

### Program Flow

1. **Setup** - Define questions, options, answers in tuples
2. **Initialize** - Create empty guesses list and score counter
3. **Loop** - For each question:
   - Display question and options
   - Get user input
   - Store guess
   - Compare with correct answer
   - Update score
4. **Results** - Display final score

### Key Components

#### Tuple of Tuples
```python
options = (
    ("A. Option1", "B. Option2", "C. Option3", "D. Option4"),  # Q1 options
    ("A. Option1", "B. Option2", "C. Option3", "D. Option4"),  # Q2 options
)
```

#### Score Tracking
```python
score = 0
if guess.upper() == answers[question_num]:
    score += 1
```

#### Input Validation
```python
guess = input("Enter your guess: ")
guesses.append(guess)  # Store even if wrong
```

## Examples

### Example 1: Basic Tuple Usage
```python
# Tuples are immutable - perfect for constant data
colors = ("red", "green", "blue")

# Can access elements
print(colors[0])  # "red"

# Cannot modify (this would cause error)
# colors[0] = "yellow"  # TypeError!

# Can iterate
for color in colors:
    print(color)
```

### Example 2: Using zip() Function
```python
questions = ("What is 1+1?", "What is 2+2?")
answers = ("2", "4")

# zip pairs them together
for q, a in zip(questions, answers):
    print(f"Question: {q}")
    print(f"Answer: {a}")
    print()

# Output:
# Question: What is 1+1?
# Answer: 2
#
# Question: What is 2+2?
# Answer: 4
```

### Example 3: Simple Quiz with Scoring
```python
questions = ("What is the capital of France?", 
             "What is 5 * 6?")
answers = ("Paris", "30")

score = 0

for i, question in enumerate(questions):
    print(f"\nQuestion {i+1}: {question}")
    guess = input("Your answer: ")
    
    if guess == answers[i]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer is {answers[i]}")

print(f"\nFinal Score: {score}/{len(questions)}")
```

### Example 4: Multiple Choice Quiz
```python
questions = ("What is Python?",)
options = (
    ("A. A snake", "B. A programming language", 
     "C. A food", "D. A movie"),
)
answers = ("B",)

print(questions[0])
for option in options[0]:
    print(option)

guess = input("Enter A, B, C, or D: ").upper()
if guess == answers[0]:
    print("Correct!")
else:
    print(f"Wrong! Answer is {answers[0]}")
```

### Example 5: Case-Insensitive Input
```python
questions = ("What color is the sky?",)
answers = ("BLUE",)

guess = input("Your answer: ").upper()  # Convert to uppercase

if guess == answers[0]:
    print("Correct!")
else:
    print("Wrong!")

# Works with: "blue", "Blue", "BLUE", "bLuE"
```

### Example 6: Storing and Reviewing Guesses
```python
questions = ("What is 2+2?", "What is 3+3?", "What is 4+4?")
answers = ("4", "6", "8")
guesses = []

# Collect all answers
for question in questions:
    print(question)
    guess = input("Answer: ")
    guesses.append(guess)

# Review all answers
print("\n--- REVIEW ---")
for i in range(len(questions)):
    status = "✓" if guesses[i] == answers[i] else "✗"
    print(f"{status} Q{i+1}: You said '{guesses[i]}', Answer: '{answers[i]}'")
```

### Example 7: Complete Mini Quiz
```python
# Quiz data in tuples (immutable)
questions = (
    "What is the largest planet?",
    "How many continents are there?",
    "What is H2O?"
)

options = (
    ("A. Mars", "B. Jupiter", "C. Saturn", "D. Earth"),
    ("A. 5", "B. 6", "C. 7", "D. 8"),
    ("A. Oxygen", "B. Hydrogen", "C. Water", "D. Carbon")
)

answers = ("B", "C", "C")

# Game variables
guesses = []
score = 0
question_num = 0

print("=== SCIENCE QUIZ ===\n")

# Main quiz loop
for question, option in zip(questions, options):
    print(f"Question {question_num + 1}: {question}")
    for opt in option:
        print(f"  {opt}")
    
    guess = input("Your answer (A/B/C/D): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        print("Correct! ✓\n")
        score += 1
    else:
        print(f"Wrong! ✗ The answer is {answers[question_num]}\n")
    
    question_num += 1

# Final score
percentage = (score / len(questions)) * 100
print(f"Final Score: {score}/{len(questions)} ({percentage:.1f}%)")

if percentage >= 70:
    print("Great job! 🎉")
elif percentage >= 50:
    print("Good effort! 👍")
else:
    print("Keep practicing! 📚")
```

## Practice Exercises

### Beginner Level

1. **True/False Quiz**: Create a quiz with 5 true/false questions. Store answers as "T" or "F".

2. **Math Quiz**: Build a simple math quiz with 5 arithmetic questions. Calculate and display percentage score.

3. **Single Question**: Practice zip() by creating a quiz with just one question and its four options.

4. **Answer Review**: After the quiz, display all questions with the user's answers and correct answers side-by-side.

5. **Passing Score**: Set a passing score (e.g., 60%) and display "Pass" or "Fail" message at the end.

### Intermediate Level

6. **Timed Quiz**: Add a time limit for each question using the time module. Skip question if time expires.

7. **Question Categories**: Add categories to questions (History, Science, Math) and display category before each question.

8. **Difficulty Levels**: Create three difficulty levels (Easy, Medium, Hard) with different point values.

9. **Hint System**: Give users 2 hints they can use during the quiz to eliminate wrong answers.

10. **Score Tracking**: Store scores in a file and display high score at the beginning of each game.

### Advanced Level

11. **Random Question Order**: Shuffle questions each time the quiz runs using random module (requires converting tuples to lists).

12. **Multiple Quiz Topics**: Let users choose from different quiz topics, each with its own set of questions.

13. **Multiplayer Quiz**: Allow 2 players to take turns answering questions. Track and compare their scores.

14. **Question Bank**: Load questions from a text file instead of hardcoding them. Support adding new questions.

15. **Quiz Generator**: Create a program that generates quiz questions using APIs (like Open Trivia Database) and builds a dynamic quiz.

## Common Mistakes to Avoid

### Mistake 1: Using Lists Instead of Tuples for Constants

**Wrong:**
```python
# Using list (mutable) for data that shouldn't change
questions = ["What is 2+2?", "What is 3+3?"]
# Could accidentally modify: questions[0] = "Wrong!"
```

**Correct:**
```python
# Using tuple (immutable) for constant data
questions = ("What is 2+2?", "What is 3+3?")
# questions[0] = "Wrong!"  # This raises TypeError
```

**Why:** Tuples prevent accidental modification and signal immutability to other programmers.

### Mistake 2: Not Converting Input to Uppercase

**Wrong:**
```python
answers = ("A", "B", "C")
guess = input("Enter A, B, or C: ")  # User enters "a"
if guess == answers[0]:  # "a" != "A"
    score += 1  # Won't execute even if answer is A
```

**Correct:**
```python
answers = ("A", "B", "C")
guess = input("Enter A, B, or C: ").upper()  # Converts to "A"
if guess == answers[0]:  # "A" == "A"
    score += 1  # Works correctly
```

**Why:** User input case may vary. Always normalize case for comparison.

### Mistake 3: Forgetting to Track Question Number

**Wrong:**
```python
for question, option in zip(questions, options):
    # ... display and get answer ...
    if guess == answers[0]:  # Always checking first answer!
        score += 1
```

**Correct:**
```python
question_num = 0
for question, option in zip(questions, options):
    # ... display and get answer ...
    if guess == answers[question_num]:  # Correct answer
        score += 1
    question_num += 1
```

**Why:** Must track which question you're on to compare with correct answer.

### Mistake 4: Mismatched Tuple Lengths

**Wrong:**
```python
questions = ("Q1?", "Q2?", "Q3?")
options = (("A", "B"), ("A", "B"))  # Only 2!
answers = ("A", "B", "C")

for q, opt in zip(questions, options):  # Stops after 2
    print(q)
```

**Correct:**
```python
questions = ("Q1?", "Q2?", "Q3?")
options = (("A", "B"), ("A", "B"), ("A", "B"))  # 3 tuples
answers = ("A", "B", "C")
# All same length - won't skip questions
```

**Why:** zip() stops at the shortest sequence. Keep parallel tuples the same length.

## Real-World Applications

### 1. **Educational Platforms**
Online learning platforms like Khan Academy, Coursera, and Duolingo use quiz systems to test student knowledge, track progress, and provide immediate feedback on learning.

### 2. **Certification Exams**
Professional certification tests (AWS, CompTIA, etc.) use computerized quiz systems with multiple-choice questions, scoring algorithms, and pass/fail determination.

### 3. **Trivia Games**
Mobile apps and TV game shows use quiz databases to present questions, track scores, and determine winners. Shows like "Jeopardy!" and apps like "HQ Trivia" are sophisticated versions.

### 4. **Employee Training**
Companies use quiz systems to verify that employees understand safety procedures, company policies, or technical training materials before certification.

## Challenge Projects

### 1. **Trivia API Quiz**
Create a quiz that fetches random questions from the Open Trivia Database API.

**Requirements:**
- Fetch questions from API
- Parse JSON response
- Decode HTML entities in questions
- Mix correct answer with incorrect ones
- Display and score results

### 2. **Flashcard Study System**
Build a study tool with quiz mode and review mode.

**Requirements:**
- Create flashcard sets (question/answer pairs)
- Quiz mode: random questions with scoring
- Review mode: cycle through all cards
- Track which cards were missed
- Mark cards as "learned" or "needs review"

### 3. **Subject-Based Quiz Manager**
Create a comprehensive quiz system with multiple subjects.

**Requirements:**
- Multiple quiz topics (Math, Science, History)
- User can select topic
- Track scores per topic
- Display statistics (average, best, worst)
- Save progress to file

### 4. **Adaptive Difficulty Quiz**
Build a quiz that adjusts difficulty based on performance.

**Requirements:**
- Start with medium difficulty
- Increase difficulty after correct answers
- Decrease difficulty after wrong answers
- Track accuracy by difficulty level
- Calculate final score based on difficulty

### 5. **Multiplayer Quiz Competition**
Create a competitive quiz game for 2-4 players.

**Requirements:**
- Player registration
- Turn-based question answering
- Points based on speed and accuracy
- Power-ups (skip question, 50/50, etc.)
- Leaderboard display
- Winner determination

---

## Navigation

- **Previous:** [23. 2D Collections](23-2d-collections.md)
- **Next:** [25. Dictionaries](25-dictionaries.md)
- **[Back to Main README](../README.md)**

## 🎓 Key Takeaways from Video

1. Variables store data values that can be reused
2. Define functions using the def keyword
3. Use if-elif-else for conditional logic

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*
