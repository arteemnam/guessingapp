from random import random, seed
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

class GuessingGame(App):
    def __init__(self, difficulty):
        self.guesses = 0
        self.min = 0

        if difficulty == "Easy":
            self.number = 69
            self.max = 100
        elif difficulty == "Hard":
            self.number = 420
            self.max = 1000

    def guess_number(self):
        guess = input(f"Please guess a number {self.min} - {self.max}: ")

        if self.valid_number(guess):
            return int(guess)
        else: 
            print("Please enter a valid number.")
            return self.guess_number()

    def valid_number(self, str_number):
        try: 
            number = int(str_number)
        except: 
            return False
        return self.min <= number <= self.max

    def play(self):
        while True:
            self.guesses += 1

            guess = self.guess_number()

            if guess < self.number:
                print("Your guess was under.")
            elif guess > self.number:
                print("Your guess was over.")
            else:
                break

        print(f"You guessed it in {self.guesses} guesses.")

kv = Builder.load_file("guessing.kv")

class GuessingApp(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    GuessingApp().run()
