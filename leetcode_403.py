class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        self.result = False
        self.stones = stones
        self.jump = [[-1 for i in range(len(stones))] for j in range(len(stones))]
        self.Cross(0, 1)
        return self.result

    def Cross(self, loc, step):
        if(self.result):
            return
        if(loc == len(self.stones) - 1):
            self.result = True
            return
        elif(loc > len(self.stones) - 1):
            return
        if(self.jump[loc][step] == 0):
            return
        elif(self.jump[loc][step] == 1):
            self.Cross(loc, step + 1)
            self.Cross(loc, step)
            if(step > 1):
                self.Cross(loc, step - 1)
        else:
            i = loc + 1
            ne = self.stones[loc] + step
            while(self.stones[i] < ne):
                i += 1
                if(i > len(self.stones) - 1):
                    return
            if(self.stones[i] == ne):
                self.Cross(i, step + 1)
                self.Cross(i, step)
                if(step > 1):
                    self.Cross(i, step - 1)
            else:
                return
        
s = Solution()
print(s.canCross([0,1,3,4,5,7,9,10,12]))