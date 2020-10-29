import random

MIN_VALUE = 1
MAX_VALUE = 10
MAX_NUMBER_OF_GUESSES = 4

print('Welcome to the number guess game')

# Initialise the number to be guessed
number_to_guess = random.randint(MIN_VALUE, MAX_VALUE)

# Initialise the number of tries the player has made
count_number_of_tries = 1

# Obtain their initial guess
guess = int(input('Please guess a number between ' + MIN_VALUE + ' and ' + MAX_VALUE + ': '))
while number_to_guess != guess:
    print('Sorry wrong number')

    # Check to see they have not exceeded the maximum
    # number of attempts if so break out of loop otherwise
    # give the user come feedback
    if count_number_of_tries == MAX_NUMBER_OF_GUESSES:
        break
    elif guess < number_to_guess:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')

    # Obtain their next guess and increment number of attempts
    guess = int(input('Please guess again: '))
    count_number_of_tries += 1

# Check to see if they did guess the correct number
if number_to_guess == guess:
    print('Well done you won!')
    print('You took', count_number_of_tries, 'goes to complete the game')
else:
    print("Sorry - you loose")
    print('The number you needed to guess was',
          number_to_guess)

print('Game Over')
