
import unittest

from app.player import Player
from app.player_list import PlayerList

class Test_player_list(unittest.TestCase):
    def test_player_list_is_empty_true(self):
        pl1 = PlayerList()
        self.assertTrue(pl1.is_empty(), "Expected Return: True thats it is indeed a empty list")

    def test_player_list_is_empty_false(self):
        pl1 = PlayerList()
        person1 = Player("001", "Sam")
        pl1.push(person1)
        self.assertFalse(pl1.is_empty(), "Expected Return: False for a empty list")

