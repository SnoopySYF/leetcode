class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(grid)
        m = len(grid[0])
        step = k % (m * n)
        if(step == 0):
            return grid
        res = [[0 for i in range(m)] for j in range(n)]
        row = step // m
        col = step % m
        for i in range(n):
            for j in range(m):
                res[(i + row + (j + col) // m) % n][(j + col) % m] = grid[i][j]
        return res