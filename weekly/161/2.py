class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sn = len(nums)
        i, l, r, count, res = 0, 0, 0, 0, 0
        l_id, r_id = 0, 0
        f = list()
        while(i < sn):
            if(nums[i] % 2 == 0):
                if(count == 0):
                    l += 1
                elif(count == k):
                    r += 1
                i += 1
                r_id += 1
            else:
                f.append(i)
                if(count < k):
                    count += 1
                    i += 1
                    r_id += 1
                else:
                    res += (r + 1)*(l + 1)
                    l = f[1] - f[0] - 1
                    l_id = f[0] + 1
                    f.pop(0)
                    r = 0
                    i += 1
                    r_id += 1
        if(count == k):
            res += (r + 1)*(l + 1)
        return res

s = Solution()
print(s.numberOfSubarrays([91473,45388,24720,35841,29648,77363,86290,58032,53752,87188,34428,85343,19801,73201], 4))