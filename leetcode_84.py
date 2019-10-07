class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        le = len(heights)
        stack = list()
        mx, i = 0, 0
        while(i < le):
            if(not stack or (heights[stack[-1]] <= heights[i])):
                stack.append(i)
                i += 1
            else:
                j = stack.pop()
                if(stack):
                    mx = max(mx, (i - stack[-1] - 1) * heights[j])
                else:
                    mx = max(mx, i * heights[j])
        
        while(stack):
            j = stack.pop()
            if(stack):
                mx = max(mx, (i - stack[-1] - 1) * heights[j])
            else:
                mx = max(mx, i * heights[j])

        return mx


#使用递增栈
s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))

        