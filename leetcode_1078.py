class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        tx = text.split(' ')
        tlen = len(tx)
        res = list()
        for i in range(tlen - 2):
            if(tx[i] == first and tx[i + 1] == second):
                res.append(tx[i + 2])
        return res