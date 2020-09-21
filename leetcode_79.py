class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if(word == ""):
            return True
        if(board == [[]]):
            return False
        self.board = board
        self.word = word
        self.x = len(board)
        self.y = len(board[0])
        self.rs = False
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(self.board[i][j] == self.word[0]):
                    self.DFS(i, j, 0)
        return self.rs

    def DFS(self, x, y, key):
        if(self.rs == True):
            return
        if(key == len(self.word)):
            self.rs = True
            return
        if(x < 0 or x >= self.x or y < 0 or y >= self.y):
            return
        k = self.board[x][y]
        if(k == self.word[key]):
            self.board[x][y] = 0
            self.DFS(x-1, y, key+1)
            self.DFS(x+1, y, key+1)
            self.DFS(x, y-1, key+1)
            self.DFS(x, y+1, key+1)
            self.board[x][y] = k
        return
        
s = Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
