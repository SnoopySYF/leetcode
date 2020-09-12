class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        lmove = len(moves)
        if(lmove < 5):
            return "Pending"
        num = [[0 for i in range(3)] for j in range(3)]
        for i in range(lmove):
            if(i % 2 == 0):
                num[moves[i][0]][moves[i][1]] = 1
            else:
                num[moves[i][0]][moves[i][1]] = 2
        for i in range(3):
            co = num[i][i]
            if(num[i][0] == num[i][1] == num[i][2]):
                if(co == 1):
                    return "A"
                elif(co == 2):
                    return "B"
            if(num[0][i] == num[1][i] == num[2][i]):
                if(co == 1):
                    return "A"
                elif(co == 2):
                    return "B"
        co = num[1][1]
        if(co != 0):
            if(num[0][0] == num[1][1] == num[2][2]):
                if(co == 1):
                    return "A"
                elif(co == 2):
                    return "B"
            if(num[2][0] == num[1][1] == num[0][2]):
                if(co == 1):
                    return "A"
                elif(co == 2):
                    return "B" 
        if(lmove == 9):
            return "Draw"
        else:
            return "Pending" 

        
