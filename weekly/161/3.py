class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        slen = len(s)
        loc = list()
        oc = list()
        for i in range(slen):
            if(s[i] == '('):
                loc.append(i)
            elif(s[i] == ')'):
                if(loc):
                    loc.pop()
                else:
                    oc.append(i)
        sl = list(s)
        while(loc or oc):
            if(loc and oc):
                if(loc[-1] > oc[-1]):
                    sl.pop(loc[-1])
                    loc.pop()
                else:
                    sl.pop(oc[-1])
                    oc.pop()
            elif(loc):
                sl.pop(loc[-1])
                loc.pop()
            else:
               sl.pop(oc[-1])
               oc.pop()
        res = "".join(sl)
        return res
                    

      
