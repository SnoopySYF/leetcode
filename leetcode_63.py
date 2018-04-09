class Solution(object):
    def uniquePathWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return DFS(0, 0, m-1, n-1, obstacleGrid)

def DFS(x, y, m, n, obstacleGrid):
    if(obstacleGrid[x][y] == 1):
        return 0
    elif(x == m and y == n):
        return 1
    elif(x == m):
        return DFS(x, y + 1, m, n, obstacleGrid)
    elif(y == n):
        return DFS(x + 1, y, m, n, obstacleGrid)
    else:
        return DFS(x, y + 1, m, n, obstacleGrid) + DFS(x + 1, y, m, n, obstacleGrid)
    
#使用递归扫描所有路径，但是最后时间超了

print(Solution().uniquePathWithObstacles([[1]]))