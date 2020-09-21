class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = list()
        if(root == None):
            return root
        queue.append(root)
        while(len(queue)):
            n = queue.pop(0)
            m = n.right
            n.right = n.left
            n.left = m
            if(n.left):
                queue.append(n.left)
            if(n.right):
                queue.append(n.right)
        return root
