class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ##牛顿迭代法
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2   ## // 除法取整数
        return int(r)

print(Solution().mySqrt(7))
