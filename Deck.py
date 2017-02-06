import random
import itertools


class Deck(object):

    def __init__(self):
        self.currentCard = 0
        self.cardDeck = self.createDeck()

    def createDeck(self):
        SUITS = u'\u2660\u2663\u2665\u2666'
        RANKS = '23456789TJQKA'
        DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
        randDeck = list(DECK)
        for x in range(0, 1000):
            random.shuffle(randDeck)
        return randDeck