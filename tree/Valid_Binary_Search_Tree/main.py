from typing import Optional
from collections import deque

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
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:

#         def valid(node, left, right):
#             if not node:
#                 return True
#             if not (left < node.val < right):
#                 return False
             
#             l = valid(node.left, left, node.val)
#             r = valid(node.right, node.val, right)
#             return l and r

#         return valid(root, float("-inf"), float("inf"))


# BFS
# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque()
        q.append([root, float("-inf"), float("inf")])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False

            if node.left:
                q.append([node.left, left, node.val])
            if node.right:
                q.append([node.right, node.val, right])
        
        return True
            
# test
#### 要和前一層的root比較
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
sol = Solution()
print(sol.isValidBST(root)) # expect True

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.isValidBST(root)) # expect False

