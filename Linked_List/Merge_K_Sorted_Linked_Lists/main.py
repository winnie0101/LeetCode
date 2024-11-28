from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# minHeap
# time complexity: O(nlogk) 因為heap最多只有k個
# space complexity: O(k)
# n是node總數，k是list數量
# class NodeWrapper:
#     def __init__(self, node):
#         self.node = node

#     def __lt__(self, other):
#         return self.node.val < other.node.val

# class Solution:   
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if len(lists) == 0:
#             return None

#         minHeap = []
#         res = ListNode(0)
#         cur = res

#         for lst in lists:
#             if lst is not None:
#                 heapq.heappush(minHeap, NodeWrapper(lst))

#         while minHeap:
#             wrapper = heapq.heappop(minHeap)
#             node = wrapper.node
#             cur.next = node
#             cur = cur.next
#             if node.next:
#                 heapq.heappush(minHeap, NodeWrapper(node.next))

#         return res.next


# merge list one by one
# time complexity: O(n*k) 
# space complexity: O(1)
# n是node總數，k是list數量
# class Solution:   
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if len(lists) == 0:
#             return None

#         for i in range(1, len(lists)):
#             lists[i] = self.merge(lists[i-1], lists[i])

#         return lists[-1]

#     def merge(self, l1, l2):
#         dummy = ListNode()
#         tail = dummy
#         # print(l1.val, l2.val)
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next

#         if l1:
#             tail.next = l1
#         if l2:
#             tail.next = l2
#         return dummy.next


# divide and conquer(recursion)
# time complexity: O(nlogk) 
# space complexity: O(logk)
# n是node總數，k是list數量
class Solution:   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.divide(lists, 0, len(lists)-1)

    def divide(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        m = (l + r) // 2
        left = self.divide(lists, l, m)
        right = self.divide(lists, m + 1, r)
        return self.conquer(left, right)

    def conquer(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next

                
# Test
head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)

sol = Solution()
res = sol.mergeKLists([head1, head2, head3])
while res:
    print(res.val)
    res = res.next
# Expected: 1 1 2 3 4 4 5 6


