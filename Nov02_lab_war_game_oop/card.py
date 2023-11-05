from termcolor import colored
#why is this functional just in vscode debug run?

class Card:
    _RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    _NUMRANKS = 13

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    def getRank(self):
        return Card._NUMRANKS - Card._RANKS.index(self._rank) + 1   #to make it compatible with digits

    def display(self):
        print(colored(self._rank, 'green'), colored(self._suit, "green"))
