

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive
# time complexity: O(h)
# space complexity: O(h)
# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         if not root or not p or not q:
#             return None
        
#         if max(p.val, q.val) < root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif min(p.val, q.val) > root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root


# Iteration
# time complexity: O(h)
# space complexity: O(1)
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        


# Test
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left
q = root.right
sol = Solution()
print(sol.lowestCommonAncestor(root, p, q).val) # Expect 6

        