class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        le = len(words)
        if(le == 1):
            return True
        List = list()
        for i in range(le):
            w = ""
            for c in words[i]:
                w += str(chr(order.index(c) + 1))
            List.append(w)
        for i in range(1, le):
            if(List[i] < List[i - 1]):
                return False
        return True


s = Solution()
print(s.isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz"))