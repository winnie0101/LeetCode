from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
# time complexity: O(n)
# space complexity: O(n)
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []

#         def dfs(node, level):
#             if not node:
#                 return None
#             if len(res) == level:
#                 res.append([])

#             res[level].append(node.val)
#             dfs(node.left, level + 1)
#             dfs(node.right, level + 1)

#         dfs(root, 0)
    
#         return res

            
# BFS
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                res.append(level)

        return res


# test
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.levelOrder(root)) # [[3], [9, 20], [15, 7]]