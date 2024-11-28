from typing import List


# binary search
# time complexity: O(log n)
# space complexity: O(1)
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         l, r = 0, len(nums) - 1
#         res = nums[0]

#         while l <= r:
#             if nums[l] < nums[r]:
#                 res = min(res, nums[l])
#                 return res
            
#             m = (l + r) // 2
#             res = min(res, nums[m])
#             if nums[l] <= nums[m]:
#                 l = m + 1
#             else:
#                 r = m - 1

#         return res
                 
# binary search (lower bound)
# time complexity: O(log n)
# space complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:    
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

# Test
nums = [3,4,5,1,2]
sol = Solution()
print(sol.findMin(nums)) # 1

nums = [4,5,6,7,0,1,2]
print(sol.findMin(nums)) # 0

nums = [11,13,15,17]
print(sol.findMin(nums)) # 11