class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(not matrix or not matrix[0]):
            return False
        m , n = len(matrix), len(matrix[0])
        for i in range(m):
            if(target <= matrix[i][-1]):
                if(target == matrix[i][-1] or target == matrix[i][0]):
                    return True
                else:
                    a , b = 0, n-1
                    while(a < b):
                        mid = int((a + b)/2)
                        if(mid == a):
                            return False
                        if(target == matrix[i][mid]):
                            return True
                        elif(target < matrix[i][mid]):
                            b = mid
                        else:
                            a = mid
                    return False
        return False

s = Solution()
print(s.searchMatrix([[1, 3]], 2))