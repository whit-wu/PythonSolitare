# class to dictate the rules of the game.
from Board import Board
from Deck import Deck
import os

playedCards = 0
# myBoard = Board()
# myDeck = Deck()

class Rules(object):

    def __init__(self,  boarVars, deckVars):
        # Dictionary to store the values in each cell of the board
        self.boardVals = {'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0,
                     'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0,
                     'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0,
                     'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0}
        self.Board = boarVars
        self.Deck = deckVars



    # function that moves values to each cell.  Calls upon assignval function to do this.
    def moveValue(self, move):

        if self.EntryValidation(move) == True:
            if self.CellAvailable(move) == True:
                self.Board.theBoard[move] = self.Deck.cardDeck[self.Deck.currentCard]
                self.Deck.currentCard += 1

                self.AssignVal(move)
            # cardsPlayed(playedCards)
            else:
                print("Cell Occupied")
                os.system('pause')
        else:
            print("Invalid Entry")
            os.system("pause")

    # Clears cells from board
    def ClearCell(self, cellInput1, cellInput2):
        # checks if cells are neighbors
        if (self.EntryValidation(cellInput1) == False):
            print("First entry invalid")
            os.system('pause')
        if (self.EntryValidation(cellInput2) == False):
            print('Second Entry invalid')
            os.system('pause')
        if (self.IsNeighbor(cellInput1, cellInput2) == True or cellInput2 == 'N' or cellInput2 == 'n'):
            if (self.EqualsTen(cellInput1, cellInput2) == True):
                # Displays a discard
                self.Board.theBoard['DC'] = self.Board.theBoard[cellInput1]
                # come back to this
                self.Board.theBoard[cellInput1] = '  '
                self.Board.theBoard[cellInput2] = '  '
                self.boardVals[cellInput1] = 0
                self.boardVals[cellInput2] = 0
        else:
            print("Invalid Entry.  Cells are not neighbors")
            os.system('pause')

    # checks if board is full.  if yes, returns true.  Else, returns false
    def CheckBoard(self):
        count = 0
        for k in self.boardVals.keys():
            if self.boardVals[k] != 0:
                count += 1

        if count == 16:
            return True
        else:
            return False

    # assigns value to each cell upon input
    def AssignVal(self, cellInput):

        if 'A' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 1
        if '2' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 2
        if '3' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 3
        if '4' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 4
        if '5' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 5
        if '6' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 6
        if '7' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 7
        if '8' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 8
        if '9' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 9
        if 'T' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 10
        if 'J' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 11
        if 'Q' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 12
        if 'K' in self.Board.theBoard[cellInput]:
            self.boardVals[cellInput] = 13

    # determines if there are any pairs left on the board
    # returns true if pairs exist, else returns false
    def PairsLeft(self):
        # create local variables with shortened names to save on typing
        A1 = self.boardVals['A1']
        A2 = self.boardVals['A2']
        A3 = self.boardVals['A3']
        A4 = self.boardVals['A4']
        B1 = self.boardVals['B1']
        B2 = self.boardVals['B2']
        B3 = self.boardVals['B3']
        B4 = self.boardVals['B4']
        C1 = self.boardVals['C1']
        C2 = self.boardVals['C2']
        C3 = self.boardVals['C3']
        C4 = self.boardVals['C4']
        D1 = self.boardVals['D1']
        D2 = self.boardVals['D2']
        D3 = self.boardVals['D3']
        D4 = self.boardVals['D4']

        # Check if any pairs are left on the board
        if (A1 + B1 == 10 or A1 + B2 == 10 or A1 + A2 == 10 or A1 == 10 or
                        A2 + B1 == 10 or A2 + B2 == 10 or A2 + B3 == 10 or A2 + A3 == 10 or A2 == 10 or
                        A3 + B2 == 10 or A3 + B3 == 10 or A3 + B4 == 10 or A3 + A4 == 10 or A3 == 10 or
                        A4 + B3 == 10 or A4 + B4 == 10 or A4 == 10 or B1 + B2 == 10 or B1 + C2 == 10 or
                        B1 + C1 == 10 or B1 == 10 or B2 + B3 == 10 or B2 + C3 == 10 or B2 + C2 == 10 or
                        B2 + C1 == 10 or B2 == 10 or B3 + C2 == 10 or B3 + C3 == 10 or B3 + C4 == 10 or
                        B3 + B4 == 10 or B3 == 10 or B4 + C3 == 10 or B4 + C4 == 10 or B4 == 10 or
                        C1 + C2 == 10 or C1 + D2 == 10 or C1 + D1 == 10 or C1 == 10 or C2 + C3 == 10 or
                        C2 + D3 == 10 or C2 + D2 == 10 or C2 + D1 == 10 or C2 == 10 or C3 + C4 == 10 or
                        C3 + D4 == 10 or C3 + D3 == 10 or C3 + D2 == 10 or C3 == 10 or C4 + D3 == 10 or
                        C4 + D4 == 10 or C4 == 10 or D1 + D2 == 10 or D1 == 10 or D2 + D3 == 10 or D2 == 10 or
                        D3 + D4 == 10 or D3 == 10 or D4 == 10):
            return True
        else:
            return False

    # checks if inputed cards are next to eachother.  If so, returns true
    def IsNeighbor(self, cellInput1, cellInput2):
        if (cellInput1 == 'A1'):
            if (cellInput2 == 'B1' or cellInput2 == 'B2' or cellInput2 == 'A2'):
                return True
            else:
                return False

        if (cellInput1 == 'A2'):
            if (
                                cellInput2 == 'A1' or cellInput2 == 'B1' or cellInput2 == 'B2' or cellInput2 == 'B3' or cellInput2 == 'A3'):
                return True
            else:
                return False

        if (cellInput1 == 'A3'):
            if (
                                cellInput2 == 'A2' or cellInput2 == 'B2' or cellInput2 == 'B3' or cellInput2 == 'B4' or cellInput2 == 'A4'):
                return True
            else:
                return False

        if (cellInput1 == 'A4'):
            if (cellInput2 == 'A3' or cellInput2 == 'B3' or cellInput2 == 'B4'):
                return True
            else:
                return False

        if (cellInput1 == 'B1'):
            if (
                                cellInput2 == 'A1' or cellInput2 == 'A2' or cellInput2 == 'B2' or cellInput2 == 'C2' or cellInput2 == 'C1'):
                return True
            else:
                return False

        if (cellInput1 == 'B2'):
            if (
                                            cellInput2 == 'B1' or cellInput2 == 'A1' or cellInput2 == 'A2' or cellInput2 == 'A3' or cellInput2 == 'B3' or
                            cellInput2 == 'C3' or cellInput2 == 'C2' or cellInput2 == 'C1'):
                return True
            else:
                return False

        if (cellInput1 == 'B3'):
            if (
                                            cellInput2 == 'B2' or cellInput2 == 'A2' or cellInput2 == 'A3' or cellInput2 == 'A4' or cellInput2 == 'B4' or
                            cellInput2 == 'C4' or cellInput2 == 'C3' or cellInput2 == 'C2'):
                return True
            else:
                return False

        if (cellInput1 == 'B4'):
            if (
                                cellInput2 == 'B3' or cellInput2 == 'A3' or cellInput2 == 'A4' or cellInput2 == 'C4' or cellInput2 == 'C3'):
                return True
            else:
                return False

        if (cellInput1 == 'C1'):
            if (
                                cellInput2 == 'B1' or cellInput2 == 'B2' or cellInput2 == 'C2' or cellInput2 == 'D2' or cellInput2 == 'D1'):
                return True
            else:
                return False

        if (cellInput1 == 'C2'):
            if (
                                            cellInput2 == 'C1' or cellInput2 == 'B1' or cellInput2 == 'B2' or cellInput2 == 'B3' or cellInput2 == 'C3' or
                            cellInput2 == 'D3' or cellInput2 == 'D2' or cellInput2 == 'D1'):
                return True
            else:
                return False

        if (cellInput1 == 'C3'):
            if (
                                            cellInput2 == 'C2' or cellInput2 == 'B2' or cellInput2 == 'B3' or cellInput2 == 'B4' or cellInput2 == 'C4' or
                            cellInput2 == 'D4' or cellInput2 == 'D3' or cellInput2 == 'D2'):
                return True
            else:
                return False

        if (cellInput1 == 'C4'):
            if (
                                cellInput2 == 'C3' or cellInput2 == 'B3' or cellInput2 == 'B4' or cellInput2 == 'D4' or cellInput2 == 'D3'):
                return True
            else:
                return False

        if (cellInput1 == 'D1'):
            if (cellInput2 == 'C1' or cellInput2 == 'C2' or cellInput2 == 'D2'):
                return True
            else:
                return False

        if (cellInput1 == 'D2'):
            if (
                                cellInput2 == 'D1' or cellInput2 == 'C1' or cellInput2 == 'C2' or cellInput2 == 'C3' or cellInput2 == 'D3'):
                return True
            else:
                return False

        if (cellInput1 == 'D3'):
            if (
                                cellInput2 == 'D2' or cellInput2 == 'C2' or cellInput2 == 'C3' or cellInput2 == 'C4' or cellInput2 == 'D4'):
                return True
            else:
                return False

        if (cellInput1 == 'D4'):
            if (cellInput2 == 'D3' or cellInput2 == 'C3' or cellInput2 == 'C4'):
                return True
            else:
                return False

    # checks if inputted values equal 10
    def EqualsTen(self, cellInput1, cellInput2):
        if (self.boardVals[cellInput1] == 10 and cellInput2 == 'N'):
            return True
        if (self.boardVals[cellInput1] + self.boardVals[cellInput2] == 10):
            return True
        else:
            print("Values do not add up to 10.")
            os.system('pause')
            return False

    # checks if user input is valid
    def EntryValidation(self, givenKey):
        keyNames = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4', 'N']
        valueExists = False
        givenKey.upper()
        if any(givenKey in s for s in keyNames):
            valueExists = True
        if valueExists == True:
            return True
        else:
            return False

    # checks if cell is available to have card placed in it.
    def CellAvailable(self, givenCell):


        if self.Board.theBoard[givenCell] == '  ':
            return True
        else:
            return False
