import copy
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products = sorted(products)
        p = []
        wlen = len(searchWord)
        res = [[] for i in range(wlen)]
        for i in range(wlen):
            a = searchWord[i]
            for j in range(len(products)):
                if(len(products[j]) > i and products[j][i] == a):
                    if(len(res[i]) < 3):
                        res[i].append(products[j])
                    p.append(products[j])
            products = []
            products = copy.deepcopy(p)
            p = []
        return res

                
