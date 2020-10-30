import random
from os import path
from constants import MIN_VALUE, MAX_VALUE, MAX_NUMBER_OF_GUESSES, LOWSCORE_FILENAME
from utils import get_user_yes_or_no
from players import Player, ComputerPlayer
import traceback

best_guess_count = 9999


class NumberGuessGameException(Exception):
    """ Class representing errors in the number guess game"""

    def __init__(self, msg):
        super().__init__(msg)


def welcome_message():
    print('Welcome to the number guess game')


def display_instructions():
    response = get_user_yes_or_no('Do you want to see the instructions?: ')
    if response == 'y':
        print("You have to guess a number between", MIN_VALUE, "and", MAX_VALUE)
        print("You can play as many times as you like")


def game_over_message():
    print('Game Over')


def load_highscore():
    global best_guess_count
    if path.isfile(LOWSCORE_FILENAME):
        with open(LOWSCORE_FILENAME, 'r') as file:
            inputStr = file.readline()
            best_guess_count = int(inputStr)
    print('The current best guess count is', best_guess_count)


def check_highscore_update(player):
    if player.guess_count < best_guess_count:
        print(player.name, 'you have the current best guess count')
        with open(LOWSCORE_FILENAME, 'w') as file:
            file.write(str(player.guess_count))


def get_player():
    player = None
    computer_plays = get_user_yes_or_no("Do you want the computer to play? ")
    if computer_plays == 'y':
        player = ComputerPlayer(MAX_VALUE)
    else:
        name = input('Please enter your name: ')
        print('', name, '')
        if name == '':
            raise NumberGuessGameException('Invalid Name')
        player = Player(name)
    return player


def play_game():
    """ Defines main loop controlling game"""
    player = get_player()

    keep_playing = True
    while keep_playing:

        # Initialise the players history of guesses
        player.reset_history()

        # Initialise the number to be guessed
        number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

        # Initialise the number of tries the player has made
        player.reset_guess_count()

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
                print(player.name, 'your guess was lower than the number')
            else:
                print(player.name, 'your guess was higher than the number')

            # Obtain their next guess and increment number of attempts
            guess = player.make_a_guess()

        # Check to see if they did guess the correct number
        if number_to_guess == guess:
            print('Well done', player.name, 'won!')
            print('You took', player.guess_count, 'goes to complete the game')
            check_highscore_update(player)
        else:
            print('Sorry -', player.name, 'you loose')
            print('The number you needed to guess was',
                  number_to_guess)

        print('The length of the player history is', len(player))
        print(player.name, 'your guesses were:')
        player.print_history()

        play_again = get_user_yes_or_no('Do you want ' + player.name + ' to play? (y/n) ')
        if play_again == 'n':
            keep_playing = False


# Start the program assume this is the main module
if __name__ == "__main__":
    try:
        welcome_message()
        load_highscore()
        display_instructions()
        play_game()
    except NumberGuessGameException as exp:
        print('A problem was encountered within the program')
        print(exp)
        # printing stack trace
        traceback.print_exc()

game_over_message()
