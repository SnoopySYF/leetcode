class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rs = 0
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if(mat[i][j] == 1):
                    u, v = 0, 0
                    for n in range(rows):
                        if(mat[n][j] == 1 and n != i):
                            break
                        if(n == rows-1):
                            u = 1
                    for m in range(cols):
                        if(mat[i][m] == 1 and m != j):
                            break
                        if(m == cols-1):
                            v = 1
                    if(u==1 and v==1):
                        rs = rs + 1
        return rs

s = Solution()
print(s.numSpecial([[0]]))
