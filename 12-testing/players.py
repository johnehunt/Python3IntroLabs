# Module used to define player classess
import random

from constants import MIN_VALUE, MAX_VALUE, GUESS_PROMPT
from utils import get_user_input

print('Loading Player Information')


class Player:
    """ Class to represent a player within the number guess game """

    def __init__(self, name):
        self.__name = name
        self.__guess_count = 0
        self.__history = []

    def __str__(self):
        return 'Player ' + self.name + ' guesses, ' + str(self.guess_count) + ', history ' + str(self.history)

    # Defining properties for the Player
    @property
    def history(self):
        return self.__history

    @property
    def name(self):
        return self.__name

    @property
    def guess_count(self):
        return self.__guess_count

    # Methods supporting the read only nature of the properties
    def increment_count(self):
        self.__guess_count = self.__guess_count + 1

    def reset_history(self):
        self.__history = []

    def reset_guess_count(self):
        self.__guess_count = 0

    # Other player related methods
    def add_guess(self, guess):
        self.__history.append(guess)

    def print_history(self):
        formatted_history = list(map(lambda guess: '\t guess ' + str(guess), self.__history))
        for guess in formatted_history:
            print(guess)

    def make_a_guess(self):
        guess = get_user_input(GUESS_PROMPT, MIN_VALUE, MAX_VALUE)
        self.add_guess(guess)
        self.increment_count()
        return guess

    # Implement the length Protocol
    def __len__(self):
        return len(self.__history)

    # Makes this class Iterable
    def __iter__(self):
        return self.__history.__iter__()


class ComputerPlayer(Player):
    """ Computer automated player """

    def __init__(self, range):
        super().__init__('Computer')
        self.range = range
        self.random_number_generator = random.Random()

    def make_a_guess(self):
        guess = self.random_number_generator.randint(0, self.range)
        self.add_guess(guess)
        self.increment_count()
        return guess

    def __str__(self):
        return 'Computer' + super().__str__()
