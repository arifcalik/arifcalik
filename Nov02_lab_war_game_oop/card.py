from termcolor import colored
#why is this functional just in vscode debug run?

class Card:

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
    
    def display(self):
        print(colored(self._rank, 'green'), colored(self._suit, "green"))
