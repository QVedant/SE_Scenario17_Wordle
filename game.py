import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=5):
        self.length = length
        self.target = random.choice([w for w in WORDS if len(w) == length])
        self.history = []

    def display_history(self):
        print("\nGuess History:")
        for i, (guess, feedback) in enumerate(self.history, start=1):
            print(f"{i}. {guess} - {' '.join(feedback)}")
        print()

    def display_summary(self, outcome):
        print("\n--- Session Summary ---")
        print(f"Outcome: {outcome}")
        print(f"Target word: {self.target}")
        print(f"Valid guesses: {len(self.history)}/6")

        if self.history:
            print("Total guesses:")
            for i, (guess, feedback) in enumerate(self.history, start=1):
                print(f"{i}. {guess} - {' '.join(feedback)}")
        else:
            print("No valid guesses were made.")

        print("-----------------------")

    def run(self):
        print(f"Wordle - {self.length} letters, 6 guesses.")

        while len(self.history) < 6:
            guess = input("> ").strip().lower()

            if guess == "q":
                print("Game quit.")
                self.display_summary("Quit")
                return

            if len(guess) != self.length or not guess.isalpha():
                print(f"Enter a valid {self.length}-letter word.")
                continue

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))

            print(" ".join(feedback))
            self.display_history()

            if guess == self.target:
                print("Solved!")
                self.display_summary("Won")
                return

        print("Out of guesses!")
        self.display_summary("Lost")


if __name__ == "__main__":
    WordleGame().run()
