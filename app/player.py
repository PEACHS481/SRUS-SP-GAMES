# Plauer.py file for Assessment 1
# Author: Samuel Peach

class Player:
    def __init__(self, unique_id: str, player_name: str):
        self._uid = unique_id
        self._name = player_name

    def __str__(self):
        return f"{self._uid}: {self._name}"

    @property
    def name(self) -> str:
        return self._name

    @property
    def uid(self) -> str:
        return self._uid


    @classmethod
    def hash_function(cls, key: str, size: int) -> int:
        total = 0
        for char in key:
            total += ord(char)
        return total % size

    def __hash__(self):
        return self.hash_function(self.uid)
