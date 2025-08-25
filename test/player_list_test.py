import unittest

from app.player import Player
from app.player_list import PlayerList


class TestPlayerList(unittest.TestCase):
    def test_player_list_is_empty_true(self):
        pl1 = PlayerList()
        self.assertTrue(pl1.is_empty(), "Expected Return: True thats it is indeed a empty list")
        self.assertIsNone(pl1.tail, "Expected Return: tail is none and list is empty")

    def test_player_list_is_empty_false(self):
        pl1 = PlayerList()
        person1 = Player("001", "Sam")
        pl1.push(person1)
        self.assertFalse(pl1.is_empty(), "Expected Return: False for a empty list")
        self.assertEqual(pl1.head._player._name, "Sam", "head should point to Sam player node" )
        self.assertEqual(pl1.tail._player._name, "Sam", "tail should point to Sam player node")

    def test_append_to_empty_list(self):
        pl1 = PlayerList()

        self.assertTrue(pl1.is_empty(), "Expected Return: List is Empty")
        person1 = Player("001", "Sam")
        pl1.append(person1)

        self.assertFalse(pl1.is_empty(), "Expected Return :List should not be empty")
        self.assertEqual(pl1.head._player._name, "Sam", "Head is pointing to Sam")
        self.assertEqual(pl1.tail._player._name, "Sam", "Tail is pointing at Sam")

    def test_append_to_non_empty_list(self):
        pl1 = PlayerList()
        person1 = Player("001", "Sam")
        person2 = Player("002", "Tony")
        pl1.append(person1)
        pl1.append(person2)

        self.assertEqual(pl1.head._player._name, "Sam", "Head pointing at Sam")
        self.assertEqual(pl1.tail._player._name, "Tony", "Tail pointing at Tony")
        self.assertEqual(pl1.head.next_node._player._name, "Tony", "Sam should be linking next to Tony")
        self.assertEqual(pl1.tail.prev_node._player._name, "Sam", "Tony should be linking prev to Sam")

    def test_pop_head(self):
        pl1 = PlayerList()
        person1 = Player("001", "Sam")
        person2 = Player("002", "Tony")
        pl1.append(person1)
        pl1.append(person2)

        removed_node = pl1.pop_head()
        self.assertEqual(removed_node.name, "Sam", "po_head should remove Sam")
        self.assertEqual(pl1.head.player.name, "Tony", "Head should now be Tony")
        self.assertEqual(pl1.tail.player.name, "Tony", "Tail should still be Tony")

    def test_pop_tail(self):
        pl1 = PlayerList()
        person1 = Player("001", "Sam")
        person2 = Player("002", "Tony")
        pl1.append(person1)
        pl1.append(person2)

        removed_node = pl1.pop_tail()
        self.assertEqual(removed_node.name, "Tony", "Tail deletion should remove Tony")
        self.assertEqual(pl1.head.player.name, "Sam", "Head should still be Sam")
        self.assertEqual(pl1.tail.player.name, "Sam", "Tail should now be Sam")

    def test_remove_by_id(self):
        pl1 = PlayerList()
        person1 = Player("001", "Sam")
        person2 = Player("002", "Tony")
        person3 = Player("003", "John")

        pl1.append(person1)
        pl1.append(person2)
        pl1.append(person3)

        removed_node = pl1.remove_by_id("002")
        self.assertEqual(removed_node.name, "Tony", "Should remove the player with unique id as uid=002")
        