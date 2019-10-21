class Solution(object):
    def __init__(self):
        self.n = 0  # 数组的长度
        self.bit = [] # 树状数组

    def lowbit(self, x):    
        return x&(-x)

    # 原数组在位置i上增加x
    def update(self, i, x):
        while(i <= self.n):
            self.bit[i] += x
            i += self.lowbit(i)

    # 求前i项之和
    def sum(self, i):
        s = 0
        while(i > 0):
            s += self.bit[i]
            i -= self.lowbit(i)
        return s

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = list(set(nums))
        nn, ind = sorted(list(set(x + list(map(lambda a: 2 * a, x))))), 1
        disc = {}
        for n in nn:
            disc[n] = ind
            ind += 1
        self.n, self.bit = ind, [0 for _ in range(ind + 5)]
        ret = 0
        for n in nums:
            if ind >= disc[n * 2]:
                ret += self.sum(ind) - self.sum(disc[n * 2])
            self.update(disc[n], 1)
        return ret  

s = Solution()
print(s.reversePairs([2,4,3,5,1]))

# 超时
# class Solution(object):
#     def reversePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = 0
#         for i in range(len(nums) - 1):
#             a = nums[i] / 2.0
#             for j in range(i + 1, len(nums)):
#                 if(a > nums[j]):
#                     res += 1
#         return res
