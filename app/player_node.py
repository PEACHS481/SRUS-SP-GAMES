#Player Node file for Assessment 1
# Author: Samuel Peach

from player import Player

class PlayerNode:
    def __init__(self, player = None):
        self.player = player
        self.next_node =  None
        self.prev_node = None

    def __str__(self):
        return self.player

    def next_node(self):
        return self.next_node

    def prev_node(self):
        return self.prev_node

    def key(self):
        return self.player.uid
