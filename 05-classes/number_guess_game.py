

class Player():
    """ Class to represent a player within the number guess game """
    def __init__(self, name):
        self.name = name
        self.guess_count = 0
        self.history = []

    def __str__(self):
        return 'Player ' + self.name + ' guesses ' + str(self.guess_count) + ', history ' + str(self.history)

