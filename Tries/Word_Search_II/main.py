from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.res = set()

    def initTree(self, words: List[str]):
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.end = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROW, COL = len(board), len(board[0])
        visited  = [[False for _ in range(COL)]for _ in range(ROW)]
        self.initTree(words)

        def dfs(r, c, root, findWord):
            if root.end:
                self.res.add(findWord)
                root.end = False
            
            if (r < 0 or c < 0 or r >= ROW or c >= COL or visited[r][c]
                or board[r][c] not in root.children):
                return False

            visited[r][c] = True
            next_root = root.children[board[r][c]]
            dfs(r, c+1, next_root, findWord+board[r][c])
            dfs(r, c-1, next_root, findWord+board[r][c])
            dfs(r+1, c, next_root, findWord+board[r][c])
            dfs(r-1, c, next_root, findWord+board[r][c])
            visited[r][c] = False

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] in self.root.children:
                    dfs(r, c, self.root, "")

        return list(self.res)


# Test
board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]

words = ["oath","pea","eat","rain"]
sol = Solution()
res = sol.findWords(board, words) # expect ["eat", "oath"]
print(res)