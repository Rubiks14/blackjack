from card import Card
from random import shuffle


class Deck(object):
    def __init__(self, num_decks=1):
        self.cards = [Card(suit, rank)
                        for i in range(num_decks)
                        for suit in Card.VALID_SUITS
                        for rank in Card.VALID_RANKS]

    def shuffle(self):
        if len(self.cards):
            shuffle(self.cards)
    
    def deal_card(self):
        if len(self.cards):
            return self.cards.pop()
        else:
            raise IndexError("Deck is empty")


if __name__ == "__main__":
    d = Deck()
    print(d.cards)
    d.shuffle()
    d.shuffle()
    print()
    print(d.cards)