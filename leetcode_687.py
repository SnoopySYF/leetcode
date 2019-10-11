class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findMax(root)
        return self.ans
        
    def findMax(self, root):
        if(not root):
            return 0
        left = self.findMax(root.left)
        right = self.findMax(root.right)
        maxL = maxR = 0
        if(root.left and root.val == root.left.val):
            maxL = left + 1
        if(root.right and root.val == root.right.val):
            maxR = right + 1
        self.ans = max(self.ans, maxL + maxR)
        return max(maxL, maxR)
