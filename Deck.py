# class that creates a deck of cards
import random
import itertools


class Deck(object):

    def __init__(self):
        self.currentCard = 0
        self.cardDeck = self.createDeck()

    def createDeck(self):
        SUITS = u'\u2660\u2663\u2665\u2666'
        RANKS = '23456789TJQKA'
        # declaration of deck tuple.  uses for loop to populate a tuple
        DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
        # converts the tuple to a list.
        randDeck = list(DECK)
        # for loop to shuffle the deck.
        for x in range(0, 1000):
            random.shuffle(randDeck)
        return randDeck
