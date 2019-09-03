class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if(n == 0):
            return m
        if(m == 0):
            return n
        pd = [None] * (m + 1)
        for i in range(m + 1):
            pd[i] = [None] * (n + 1)
        for i in range(m + 1):
            pd[i][0] = i
        for j in range(n + 1):
            pd[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if(word1[i - 1] == word2[j - 1]):
                    pd[i][j] = pd[i - 1][j - 1]
                else:
                    pd[i][j] = min(pd[i - 1][j - 1], pd[i - 1][j], pd[i][j - 1]) + 1
        return pd[m][n]

s = Solution()
print(s.minDistance("intention", "execution"))

## 动态规划