# class Solution(object):
#     def possibleBipartition(self, N, dislikes):
#         """
#         :type N: int
#         :type dislikes: List[List[int]]
#         :rtype: bool
#         """
#         dislen = len(dislikes)
#         if(dislen == 0): return True
#         s = {}
#         for i in range(dislen):
#             if(dislikes[i][0] not in s): s[dislikes[i][0]] = []
#             s[dislikes[i][0]].append(dislikes[i][1])
#         cs = [[], []]
#         f = [0 for i in range(N+1)]
#         def add(dis, i):
#             for j in dis:
#                 if(j not in cs[i]):
#                     cs[i].append(j)
#                     f[j] = 1
#                 if(j in s):
#                     add(s[j], 1 - i)              
#         for i in range(1, N+1):
#             if(f[i] == 0):
#                 cs[0].append(i)
#                 if(i in s):
#                     add(s[i], 1)
#                     f[i] = 1
#         for i in range(1, N+1):
#             if(i not in cs[0] and i not in cs[1]):
#                 cs[0].append(i)
#         if(len(cs[0]) + len(cs[1]) == N):
#             return True
#         else:
#             return False

# 官方答案
import collections
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N+1)
                   if node not in color)


s = Solution()
print(s.possibleBipartition(3, [[1,2],[1,3],[2,3]]))


