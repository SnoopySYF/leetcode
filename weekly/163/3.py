class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nlen = len(nums)
        judge = [nums[i]%3 for i in range(nlen)]
        nums2 = list()
        nums1 = list()
        res = 0
        for i in range(nlen):
            if(judge[i] == 0):
                res += nums[i]
            elif(judge[i] == 1):
                nums1.append(i)
            else:
                nums2.append(i)
        while((nums1 and nums2) or len(nums1) > 3):
            if(nums2):
                if(len(nums1) == 1):
                    res = res + nums[nums2[-1]] + nums[nums1[-1]]
                    nums2.pop()
                    nums1.pop()
                elif(nums[nums2[-1]] >= (nums[nums1[-2]] + nums[nums1[-3]])):
                    res = res + nums[nums2[-1]] + nums[nums1[-1]]
                    nums2.pop()
                    nums1.pop()
                elif(len(nums1) > 3):
                    res = res + nums[nums1[-1]] + nums[nums1[-2]] + nums[nums1[-3]]
                    nums1.pop()
                    nums1.pop()
                    nums1.pop()
            else:
                res = res + nums[nums1[-1]] + nums[nums1[-2]] + nums[nums1[-3]]
                nums1.pop()
                nums1.pop()
                nums1.pop()
        return res
            
nums = [3,6,5,1,8]  
nums.sort() 
print(nums)
nlen = len(nums)            
judge = [nums[i]%3 for i in range(nlen)]
print(judge)
