class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """ 
        a_c = a[::-1]
        b_c = b[::-1]
        r = ""
        c = 0
        if len(a_c) > len(b_c):
            mi = len(b_c)
            ma = len(a_c)
            ma_c = a_c
        else:
            mi = len(a_c)
            ma = len(b_c)
            ma_c = b_c
        for i in range(mi):
            if(a_c[i] == '1' and b_c[i] == '1'):
                if(c == 0):
                    r += "0"
                    c = 1
                else:
                    r += "1"
            elif(a_c[i] == '0' and b_c[i] == '0'):
                if(c == 0):
                    r += "0"
                else:
                    r += "1"
                    c = 0
            else:
                if(c == 0):
                    r += "1"
                else:
                    r += "0"
                    c = 1
        for i in range(mi, ma):
            if(c == 1):
                if(ma_c[i] == '1'):
                    r += "0"
                else:
                    r += "1"
                    c = 0
            else:
                r += ma_c[i]
        if(c == 1):
            r += "1"
        return r[::-1]
        
        # 二进制和多种进制数可以直接转换
        # inta=int(a,2)
        # intb=int(b,2)
        # return bin(inta+intb)[2:]

print(Solution().addBinary("1010", "1011"))