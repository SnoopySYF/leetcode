class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        length = len(words)
        s = ""
        l = 0  #每行字符个数
        flag = 0
        i = 0
        start = 0  #每行开始单词的位置
        end = 0  #每行结束单词的位置
        num = 0 #每行单词个数
        while(i < length):
            if(flag == 0):
                s = ""
                l = 0
                start = i
                flag = 1
            if(flag):
                if(l + len(words[i]) > maxWidth):
                    i -= 1
                    end = i
                    flag = 0
                else:
                    l += len(words[i])
                    num += 1
            if(num == 1):
                s += words[start]
                Dspace = maxWidth - l
                while(Dspace > 0):
                    s += ' '
                    Dspace -= 1
                result.append(s)
            else:
                sspace = (maxWidth - l) % (num - 1)
                space = (maxWidth - l - sspace) / (num - 1)
                for j in range(start, end + 1):
                    s += words[j]
                    z = space
                    while(z > 0):
                        s += ' '
                        z -= 1
                    if(sspace > 0):
                        s += ' '
                        sspace -= 1
                result.append(s)
        return result


print(Solution().fullJustify( ["This", "is", "an", "example", "of", "text", "justification."], 16))
            
                

