class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        if(len(folder) == 1):
            return folder
        i = 0
        le = len(folder)
        while(i < le):
            s = folder[i]
            j = i + 1
            while(j < le):
                if(s in folder[j] and folder[j][len(s)] == '/'):
                    folder.remove(folder[j])
                    le -= 1
                elif(folder[j] in s and s[len(folder[j])] == '/'):
                    folder.remove(s)
                    le -= 1
                    i -= 1
                    break
                else:
                    j += 1
            i += 1
        return folder

#超时
# class Solution(object):
#     def removeSubfolders(self, folder):
#         """
#         :type folder: List[str]
#         :rtype: List[str]
#         """
#         if(len(folder) == 1):
#             return folder
#         i = 0
#         le = len(folder)
#         while(i < le):
#             s = folder[i].split('/')
#             j = i + 1
#             while(j < le):
#                 f = folder[j].split('/')
#                 for k in range(min(len(s), len(f))):
#                     if(s[k] != f[k]):
#                         break
#                 else:
#                     if(len(s) < len(f)):
#                         folder.remove(folder[j])
#                         le -= 1
#                         continue
#                     elif(len(s) > len(f)):
#                         folder.remove(folder[i])
#                         le -= 1
#                         i -= 1
#                         break
#                 j += 1
#             i += 1
#         return folder


s = Solution()
print(s.removeSubfolders(["/a","/a/b/c","/a/b/d"]))