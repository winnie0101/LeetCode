from typing import List
from collections import deque

# DFS
# 每當發現一個陸地，將其向同一方向前進，直到碰到水
# 並將經過的陸地標示為水
# time complexity: O(m*n)
# space complexity: O(m*n)
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         islands = 0
#         ROW, COL = len(grid), len(grid[0])
#         DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]

#         def dfs(r, c):
#             if (r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == "0"):
#                 return

#             grid[r][c] = "0"
#             for dr, dc in DIR:
#                 dfs(r + dr, c + dc)

#         for r in range(ROW):
#             for c in range(COL):
#                 if grid[r][c] == "1":
#                     dfs(r, c)
#                     islands += 1
        
#         return islands


# BFS
# 每當發現一個陸地，將探索其四周，將陸地的位置儲存起來
# 並將經過的陸地標示為水
# time complexity: O(m*n)
# space complexity: O(m*n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        islands = 0
        DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in DIR:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROW or nc >= COL or grid[nr][nc]=="0"):
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands


# test
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
sol = Solution()
print(sol.numIslands(grid)) # expect 1
