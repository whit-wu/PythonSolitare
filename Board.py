# Class that prints a board onto the console.
from Deck import Deck
class Board(object):

    # A dictionary to store the card values in each board cell
    def __init__(self, deckVars):
        self.theBoard = {'A1': '  ', 'A2': '  ', 'A3': '  ', 'A4': '  ', 'DC': '  ',
                        'B1': '  ', 'B2': '  ', 'B3': '  ', 'B4': '  ',
                        'C1': '  ', 'C2': '  ', 'C3': '  ', 'C4': '  ',
                        'D1': '  ', 'D2': '  ', 'D3': '  ', 'D4': '  ', 'CC': '  '}

    # theBoard = {'A1': '  ', 'A2': '  ', 'A3': '  ', 'A4': '  ', 'DC': '  ',
    #             'B1': '  ', 'B2': '  ', 'B3': '  ', 'B4': '  ',
    #             'C1': '  ', 'C2': '  ', 'C3': '  ', 'C4': '  ',
    #             'D1': '  ', 'D2': '  ', 'D3': '  ', 'D4': '  ', 'CC': '  '}
        self.Deck = deckVars
    # function that prints the board onto the screen. 
    def printBoard(self):
        #self.theBoard['CC'] = Deck.cardDeck[Deck.currentCard]
        boardDeck = Deck()
        self.theBoard['CC'] = self.Deck.cardDeck[self.Deck.currentCard]
        print('  A   B    C   D     Discard')
        print(' +---+---+---+---+   +---+')
        print('1| ' + self.theBoard['A1'] + '| ' + self.theBoard['B1'] + '| ' + self.theBoard['C1'] + '| ' + self.theBoard['D1'] + '|   |' + self.theBoard['DC'] + ' |')
        print(' +---+---+---+---+   +---+')
        print('2| ' + self.theBoard['A2'] + '| ' + self.theBoard['B2'] + '| ' + self.theBoard['C2'] + '| ' + self.theBoard['D2'] + '|')
        print(' +---+---+---+---+')
        print('3| ' + self.theBoard['A3'] + '| ' + self.theBoard['B3'] + '| ' + self.theBoard['C3'] + '| ' + self.theBoard['D3'] + '|   Deck')
        print(' +---+---+---+---+   +---+')
        print('4| ' + self.theBoard['A4'] + '| ' + self.theBoard['B4'] + '| ' + self.theBoard['C4'] + '| ' + self.theBoard['D4'] + '|   |' + self.theBoard['CC'] + ' |')
        print(' +---+---+---+---+   +---+')
