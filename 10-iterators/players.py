# Module used to define player classess
import random
from utils import get_user_input
from constants import MIN_VALUE, MAX_VALUE, GUESS_PROMPT

print('Loading Player Information')


class Player:
    """ Class to represent a player within the number guess game """

    def __init__(self, name):
        self.name = name
        self.guess_count = 0
        self.history = []

    def __str__(self):
        return 'Player ' + self.name + ' guesses ' + str(self.guess_count) + ', history ' + str(self.history)

    def increment_count(self):
        self.guess_count = self.guess_count + 1

    def add_guess(self, guess):
        self.history.append(guess)

    def print_history(self):
        formatted_history = list(map(lambda guess: '\t guess ' + str(guess), self.history))
        for guess in formatted_history:
            print(guess)

    def make_a_guess(self):
        guess = get_user_input(GUESS_PROMPT, MIN_VALUE, MAX_VALUE)
        self.add_guess(guess)
        return guess

    # Implement the length Protocol
    def __len__(self):
        return len(self.history)

    # Makes this class Iterable
    def __iter__(self):
        return self.history.__iter__()


class ComputerPlayer(Player):
    """ Computer automated player """

    def __init__(self, range):
        super().__init__('Computer')
        self.range = range
        self.random_number_generator = random.Random()

    def make_a_guess(self):
        guess = self.random_number_generator.randint(0, self.range)
        self.add_guess(guess)
        return guess

    def __str__(self):
        return 'Computer' + super().__str__()
