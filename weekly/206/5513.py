class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if(len(points) == 1):
            return 0
        d = [[0 for i in range(len(points))] for j in range(len(points))]
        for i in range(len(points)):
            for j in range(len(points)):
                d[i][j] = d[j][i] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        rs = 0
        suc = [0 for i in range(len(points))]
        for i in range(len(suc)):
            if(suc[i] == 0):
                if(i != 0):
                    mi = d[i][0]
                else:
                    mi = d[i][1]
                l = 0
                for j in range(len(d)):
                    if(j != i):
                        if(d[i][j] <= mi):
                            mi = d[i][j]
                            l = j
                rs = rs + mi
                suc[i] = 1
                suc[l] = 1
        return rs

s = Solution()
print(s.minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]))
