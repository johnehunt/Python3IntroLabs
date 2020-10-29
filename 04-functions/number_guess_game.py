import random

MIN_VALUE = 1
MAX_VALUE = 10


def welcome_message():
    print('Welcome to the number guess game')


def game_over_message():
    print('Game Over')


def get_user_input(prompt):
    invalid_input = True
    while invalid_input:
        print(prompt, end='')
        user_input = input()
        if not user_input.isdigit():
            print('Input must be a positive number')
        else:
            user_input_int = int(user_input)
            if (user_input_int < MIN_VALUE or user_input_int > MAX_VALUE):
                print('Input must be a number in the range 1 to 10')
            else:
                invalid_input = False
    return user_input_int


def get_user_yes_or_no(prompt):
    """ get input from the user and check that it is y or n"""
    invalid_input = True
    while invalid_input:
        user_input = input(prompt).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input.lower()
        else:
            print('Input Error - Input must be "y" or "n"')


def print_history(history):
    formatted_history = list(map(lambda guess: '\t guess ' + str(guess), history))
    for guess in formatted_history:
        print(guess)


def play_game():
    """ Defines main loop controlling game"""
    keep_playing = True
    while keep_playing:

        # Initialise the history of guesses
        history = []

        # Initialise the number to be guessed
        number_to_guess = random.randint(1, 10)

        # Initialise the number of tries the player has made
        count_number_of_tries = 1

        # Obtain their initial guess
        guess = get_user_input('Please guess a number between 1 and 10: ')
        history.append(guess)
        while number_to_guess != guess:
            print('Sorry wrong number')

            # Check to see they have not exceeded the maximum
            # number of attempts if so break out of loop otherwise
            # give the user come feedback
            if count_number_of_tries == 4:
                break
            elif guess < number_to_guess:
                print('Your guess was lower than the number')
            else:
                print('Your guess was higher than the number')

            # Obtain their next guess and increment number of attempts
            guess = get_user_input('Please guess again: ')
            history.append(guess)
            count_number_of_tries += 1

        # Check to see if they did guess the correct number
        if number_to_guess == guess:
            print('Well done you won!')
            print('You took', count_number_of_tries, 'goes to complete the game')
        else:
            print("Sorry - you loose")
            print('The number you needed to guess was',
                  number_to_guess)

        print('Your guesses were:')
        print_history(history)

        play_again = get_user_yes_or_no('Do you want to play? (y/n) ')
        if play_again == 'n':
            keep_playing = False


# Start the program

welcome_message()
play_game()
game_over_message()
