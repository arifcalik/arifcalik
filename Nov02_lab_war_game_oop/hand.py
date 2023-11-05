class Hand:
    '''
    This hand should be taken from relevant players split
    and must be composed of cards upfront and downfront cards in order.
    As a rule always take the first card from split as downfront
    and second one as upfront as in pokers discard cards to
    get rid of possible cheating.

    In peace case each player has just an upfront and a downfront card
    but in war case:
    in addition to those two downfront and a upfront cards
    in total there will be 10 cards(two downfront and one upfront for each player)
    and sure for fairness, first two top cards from the deck will be downfront and
    third card will be upfront!
    '''
    from card import Card

    def __init__(self, cards):   #0:computer 1:player
        self._cards = cards
        self._upfrontCard = self._cards[-1]
        #any need for revealing downfront? for now big NO as in poker
        '''
        first indices are always downfront cards as in poker
        last card is upfront one!
        '''
    def getUpfrontCardRank(self):   #no need for suit
         return self._upfrontCard.getRank()

    def getCards(self):
        return self._cards

    def display(self):
            print("Upfront card: ")
            #self._cards[-1].display()
            self._upfrontCard.display()
            print("Downfront card(s): ")
            for i, c in enumerate(self._cards):
                 if i != len(self._cards) - 1:
                    c.display()
                            