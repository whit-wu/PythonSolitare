# main class.  contains flow control for the game.
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
    
    # creation of objects
    myDeck = Deck()
    myDeck.createDeck()
    myBoard = Board(myDeck)

    # prints board onto screen
    myBoard.printBoard()

    myRules = Rules(myBoard, myDeck)

    # boardFull = myRules.CheckBoard()
    playGame = True
    gameOver = True

    # while the game is being played...
    while (playGame == True):
        while (myRules.CheckBoard() == False): # check if values can be placed onto the board
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

        pairsRemaining = myRules.PairsLeft() # check if their are any neighbor pairs that add up to 10 and cards with value of 10
        if (myDeck.currentCard > 51): # if we use up the deck, break from the loop
            break
        if (pairsRemaining == False): # if there are no pairs remaining and the board is full, 
            gameOver = False            # set gameOver to false and break from loop.
            break

        while (pairsRemaining == True):  # while there are pairs neighbor remaining that add up to 10 and cards with value of 10
            # os.system('cls')
            # myBoard.printBoard()
            print("Enter first card to clear: ") # prompt user for input on which cards to clear
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
    if (gameOver == False):  # if this is false, player loses the game
        os.system('cls')
        print("You lose!")
        print("Cards you have played: " + str(myDeck.currentCard))
        # print(myRules.boardVals)
    elif (gameOver == True): # if this is true, player wins the game.
        os.system('CLS')
        print("You Win!")

    return 0

if __name__ == "__main__":
    main()
