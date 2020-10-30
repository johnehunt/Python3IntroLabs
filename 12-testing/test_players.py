import pytest

from players import Player


@pytest.fixture
def player():
    """ Returns a Calculator instance """
    print('Player fixture')
    return Player('John')


def test_initial_player_setup(player):
    assert player.name == 'John', 'Name should be John'
    assert player.guess_count == 0, 'Initial guess count should be zero'
    assert len(player) == 0, 'Player history should have length zero'


def test_player_make_a_guess(player):
    player.add_guess(5)
    assert len(player) == 1, 'Player history should be incremented by one'
    assert 5 in player.history, 'Player history should contain 5'


def test_player_guess_count_incremented(player):
    player.add_guess(5)  # There is a bug here
    assert player.guess_count == 1, 'Guess count should be 1'
    player.add_guess(6)
    assert player.guess_count == 2, 'Guess count should be 2 after 2 guesses'
