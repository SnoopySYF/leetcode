class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(not root):
            return None
        self.check(root)
        return root
        
    def check(self, node):
        if(not node.left and not node.right):
            if(node.val == 0):
                return False
            return True
        if(node.left):
            if(not self.check(node.left)):
                node.left = None
        if(node.right):
            if(not self.check(node.right)):
                node.right = None
        if(not node.left and not node.right):
            if(node.val == 0):
                return False
        return True

s = Solution()
root = TreeNode(1)
node1 = TreeNode(0)
node2 = TreeNode(0)
node3 = TreeNode(1)
root.right = node1
node1.left = node2
node1.right = node3
print(s.pruneTree(root))