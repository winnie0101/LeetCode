from typing import List

# binary search
# time complexity: O(log n)
# space complexity: O(1)
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         minIdx = self.findMin(nums)
#         pivot = minIdx

#         l, r = 0, len(nums) - 1
#         if target >= nums[pivot] and target <= nums[r]:
#             l = pivot
#         else:
#             r = pivot - 1

#         while l <= r :
#             m = (l + r) // 2
#             if target == nums[m]:
#                 return m
#             elif target > nums[m]:
#                 l = m + 1
#             elif target < nums[m]:
#                 r = m - 1
            
#         return -1
        
        
#     def findMin(self, nums: List[int]) -> int:
#         l, r = 0, len(nums) - 1
#         while l < r:
#             m = (l + r) // 2
#             if nums[m] < nums[r]:
#                 r = m
#             else:
#                 l = m + 1

#         return l
        
        
# binary search (one pass)
# time complexity: O(log n)
# space complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:   
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] <= nums[r]:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1

# Test
nums = [4,5,6,7,0,1,2]
target = 0
sol = Solution()
print(sol.search(nums, target)) # 4