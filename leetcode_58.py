class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split()
        if(len(word) == 0): return 0
        return len(word[-1])

s = Solution()
print(s.lengthOfLastWord("Hello World"))