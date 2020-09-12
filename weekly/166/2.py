class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        mp = {}
        glen = len(groupSizes)
        for i in range(glen):
            if(groupSizes[i] in mp):
                mp[groupSizes[i]].append(i)
            else:
                mp[groupSizes[i]] = [i]
        res = []
        for i in mp.keys():
            v = mp[i]
            vlen = len(v)
            if(vlen == i):
                res.append(v)
            else:
                t = vlen // i
                for j in range(t):
                    res.append(v[j*i : (j+1)*i])
        return res

s = Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))