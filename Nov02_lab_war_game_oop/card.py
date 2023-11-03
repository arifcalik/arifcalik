class Card:

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
    
    def display(self):
        print(f"{self._rank:2}:{self._suit}", end=" ")