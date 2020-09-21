class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.rs = list()

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.find(root)
        return self.rs

    def find(self, root):
        if(not root):
            return
        if(not (root.left or root.right)):
            self.rs.append(root.val)
            return
        self.find(root.left)
        self.rs.append(root.val)
        self.find(root.right)