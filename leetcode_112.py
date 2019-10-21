class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if(not root):
            return False
        stack = list()
        stack.append([root, root.val])
        while(len(stack)):
            node = stack.pop()
            if(node[0].right):
                stack.append([node[0].right, node[1] + node[0].right.val])
            if(node[0].left):
                stack.append([node[0].left, node[1] + node[0].left.val])
            if(not (node[0].right or node[0].left)):
                if(node[1] == sum):
                    return True
        return False
