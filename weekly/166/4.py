class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        if(m == 1 and n == 1):
            if(mat == [[0]]):
                return 0
            else:
                return 1
        elif((m == 1 and n == 2) or (m == 2 and n == 1)):
            if(mat == [[0], [0]] or mat == [[0, 0]]):
                return 0
            elif(mat == [[1], [1]] or mat == [[1, 1]]):
                return 1
            else:
                return -1
        elif((m == 1 and n == 3) or (m == 3 and n == 1)):
            if(mat == [[0], [0], [0]] or mat == [[0, 0, 0]]):
                return 0
            elif(mat == [[1], [1], [1]] or mat == [[1, 1, 1]]):
                return 1
            elif(mat == [[0], [1], [0]] or mat == [[0, 1, 0]]):
                return 3
            else:
                return 2
        elif((m == 2 and n == 3) or (m == 3 and n == 2)):
            