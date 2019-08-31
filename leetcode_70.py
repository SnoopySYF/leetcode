class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 1):
            return 1
        elif(n == 2):
            return 2
        else:
            num = [0]*n
            num[0] = 1
            num[1] = 2
            for i in range(3, n + 1):
                num[i-1] = num[i-2] + num[i-3]
        return num[n-1]

s = Solution()
print(s.climbStairs(1))

#！！！斐波那契数列！！！
