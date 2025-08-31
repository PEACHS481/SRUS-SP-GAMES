# Player hash map test for Assessment 1 Portfolio part 2
# Author Samuel Peach

import unittest

from app.player import Player
from app.player_list import PlayerList, PlayerHashMap
from app.player_node import PlayerNode


class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.hashmap = PlayerHashMap(size=10)

    def test_hash_len(self):
        self.hashmap["001"] = "Sam"
        self.hashmap["002"] = "Tony"
        self.hashmap["003"] = "Alex"

        self.assertEqual(len(self.hashmap), 3)


    def test_hash_get_item(self):
        self.hashmap["001"] = "Sam"
        self.hashmap["002"] = "Tony"

        player1 = self.hashmap["001"]
        player2 = self.hashmap["002"]

        self.assertEqual(player1.name, 'Sam')
        self.assertEqual(player2.name, "Tony")

    def test_display(self):
        self.hashmap["001"] = "Sam"
        self.hashmap["002"] = "Tony"
        self.hashmap.display()
