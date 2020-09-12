class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if(i == 0):
                    if(j == 0):
                        res[i][j] = matrix[i][j]
                    else:
                        res[i][j] = res[i][j-1] + matrix[i][j]
                elif(i == 1):
                    if(j == 0):
                        res[i][j] = res[i-1][j] + matrix[i][j]
                    else:
                        if(matrix[i][j] == 0):
                            res[i][j] = res[i][j-1] + res[i-1][j] - res[i-1][j-1]
                        elif(matrix[i][j] == matrix[i][j-1] == matrix[i-1][j] == matrix[i-1][j-1] == 1):
                            res[i][j] = res[i][j-1] + res[i-1][j] - res[i-1][j-1] + 2
                        else:
                            res[i][j] = res[i][j-1] + res[i-1][j] - res[i-1][j-1] + 1
                else:
                    if(j == 0):
                        res[i][j] = res[i-1][j] + matrix[i][j]
                    elif(j == 1):
                        if(matrix[i][j] == 0):
                            res[i][j] = res[i][j-1] + res[i-1][j] - res[i-1][j-1]
                        elif(matrix[i][j] == matrix[i][j-1] == matrix[i-1][j] == matrix[i-1][j-1] == 1):
                            res[i][j] = res[i][j-1] + res[i-1][j] - res[i-1][j-1] + 2
                        else:
                            res[i][j] = res[i][j-1] + res[i-1][j] - res[i-1][j-1] + 1
                    else:
                        if(matrix[i][j] == 0):
                            res[i][j] = res[i][j-1] + res[i-1][j] - res[i-1][j-1]
                        else:
                            k = res[i-1][j-1] + res[i-2][j-2] - res[i-1][j-2] - res[i-2][j-1]
                            ad = 1
                            for p in range(1, k+1):
                                if(matrix[i][j-p] == matrix[i-p][j] == 1):
                                    ad += 1
                                else:
                                    break
                            res[i][j] = res[i][j-1] + res[i-1][j] - res[i-1][j-1] + ad
        return res[m-1][n-1]

        