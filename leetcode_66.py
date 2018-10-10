class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = 0
        for i in range(0, len(digits))[::-1]:  ##倒序读取数组   也可以先digits.reverse()将数组倒过来
            if(digits[i] != 9):
                flag = 1
                digits[i] = digits[i] + 1
                break
            else:
                digits[i] = 0
        if(flag == 0):
            digits.insert(0, 1)
        return digits

print(Solution().plusOne([9,9,9,9]))