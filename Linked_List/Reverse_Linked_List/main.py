from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        # 將所有link反轉
        while curr:
            next_head = curr.next
            curr.next = prev
            prev = curr
            curr = next_head

        return prev

    def printList(self, head: Optional[ListNode]) -> None:
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
head = sol.reverseList(head)
sol.printList(head) # Output: 5 4 3 2 1



