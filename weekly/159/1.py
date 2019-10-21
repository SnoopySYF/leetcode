class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if(len(coordinates) == 2):
            return True
        y = coordinates[0][1]
        x = coordinates[0][0]
        if(x - coordinates[1][0] == 0):
            for i in range(2, len(coordinates)):
                if(coordinates[i][0] != x):
                    return False
            return True
        w = float(y - coordinates[1][1])/float(x - coordinates[1][0])
        for i in range(2, len(coordinates)):
            if(coordinates[i][0] == x):
                return False
            if(w != (float(y - coordinates[i][1])/float(x - coordinates[i][0]))):
                return False
        return True

s = Solution()
print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))