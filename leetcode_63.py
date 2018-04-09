class Solution(object):
    def uniquePathWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[1 for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if(obstacleGrid[i][j] == 1):
                    grid[i][j] = 0
                elif(i > 0 and j > 0):
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                elif(i == 0 and j > 0):
                    grid[i][j] = grid[i][j - 1]
                elif(j == 0 and i > 0):
                    grid[i][j] = grid[i - 1][j]
        return grid[m - 1][n - 1]

        

    
#使用递归扫描所有路径，但是最后时间超了

print(Solution().uniquePathWithObstacles([[0, 0, 0]]))