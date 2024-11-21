
from typing import List

# Brute Force
# time complexity: O(n^2)
# space complexity: O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxP = 0
#         for i in range(len(prices)-1):
#             for j in range(i+1, len(prices)):
#                 maxP = max(maxP, prices[j]-prices[i])

#         return maxP

# Dynamic Programming
# time complexity: O(n)
# space complexity: O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxP = 0
#         minBuy = prices[0]

#         for i in range(len(prices)):
#             minBuy = min(minBuy, prices[i])
#             maxP = max(maxP, prices[i]-minBuy)

#         return maxP


# Two Pointers / Greedy
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l]<prices[r]:
                maxP = max(maxP, prices[r]-prices[l])
            else:
                # 表示當前的買價不再有優勢，所以將買價換成更小的prices[r]
                l = r
            r += 1

        return maxP

# Test
prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices)) # Expect 5