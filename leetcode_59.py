class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if(n == 0):
            return []
        arr = [[0 for i in range(n)] for i in range(n)]
        weight, direct, cnt = 0, 0, 1
        i, j = 0, 0
        arr[0][0] = 1
        while cnt < n*n:
            if(direct == 0):
                j+=1
                arr[i][j] = cnt + 1
                if(j + weight == n - 1):
                    direct = 1
            elif(direct == 1):
                i+=1
                arr[i][j] = cnt + 1
                if(i + weight == n - 1):
                    direct = 2
            elif(direct == 2):
                j-=1
                arr[i][j] = cnt + 1
                if(j - weight == 0):
                    direct = 3
            elif(direct == 3):
                i-=1
                arr[i][j] = cnt + 1
                if(i - weight - 1 == 0):
                    direct = 0
                    weight += 1
            cnt += 1
        return arr

print(Solution().generateMatrix(3))
#判断比较多所以时间比较长，将判断改为一个大循环里四个小循环赋值会快很多