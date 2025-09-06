# Player hash map test for Assessment 1 Portfolio part 2
# Author Samuel Peach

import unittest


from app.player_list import PlayerHashMap


class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.hashmap = PlayerHashMap(size=10)

    def test_hash_len_count_players(self):
        self.hashmap["001"] = "Sam"
        self.hashmap["002"] = "Tony"
        self.hashmap["003"] = "Alex"
        # Expect 3 total players
        self.assertEqual(len(self.hashmap), 3)

    def test_hash_get_item(self):
        self.hashmap["001"] = "Sam"
        self.hashmap["002"] = "Tony"

        player1 = self.hashmap["001"]
        player2 = self.hashmap["002"]

        self.assertEqual(player1.uid, "001")
        self.assertEqual(player1.name, "Sam")
        self.assertEqual(player2.uid, "002")
        self.assertEqual(player2.name, "Tony")

    def test_display(self):
        self.hashmap["001"] = "Sam"
        self.hashmap["002"] = "Tony"
        self.hashmap["003"] = "Alex"
        self.hashmap["004"] = "John"
        self.hashmap["005"] = "Tom"

        #Expected result player lists 5,6,7,8,9 all have one player each
        self.hashmap.display()

    def test_delete_item(self):
        self.hashmap["001"] = "Sam"
        del self.hashmap["001"]

        self.assertEqual(len(self.hashmap), 0)

        with self.assertRaises(KeyError):
            _ = self.hashmap["001"]

    def test_set_item(self):
        self.hashmap["001"] = "Sam"
        player1 = self.hashmap["001"]
        self.assertEqual(player1.name, "Sam")

        self.hashmap["001"] = "Samuel"
        updated_player = self.hashmap["001"]
        self.assertEqual(updated_player.name, "Samuel")

        self.assertEqual(len(self.hashmap), 1)


    def test_collision_handling(self):
        """Basic collision test, Both players should collide, as they will both be in the same playerList (5)."""
        self.hashmap["001"] = "Sam"
        self.hashmap["010"] = "Tony"

        player1 = self.hashmap["001"]
        player2 = self.hashmap["010"]

        self.assertEqual(player1.name, "Sam")
        self.assertEqual(player2.name, "Tony")

        # self.hashmap.display() //testing

        playerlist = self.hashmap._map[5]

        # search through list to see they are added
        players_in_list = []
        current_node = playerlist.head
        while current_node:
            players_in_list.append(current_node.player)
            current_node = current_node.next_node

        self.assertEqual(players_in_list[0].name, "Sam")
        self.assertEqual(players_in_list[1].name, "Tony")


    def test_initial_hashmap(self):
        """Checking the state of the hashmap on initialization"""

        # Check it has zero players
        self.assertEqual(len(self.hashmap), 0)

        # Size of hashmap is equal to size defined
        self.assertEqual(self.hashmap.len_lists(), 10)



if __name__ == '__main__':
    unittest.main()
