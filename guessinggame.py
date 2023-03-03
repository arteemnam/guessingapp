import random

class GuessingGame():
    def __init__(self, difficulty):
        self.guesses = 0
        self.min = 0

        if difficulty == "Easy":
            self.max = 100
            self.number = random.randrange(self.max)
        elif difficulty =="Medium":
            self.max = 1000
            self.number = random.randrange(self.max)
        elif difficulty == "Hard":
            self.max = 10000
            self.number = random.randrange(self.max)
        elif difficulty == "Extra Hard":
            self.max = 100000
            self.number = random.randrange(self.max)

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

GuessingGame("Easy").play()
