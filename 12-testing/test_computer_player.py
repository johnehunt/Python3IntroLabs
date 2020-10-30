import pytest

from constants import MAX_VALUE
from players import ComputerPlayer


@pytest.fixture
def computer_player():
    print('ComputerPlayer fixture')
    return ComputerPlayer(MAX_VALUE)


def test_initial_computer_player_setup(computer_player):
    assert computer_player.name == 'Computer', 'Name should be Computer'
    assert computer_player.guess_count == 0, 'Initial guess count should be zero'
    assert len(computer_player) == 0, 'Player history should have length zero'


def test_make_a_test(computer_player):
    computer_player.make_a_guess()
    assert computer_player.guess_count == 1, 'Initial guess count should be one'
    assert len(computer_player) == 1, 'Player history should have length one'
