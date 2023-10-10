from random import randint


class GuessingGame:
    def __init__(self, start: int, end: int):
        self.__start = start
        self.__end = end
        self.__answer = randint(start, end)
        self.__solved = False
        self.__guesses = 0

    @property
    def guesses(self):
        return self.__guesses

    def increment_guesses(self):
        self.__guesses += 1

    def guess(self, user_guess: int):
        try:
            user_guess = int(user_guess)

        except:
            print("That input isn't valid")
            return
        if user_guess < self.__start or user_guess > self.__end:
            return f"out of bounds, please type a number beteen {self.__start} and {self.__end}"
        self.increment_guesses()
        if self.__answer == user_guess:
            self.__solved = True
            return "answer"
        elif user_guess < self.__answer:
            return "low"
        else:
            return "high"

    @property
    def solved(self):
        return self.__solved


class GuessingGameApplication:
    def __init__(self, start: int = 1, end: int = 100):
        self.__start = start
        self.__end = end
        self.__game = GuessingGame(start, end)
        self.__last_guess = None
        self.__last_result = None

    def intro(self):
        print("Let's play a guessing game")
        print(f"Guess a number between {self.__start} and {self.__end}")

    def end_game(self):
        print(f"{self.__last_guess} was correct!")
        print(f"It took you {self.__game.guesses} guesses")

    def execute(self):
        self.intro()
        while not self.__game.solved:
            if self.__last_guess != None:
                print(
                    f"Oops! Your last guess ({self.__last_guess}) was {self.__last_result}"
                )
                print()
            self.__last_guess = input("Enter your guess: ")
            self.__last_result = self.__game.guess(self.__last_guess)
        self.end_game()


game = GuessingGameApplication(1, 1000)
game.execute()
