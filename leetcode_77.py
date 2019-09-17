###比较优秀的一题，解法参考的网上

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if(n < k):
            return
        result = list()
        num = [i for i in range(1, n+1)]       
        ind = [i for i in range(k)]
        result.append([num[i] for i in ind])
        while True:
            for i in reversed(range(k)):
                if(ind[i] != i + n - k):
                    break
            else:
                return result

            ind[i] += 1
            for j in range(i + 1, k):
                ind[j] = ind[j - 1] + 1
            result.append([num[i] for i in ind])          

s = Solution()
print(s.combine(4, 2))
