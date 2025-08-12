import unittest

from player import Player

class TestPlayerClass(unittest.Testcase):
    def add_player_with_uid(self):
        player1 = Player("J271481", None)
        self.assertEqual(player1.uid, "J271481")

    def add_player_with_name(self):
        player1 = Player(None, "Myself")
        self.assertEqual(player1.name, "Myself")
