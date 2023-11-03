'''
This is card deck of 4-suites 13-ranks
'''
from card import Card
import random

class Deck:
    #try tuples for speeds sake later
    _SUITS = ["H", "D", "S", "C"]
    _RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self):
        self._cards = []
        self._splits = []
        for suit in self._SUITS:
            for rank in self._RANKS:
                self._cards.append(Card(suit, rank))

    def display(self):
        print("...............DECK...............")
        for i, card in enumerate(self._cards):
            print(i, end =': ')
            card.display()
        print("\n...............DECK...............")

    def shuffle(self):
        random.shuffle(self._cards)
        #self.display()

    def split(self, players=3):
        per_player = len(self._SUITS) * len(self._RANKS) // players
        for division in range(players):
            self._splits.append(self._cards[division * per_player : division * per_player + per_player])
        #return self._splits
    
    def display_splits(self):
        for index, _split in enumerate(self._splits):
            print(f"Split #{index}-----------------------\n")
            for i, card in enumerate(_split):
                print(i, end =': ')
                card.display()  
            print(f"\nSplit #{index}-----------------------\n")          