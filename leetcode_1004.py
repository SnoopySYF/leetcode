# class Solution(object):
#     def longestOnes(self, A, K):
#         """
#         :type A: List[int]
#         :type K: int
#         :rtype: int
#         """
#         num = list()
#         if(A == []):
#             return 0
#         if(A[0] == 1):
#             num.append(0)
#         f = A[0]
#         n = 0
#         num0 = 0
#         for i in range(len(A)):
#             if(A[i] == 0):
#                 num0 = num0 + 1
#             if(A[i] == f):
#                 n = n + 1
#             else:
#                 f = A[i]
#                 num.append(n)
#                 n = 1
#         num.append(n)
#         if(num0 <= K):
#             return len(A)
#         elif(num0 - num[0] <=K):
#             return len(A)-num0+K
#         if(len(num) == 1):
#             return K
#         elif(len(num) < 4):
#             return num[1] + K
#         if(len(num) % 2 == 0):
#             num.append(0)
#         rs = 0
#         r = 0
#         rest = K
#         for i in range(2, len(num), 2):
#             if(num[i] > K):
#                 rs = max(num[i-1]+K, rs)
#             else:
#                 rest = rest - num[i]
#                 r = num[i-1] + num[i]
#                 for j in range(i+2, len(num), 2):
#                     if(num[j] > rest or num[j] == 0):
#                         r = r + num[j-1] + rest
#                         rest = 0
#                         break
#                     else:
#                         rest = rest - num[j]
#                         r = r + num[j-1] + num[j]
#                 rs = max(r+rest, rs)
#                 rest = K
#         return rs

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        left, right, count = 0, 0, 0  # 本来定义了max_len用来实时记录窗口大小，但后来发现非必要,因为窗口大小没有变小
        for right in range(len(A)):
            if A[right] == 0:
                count += 1
            if count > K:
                if A[left] == 0:
                    count -= 1
                left += 1
        return right - left + 1
            
s = Solution()
print(s.longestOnes([1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1], 8))       
