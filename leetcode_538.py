class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.sum = 0
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.find(root)
        return root
        
    def find(self, root):
        if(not root):
            return
        self.find(root.right)
        self.sum += root.val
        root.val = self.sum
        self.find(root.left)

s = Solution()
n1 = TreeNode(-4)
n2 = TreeNode(1)
n3 = TreeNode(0, n1, n2)
n4 = TreeNode(3)
n5 = TreeNode(2, n3, n4)
s.convertBST(n5)