

def get_user_yes_or_no(prompt):
    """ get input from the user and check that it is y or n"""
    invalid_input = True
    while invalid_input:
        user_input = input(prompt).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input.lower()
        else:
            print('Input Error - Input must be "y" or "n"')


def get_user_input(prompt, min_value, max_value):
    invalid_input = True
    while invalid_input:
        user_input = input(prompt)
        if not user_input.isdigit():
            print('Input must be a positive number')
        else:
            user_input_int = int(user_input)
            if user_input_int < min_value or user_input_int > max_value:
                print('Error ' + prompt)
            else:
                invalid_input = False
    return user_input_int

