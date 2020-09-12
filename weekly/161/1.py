class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        x1_num, x2_num = s1.count('x'), s2.count('x')
        y1_num, y2_num = s1.count('y'), s2.count('y')
        s1_len, s2_len = len(s1), len(s2)
        if((x1_num + x2_num) % 2 == 1 or (y1_num + y2_num) % 2 == 1 or s1_len != s2_len):
            return -1
        res, chx, chy = 0, 0, 0
        for i in range(s1_len):
            if(s1[i] == 'x' and s2[i] == 'y'):
                if(chx):
                    chx -= 1
                else:
                    chx += 1
                    res += 1
            elif(s1[i] == 'y' and s2[i] == 'x'):
                if(chy):
                    chy -= 1
                else:
                    chy += 1
                    res += 1
        return res
        