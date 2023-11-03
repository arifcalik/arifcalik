from deck import Deck

def main():
    deck = Deck()
    deck.shuffle()
    #deck.display()
    deck.split(5)   #5players
    deck.display_splits()

if __name__ == "__main__":
    main()