from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mem = Counter(t)
        t_len = len(t)
        
        minL, minR = 0, float('inf')
        
        l = 0
        for r, c in enumerate(s):
            if mem[c] > 0:
                t_len -= 1
            mem[c] -= 1
                
            if t_len == 0:
                while mem[s[l]] < 0:
                    mem[s[l]] += 1
                    l += 1
                    
                if r - l < minR - minL:
                    minL, minR = l, r
                
                mem[s[l]] += 1
                t_len += 1
                l += 1
        
        return '' if minR == float('inf') else s[minL:minR+1]
    
        # def check(s1, s2):
        #     s_1, s_2 = collections.Counter(s1), collections.Counter(s2)
        #     for i, val in s_2.items():
        #         if(i in s_1 and val <= s_1[i]):
        #             continue
        #         return False
        #     return True

#######################################    方法2--超时     #######################################################################

        # if(not check(s, t)):
        #     return ""
        # slen, tlen = len(s), len(t)
        # if(slen < tlen): return ""
        # tmin, minst, mined = slen, 0, slen-1
        # l, r, f = 0, tlen-1, 0
        # while(r >= l and r < slen):
        #     if(not (s[l] in t)):
        #         l += 1
        #         if(r-l+1 < tlen):r += 1
        #     elif(check(s[l : r+1], t)):
        #         tmin = min(tmin, r-l+1)
        #         if(tmin == r-l+1):
        #             minst, mined = l, r
        #         l += 1
        #         f = 1
        #     else:
        #         r += 1
        #         if(f == 1):
        #             l -= 1
        #             f = 0
        # return s[minst : mined+1]

####################################     方法1--超时     ########################################################   
        # for i in range(slen):
        #     if(s[i] in t):
        #         st, ed, md = i, slen-1, slen-1
        #         while(ed - st + 1 >= tlen):
        #             if(check(s[i:md+1], t)):
        #                 tmin = min(tmin, md-i+1)
        #                 if(tmin == md-i+1):
        #                     minst, mined = i, md
        #                 ed = md
        #                 md = int((st+ed)/2)
        #                 if(md >= ed): break
        #             else:
        #                 if(md == int((md+ed)/2)): 
        #                     md+=1
        #                     if(md >= ed): break
        #                 else: md = int((md+ed)/2)
        # return s[minst:mined+1]
      
s = Solution()
print(s.minWindow("abc", "ab"))                        
