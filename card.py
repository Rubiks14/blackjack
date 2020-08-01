from enum import Enum


class Card(object):
    """
    Contains the textual representation of a standard playing card
    """
    VALID_RANKS = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')
    VALID_SUITS = ('\U00002660', '\U00002663', '\U00002666', '\U00002665')

    def __init__(self, suit:str, rank:str):
        if suit.value not in self.VALID_SUITS:
            raise ValueError(f'{suit} is not a valid card suit')
        if rank not in self.VALID_RANKS:
            raise ValueError(f'{rank} is not a valid card rank')
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
        elif self.rank in 'JQK':
            return 10
