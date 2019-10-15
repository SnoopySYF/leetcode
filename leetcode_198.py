class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(not nums):
            return 0
        self.le = len(nums)
        self.max = [-1 for i in range(self.le)]
        self.findmax(0, nums)
        return self.max[0]

    def findmax(self, k, nums):
        if(k >= self.le):
            return 0
        elif(k == self.le - 1):
            self.max[k] = nums[k]
        else:
            if(self.max[k] == -1):
                self.max[k] = max(nums[k] + self.findmax(k + 2, nums), nums[k + 1] + self.findmax(k + 3, nums))
        return self.max[k]

s = Solution()
print(s.rob([1, 2]))
                