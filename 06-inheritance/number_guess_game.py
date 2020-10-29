import random

MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = 'Please guess a number between ' + str(MIN_VALUE) + ' and ' + str(MAX_VALUE) + ': '


def get_user_yes_or_no(prompt):
    """ get input from the user and check that it is y or n"""
    invalid_input = True
    while invalid_input:
        user_input = input(prompt).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input.lower()
        else:
            print('Input Error - Input must be "y" or "n"')


def welcome_message():
    print('Welcome to the number guess game')


def display_instructions():
    response = get_user_yes_or_no('Do you want to see the instructions?: ')
    if response == 'y':
        print("You have to guess a number between", MIN_VALUE, "and", MAX_VALUE)
        print("You can play as many times as you like")


def game_over_message():
    print('Game Over')


def get_user_input(prompt):
    invalid_input = True
    while invalid_input:
        user_input = input(prompt)
        if not user_input.isdigit():
            print('Input must be a positive number')
        else:
            user_input_int = int(user_input)
            if user_input_int < MIN_VALUE or user_input_int > MAX_VALUE:
                print('Error ' + GUESS_PROMPT)
            else:
                invalid_input = False
    return user_input_int


class Player():
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
        guess = get_user_input(GUESS_PROMPT)
        self.add_guess(guess)
        return guess


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


def get_player():
    name = input('Please enter your name: ')
    player = Player(name)
    return player


def play_game():
    """ Defines main loop controlling game"""
    player = None
    computer_plays = get_user_yes_or_no("Do you want the computer to play? ")
    if computer_plays == 'y':
        player = ComputerPlayer(MAX_VALUE)
    else:
        name = input('Please enter your name: ')
        player = Player(name)

    keep_playing = True
    while keep_playing:

        # Initialise the players history of guesses
        player.history = []

        # Initialise the number to be guessed
        number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

        # Initialise the number of tries the player has made
        player.guess_count = 1

        # Obtain their initial guess
        guess = player.make_a_guess()
        while number_to_guess != guess:
            print('Sorry wrong number')

            # Check to see they have not exceeded the maximum
            # number of attempts if so break out of loop otherwise
            # give the user come feedback
            if player.guess_count == MAX_NUMBER_OF_GUESSES:
                break
            elif guess < number_to_guess:
                print('Your guess was lower than the number')
            else:
                print('Your guess was higher than the number')

            # Obtain their next guess and increment number of attempts
            guess = player.make_a_guess()
            player.increment_count()

        # Check to see if they did guess the correct number
        if number_to_guess == guess:
            print('Well done', player.name, 'won!')
            print('You took', player.guess_count, 'goes to complete the game')
        else:
            print("Sorry - you loose")
            print('The number you needed to guess was',
                  number_to_guess)

        print('Your guesses were:')
        player.print_history()

        play_again = get_user_yes_or_no('Do you want to play? (y/n) ')
        if play_again == 'n':
            keep_playing = False


# Start the program

welcome_message()
display_instructions()
play_game()
game_over_message()
