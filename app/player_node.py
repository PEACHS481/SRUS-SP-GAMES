#Player Node file for Assessment 1
# Author: Samuel Peach

from app.player import Player

class PlayerNode:
    def __init__(self, player: Player) -> None:
        self._player = player
        self._next_node =  None
        self._prev_node = None

    def __str__(self) -> str:
        return str(self._player)

    @property
    def key(self) -> str:
        return self._player.uid

    @property
    def player(self) -> Player:
        """Expose the Player object stored in this node."""
        return self._player

    @property
    def next_node(self):
        """Expose the Next Node stored in this node."""
        return self._next_node

    @property
    def prev_node(self):
        """Expose the Previous Node stored in this node."""
        return self._prev_node