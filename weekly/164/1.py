class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        plen = len(points)
        if(plen == 0):
            return 0
        prx = points[0][0]
        pry = points[0][1]
        for i in range(1, plen):
            x = points[i][0]
            y = points[i][1]
            res += max(abs(x - prx), abs(y - pry))
            prx, pry = x, y
        return res