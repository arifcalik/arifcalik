from deck import Deck
'''
An overview goes here!
'''
#better later to move those as war class attribute?
COMPUTER = 0
PLAYER = 1


#temporariyl import
from card import Card
from hand import Hand

def game():
    deck = Deck()
    deck.shuffle()
    #deck.display()
    split_computer, split_player = deck.split()   #default 2 players
    #deck.display_splits()
    deck.display_split(COMPUTER)
    handCardsComputer = deck.get_cards_from_split(COMPUTER)
    print("After removing first two cards from 1st split")
    deck.display_split(COMPUTER)
    deck.display_split(PLAYER)
    handCardsPlayer = deck.get_cards_from_split(PLAYER)
    print("After removing first two cards from 2nd split")
    deck.display_split(PLAYER)

    handComputer = Hand(handCardsComputer)
    handComputer.display()
    handPlayer = Hand(handCardsPlayer)
    handPlayer.display()

    print("Computer has " + str(handComputer.getUpfrontCardRank()))
    print("VERSUS")
    print("Player has " + str(handPlayer.getUpfrontCardRank()))

    cardsWon = handComputer.getCards() + handPlayer.getCards()

    if handComputer.getUpfrontCardRank() > handPlayer.getUpfrontCardRank():
        print("Computer wins!!!")
        deck.add_cards_to_winners_split(COMPUTER, cardsWon)
        deck.display_split(COMPUTER)
    elif(handComputer.getUpfrontCardRank() < handPlayer.getUpfrontCardRank()):
        print("Player wins!!!")
        deck.add_cards_to_winners_split(PLAYER, cardsWon)
        deck.display_split(PLAYER)
    else:
        print("This is WAR!!!!")

def main():
    game()

if __name__ == "__main__":
    main()