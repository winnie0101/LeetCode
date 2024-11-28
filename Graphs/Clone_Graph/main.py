from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# DFS
# time complexity: O(V + E)
# space complexity: O(V)
# V是頂點數，E是邊數
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        create = {}

        def dfs(node):
            if not node:
                return None
            if node in create:
                return create[node]

            copy = Node(node.val)
            create[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
        
            return copy
        
        if not node:
            return None
        else:
            return dfs(node)


# BFS
# time complexity: O(V + E)
# space complexity: O(V)
# V是頂點數，E是邊數
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return None

#         create = {}
#         create[node] = Node(node.val)
#         q = deque()
#         q.append(node)

#         while q:
#             cur = q.popleft()
#             for nei in cur.neighbors:
#                 if nei not in create:
#                     create[nei] = Node(nei.val)
#                     q.append(nei)

#                 create[cur].neighbors.append(create[nei])

#         return create[node]

                

# test
# 1 - 2
# |   |
# 4 - 3
# 1's neighbors are [2, 4]
# 2's neighbors are [1, 3]
# 3's neighbors are [2, 4]
# 4's neighbors are [1, 3]
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
sol = Solution()
print(sol.cloneGraph(node1).val) # expect 1

        