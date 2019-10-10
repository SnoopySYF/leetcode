class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if(n == 0):
            return nums1
        if(m == 0):
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1
        num = [0 for i in range(m + n)]
        i = j = 0
        while(i < m or j < n):
            if(i == m):
                num[i + j] = nums2[j]
                j += 1
            elif(j == n):
                num[i + j] = nums1[i]
                i += 1
            else:
                if(nums1[i] < nums2[j]):
                    num[i + j] = nums1[i]
                    i += 1
                else:
                    num[i + j] = nums2[j]
                    j += 1
        for k in range(m + n):
            nums1[k] = num[k]
        return nums1

s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3))


#大佬解法：
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n >0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m = m -1
            else :
                nums1[m+n-1] = nums2[n-1]
                n = n-1
        if n > 0 :
            nums1[:n] = nums2[:n]
'''