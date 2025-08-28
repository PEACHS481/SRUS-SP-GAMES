# Player List for Assessment 1
# Author Samuel Peach
# Docstrings may include method description taken from tasks 2 implementation guide inside brackets (like this)

from app.player_node import PlayerNode
from app.player import Player


# Initialise Class PlayerList
class PlayerList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Push method to insert new node at head of list
    def push(self, player):
        new_node = PlayerNode(player)
        new_node.next_node = self.head

        if not self.is_empty():
            self.head.prev_node = new_node
        else:
            self.tail = new_node

        self.head = new_node

    def append(self, player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def pop_head(self):
        if self.is_empty():
            return None

        removed_node = self.head
        self.head = self.head.next_node

        if not self.is_empty():
            self.head.prev_node = None
        else:
            # list is empty so tail must be updated to be None
            self.tail = None

        return removed_node.player

    def pop_tail(self):
        if self.is_empty():
            return None

        removed_node = self.tail
        self.tail = self.tail.prev_node

        if not self.is_empty():
            self.tail.next_node = None
        else:
            # list is empty and head must be updated to be None
            self.head = None

        return removed_node.player

    def remove_by_id(self, uniqueid):
        """remove specific node via player.uid"""
        current_node = self.head
        while current_node is not None:
            if current_node.player.uid == uniqueid:
                if current_node == self.head:
                    # if head of list use pop_head function
                    return self.pop_head()
                # Case 2: removing tail
                elif current_node == self.tail:
                    # if tail of list use pop_tail function
                    return self.pop_tail()
                else:
                    # remove node from list, update references for both prev and next node
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    return current_node.player
            current_node = current_node.next_node
        return None  # No unique_id found

    def display(self, forward=True):
        """ display the list of players
        Forward=True: Head to Tail
        Forward=False: Tail to Head """
        if forward:
            current_node = self.head
            print("Forward=True: Head to Tail")
            while current_node is not None:
                print(f"uid: {current_node.player.uid}, Name: {current_node.player.name}")
                current_node = current_node.next_node

        # Logic for tail to head linked list iteration
        else:
            current_node = self.tail
            print("Forward=False: Tail to Head")
            while current_node is not None:
                print(f"uid: {current_node.player.uid}, Name: {current_node.player.name}")
                current_node = current_node.prev_node

    def is_empty(self):
        return self.head is None


class PlayerHashMap:
    def __init__(self, size=10):
        """Initialise Player Hash Map"""
        self.size = size
        self._map = {i: PlayerList() for i in range(size)}

    def get_index(self, key: str | Player):
        """Get a particular index player list via key"""
        if isinstance(key, Player):
            return hash(key) % self.size
        else:
            return Player.hash_function(key, self.size)

    def __getitem__(self, key: str | Player) -> None:
        """Get a player by key(Retrieve a player from the PlayerList with the corresponding index in the hash map.)"""
        if isinstance(key, Player):
            uid = key.uid
        else:
            uid = key

        #use has function inside player, get the particular index of the player list containing uid
        index = Player.hash_function(uid, self.size)
        playerlist = self._map[index]

        current_node = playerlist.head

        while current_node:
            if current_node.player.uid == uid:
                print(f"Player found: uid: {current_node.player.uid}, Name: {current_node.player.name}")
                return current_node.player
            current_node = current_node.next_node

        # if no player is found at all, should raise an error displaying uid was not found
        if current_node.is_empty():
            raise KeyError(f"Player not found: {uid}")
        return None

    # Add a new player to PlayerList in a corresponding index in the hash map.
    def __setitem__(self, key: str, name: str) -> None:
        """Adding new player to the hash map
           if player exist already, update the name
           if not, create a new player"""

        index = self.get_index(key)
        playerlist = self._map[index]

        current_node = playerlist.head
        while current_node:
            if current_node.player.uid == key:
                #found player using uid, update name
                current_node.name = name
                return
            #search through list
            current_node = current_node.next_node

        new_player = Player(key, name)
        playerlist.append(new_player)

    def len_lists(self) -> int:
        """ Return the number of player lists in the hash map.
            For testing only"""
        return len(self._map)

    def __len__(self) -> int:
        """Return number of players in hashmap (size(): Return the number of players in the hash map.)"""
        count = 0
        for playerlist in self._map.values():
            current_node = playerlist.head
            while current_node:
                count += 1
                current_node = current_node.next_node
        return count


    def __delitem__(self, key: str):
        """# Remove a player from the PlayerList with the corresponding index in the hash map."""
        index = self.get_index(key)
        playerlist = self._map[index]
        removed_node = playerlist.remove_by_id(key)
        if removed_node is None:
            print(f"Player not found: {key}")



# Testing
# pl1 = PlayerList()
# person1 = Player("001", "Sam")
# pl1.push(person1)
