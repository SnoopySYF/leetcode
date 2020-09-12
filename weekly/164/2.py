class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = 0
        row = [0 for i in range(m)]
        col = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    row[i] += 1
                    col[j] += 1
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    if(row[i] >1 or col[j] > 1):
                        res += 1
        return res
