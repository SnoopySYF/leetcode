class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        alen = len(arr)
        if(alen == 0):
            return 0
        lenset = {}
        for i in range(alen):
            lenset[arr[i]] = len(arr[i])
        a = sorted(lenset.items(), key=lambda x: x[1], reverse=True)
        res = 0
        for key, value in a:
            
        
        