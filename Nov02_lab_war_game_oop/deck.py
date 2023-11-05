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
        self._splits = []   #first split belongs to computer and followings are for players
        for suit in Deck._SUITS:
            for rank in Deck._RANKS:
                self._cards.append(Card(suit, rank))

    def display(self):
        print("...............DECK...............")
        for i, card in enumerate(self._cards):
            print(i, end =': ')
            card.display()

    def shuffle(self):
        random.shuffle(self._cards)
        #self.display()

    def split(self, players = 2):
        per_player = len(self._SUITS) * len(self._RANKS) // players
        for division in range(players):
            split = (self._cards[division * per_player : division * per_player + per_player])
            self._splits.append(split)
        return self._splits

    def remainingCardNumbers(self, split = 0):
        return len(self._splits[split])
    
    def display_splits(self):
        for index, split in enumerate(self._splits):
            print(f"\nSplit #{index}-----------------------")
            for i, card in enumerate(split):
                print(i, end =': ')
                card.display()

    def display_split(self, split):     #0 : computer 1:player
        if not split:   #computers split
            chosenSplit = self._splits[0]    #assumes 2players/extend for more players
        else:   #players split
            chosenSplit = self._splits[1]
        print(f"\nSplit #{split}-----------------------")
        for index, card in enumerate(chosenSplit):
            print(index, end =': ')
            card.display()

    def get_cards_from_split(self, split , numcards = 2):
        '''
        Think split array as a queue and take from beginning and add to the end!
        Take 2: one downfront first and then one upfront(peace case)
        Take 3: two downfront first and then one upfront(war case)
        '''
        if not split:   #computers split
            chosenSplit = self._splits[split]    #assumes 2players/extend for more players
        else:   #players split
            chosenSplit = self._splits[split]
        chosenCards = chosenSplit[:numcards]
        print(f"\nCards chosen #{split}***********************")
        for i in range(numcards):
            chosenSplit[i].display()
        #dont forget removing it from split
        self._splits[split] = self._splits[split][numcards:]
        return chosenCards

    def add_cards_to_winners_split(self, winner, cardsWon):
        '''
        before adding cards that has been won to the winners split
        shuffle it!
        '''
        if not winner:   #computers split
            chosenSplit = self._splits[winner]    #assumes 2players/extend for more players
        else:   #players split
            chosenSplit = self._splits[winner]
        random.shuffle(cardsWon)
        self._splits[winner].extend(cardsWon)
