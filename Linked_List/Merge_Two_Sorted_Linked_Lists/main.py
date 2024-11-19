from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iteration
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         result = node = ListNode()
#         while list1 and list2:
#             if list1.val <= list2.val:
#                 node.next = list1
#                 list1 = list1.next

#             else:
#                 node.next = list2
#                 list2 = list2.next

#             node = node.next

#         node.next = list1 or list2
                
#         return result.next


# Recursive
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(5)

sol = Solution()
result = sol.mergeTwoLists(list1, list2)
while result:
    print(result.val, end=' ')
    result = result.next