#Plauer.py file for Assessment 1
# Author: Samuel Peach

class Player:
    def __init__(self, uniqueid, playername):
        self.uid = uniqueid
        self.name = playername

    def __str__(self):
        return f"{self.uid}: {self.name}"
    
