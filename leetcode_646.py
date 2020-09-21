class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if(pairs == [[]]):
            return 0
        pairs.sort()
        rs = 1
        k = pairs[0][1]
        for i in range(1, len(pairs)):
            if(pairs[i][1] < k):
                k = pairs[i][1]
            elif(pairs[i][0] > k):
                rs = rs + 1
                k = pairs[i][1]
        return rs

s = Solution()
s.findLongestChain([[1,2], [2,3],[5,6], [3,4]])