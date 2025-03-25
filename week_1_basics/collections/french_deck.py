from collections import namedtuple
import random

Card = namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(i) for i in range(1, 11)] + list("JQKA")
    suits = "spades, diamonds, clubs, hearts".split(", ")

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]


deck = FrenchDeck()

for card in deck:
    print(card)
