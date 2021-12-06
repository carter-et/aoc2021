import numpy as np
class Board:
    #init expects a string input of a board 
    def __init__(self, board_array):
        self.board = self.createBoard(board_array)
        self.total = self.getInitialTotal()
        self.hasWon = False

    #create a 5x5 board to this object
    def createBoard(self, board_array):
        return np.array(board_array)
    
    #get the starting value of all numbers on the board
    def getInitialTotal(self):
        return int(np.sum(self.board))

    #adjust the total by the value that hit
    def adjustTotal(self, value):
        self.total -= value
    
    #check if board contains value. Returns true if found.
    def checkBoardForValue(self, value):
        found = list(zip(*np.where(self.board == value)))
        if(len(found) == 1): #if there are more than one, we messed up
            (x, y) = found[0]
            self.board[x,y] = -1
            return True
        return False

    #check if board is in a winning condition    
    def checkBoardForWin(self):
        for row in self.board:
            if(int(np.sum(row)) == -5):
                return True
        for col in self.board.transpose():
            if(int(np.sum(col)) == -5):
                return True
        return False

    #check if board has won, and process hits
    def calculateBoard(self, value):
        if(self.checkBoardForValue(value) and not self.hasWon):
            self.adjustTotal(value)
            if(self.checkBoardForWin()):
                self.hasWon = True
                return(True, self.total)
        return(False,0)