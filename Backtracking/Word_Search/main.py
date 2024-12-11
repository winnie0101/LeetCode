from typing import List

# time complexity: O(m * 4^n)
# space complexity: O(m)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False for _ in range(COL)] for _ in range(ROW)]

        def dfs(r, c, i):
            if i  == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROW or c >= COL or 
                word[i] != board[r][c] or visited[r][c]):
                return False

            visited[r][c] = True
            res = (
                    dfs(r, c+1, i+1) or 
                    dfs(r, c-1, i+1) or 
                    dfs(r+1, c, i+1) or 
                    dfs(r-1, c, i+1)
                )
            visited[r][c] = False
            return res


        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True
        return False

                
# Test
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCCED"
sol = Solution()
print(sol.exist(board, word)) # expect True
