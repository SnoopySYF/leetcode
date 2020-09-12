# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        root.val = 0
        stack = list()
        stack.append(root)
        while(stack):
            node = stack.pop()
            if(node.left):
                node.left.val = 2*node.val + 1
                stack.append(node.left)
            if(node.right):
                node.right.val = 2*node.val + 2
                stack.append(node.right)
        self.root = root

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        num = list()
        num.append(target)
        while(target):
            if(target % 2 == 1):
                target = (target-1) // 2
                num.append(target)
            else:
                target = (target-2) // 2
                num.append(target)
        node = self.root
        num.pop()
        while(num):
            n = num.pop()
            if(node.right):
                if(node.right.val == n):
                    node = node.right
                    continue
            if(node.left):
                if(node.left.val == n):
                    node = node.left
                else:
                    return False
            else:
                return False
        return True
