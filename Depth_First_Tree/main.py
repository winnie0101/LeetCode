from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# DFS
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return root

#         temp = root.left
#         root.left = root.right
#         root.right = temp

#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         return root

# BFS
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

    def printTree(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return

        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    

# Test
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
sol = Solution()
root = sol.invertTree(root)
sol.printTree(root) # Output: 4 7 2 9 6 3 1
    
        