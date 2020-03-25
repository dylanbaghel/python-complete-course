"""
Card:
    # Each instance of `Card` should have a suit("Hearts", "Diamonds", "Clubs", "Spades").
    # Each instance of `Card` should have a value("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    # `Card's` `__repr__` method shoud display the card's value and suit(e.g "A of Clubs", "J of Diamonds", etc.)

Deck:
    # Each instance `Deck` should have a cards attribute with all 52 possible instance of `Card`.
    # `Deck` should have an instance method called `count` which returns a count of how many cards remain in the deck.
    # `Deck's` `__repr__` method should display information on how many cards are in the deck(e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
    # `Deck` should have an instance method called `_deal` which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a `ValueError` with the message "All cards have been dealt".
    # `Deck` should have an instance method called `shuffle` which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a `ValueError` with message 'Only full decks can be shuffled'.
    # `Deck` should have an instance method called `deal_card` which uses the `_deal` method to deal a single card from the desk.
    # `Deck` should have an instance method called `deal_hand` which accepts a number and uses the `_deal` method to deal a list of cards from the deck.
"""


import random

class Card:
    allowed_suits = ('Hearts', 'Diamond', 'Clubs', 'Spades')
    allowed_values = tuple("A,2,3,4,5,6,7,8,9,10,J,Q,K".split(','))

    def __init__(self, suit, value):
        if suit not in Card.allowed_suits:
            raise ValueError(f"{suit} is not allowed.")
        if value not in Card.allowed_values:
            raise ValueError(f"{value} is not allowed")
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        allowed_suits = ('Hearts', 'Diamond', 'Clubs', 'Spades')
        allowed_values = "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(',')
        self.cards = [ Card(suit, value) for suit in allowed_suits for value in allowed_values]
    
    def count(self):
        return len(self.cards)
    
    def _deal(self, limit):
        if self.count() <= 0:
            raise ValueError('All Cards Have Been Dealt')
        counter = min([limit, self.count()])
        print(f"Removing {counter} Cards")
        for i in range(0, counter):
            self.cards.pop()
    
    def shuffle(self):
        if (self.count() < 52):
            raise ValueError('Only Full Decks Can Be Shuffled')
        random.shuffle(self.cards)
    
    def deal_card(self):
        self._deal(1)

    def deal_hand(self, limit):
        self._deal(limit)

    def __repr__(self):
        return f"Deck of {self.count()} cards"


deck = Deck()
print(deck)
deck.deal_card()
print(deck)
deck.deal_card()
print(deck)
deck.deal_hand(12)
print(deck)
deck.deal_hand(40)
print(deck)
