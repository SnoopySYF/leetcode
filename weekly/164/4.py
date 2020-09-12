class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        ma = 1000000007
        res = 0
        if(arrLen == 1):
            return 1
