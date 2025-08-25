import unittest

from app.player import Player

class TestPlayerClass(unittest.Testcase):
    def test_add_player_with_uid(self):
        player1 = Player("J271481", "")
        self.assertEqual(player1.uid, "J271481")

    def test_add_player_with_name(self):
        player1 = Player("", "Myself")
        self.assertEqual(player1.name, "Myself")
