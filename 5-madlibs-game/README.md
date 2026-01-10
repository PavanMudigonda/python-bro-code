# Chapter 5: Madlibs Game

## 📚 What You'll Learn
Create a fun word game that combines user input and string formatting to generate silly stories!

## 🎯 Learning Objectives
- Practice using multiple `input()` statements
- Use f-strings to create dynamic text
- Understand how to structure an interactive program
- Have fun with creative programming!

## 📖 Concept Explanation

### What is Madlibs?
Madlibs is a phrasal template word game where:
1. Players are asked to provide words (noun, verb, adjective, etc.)
2. They DON'T know the story context
3. Their words are inserted into a pre-written story
4. The result is usually funny and unexpected!

### Parts of Speech Reminder
- **Noun**: Person, place, or thing (cat, pizza, teacher, ocean)
- **Verb**: Action word (run, jump, sing, dance)
- **Adjective**: Describes a noun (big, red, funny, delicious)
- **Adverb**: Describes a verb (quickly, slowly, happily)
- **-ing Verb**: Present continuous (running, jumping, singing)

### How the Program Works
```python
1. Ask user for words (without showing the story)
2. Store each word in a variable
3. Insert variables into story template using f-strings
4. Display the completed story
```

## 💡 Example Run

### User Input:
```
Enter an adjective: sparkly
Enter a noun: elephant
Enter another adjective: purple
Enter a verb ending with 'ing': dancing
Enter a third adjective: confused
```

### Output Story:
```
today i went to a sparkly zoo.
in an exhibit, i saw elephant
elephant was purple and dancing
I was confused!
```

## ✍️ Practice Exercises

### Exercise 1: Extend the Story
Add more lines to the story! Ask for:
- A color
- An adverb (word ending in -ly)
- A place
- A food item

### Exercise 2: Create Your Own Madlib
Write a completely new story template about:
- Going to school
- A superhero adventure
- A cooking disaster
- A space journey

### Exercise 3: Themed Madlibs
Create madlibs for specific themes:
- **Horror Story**: scary adjectives, spooky nouns
- **Romance**: romantic verbs, lovely adjectives
- **Comedy**: funny situations

## 💻 Code Template for Your Own Madlib
```python
# Get user input
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective1 = input("Enter an adjective: ")
place = input("Enter a place: ")

# Create your story
print(f"\nOnce upon a time, in a {adjective1} {place},")
print(f"there was a {noun1} who loved to {verb1}.")
print("The end!")
```

## 🎨 Story Templates to Try

### Template 1: Adventure Story
```python
character = input("Character name: ")
adjective = input("Adjective: ")
place = input("Place: ")
verb = input("Verb (past tense): ")

print(f"{character} went to the {adjective} {place}.")
print(f"There, {character} {verb} and found treasure!")
```

### Template 2: News Report
```python
city = input("City name: ")
noun = input("Noun: ")
number = input("Number: ")
adjective = input("Adjective: ")

print(f"BREAKING NEWS from {city}!")
print(f"A {adjective} {noun} was spotted {number} times today!")
```

## 🔍 Tips for Great Madlibs

### 1. Be Specific in Prompts
```python
# Vague:
word = input("Enter a word: ")  # User doesn't know what kind

# Better:
animal = input("Enter an animal: ")  # Clear instruction
```

### 2. Use Descriptive Variable Names
```python
# Confusing:
x = input("Enter something: ")

# Clear:
favorite_food = input("Enter your favorite food: ")
```

### 3. Add Context to Output
```python
print("\n===== YOUR MADLIB STORY =====\n")
# ... story here ...
print("\n==============================")
```

## 🎮 Challenge Projects

### Challenge 1: Multiple Endings
Create a madlib with 2-3 different endings that randomly select.

### Challenge 2: Repeated Words
Ask for one word and use it multiple times in the story in different contexts.

### Challenge 3: Long Story
Create a madlib that uses at least 10 different words and tells a complete story with beginning, middle, and end.

## 🚀 Try It Yourself
1. Run the existing madlib and try it with different words
2. Modify the story template to make it funnier
3. Create a brand new madlib about your favorite topic
4. Share your madlib with friends and see what funny stories they create!

## 📝 Key Learning Points
- User input can be stored in many variables
- F-strings make it easy to insert variables into text
- The order of `input()` statements determines the user experience
- Creative prompts lead to funnier results
- Programs can be fun and educational at the same time!

## 🔗 Next Chapter
Continue to [Chapter 6: Arithmetic & Math](../6-arithmetics-maths/) to learn about mathematical operations in Python!
