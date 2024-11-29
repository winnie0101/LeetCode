from typing import List

# dynamic programming (top-down)
# time complexity: O(n)
# space complexity: O(n)
# 拆解成兩個線性問題：
# 1. 不取最後一個
# 2. 不取第一個
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]

#         memo1 = [-1] * len(nums)
#         memo2 = [-1] * len(nums)

#         def dfs(i, flag, memo):
#             if flag == 0 and i >= len(nums)-1:
#                 return 0
#             if flag == len(nums)-1 and i >= len(nums):
#                 return 0
            
#             if memo[i] != -1:
#                 return memo[i]

#             memo[i] = max(dfs(i+1, flag, memo), nums[i] +dfs(i+2, flag, memo))
#             return memo[i]

#         # 不取最後一個
#         res1 = dfs(0, 0, memo1)
#         # 不取第一個
#         res2 = dfs(1, len(nums)-1, memo2)

#         return max(res1, res2)
        

# dynamic programming (bottom-up)
# time complexity: O(n)
# space complexity: O(n)
# 拆解成兩個線性問題：
# 1. 不取最後一個
# 2. 不取第一個
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return nums[0]

#         memo1 = [0] * len(nums)
#         memo2 = [0] * len(nums)

#         memo1[0] = nums[0]
#         memo1[1] = max(nums[0], nums[1])

#         if len(nums) == 2:
#             return memo1[-1]

#         memo2[1] = nums[1]
#         memo2[2] = max(nums[1], nums[2])

#         for i in range(2, len(nums)-1):
#             memo1[i] = max(memo1[i-1], nums[i]+memo1[i-2])

#         for i in range(3, len(nums)):
#             memo2[i] = max(memo2[i-1], nums[i]+memo2[i-2])

#         res1 = memo1[-2]
#         res2 = memo2[-1]

#         return max(res1, res2)

# dynamic programming (space optimized)
# time complexity: O(n)
# space complexity: O(1)
# 拆解成兩個線性問題：
# 1. 不取最後一個
# 2. 不取第一個
class Solution:
    def rob(self, nums: List[int]) -> int:
        res1 = max(nums[0], self.helper(nums[:-1]))
        res2 = max(nums[0], self.helper(nums[1:]))
        return max(res1, res2)


    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2


# Test
nums = [2,3,2]
sol = Solution()
print(sol.rob(nums)) # 3

nums = [1,2,3,1]
sol = Solution()
print(sol.rob(nums)) # 4