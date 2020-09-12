class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        hlen = len(hours)
        nums = [0 for i in range(hlen + 1)]
        res = 0
        for i in range(hlen):
            nums[i+1] = nums[i] + (1 if(hours[i] > 8) else -1)
        stack = list()
        for i, v in enumerate(nums):
            if(not stack or nums[stack[-1]] > v):
                stack.append(i)
        for i in range(hlen, -1, -1):
            while(stack and nums[stack[-1]] < nums[i]):
                res = max(res, i - stack[-1])
                stack.pop()
        return res
        
        