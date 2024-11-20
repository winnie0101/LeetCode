from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         elif not p or not q:
#             return False
        
#         if p.val == q.val:
#             isSame_left = self.isSameTree(p.left, q.left)
#             isSame_right = self.isSameTree(p.right, q.right)
#             isSame = isSame_left and isSame_right
#         else:
#             return False

#         return isSame

# BFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_left = deque([p])
        q_right = deque([q])

        while q_left and q_right:
            node_left = q_left.popleft()
            node_right = q_right.popleft()
            if not node_left and not node_right:
                continue
            if not node_left or not node_right or node_left.val!=node_right.val:
                return False

            q_left.append(node_left.left)
            q_left.append(node_left.right)

            q_right.append(node_right.left)
            q_right.append(node_right.right)

        return True


# Test
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

sol = Solution()
print(sol.isSameTree(p, q))

p2 = TreeNode(1)
p2.left = TreeNode(-8)

q2 = TreeNode(1)
q2.right = TreeNode(-5)
print(sol.isSameTree(p, q))