# hangman in python

from words_list import words

import random


hangman_art = {
    0: """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    1: """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    2: """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    3: """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    4: """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    5: """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    6: """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
}


def display_man(wrong_guesses):
    print(hangman_art[wrong_guesses])


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print("The answer was: " + answer)


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    max_wrong = len(hangman_art) - 1

    while True:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
            if "_" not in hint:
                print("🎉 You win! The word was:", answer)
                break
        else:
            wrong_guesses += 1
            if wrong_guesses == max_wrong:
                display_man(wrong_guesses)
                print("💀 You lost!")
                display_answer(answer)
                break


if __name__ == "__main__":
    main()
