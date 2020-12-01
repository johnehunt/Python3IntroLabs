# Illustrates creating a history with information
# on the result of each guess i.e. was it higher or lower
import random

MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4
GUESS_PROMPT = 'Please guess a number between ' + str(MIN_VALUE) + ' and ' + str(MAX_VALUE) + ': '

keep_playing = True

print('Welcome to the number guess game')

while keep_playing:

    # Initialise the history of guesses
    history = []

    # Initialise the number to be guessed
    number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

    # Initialise the number of tries the player has made
    count_number_of_tries = 0

    guess = 0
    while number_to_guess != guess:
        message_to_user = ''

        # Obtain their guess
        guess = int(input(GUESS_PROMPT))

        # Check to see they have not exceeded the maximum
        # number of attempts if so break out of loop otherwise
        # give the user come feedback
        if guess == -1:
            print('The number to guess is', number_to_guess)
            continue
        elif count_number_of_tries == MAX_NUMBER_OF_GUESSES:
            message_to_user = 'Max number of guesses made'
            break
        elif number_to_guess == guess:
            message_to_user = 'Correct Guess'
        elif guess < number_to_guess:
            message_to_user = 'Your guess was lower than the number'
            print(message_to_user)
        elif guess > number_to_guess:
            message_to_user = 'Your guess was higher than the number'
            print(message_to_user)

        # Add the guess to the history and increment number of attempts
        history.append((guess, message_to_user))
        count_number_of_tries += 1

    # Check to see if they did guess the correct number
    if number_to_guess == guess:
        print('Well done you won!')
        print('You took', count_number_of_tries , 'goes to complete the game')
    else:
        print("Sorry - you loose")
        print('The number you needed to guess was',
              number_to_guess)

    print('Your guesses were:')
    print(history)

    play_again = input('Do you want to play again? (y/n) ')
    if play_again.lower() == 'n':
        keep_playing = False

print('Game Over')