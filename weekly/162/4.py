from collections import Counter
import operator

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        let = "abcdefghijklmnopqrstuvwxyz"
        m = {}
        for i in range(26):
            m[let[i]] = i
        word = list()
        w_num = {}
        letter = Counter(letters)
        sco = {}
        for i in range(len(words)):
            wor = words[i]
            ws = Counter(wor)
            for w in ws:
                if(ws[w] > letter[w]):
                    break
            else:
                word.append(wor)
                wscore = 0
                for a in wor:
                    wscore += score[m[a]]
                sco[wor] = wscore
                w_num[wor] = ws
        res = 0
        if(not word):
            return res
        
        
        
