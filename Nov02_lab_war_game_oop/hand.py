class Hand:
    '''
    This hand should be taken from relevant players split
    and must be composed of cards upfront and downfront cards
    in order 
    As a rule always take the first card from split as downfront
    and second one as upfront as in poker discard cards to
    get rid of possible cheating.

    In peace case each player has just an upfront and a downfront card
    but in war case
    in addition to those two downfront and a upfront card
    in total there will be 10 cards
    '''
    def __init__(self, num_cards):
        self._cards = []
        self._cards.append()
    
    def display(self):
        print(f"{self._rank:2}:{self._suit}", end=" ")