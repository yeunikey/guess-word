import random
from utils import Utils

class GuessTheWordGame:

    MAX_ATTEMPTS = 10

    def __init__(self, words):
        self.words = words
        self.word = random.choice(self.words)
        self.attempts = 0
        self.current_guess = ['_'] * len(self.word)
        self.guessed_letters = set()

    def guess_letter(self, letter):
        if self.attempts >= self.MAX_ATTEMPTS:
            print("You've reached the maximum number of attempts.")
            return

        self.attempts += 1
        if letter in self.guessed_letters:
            print("You already guessed that letter.")
            return

        self.guessed_letters.add(letter)
        if letter in self.word:
            for index, char in enumerate(self.word):
                if char == letter:
                    self.current_guess[index] = letter
        
        print(f"Attempts: {self.attempts}/{self.MAX_ATTEMPTS}")
        print("Current guess: ", " ".join(self.current_guess))
    
    def is_complete(self):
        return '_' not in self.current_guess

    def save_results(self, filename, success):
        with open(filename, 'a') as file:
            outcome = 'Success' if success else 'Failure'
            file.write(f"Word: {self.word}, Attempts: {self.attempts}, Outcome: {outcome}\n")

class Application:

    def __init__(self):
        self.game = GuessTheWordGame(['python', 'java', 'kotlin'])

    def start(self):
        Utils.clean()

        while not self.game.is_complete():
            letter = input("Guess a letter: ")
            self.game.guess_letter(letter)

            if self.game.is_complete():
                print("Congratulations! You've guessed the word!")
                self.game.save_results('game_results.txt', success=True)
                break
            elif self.game.attempts >= self.game.MAX_ATTEMPTS:
                print("Sorry, you've used up all your attempts!")
                self.game.save_results('game_results.txt', success=False)
                break

application = Application()
application.start()