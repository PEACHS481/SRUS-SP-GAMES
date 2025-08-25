#Plauer.py file for Assessment 1
# Author: Samuel Peach

class Player:
    def __init__(self, unique_id: str, player_name: str):
        self._uid = unique_id
        self._name = player_name

    def __str__(self):
        return f"{self._uid}: {self._name}"
    
    @property
    def name(self) -> str:
        return  self._name

    @property
    def uid(self) -> str:
        return self._uid

# setup for hashmap
    @classmethod
    def your_chosen_hash_function(cls, key: str) -> int:
        ...

    def __hash__(self):
        return self.your_chosen_hash_function(self.uid)