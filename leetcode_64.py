class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if(i > 0 and j > 0):
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif(i == 0 and j > 0):
                    grid[i][j] += grid[i][j - 1]
                elif(j == 0 and i > 0):
                    grid[i][j] += grid[i - 1][j]
        return grid[m - 1][n - 1]
                    