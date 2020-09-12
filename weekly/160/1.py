"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
"""
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x*y
  
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = list()
        m = 1000
        for x in range(1, 1001):
            if(customfunction.f(x, 1) > z):
                return res
            elif(customfunction.f(x, 1) == z):
                res.append([x, 1])
                return res
            l, r = 1, m
            y = int((l + r)/2)
            while(1):
                if(customfunction.f(x, y) == z):
                    m = y
                    res.append([x, y])
                    break
                elif(customfunction.f(x, y) > z):
                    r = y
                else:
                    l = y
                if(y == int((l + r)/2)):
                    break
                y = int((l + r)/2)
        return res
                
s = Solution()
c = CustomFunction()
print(s.findSolution(c, 5))

        