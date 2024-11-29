from typing import List
from collections import deque

# dfs
# time complexity: O(r * c)
# space complexity: O(r * c)
# 從邊界出發，找可以到達的點並儲存起來
# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         ROW, COL = len(heights), len(heights[0])
#         DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         res = []
#         pacific = set()
#         atlantic = set()

#         def dfs(r, c, curSet, prevH):
#             curH = heights[r][c]
#             if prevH > curH or (r, c) in curSet:
#                 return 
#             curSet.add((r, c))
#             for dr, dc in DIR:
#                 nr, nc = r + dr, c + dc
#                 if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
#                     continue
#                 # print(nr, nc)
#                 dfs(nr, nc, curSet, curH)
        
#         for c in range(COL):
#             dfs(0, c, pacific, 0)
#             dfs(ROW-1, COL-c-1, atlantic, 0)

#         for r in range(ROW):
#             dfs(r, 0, pacific, 0)
#             dfs(ROW-r-1, COL-1, atlantic, 0)

#         # set_a.intersection(set_b)
#         new = pacific.intersection(atlantic)
#         for item in new:
#             res.append(list(item))
            
            
#         return res


# bfs
# time complexity: O(r * c)
# space complexity: O(r * c)
# 從邊界出發，找可以到達的點並儲存起來
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = []

        q_pac = deque()
        q_atl = deque()

        pacific = set()
        atlantic = set()

        def bfs(q, curSet):
            while q:
                r, c, prevH = q.popleft()
                curH = heights[r][c]
                if prevH > curH or (r, c) in curSet:
                    continue
                curSet.add((r, c))
                for dr, dc in DIR:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
                        continue
                    q.append([nr, nc, curH])

        for c in range(COL):
            q_pac.append([0, c, 0])
            q_atl.append([ROW-1, COL-c-1, 0])

        for r in range(ROW):
            q_pac.append([r, 0, 0])
            q_atl.append([ROW-r-1, COL-1, 0])

        bfs(q_pac, pacific)
        bfs(q_atl, atlantic)

        new = pacific.intersection(atlantic)
        for item in new:
            res.append(list(item))

        return res


# test
heights = [[1,2,2,3,5],
           [3,2,3,4,4],
           [2,4,5,3,1],
           [6,7,1,4,5],
           [5,1,1,2,4]]
sol = Solution()
print(sol.pacificAtlantic(heights)) # expect [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
