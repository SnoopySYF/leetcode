class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        num = [[0 for i in range(m)] for j in range(n)]
        for i in range(len(indices)):
            for p in range(m):
                num[indices[i][0]][p] += 1
            for q in range(n):
                num[q][indices[i][1]] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if(num[i][j] % 2 == 1):
                    res += 1
        return res