import unittest

from app.player import Player
from app.player_list import PlayerList

class Test_player_list(unittest.TestCase):
    def test_player_list_is_empty_true(self):
        pl1 = PlayerList()
        self.assertTrue(pl1.is_empty(), "Expected Return: True thats it is indeed a empty list")
        self.assertIsNone(pl1.tail, "Expected Return: tail is none and list is empty")

    def test_player_list_is_empty_false(self):
        pl1 = PlayerList()
        person1 = Player("001", "Sam")
        pl1.push(person1)
        self.assertFalse(pl1.is_empty(), "Expected Return: False for a empty list")
        self.assertEqual(pl1.head.player.name, "Sam", "head should point to Sam player node" )
        self.assertEqual(pl1.tail.player.name, "Sam", "tail should point to Sam player node")


