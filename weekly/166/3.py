class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        lnum = len(nums)
        mx = 0
        for i in range(lnum):
            mx = max(mx, nums[i])
        if(lnum == threshold):
            return mx
        r, l = 1, mx
        res = mx
        while(r < l):
            mid = (r+l)//2
            sm = 0
            for i in range(lnum):
                n = nums[i] // mid
                m = 0
                if(nums[i] % mid):
                    m = 1
                sm = sm + n + m
            if(sm <= threshold):
                res, l = mid, mid
            else:
                if(res == mid+1):
                    return int(res)
                else:
                    r = mid
        return int(res)

s = Solution()
print(s.smallestDivisor([19], 5))