from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Hash Set
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         isSeen = set()
#         cur = head

#         while cur:
#             if cur in isSeen:
#                 return True
#             isSeen.add(cur)
#             cur = cur.next

#         return False

# Fast And Slow Pointers
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next #每次走一步
            fast = fast.next.next #每次走兩步
            if slow == fast: #如果有圈，快的一定可以追上慢的
                return True
        return False

# Test
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

sol = Solution()
print(sol.hasCycle(head)) # Output: True