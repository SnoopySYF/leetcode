class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        if(tomatoSlices < cheeseSlices*2 or tomatoSlices > cheeseSlices*4 or tomatoSlices % 2 == 1):
            return []
        if(cheeseSlices == 0):
            return [0,0]
        res = [0, 0]
        retomato = tomatoSlices % (cheeseSlices * 2)
        res[0] = retomato // 2
        res[1] = cheeseSlices - res[0]
        return res