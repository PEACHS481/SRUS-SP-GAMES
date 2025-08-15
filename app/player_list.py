#Player List for Assessment 1
#Author Samuel Peach

from player_node import PlayerNode
from player import Player  

#Initialise Class PlayerList
class PlayerList:
    def __init__(self):
        self.head = None

# Push method to insert new node at head of list
    def push(self, player):
        new_node = PlayerNode(player)
        new_node.next_node = self.head

        if self.head is not None:
            self.head.prev_node = new_node
        self.head = new_node 

    def is_empty(self):
        return self.head is None
    
#Testing
#pl1 = PlayerList()
#person1 = Player("001", "Sam")
#pl1.push(person1)
