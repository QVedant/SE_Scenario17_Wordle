import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def run(self):
        print(f"Wordle — {self.length} letters, 6 guesses.")
        accepted_guesses = 0

        while accepted_guesses < 6:
            guess = input("> ").strip().lower()

            if guess == "q":
                print("Game quit.")
                return

            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue

            accepted_guesses += 1
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            print(" ".join(feedback))

            if guess == self.target:
                print("Solved!")
                return

        print("Out of guesses!")
        print("The word was:", self.target)
