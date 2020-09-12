class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.num = list()
        self.rs = list()

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if(root == None):
            return []
        self.rs.append(float(root.val))
        self.num.append(1)
        if(root.left):
            self.BFS(root.left, 2)
        if(root.right):
            self.BFS(root.right, 2)
        for i in range(len(self.rs)):
            self.rs[i] = self.rs[i] / self.num[i]
        return self.rs

    def BFS(self, root, key):
        if(len(self.rs) < key):
            self.rs.append(float(root.val))
        else:
            self.rs[key-1] = self.rs[key-1] + root.val
        if(len(self.num) < key):
            self.num.append(1)
        else:
            self.num[key-1] = self.num[key-1] + 1
        if(root.left):
            self.BFS(root.left, key+1)
        if(root.right):
            self.BFS(root.right, key+1)
