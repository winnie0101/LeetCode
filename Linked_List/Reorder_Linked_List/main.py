from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# recursive
# time complexity: O(n)
# space complexity: O(n)
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         def rec(root: ListNode, cur: ListNode):
#             if not cur:
#                 return root

#             root = rec(root, cur.next)

#             if not root:
#                 return None
            
#             tmp = None
#             if (root == cur) or (root.next == cur):
#                 cur.next = None
#             else:
#                 tmp = root.next
#                 root.next = cur
#                 cur.next = tmp
#             return tmp

#         head = rec(head, head.next)
        

# reverse and merge
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        l2 = s.next
        s.next = None
        l1 = head

        # reverse l2
        prev = None
        while l2:
            tmp = l2.next
            l2.next = prev
            prev = l2
            l2 = tmp
            
        l2 = prev

        # merge l1 and l2
        while l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2



# test
def printList(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol = Solution()
sol.reorderList(head)
printList(head) # 1 5 2 4 3

            
