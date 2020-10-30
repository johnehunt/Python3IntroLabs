import pytest

from players import Player


@pytest.fixture
def player():
    """ Returns a Calculator instance """
    print('Player fixture')
    return Player('John')


def test_initial_setup(player):
    assert player.name == 'John', 'Name should be John'
    assert player.guess_count == 0, 'Initial guess count should be zero'
    assert len(player) == 0, 'Player history should have length zero'


