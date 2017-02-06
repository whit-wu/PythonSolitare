# chcp 65001
import os
from Board import Board
from Rules import Rules
from Deck import Deck
def main():
    # myBoard = Board()
    # myRules = Rules()
    # myDeck = Deck()
    # myBoard.printBoard()
    os.system('cls')
    myDeck = Deck()
    myDeck.createDeck()
    myBoard = Board(myDeck)

    myBoard.printBoard()

    myRules = Rules(myBoard, myDeck)

    # boardFull = myRules.CheckBoard()
    playGame = True
    gameOver = True

    while (playGame == True):
        while (myRules.CheckBoard() == False):
            print("Insert location to place card")
            move = input()
            move = move.upper()
            myRules.moveValue(move)
            os.system('CLS')
            myBoard.printBoard()
            # print(myDeck.currentCard)
            if (myDeck.currentCard > 51):
                gameOver = True
                # playGame = False
                break

        pairsRemaining = myRules.PairsLeft()
        if (myDeck.currentCard > 51):
            break
        if (pairsRemaining == False):
            gameOver = False
            break

        while (pairsRemaining == True):
            # os.system('cls')
            # myBoard.printBoard()
            print("Enter first card to clear: ")
            cellInput1 = input()
            cellInput1 = cellInput1.upper()
            os.system('cls')
            myBoard.printBoard()
            print("Enter second card to clear (N if none): ")
            cellInput2 = input()
            cellInput2 = cellInput2.upper()
            myRules.ClearCell(cellInput1, cellInput2)
            pairsRemaining = myRules.PairsLeft()
            # boardFull == myRules.CheckBoard()
            os.system('cls')
            myBoard.printBoard()
        continue
    if (gameOver == False):
        os.system('cls')
        print("You lose!")
        print("Cards you have played: " + str(myDeck.currentCard))
        # print(myRules.boardVals)
    elif (gameOver == True):
        os.system('CLS')
        print("You Win!")

    return 0

if __name__ == "__main__":
    main()