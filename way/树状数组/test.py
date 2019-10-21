class Tree:
    def __init__(self):
        self.n = 100  # 数组的长度
        self.bit = [] # 树状数组

    def lowbit(self, x):    
        return x&(-x)

    # 原数组在位置i上增加x
    def updata(self, i, x):
        while(i < self.n):
            self.bit[i] += x
            i = self.lowbit(i)

    # 求前i项之和
    def sum(self, i):
        s = 0
        while(i > 0):
            s += self.bit[i]
            i -= self.lowbit(i)
        return i

