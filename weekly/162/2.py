class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        s = 0
        le = len(colsum)
        for i in range(le):
            s += colsum[i]
        if(s != (upper + lower)):
            return []
        res = [[0 for i in range(le)] for j in range(2)]
        for i in range(le):
            if(colsum[i] == 2):
                res[0][i], res[1][i] = 1, 1
                upper -= 1
                lower -= 1
            elif(colsum[i] == 1):
                if(upper >= lower):
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
            if(upper < 0 or lower < 0):
                return []
        return res