class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(not nums):
            return 0
        le = len(nums)
        self.max = [-1 for i in range(le)]
        max1 = nums[0] + self.findmax(2, nums[:-1])
        self.max = [-1 for i in range(le)]
        max2 = self.findmax(1, nums)
        return max(max1, max2)

    def findmax(self, k, nums):
        if(k >= len(nums)):
            return 0
        elif(k == len(nums) - 1):
            self.max[k] = nums[k]
        else:
            if(self.max[k] == -1):
                self.max[k] = max(nums[k] + self.findmax(k + 2, nums), nums[k + 1] + self.findmax(k + 3, nums))
        return self.max[k]

s = Solution()
print(s.rob([1, 2, 3, 1]))