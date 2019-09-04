import numpy as np

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if(matrix == None):
            return
        m = np.shape(matrix)[0]
        n = np.shape(matrix)[1]
        M = [1] * m
        N = [1] * n
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                    M[i] = 0
                    N[j] = 0
        for i in range(m):
            if(M[i] == 0):
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if(N[j] == 0):
                for i in range(m):
                    matrix[i][j] = 0
        return matrix


A=[[2,2],[2,2],[2,2]]
print(np.shape(A)[1])