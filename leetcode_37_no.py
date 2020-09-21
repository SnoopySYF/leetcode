class Solution(object):
    def __init__(self):
        self.board = 0

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.getNum(0, 0)
        return self.board

    def getNum(self, x, y):
        if(x == 9):
            return True
        if(y == 9):
            return self.getNum(x+1, 0)
        if(self.board[x][y] != "."):
            self.getNum(x, y+1)
        for i in range(1,10):
            if(not self.isValid(x, y, str(i))):
                continue
            self.board[x][y] = str(i)
            if(self.getNum(x, y+1)):
                return True
            self.board[x][y] = "."
        return False


    def isValid(self, x, y, val):
        for i in range(9):
            if(self.board[i][y] == val or self.board[x][i] == val):
                return False
        row = x - x % 3
        col = y - y % 3
        for i in range(3):
            for j in range(3):
                if(self.board[row+i][col+j] == val):
                    return False
        return True
