class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0):
            return 0
        mul, sm = 1, 0
        m = 0
        while(n):
            m = n % 10
            n = n // 10
            mul = mul * m
            sm = sm + m
        return mul - sm