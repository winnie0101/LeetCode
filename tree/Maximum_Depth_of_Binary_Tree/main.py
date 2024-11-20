from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

c# Recursive
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0

#         current_depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
#         return current_depth 


# Iterative DFS(stack)
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         stack = [[root, 1]]
#         res = 0

#         while stack:
#             node, depth = stack.pop()

#             if node:
#                 print(node.val)
#                 res = max(res, depth)
#                 stack.append([node.left, depth+1])
#                 stack.append([node.right, depth+1])

#         return res


# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        res = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res += 1
        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.maxDepth(root)) # Output: 3


        