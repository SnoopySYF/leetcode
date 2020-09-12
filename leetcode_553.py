class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nlen = len(nums)
        if(nlen == 1): 
            return str(nums[0])
        elif(nlen == 2):
            return str(nums[0]) + "/" + str(nums[1])
        else:
            return str(nums[0]) + "/(" + "/".join([str(i) for i in nums[1:]]) + ")"
        