from enum import Enum

class Suit(Enum):
    SPADES = '\U00002660'
    CLUBS = '\U00002663'
    DIAMONDS = '\U00002666'
    HEARTS = '\U00002665'

    def __str__(self):
        return f'{self.value}'


class Card(object):
    """
    Contains the textual representation of a standard playing card
    """

    def __init__(self, suit:str, rank:str):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.suit}{self.rank}'.upper()
    
    def __repr__(self):
        return f'Card({self.suit}, {self.rank})'

    @property
    def value(self):
        """
        returns the value of the card based on the rank, 1 - 10; J, Q, K == 10; A == 11
        """
        if all(0 <= ord(num) - ord('0') < 10 for num in self.rank):
            return int(self.rank)
        elif self.rank == 'A':
            return 11
        else:
            return 10
