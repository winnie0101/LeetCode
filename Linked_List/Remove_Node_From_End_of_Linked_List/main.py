from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iteration
# time complexity: O(n)
# space complexity: O(1)
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         listLen = 0
#         cur = head
#         while cur:
#             listLen += 1
#             cur = cur.next

#         removeIdx = listLen - n

#         if removeIdx == 0:
#             return head.next

#         cur = head
#         count = 0
#         prev = None
#         while cur:
#             if count == removeIdx:
#                 prev.next = cur.next
#                 break

#             count += 1
#             prev = cur
#             cur = cur.next

#         return head


# Recursive
# time complexity: O(n)
# space complexity: O(n)
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
#         return self.rec(head, [n])

#     def rec(self, head, n):
#         if not head:
#             return None

#         head.next = self.rec(head.next, n)

#         n[0] -= 1
#         if n[0] == 0:
#             return head.next
#         return head


# two pointers
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for i in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

def printList(head):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next      

# test
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

target = 2
sol = Solution()
head = sol.removeNthFromEnd(head, target)
printList(head) # 1 2 3 5

