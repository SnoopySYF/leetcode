class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        res = list()
        res.append(start)
        med = {}
        for i in range(n):
            med[i] = list()
        