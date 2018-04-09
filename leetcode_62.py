class Solution(object):
    def uniquePaths(self, m, n):
        p = m + n - 2
        q = min(m - 1, n - 1)
        if(q == 0):
            return 1
        m1 = 1
        m2 = 1
        while(q):
            m1 *= p
            m2 *= q
            p -= 1
            q -= 1
        return m1 / m2
        