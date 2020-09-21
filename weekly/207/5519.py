class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        tx = text.split(" ")
        w_len = 0
        w_num = 0
        word = list()
        for i in range(len(tx)):
            if(tx[i] != ''):
                w_len = w_len + len(tx[i])
                w_num = w_num + 1
                word.append(tx[i])
        s_num = len(text) - w_len
        if(w_num != 1):
            s_in = s_num // (w_num-1)
            e_s = s_num % (w_num-1)
        else:
            e_s = s_num
        rs = word[0]
        for i in range(1, len(word)):
            for j in range(s_in):
                rs = rs + " "
            rs = rs + word[i]
        for i in range(e_s):
            rs = rs + " "
        return rs

s = Solution()
s.reorderSpaces("a")
