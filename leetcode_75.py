class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        if(le < 2):
            return nums
        start, mid01, mid12 = 0, 0, le-1
        while(start <= mid12):
            if(nums[start] == 0):
                nums[start] = nums[mid01]
                nums[mid01] = 0
                start += 1
                mid01 += 1
            elif(nums[start] == 2):
                nums[start] = nums[mid12]
                nums[mid12] = 2
                mid12 -= 1
            else:
                start += 1
        return nums

s = Solution()
print(s.sortColors([2, 0, 2, 1, 1, 0]))
