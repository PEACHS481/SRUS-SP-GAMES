#Player List for Assessment 1
#Author Samuel Peach

from player_node import PlayerNode
from player import Player  

#Initialise Class PlayerList
class PlayerList:
    def __init__(self):
        self.head = None
        self.tail = None

# Push method to insert new node at head of list
    def push(self, player):
        new_node = PlayerNode(player)
        new_node.next_node = self.head

        if self.head is not None:
            self.head.prev_node = new_node
        else:
            self.tail = new_node

        self.head = new_node 

    def append(self, player):
        new_node = Player(player)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def pop_head(self):
        if self.head is None:
            return None
        
        removed_node = self.head
        self.head = self.head.next_node

        if self.head is not None:
            self.head.prev_node = None
        else:
            # list is empty so tail must be updated to be None
            self.tail = None
        
        return removed_node.player
    
    def pop_tail(self):
        if self.tail is None:
            return None
        
        removed_node = self.tail
        self.tail = self.tail.prev_node

        if self.tail is not None:
            self.tail.next_node = None
        else:
            #list is empty and head must be updated to be None
            self.head = None

        return removed_node.player

    def is_empty(self):
        return self.head is None
    
#Testing
#pl1 = PlayerList()
#person1 = Player("001", "Sam")
#pl1.push(person1)
