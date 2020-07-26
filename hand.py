from card import Card, Suit


class Hand(object):
    def __init__(self, is_dealer=False):
        self.cards = []
        self.is_dealer = is_dealer
        self.revealed = not is_dealer
    
    def add_card(self, card:Card):
        if not card:
            raise ValueError('dealt a blank card')
        self.cards.append(card)

    def get_hand(self):
        if self.is_dealer and not self.revealed:
            return '** ' + ' '.join([str(card) for card in self.cards[1:]])
        else:
            return ' '.join([str(card) for card in self.cards])

    @property
    def hand_value(self):
        card_values = [card.value for card in self.cards]
        total = sum(card_values)
        if self.is_dealer and not self.revealed:
            total -= card_values[0]
        elif total > 21 and 11 in card_values:
            total -= 10
        return total

if __name__ == '__main__':
    h1 = Hand(True)
    h1.add_card(Card(Suit.DIAMONDS, 'A'))
    h1.add_card(Card(Suit.SPADES, '6'))
    h1.add_card(Card(Suit.HEARTS, '4'))
    print(h1.get_hand())
    print(f"hand worth: {h1.hand_value}")
    print("Revealing dealer's last card")
    h1.revealed = True
    print(h1.get_hand())
    print(f"hand worth: {h1.hand_value}")

